"""
"""

import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np
from sksparse.cholmod import cholesky_AAt
import matplotlib.pyplot as plt
from scipy import sparse

import pathlib

import pickle
import bz2
import lzma

try:
    from sparse_dot_mkl import dot_product_mkl
except:
    logging.warning('sparse_dot_mkl not available')

from .sncosmoutils import retrieve_bandpass_model, check_bandpass_type, check_interp_xy_range
from .bspline import BSpline, BSpline2D, lgram


__all__ = ['XYBandpass', 'RadialBandpass', 'Bandpass', 'FilterLib']


def _refine_grid(grid):
    g = grid.repeat(2)
    return 0.5 * (g[1:] + g[:-1])


def _refine_grid_2(grid, scale=0.5):
    dx = (grid[1:] - grid[:-1]).min()
    xmin, xmax = grid.min(), grid.max()
    N = int(np.floor((xmax-xmin)/(scale * dx)))
    return np.linspace(xmin, xmax, N)


def _pick_matrix(star, Ns):
    """generate a choice matrix
    """
    Nm = len(star)
    j = star
    assert np.all((star>=0) & (star<Ns))
    i = np.arange(Nm)
    v = np.ones(Nm)
    return sparse.coo_matrix((v, (i,j)), shape=(Nm,Ns))


def _compress(c, thresh=1.E-9):
    """
    """
    cmax = c.max()
    idx = np.abs(c/cmax < thresh)
    cc = c.copy()
    cc[idx] = 0.
    return cc


class XYBandpass:
    """A spatially variable bandpass model

    """
    def __init__(self, interp, basis, **kwargs):
        """Constructor
        """
        self.interp = interp
        self.basis = basis
        self.xy_size = kwargs.get('xy_size', 20)
        self.xy_order = kwargs.get('xy_order', 2)
        self.sensor_id = kwargs.get('sensor_id', -1)
        self.beta = kwargs.get('beta', 1.E-6)
        self.force_spgemm = kwargs.get('force_spgemm', False)
        self.disable_zero_suppression = kwargs.get('disable_zero_suppression', False)
        init = kwargs.get('init', True)

        self.to_filter = interp.transforms.to_filter
        self.to_focalplane = interp.transforms.to_focalplane

        if not init:
            return

        # TODO : move all this below into project method spatial basis
        xy_basis_grid = check_interp_xy_range(self.interp, size=self.xy_size)
        spatial_basis = BSpline2D(
            xy_basis_grid[0],
            xy_basis_grid[1],
            x_order=self.xy_order,
            y_order=self.xy_order)

        # resampling grid
        # 1. in wavelength
        wl_resample = _refine_grid(self.basis.grid)
        wl_J = self.basis.eval(wl_resample).tocsr()

        # 2. in position
        xx = _refine_grid_2(spatial_basis.bx.grid, 0.5)
        yy = _refine_grid_2(spatial_basis.by.grid, 0.5)
        # TODO why was this commented out ?
        xx, yy = np.meshgrid(xx, yy)
        spatial_J = spatial_basis.eval(xx.ravel(), yy.ravel()).tocsr()

        # resample bandpass
        sensor_id = np.full(len(xx), self.sensor_id)#_init)
        v = self.interp.eval_at(
            xx.ravel(), yy.ravel(), sensor_id,
            wl=wl_resample, filter_frame=True)

        # project on the wavelength basis
        wl_factor = cholesky_AAt(wl_J.T, beta=self.beta)
        if self.disable_zero_suppression:
            coeffs = wl_factor(wl_J.T @ v.T)
        else:
            coeffs = _compress(wl_factor(wl_J.T @ v.T), thresh=1.E-9)

        # project the result on the XY basis
        spatial_factor = cholesky_AAt(spatial_J.T, beta=self.beta)
        self.coeffs = spatial_factor(spatial_J.T @ coeffs.T)
        self.spatial_basis = spatial_basis

    def flux(self, stellarlib, star, x, y, sensor_id=None, airmass=None, filter_frame=False):
        """
        """
        if not filter_frame:
            s_id = sensor_id if sensor_id is not None else self.sensor_id
            xf, yf = self.to_filter(x, y, s_id)
        else:
            xf, yf = x, y

        Jxy = self.spatial_basis.eval(xf, yf).tocsr()
        G = lgram(stellarlib.basis, self.basis).tocsr()
        P = _pick_matrix(star, len(stellarlib)).tocsr()

        if 'dot_product_mkl' in globals() and not self.force_spgemm:
            FF = dot_product_mkl(G, dot_product_mkl(Jxy, self.coeffs).T)
            del Jxy
            # FF = G @ (Jxy @ self.coeffs).T
            SS = dot_product_mkl(P, stellarlib.coeffs.T)
            # SS = P @ stellarlib.coeffs.T
        else:
            FF = G @ (Jxy @ self.coeffs).T
            del Jxy
            SS = P @ stellarlib.coeffs.T

        flx = (SS * FF.T).sum(axis=1)

        return flx

    def __call__(
            self, x, y,
            sensor_id=None, wl=None, z=0., airmass=None, filter_frame=False):
        """
        """
        x = np.atleast_1d(x)
        y = np.atleast_1d(y)
        if wl is None:
            wl = np.arange(3000., 11000., 10.)
        wl = np.atleast_1d(wl)

        if not filter_frame:
            s_id = sensor_id if sensor_id is not None else self.sensor_id
            xf, yf = self.to_filter(x, y, s_id)
        else:
            xf, yf = x, y

        Jxy = self.spatial_basis.eval(xf, yf)
        theta = (Jxy @ self.coeffs).T.squeeze()
        J = self.basis.eval(wl * (1.+z))
        return J @ theta

    # def get_bandpass(self, x, y, sensor_id=None, wl=None, z=0., airmass=None, filter_frame=False):
    #     if wl is None:
    #         wl = np.arange(3000., 11000., 10.)
    #     tr = self(x=x, y=y, sensor_id=sensor_id, wl=wl, z=z,
    #               airmass=airmass, filter_frame=filter_frame)
    #     return sncosmo.Bandpass(wl, tr, name=)

    def wave_eff(self, x=None, y=None, airmass=None):
        """
        """
        raise NotImplementedError()

    def plot(self, x, y, wl=None, airmass=None, axis=None, **kw):
        """
        """
        x = np.atleast_1d(x)
        y = np.atleast_1d(y)
        if wl is None:
            wl = np.arange(3000., 11000., 10.)

        wl = np.atleast_1d(wl)
        Jxy = self.spatial_basis.eval(x, y)
        theta = (Jxy @ self.coeffs).T.squeeze()
        J = self.basis.eval(wl)

        if axis is None:
            fig = plt.figure(figsize=kw.get('figsize', (8,8)))
            axis = fig.add_subplot(111)
        axis.plot(wl, J @ theta, ls=kw.get('ls', '-'),
                  color=kw.get('color', 'b'),
                  marker=kw.get('markger', '.'))
        axis.set_xlabel(r'$\lambda [\AA]$')
        axis.set_ylabel(r'$T(\lambda)$')


class RadialBandpass:
    """A radially variable bandpass model
    """
    def __init__(self, interp, basis, **kwargs):
        """Constructor - build the bases
        """
        self.interp = interp
        self.basis = basis
        self.spatial_basis_size = kwargs.get('spatial_basis_size', 10)
        self.radial_order = kwargs.get('radial_order', 2)
        self.sensor_id = kwargs.get('sensor_id', -1)
        self.beta = kwargs.get('beta', 1.E-6)
        self.force_spgemm = kwargs.get('force_spgemm', False)
        self.disable_zero_suppression = kwargs.get('disable_zero_suppression', False)
        init = kwargs.get('init', True)

        self.to_filter = self.interp.transforms.to_filter
        self.to_focalplane = self.interp.transforms.to_focalplane

        if not init:
            return

        # TODO : move all this below into project method
        # spatial basis
        radial_basis_grid = check_interp_xy_range(self.interp, size=self.spatial_basis_size)
        assert(len(radial_basis_grid)) == 1
        radial_basis_grid = radial_basis_grid[0]
        spatial_basis = BSpline(radial_basis_grid,
                                order=self.radial_order)

        # resampling grid
        # 1. in wavelength
        wl_resample = _refine_grid(self.basis.grid)
        wl_J = self.basis.eval(wl_resample).tocsr()

        # 2. in position
        rr = _refine_grid(spatial_basis.grid)
        # xx, yy = np.meshgrid(xx, yy)
        spatial_J = spatial_basis.eval(rr.ravel()).tocsr()

        # resample bandpass
        sensor_id = np.full(len(rr), self.sensor_id)
        v = self.interp.eval_at(rr, rr, sensor_id, wl=wl_resample, filter_frame=True)

        # project on the wavelength basis
        wl_factor = cholesky_AAt(wl_J.T, beta=self.beta)
        if self.disable_zero_suppression:
            coeffs = wl_factor(wl_J.T @ v.T)
        else:
            coeffs = _compress(wl_factor(wl_J.T @ v.T), thresh=1.E-9)

        # project the result on the XY basis
        spatial_factor = cholesky_AAt(spatial_J.T, beta=1.E-6)
        self.coeffs = spatial_factor(spatial_J.T @ coeffs.T)
        self.spatial_basis = spatial_basis

    def flux(self, stellarlib, star, x, y, sensor_id=None, airmass=None, filter_frame=False):
        """
        """
        if not filter_frame:
            s_id = sensor_id if sensor_id is not None else self.sensor_id
            xf, yf = self.to_filter(x, y, s_id)
        else:
            xf, yf = x, y

        rad = np.sqrt(xf**2 + yf**2)
        Jxy = self.spatial_basis.eval(rad).tocsr()
        G = lgram(stellarlib.basis, self.basis).tocsr()
        P = _pick_matrix(star, len(stellarlib)).tocsr()

        if 'dot_product_mkl' in globals() and not self.force_spgemm:
            FF = dot_product_mkl(G, dot_product_mkl(Jxy, self.coeffs).T)
            del Jxy
            SS = dot_product_mkl(P, stellarlib.coeffs.T)
            # FF = G @ (Jxy @ self.coeffs).T
            # SS = P @ stellarlib.coeffs.T
        else:
            FF = G @ (Jxy @ self.coeffs).T
            del Jxy
            SS = P @ stellarlib.coeffs.T

        flx = (SS * FF.T).sum(axis=1)

        return flx

    def __call__(self, x, y, sensor_id=None, wl=None, z=0., airmass=None, filter_frame=False):
        """
        """
        x = np.atleast_1d(x)
        y = np.atleast_1d(y)
        if wl is None:
            wl = np.arange(3000., 11000., 10.)
        wl = np.atleast_1d(wl)

        if not filter_frame:
            s_id = sensor_id if sensor_id is not None else self.sensor_id
            xf, yf = self.to_filter(x, y, s_id)
        else:
            xf, yf = x, y

        rad = np.sqrt(xf**2 + yf**2)
        Jxy = self.spatial_basis.eval(rad)
        theta = (Jxy @ self.coeffs).T.squeeze()
        J = self.basis.eval(wl * (1.+z))
        return J @ theta

    def wave_eff(self, x=None, y=None, airmass=None):
        """
        """
        raise NotImplementedError()


class CompositeBandpass:
    """ Bandpasses which depend on the sensor id.
    """
    def __init__(self, bandpass_dict):
        """Bandpasses are stored in a dict, with sensor id as keys
        """
        self._bandpasses = bandpass_dict
        self.sensors = list(self._bandpasses.keys())
        interp = self._bandpasses[self.sensors[0]].interp #default
        self.to_filter = interp.transforms.to_filter
        self.to_focalplane = interp.transforms.to_focalplane

    def __call__(self, x, y, sensor_id=None, **kwargs):
        if sensor_id is None:
            raise ValueError("Missing sensor_id keyword argument")

        shape = self._bandpasses[self.sensors[0]](x=x,
                                                  y=y,
                                                  sensor_id=self.sensors[0],
                                                  **kwargs).shape
        ret = np.zeros(shape) * np.nan
        _sensors = list(set(sensor_id))
        for s_id in _sensors:
            selec = sensor_id==s_id
            ret[:,selec] = self._bandpasses[s_id](x=x[selec],
                                                y=y[selec],
                                                sensor_id=sensor_id[selec],
                                                **kwargs)
        return ret

    def flux(self, stellarlib, star, x, y, sensor_id=None, filter_frame=False, **kwargs):
        if filter_frame:
            sensor_id = np.tile(self.sensors[0], len(x))
        if sensor_id is None:
            raise ValueError("Missing sensor_id keyword argument")
        ret = np.zeros((len(x))) * np.nan
        _sensors = list(set(sensor_id))
        for s_id in _sensors:
            selec = sensor_id==s_id
            ret[selec] = self._bandpasses[s_id].flux(stellarlib, star[selec],
                                                     x=x[selec],
                                                     y=y[selec],
                                                     sensor_id=sensor_id[selec],
                                                     **kwargs)
        return ret


class Bandpass:
    """A standard bandpass
    """
    def __init__(self, bandpass, basis, **kwargs):
        """
        """
        self.bandpass = bandpass
        self.basis = basis
        self.beta = kwargs.get('beta', 1.E-6)
        self.disable_zero_suppression = kwargs.get('disable_zero_suppression', False)

        # resampling grid
        # 1. in wavelength
        wl_resample = _refine_grid(self.basis.grid)
        wl_J = self.basis.eval(wl_resample).tocsr()

        # resample bandpass
        v = self.bandpass(wl_resample)

        # project on the wavelength basis
        wl_factor = cholesky_AAt(wl_J.T, beta=self.beta)
        coeffs = wl_factor(wl_J.T @ v.T)

        if self.disable_zero_suppression:
            self.coeffs = coeffs
        else:
            self.coeffs = _compress(coeffs)

    def flux(self, stellarlib, star=None, x=None, y=None, airmass=None, **kwargs):
        """
        """
        G = lgram(stellarlib.basis, self.basis)
        P = _pick_matrix(star, len(stellarlib))

        # flx = stellarlib.coeffs.T @ P.T @ G @ (self.coeffs).T
        FF = G @ self.coeffs.T
        SS = P @ stellarlib.coeffs.T
        flx = (SS * FF.T).sum(axis=1)

        return flx

    def __call__(self, wl=None, z=0., airmass=None, **kwargs):
        """
        """
        if wl is None:
            wl = np.arange(3000., 11000., 10.)
        else:
            wl = np.atleast_1d(wl)

        J = self.basis.eval(wl * (1.+z))
        return J @ self.coeffs

    def wave_eff(self, x=None, y=None, airmass=None):
        """
        """
        return self.bandpass.wave_eff


class _FluxArgs:
    """A utility class to manage the arguments passed to the FilterLib.flux() method
    """
    def __init__(self, filterlib, star, band, x=None, y=None, sensor_id=None):
        """check the arguments. Broadcast if necessary
        """
        self.filterlib = filterlib

        # we expect arrays as arguments
        args = list(map(lambda x: np.atleast_1d(x) if x is not None else None, [star, band, x, y, sensor_id]))

        # check that all args or 1D or None
        assert all(map(lambda xx: xx is None or (xx.ndim == 1), args))

        # if broadcasting is necessary, prepare args for that.
        # Otherwise, do nothing
        def _check(x):
            if x is None:
                return x
            if len(x) != len(star):
                return np.array([x]).T
            return x
        args = map(_check, args)

        star, band, x, y, sensor_id = args

        # if no position information, then broadcast only on star and band
        if x is None or y is None:
            self._star, self._band = np.broadcast_arrays(star, band)
            self._x, self._y, self._sensor_id = None, None, None
        else:
            if sensor_id is None:
                sensor_id = -1
            self._star, self._band, self._x, self._y, self._sensor_id = \
                np.broadcast_arrays(star, band, x, y, sensor_id)

        self.shape = self._star.shape
        self._star = self._star.ravel()
        self._band = self._band.ravel()
        self._x = self._x.ravel() if self._x is not None else None
        self._y = self._y.ravel() if self._y is not None else None
        self._sensor_id = self._sensor_id.ravel() if self._sensor_id is not None else None

    @property
    def no_position_info(self):
        no_pos = self._x is None or self._y is None
        return no_pos

    def analyze(self):
        """return bands and selectors

        The algorithm to identify bands is as follows:
         - if no pos information, fetch average bands from self.average_bandpasses, indexed by band
         - if position information, fetch bands from self.bandpasses, indexed by band
        """
        ret = []
        bands = np.unique(self._band)

        # if no position information, we use the average bandpasses
        if self.no_position_info:
            for b in bands:
                bp = self.filterlib.get(b, average=True)
                ret.append((bp, b))
            return ret

        # if position information, we fetch the other bandpasses
        for b in bands:
            try:
                bp = self.filterlib.get(b)
            except:
                bp = self.filterlib.get(b, average=True)
            ret.append((bp, b))
        return ret

    def __len__(self):
        return len(self.star)

    @property
    def star(self):
        return self._star.ravel()

    @property
    def band(self):
        return self._band.ravel()

    @property
    def x(self):
        if self._x is None:
            return None
        return self._x.ravel()

    @property
    def y(self):
        if self._y is None:
            return None
        return self._y.ravel()

    @property
    def sensor_id(self):
        if self._sensor_id is None:
            return None
        return self._sensor_id.ravel()


class FilterLib:
    """Store a collection of bandpasses, projected on a spline basis"""
    def __init__(self, basis=None, bands=None):
        """Constructor.

        Sets the wavelength basis on which all filters are projected.
        """
        if isinstance(basis, np.ndarray):
            self.basis = BSpline(basis)
        elif isinstance(basis, BSpline):
            self.basis = basis
        else:
            self.basis = self._default_basis()

        # average bandpasses
        self._average_bandpasses = {}

        # most bandpass models go here. These are the bandpasses whose
        # coefficients do not depend on the sensor id.
        self._bandpasses = {}

    def _default_basis(self, min_wave=3000., max_wave=11010, step=10.):
        """returns a default BSpline basis on which to project the passbands
        """
        grid = np.arange(min_wave, max_wave+step, step)
        return BSpline(grid)

    def __len__(self):
        return len(self._bandpasses)

    @property
    def bandpass_names(self):
        return list(set(
            list(self._average_bandpasses.keys()) +
            list(self._bandpasses.keys())))

    def list_bandpasses(self):
        ret = [k + '[avg]' for k in self._average_bandpasses]
        ret.extend([k + '[*]' for k in self._bandpasses])
        return ret

    ls = list_bandpasses

    def get(self, key, average=False):
        if average and key in self._average_bandpasses:
            return self._average_bandpasses[key]
        if key in self._bandpasses:
            return self._bandpasses[key]
        raise KeyError(key)

    def get_bandpass(self, key, **kwargs):
        return self.get(key, **kwargs)

    def __getitem__(self, key):
        return self._bandpasses[key]

    def fetch(self, band_name, xy_size=10, xy_order=2, **kwargs):
        """retrieve a bandpass model from sncosmo and project it
        """
        radius = kwargs.get('radius', None)
        sensor_id = kwargs.get('sensor_id', -1)
        average = kwargs.get('average', False)

        bp = None
        interp = retrieve_bandpass_model(
            band_name, average=average, radius=radius)
        interp_type = check_bandpass_type(interp)
        if interp_type == 'xy':
            bp = XYBandpass(interp, self.basis,
                            xy_size=xy_size, xy_order=xy_order,
                            sensor_id=sensor_id)
        elif interp_type == 'radial':
            bp = RadialBandpass(
                interp, self.basis,
                spatial_basis_size=xy_size, radial_order=xy_order,
                sensor_id=sensor_id)
        else:
            bp = Bandpass(interp, self.basis)

        return bp

    def insert(self, band, band_name, average=False):
        """Insert the bandpass model in the right dictionary"""
        if isinstance(band, Bandpass) and average:
            self._average_bandpasses[band_name] = band
        elif isinstance(band, dict):
            self._bandpasses[band_name] = CompositeBandpass(band)
        else:
            self._bandpasses[band_name] = band

    def flux(self, stellarlib, star, band,
             x=None, y=None, sensor_id=None,
             filter_frame=False):
        """Computes the broadband fluxes for a series of measurements.

        This function computes the broadband fluxes of a series of measurements
        of stars whose spectra are stored in the specified spectral library.

        If the positions are specified, the function evaluates and uses the
        effective camera passbands at those positions. If not, a default model
        of the passbands -- averaged over the focal plane in practice -- is
        used.

        The positions are specified as (x, y, sensor_id), where x and y store
        the measurement x and y positions, in pixels, and sensor_id stores the
        measurement sensor IDs (usually as ints). If `filter_frame` is True,
        then sensor_id is ignored and x and y are interpreted as filter frame
        positions in millimeters.

        More formally, the function evaluates:
        .. math::
             f_i = \\int S_i(\\lambda) \\lambda T_{x_i, y_i, s_i}(\\lambda) d\\lambda

        where :math:`i` is the index of the ith measurement, :math:`S_i` is the
        SED of the star observed in the ith measurement, and :math:`T` is the
        effective transmission evaluated at the corresponding location.

        Parameters
        ----------
        stellarlib : :obj:`StellarLib`
            the stellar lib containing the spectra (projected on a spline basis).
        star : array_like of ints
            Star indexes of each measurement.
        band : array_like of str
            Band of each measurement.
        x : array_like of floats or None, optional
            Measurement x-positions on the focal plane, in pixels.
        y : array_like of floats or None, optional
            Measurement y-positions on the focal plane, in pixels.
        sensor_id : array_like of ints or None, optional
            Measurement sensor IDs.
        filter_frame : bool, optional
            If True, x,y are interpreted as positions (in mm) in the filter
            frame. Mostly used for debugging purposes, to compare integrators.

        Returns
        -------
        fluxes : ndarray of floats
            The broadband fluxes.

        Examples
        --------
        >>> import bbf.stellarlib.pickles
        >>> from lemaitre import bandpasses
        >>> fl = bandpasses.get_filterlib()
        >>> pickles = bbf.stellarlib.pickles.fetch()
        >>> fluxes = fl.flux(pickles, [1, 4, 5], ['ztf::g', 'ztf::g', 'ztf::r'])
        >>> fluxes
        >>> # was array([3435.35454, 24543.35234, 35442.435465])
        array([3.39769617e+14, 2.48825753e+14, 4.25911990e+14])

        """
        args = _FluxArgs(self, star, band, x, y, sensor_id)

        # compute fluxes for all bandpasses
        fluxes = np.zeros(len(args))
        for bp, band in args.analyze():
            idx = args.band == band

            # fix to issue 15. _FluxArgs.__init__ converts sensor_id from None
            # to an array of -1. This may be the desirable behavior for other
            # bandpass classes but causes a bug in CompositeBandpass, where
            # sensor_id is required.
            if isinstance(bp, CompositeBandpass) and sensor_id is None:
                raise ValueError("Missing sensor_id keyword argument")

            star, x, y, sensor_id = args.star, args.x, args.y, args.sensor_id

            try:
                fluxes[idx] = bp.flux(
                    stellarlib,
                    star=star[idx],
                    x=None if x is None else x[idx],
                    y=None if y is None else y[idx],
                    sensor_id=None if sensor_id is None else sensor_id[idx],
                    filter_frame=filter_frame)
            except:
                logging.error(f'error computing fluxes for: band={band} sensor_id={sensor_id}')
                logging.error(f'{sys.exc_info()}')
                fluxes[idx] = 0.

        return fluxes.reshape(args.shape).T

#    def mag(self, stellarlib, star, band, x, y, sensor_id=None, magsys='AB'):
#        """
#        """
#        flx = self.flux(stellarlib, star, band, x, y, sensor_id)
#        magsys = get_magsys(magsys)
#        zp_scales = magsys.get_zp_scales()

    def save(self, filename, compression=None):
        """Save the FilterLib as a pickle"""
        filename = pathlib.Path(filename)
        if compression is None:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        elif compression == 'lzma':
            with lzma.open(filename.with_suffix('.pkl.xz'), 'wb') as f:
                pickle.dump(self, f)
        elif compression == 'bzip2':
            with bz2.BZ2File(filename.with_suffix('.pkl.bz2'), 'wb') as f:
                pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        """Load a pickled FilterLib"""
        filename = pathlib.Path(filename)
        if filename.suffix == '.xz':
            with lzma.open(filename, 'rb') as f:
                ret = pickle.load(f)
        elif filename.suffix == '.bz2':
            with bz2.BZ2File(filename, 'rb') as f:
                ret = pickle.load(f)
        else:
            with open(filename, 'rb') as f:
                ret = pickle.load(f)

        if isinstance(ret, cls):
            return ret
        return None
