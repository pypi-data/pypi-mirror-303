"""
"""

from dataclasses import dataclass
import numpy as np
import pylab as pl
import pandas
from sksparse.cholmod import cholesky_AAt

import sncosmo

from bbf.bspline import BSpline, Projector
from bbf.utils import sort_bands_by_mean_wavelength


__all__ = ['SNFilterSet']


default_wave_range = {
    'ztf::i': (3840., 9000.),
    'megacam6::g': (3000., 7000.),
}


@dataclass
class FilterInfo:
    tq: np.ndarray
    basis: BSpline
    z: float
    wave_eff: float
    minwave: float
    maxwave: float
    valid: bool

class SNFilterSet:
    """A utility class to handle blueshifted bandpasses projected on a BSpline basis

    Example
    -------
    >>> snf = SNFilterSet()
    """
    def __init__(self, basis=None, wave_range=default_wave_range):
        """Constructor. Build an internal basis and project the filters on it
        """
        # the coefficient database
        # indexed by band name and redshift
        self.db = {}

        # the original transmissions
        self.transmission_db = {}

        # wl_range (of restframe filter)
        self.wave_range = wave_range.copy()

        # the filter boundaries
        self._minwave = {}
        self._wave_eff = {}
        self._maxwave = {}

        # instantiate the basis
        self.basis = None
        if basis is None:
            self.basis = self._default_basis()
        elif isinstance(basis, BSpline):
            self.basis = basis
        elif isinstance(basis, np.ndarray):
            self.basis = BSpline(basis)

        # instantiate the default projector
        self._grid, self._J, self._factor = self._projector(self.basis)

    def __len__(self):
        return len(self.db)

    def __getitem__(self, key):
        if isinstance(key, str):
            key = (key, 0.0)
        if key not in self.db:
            raise KeyError
        return self.db[key]

    @staticmethod
    def _refine_grid(grid):
        """
        """
        gxx = np.hstack((grid, 0.5*(grid[1:]+grid[:-1])))
        gxx.sort()
        return gxx

    def _default_basis(self):
        grid = np.arange(2000., 8510., 10.)
        return BSpline(grid)

    def _compress(self, coeffs, thresh=1.E-9):
        """suppress the very small coefficients of the projection
        """
        if thresh <= 0.:
            return
        c = coeffs / coeffs.max(axis=0)
        idx = np.abs(c) < thresh
        coeffs[idx] = 0.
        return coeffs

    def __getstate__(self):
        """cholmod._factor not serializable. That's why.
        """
        return (self.basis, self.transmission_db, self.db)

    def __setstate__(self, state):
        """cholmod._factor not serializable.
        """
        self.basis, self.transmission_db, self.db = state
        self._grid, self._J, self._factor = self._projector(self.basis)

    def get_band_names(self, sort=False):
        """return the names of the bands stored in the filterset
        """
        bands = np.array(list(self.transmission_db.keys()))
        if not sort:
            return bands
        i_band = np.argsort(np.array([self.transmission_db[k].wave_eff for k in self.transmission_db]))
        return bands[i_band]

    def get_coeffs(self, sort=False, reverse=False):
        """get the filter coeffs as a 2D table

        .. note:: maybe we should store them as a 2D table
           the dict being just an index
        """
        ret = np.zeros((len(self.db), len(self.basis)))
        for i,k in enumerate(self.db):
            ret[i,:] = self.db[k].tq

        if sort:
            i = np.argsort(np.array([k[1] for k in self.db]))
            if reverse:
                return ret[i[::-1],:]
            else:
                return ret[i,:]

        return ret

    def get_boundaries(self):
        """return a DataFrame containing the filter boundaries
        """
        wave_eff, minwave, maxwave, valid = [], [], [], []
        for key in self.db:
            _, _, weff, minw, maxw, vld = self.db[key]
            wave_eff.append(weff)
            minwave.append(minw)
            maxwave.append(maxw)
            valid.append(vld)
        return pandas.DataFrame({'wave_eff': wave_eff,
                                 'minwave': minwave,
                                 'maxwave': maxwave,
                                 'valid': valid})

    @staticmethod
    def _projector(basis):
        r"""
        Precompute the elements and factorization of the fit matrix

        .. math:: (J^T J)^{-1} J^T

        this saves repeated calls to cholesky_AAt when processing
        other filters.

        Parameters
        ----------
        basis : BSpline
            Spline basis.

        Returns
        -------
        gxx : np.array
            Grid, spline evaluation
        jacobian : scipy.sparse.csr_matrix
            Jacobian matrix.
        factor : sksparse.cholmod.Factor
            Result of cholesky decomposition.
        """
        # refine the basis grid
        gxx = SNFilterSet._refine_grid(basis.grid)

        # precompute the projector
        # (will save repeated calls to cholesky_AAt)
        jacobian = basis.eval(gxx).tocsr()
        factor = cholesky_AAt(jacobian.T)
        return gxx, jacobian, factor

    def insert(self, tr, z=0., x=None, y=None, sensor_id=None, basis=None):
        """Project transmission `tr` on the basis and insert it into the database

        Parameters
        ----------
        tr :
            Filter transmission.
        z : float
            SN redshift.
        x : float (pixels)
            average x-position of the measurement(s)
        y : float (pixels)
            average y-position of the measurement(s)
        sensor_id : int
            sensor_id

        Returns
        -------
        tq : numpy.array
            Transmission for grid of wavelength redshift corrected.
        """
        if basis is None:  # then, use the default basis
            grid, jacobian, factor = self._grid, self._J, self._factor
            basis = self.basis
        else:
            grid, jacobian, factor = self._projector(basis)

        if isinstance(tr, str):
            if x is None or y is None or sensor_id is None:
                tr = sncosmo.get_bandpass(tr)
            else:
                tr = sncosmo.get_bandpass(tr, x=x, y=y, sensor_id=sensor_id)
        else:
            assert isinstance(tr, sncosmo.Bandpass)

        wave = tr.wave
        trans = tr.trans

        y = tr(grid * (1.+z))
        tq = self._compress(factor(jacobian.T * y))

        full_name = tr.name
        key = full_name, z
        if full_name not in self.transmission_db:
            self.transmission_db[full_name] = tr

        basis_minw, basis_maxw = self.basis.grid.min(), self.basis.grid.max()
        minw = self.minwave(tr) / (1.+z)
        maxw = self.maxwave(tr) / (1.+z)
        wave_eff = tr.wave_eff / (1.+z)
        valid =  (minw >= basis_minw) & (maxw <= basis_maxw)
        # self.db[key] = (tq, basis, wave_eff, minw, maxw, valid)
        self.db[key] = FilterInfo(tq, basis, z, wave_eff, minw, maxw, valid)

        # return tq, basis
        return self.db[key]

    def minwave(self, tr):
        if tr.name not in self.wave_range:
            return tr.minwave()
        return self.wave_range[tr.name][0]

    def maxwave(self, tr):
        if tr.name not in self.wave_range:
            return tr.maxwave()
        return self.wave_range[tr.name][1]

    # def wave_eff(self):
    #     """return the mean wavelengh of the input filters
    #     """
    #     # if list of band passes, just call 'wave_eff' for each one
    #     if check_sequence(self.transmission_db, lambda x: hasattr(x, 'wave_eff')):
    #         return np.array([b.wave_eff for b in self.transmission_db])

    #     # if a 2D table, compute the mean wavelengths
    #     tr = self.bandpasses
    #     wl = self.wave
    #     return (tr * wl).sum(axis=0) / tr.sum(axis=0)

    def plot_original_transmissions(self):
        """
        """
        xx = np.arange(3000., 11000., 10.)

        fig, axes = pl.subplots(figsize=(12,10), nrows=12, ncols=1,
                                sharex=1, sharey=1)
        band_names = sort_bands_by_mean_wavelength(self.transmission_db)
        for i,bn in enumerate(band_names):
            bp = self.transmission_db[bn]
            tr = bp(xx)
            axes[i].semilogy(xx, tr/tr.max(), 'b-')
            axes[i].axvline(bp.minwave(), ls=':', color='b')
            axes[i].axvline(bp.maxwave(), ls=':', color='b')
            axes[i].axhline(1.E-3, ls=':', color='gray', alpha=0.5)
            axes[i].axhline(1.E-2, ls=':', color='gray', alpha=0.5)
            if bn in self.wave_range:
                minwave, maxwave = self.wave_range[bn]
                axes[i].axvline(minwave, ls=':', color='r')
                axes[i].axvline(maxwave, ls=':', color='r')
            axes[i].text(0.8, 0.5, bn, transform=axes[i].transAxes)
        pl.subplots_adjust(hspace=0.05)
        axes[0].set_title('SNFilterSet original transmissions')
        axes[-1].set_xlabel(r'$\lambda [\AA]$')

    def plot_transmissions(self, **kw):
        """plot the contents of the filter set
        """
        figsize = kw.get('figsize', (8,12))
        cmap = kw.get('cmap', pl.cm.jet)
        exclude = kw.get('exclude', [])

        nbands = len(self.transmission_db)
        fig, axes = pl.subplots(figsize=figsize, nrows=nbands, ncols=1,
                                sharex=True)

        # order the bands in transmission db by wavelength
        wl = np.array([self.transmission_db[k].wave_eff for k in self.transmission_db])
        iband = np.argsort(wl)
        keys = np.array(list(self.transmission_db.keys()))
        ordered_keys = keys[iband]
        ordered_band_names = dict(zip(keys[iband],np.arange(len(wl))))
        xx = self._refine_grid(self.basis.grid)
        J = self.basis.eval(xx)
        for k in self.db:
            band, z = k
            # tq, basis, wave_eff, minw, maxw, valid =
            f_info = self.db[k]
            # col = int(255 * (wave_eff-3000.) / (11000.-3000.))
            col = cmap(int(255 * f_info.z / 1.6))
            alpha = 0.10
            lw=1
            if not f_info.valid:
                col = 'gray'
                alpha=1.
                lw=2
            axes[ordered_band_names[band]].plot(xx, J @ f_info.tq,
                                                ls='-',
                                                lw=lw,
                                                color=col,
                                                alpha=alpha)
        pl.xlabel(r'$\lambda [\AA]$')
        pl.subplots_adjust(hspace=0.02)
        axes[0].set_title('transmissions')
        for i in range(len(iband)):
            axes[i].text(0.7, 0.5, ordered_keys[i],
                         transform=axes[i].transAxes)
        # pl.colorbar()

    def plot(self, **kw):
        """plot the contents of the filter set
        """
        figsize = kw.get('figsize', (8,9))
        cmap = kw.get('cmap', pl.cm.jet)
        sort = kw.get('sort', False)

        coeffs = self.get_coeffs(sort=sort)
        pl.figure(figsize=figsize)
        pl.imshow(coeffs, aspect='auto', interpolation='nearest')
        pl.colorbar()
        pl.xlabel('band')
        pl.ylabel(r'$\lambda$')
