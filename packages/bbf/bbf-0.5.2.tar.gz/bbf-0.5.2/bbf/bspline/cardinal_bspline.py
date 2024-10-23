"""Cardinal B-spline basis defined on a regular grid"""

import numpy as np
import scipy

from bbf.bspline.bspline import BSpline
from bbf.bspline.utils import _init_ijB
from bbf.bspline_ext import _blossom_f, _blossom_d


def _blossom(dtype):
    return {
        np.float32: _blossom_f,
        np.float64: _blossom_d}[dtype]


class CardinalBSpline(BSpline):
    """1-dimensional B-spline basis defined on a regular grid"""
    def __init__(self, start, stop, num, order=4, dtype=np.float64):
        if order < 2:
            raise ValueError('order must be greater or equal to 2')

        if dtype not in (np.float32, np.float64):
            raise ValueError('dtype must be float32 or float64')

        if num < 2:
            raise ValueError('num must be >= 2')

        if start >= stop:
            raise ValueError('start must be < stop')

        self._order = order
        self._dtype = dtype
        self._nknots = num
        self._grid, self._dx = np.linspace(
            start, stop, num+1, dtype=dtype, retstep=True)

    @property
    def grid(self):
        """spline intervals"""
        return self._grid

    @property
    def dx(self):
        """Interval between two points in the grid"""
        return self._dx

    def __len__(self):
        return self._nknots + self._order - 1

    def _int_grid(self, x):
        """Return x array scaled so that the knots are at integer locations"""
        return (x - self.min) / self.dx + self.order - 1

    def astype(self, dtype):
        """Copies the CardinalBSpline to the specified data type

        The `dtype` must be either np.float32 or np.float64 or a ValueError is
        raised. If the requested `dtype` is the same as the actual spline, no
        copy is done.

        """
        if dtype == self.dtype:
            return self

        basis = CardinalBSpline.__new__(CardinalBSpline)
        basis._order = self.order
        basis._dtype = dtype
        basis._nknots = self._nknots
        basis._grid = self.grid.astype(dtype)
        return basis

    def eval(self, x):
        """Evaluates the value of the basis functions for each element of x

        Args:
          x : (ndarray of floats)
              the x-values

        Returns:
          B: (scipy.sparse.coo_matrix)
                a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                containing the basis values: B_{ij} = B_j(x_i)

        """
        x = x.astype(self.dtype)
        i, j, B = _init_ijB(self.order * x.shape[-1], dtype=self.dtype)
        _blossom(self.dtype)(
            self._int_grid(x), i, j, B, self.order, self.order, len(self))
        return self._to_coo_matrix(x, i, j, B)

    def deriv(self, x):
        """Evaluates the first derivative of the basis functions for each element of x

        Args:
           x: (ndarray of floats)

         Returns:
            a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)
        """
        x = x.astype(self.dtype)
        i, j, B = _init_ijB(self.order * x.shape[-1], dtype=self.dtype)
        _blossom(self.dtype)(
            self._int_grid(x), i, j, B, self.order - 1, self.order, len(self))
        B[:-1] -= B[1:]
        return self._to_coo_matrix(x, i, j, B) / self.dx

    def deriv_m(self, x, m=2):
        """Evaluates the m-th derivative of the basis functions for each element of x

        Args:
           x: (ndarray of floats)

         Returns:
            a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)
        """
        if self.order - m <= 0:
            return scipy.sparse.coo_matrix(
                (x.shape[-1], len(self)),
                dtype=self.dtype)

        x = x.astype(self.dtype)
        i, j, B = _init_ijB(self.order * x.shape[-1], dtype=self.dtype)
        _blossom(self.dtype)(
            self._int_grid(x), i, j, B, self.order - m, self.order, len(self))

        # NOTE(mbernard) this was in the original implementation but does not
        # replicate results from BSpline class. Not sure it is a bug or a
        # feature...
        # # d = np.arange(1, m+1) # was m+1
        # # Cmp = scipy.special.comb(m, d)
        # # Cmp[::2] *= -1.
        # # BB = B.copy()
        # # for d, c in zip(d, Cmp):
        # #     BB[:-d] += c * B[d:]
        # # return self._to_coo_array(x, i, j, BB) / self.dx
        return self._to_coo_matrix(x, i, j, B)
