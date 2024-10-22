import numpy as np
import sksparse
from bbf.bspline.bspline import BSpline
from bbf.utils import check_sequence


class Projector:
    """This class precomputes the projector on a spline basis

    This allows to save many repeated calls to cholesky_AAt

    """
    def __init__(self, basis=None, grid=None):
        """Build an internal basis, and an internal refinement of the basis grid"""
        if basis is None and grid is None:
            raise ValueError('must define basis or grid')
        if basis is not None and grid is not None:
            raise ValueError('must define basis or grid, not both')

        # internal basis
        self.basis = basis or BSpline(grid)

        # internal grid refinement (may be useful)
        gx = self.basis.grid
        gxx = np.hstack((gx, 0.5 * (gx[1:] + gx[:-1])))
        gxx.sort()
        self._grid = gxx

        self._factor, self._J = self._get_projector(self._grid)

    def _get_projector(self, x):
        J = self.basis.eval(x).tocsr()
        factor = sksparse.cholmod.cholesky_AAt(J.T)
        return factor, J

    def _compatible_arrays(self, y, x):
        """check if the datset can be projected on the basis"""
        x = np.atleast_1d(x)
        y = np.atleast_2d(y)
        if x.shape[0] == y.shape[0]:
            return y, x
        elif x.shape[0] == y.shape[1]:
            return y.T, x
        return None, None


    def __call__(self, data, x=None):
        """Projects the dataset on the internal spline basis

        The data may either be:

          - a list of callables (e.g. a list of sncosmo.Bandpass objects): each
            callable is then evaluated on refinement of the basis grid, or on
            the `x` array, if specified, and the spline coefficients are derived
            through a least square fit.

          - a 2D array of shape (n,N), along with a corresponding 1D array `x`
            of shape N. Typical use case: bandpass evaluated on the same
            wavelength grid or spectral library data with all spectra sharing
            the same binning.

        """
        # either a list of callables
        if check_sequence(data, callable):
            # if a grid is explicitely specify, let's use ot
            if x is not None:
                factor, J = self._get_projector(x)
                grid = x
            # otherwise, we default to our internal grid
            else:
                factor, J, grid = self._factor, self._J, self._grid
            # evaluate our callables on the grid and project the result
            y = np.vstack([t(grid) for t in data]).T
            return factor(J.T @ y)

        # or a 2D array of measurements
        yy, xx = self._compatible_arrays(data, x)
        if xx is None or yy is None:
            raise ValueError('incompatible arrays')
        factor, J = self._get_projector(xx)
        ret = factor(J.T @ yy)
        return ret
