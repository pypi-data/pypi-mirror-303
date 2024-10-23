"""1D BSpline basis"""

import warnings

import numpy as np
import scipy
import sksparse

from bbf.bspline.utils import leggauss, _init_ijB
from bbf.bspline_ext import (
    _blossom_grid_d, _deriv_grid_d,
    _blossom_grid_f, _deriv_grid_f)


def _blossom_grid(dtype):
    return {
        np.float32: _blossom_grid_f,
        np.float64: _blossom_grid_d}[dtype]


def _deriv_grid(dtype):
    return {
        np.float32: _deriv_grid_f,
        np.float64: _deriv_grid_d}[dtype]


class BSpline:
    """1-dimensional B-spline basis

    Implements a 1D B-spline basis of arbitrary order, defined on an arbitrary
    grid.

    Parameters
    ----------
    grid : array of shape (n,)
        B-spline grid must be a 1d array, sorted in increasing order,
        containing at least 2 unique values with no nan or inf.
    order : int, optional
        B-spline order, default to 4, must be greater or equal to 2.
    dtype : np.float64 or np.float32, optional
        Data type of the B-spline defaults to `np.float64`. All input arrays
        given to this B-spline are converted to this data type before any
        processing. Output arrays are always of that data type. Computations
        using `np.float32` are faster but but with a loss in numerical
        precsion.

    """
    def __init__(self, grid, order=4, dtype=np.float64):
        if order < 2:
            raise ValueError('order must be greater or equal to 2')

        if dtype not in (np.float32, np.float64):
            raise ValueError('dtype must be float32 or float64')

        grid = np.asarray(grid, dtype=dtype)
        if grid.ndim != 1:
            raise ValueError('grid must be one-dimensional')

        if np.any(grid[1:] - grid[:-1] < 0):
            raise ValueError('grid must be sorted in increasing order')

        if len(np.unique(grid)) < 2:
            raise ValueError('need at least two unique points in the grid')

        if not np.isfinite(grid).all():
            raise ValueError("grid should not have nans or infs")

        self._order = order
        self._dtype = dtype
        self._nknots = grid.shape[0]

        # internally, the knots must be extended to deal with (order-1)
        # derivates
        p = np.arange(1.0, order, dtype=self.dtype)
        prefix = -p[::-1] * (grid[1] - grid[0]) + grid[0]
        suffix = p * (grid[-1] - grid[-2]) + grid[-1]
        self._grid = np.ascontiguousarray(np.hstack((prefix, grid, suffix)))

    @property
    def dtype(self):
        """Floatting point data type"""
        return self._dtype

    @property
    def order(self):
        """B-spline order"""
        return self._order

    @property
    def degree(self):
        """B-spline degree"""
        return self.order - 1

    @property
    def nknots(self):
        """number of knots in the B-spline"""
        return self._nknots

    @property
    def grid(self):
        """spline intervals"""
        return self._grid[self.order-1:-self.order+1]

    def __len__(self):
        return self._nknots + self._order - 2

    @property
    def nj(self):
        # TODO opaque name and redundant with __len__, should be removed in a
        # future release
        warnings.warn(
            "The property `basis.nj` is deprecated, use `len(basis)` instead",
            DeprecationWarning)

        return len(self)

    @property
    def range(self):
        """the (min, max) values of the grid"""
        return self.min, self.max

    @property
    def min(self):
        """Minimal knot in the grid"""
        # grid is sorted so min is first element
        return self.grid[0]

    @property
    def max(self):
        """Maximal knot in the grid"""
        # grid is sorted so max is last element
        return self.grid[-1]

    def _to_coo_matrix(self, x, i, j, B):
        # TODO scipy.sparse is moving from a matrix interface to an array one
        # (https://docs.scipy.org/doc/scipy/reference/sparse.html). The major
        # change for lemaitre packages is that A * B becomes element-wise
        # multiplication, matmul is called with A @ B.
        return scipy.sparse.coo_matrix(
            (B, (i, j)),
            shape=(x.shape[-1], len(self)),
            dtype=self.dtype)

    def astype(self, dtype):
        """Copies the BSpline to the specified data type

        The `dtype` must be either np.float32 or np.float64 or a ValueError is
        raised. If the requested `dtype` is the same as the actual spline, no
        copy is done.

        """
        if dtype == self.dtype:
            return self
        return BSpline(self.grid, self.order, dtype=dtype)

    def eval(self, x):
        """Evaluates the value of the basis functions for each element of x

        Args:
            x (ndarray of floats): the values of x

        Returns:
            scipy.sparse.coo_matrix: a sparse, N x p jacobian array
            [N=len(x), p=len(self)] containing the basis values
            :math:`B_{ij} = B_j(x_i)`

        .. note:  The jacobian matrix triplets are sorted as follows:
            [i=0   j=p      B_p(x_0)      ]  p, lowest integer / B_p(x_i) > 0
            [i=0   j=p+1    B_{p+1}(x_0)  ]
            [i=0   j=p+deg  B_{p+deg}(x_0)]
            [i=1   j=q      B_q(x_1)      ]
                ...

            The BSpline2.eval function (in fact. BSpline2._cross)
            assumes that order to compute the tensor product of the 1D
            basis elements.

            Note also that the old, pure python version of
            CardinalBSpline.eval also returns ordered triplets, but
            the ordering was different.

        """
        x = x.astype(self.dtype)
        i, j, B = _init_ijB(self.order * x.shape[-1], dtype=self.dtype)
        _blossom_grid(self.dtype)(
            self._grid, x, i, j, B, self.order, self.order, len(self))
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
        _blossom_grid(self.dtype)(
            self._grid, x, i, j, B, self.order - 1, self.order, len(self))
        _deriv_grid(self.dtype)(
            self._grid, i, j, B, x.shape[-1], self.order)
        return self._to_coo_matrix(x, i, j, B)

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
        _blossom_grid(self.dtype)(
            self._grid, x, i, j, B, self.order - m, self.order, len(self))

        # NOTE(nrl) _deriv_basis derives B once, need to derive it m times.
        # Formula in book differentiates the spline in it's entirety but not
        # just the basis
        return self._to_coo_matrix(x, i, j, B)

    def gram(self):
        r"""Compute the gramian matrix of the base elements.

        The gramian is defined by:
        :math:`G_{ij} = \int B_i(x) B_j(x) dx`

        Returns:
           scipy.sparse.coo_matrix: a sparse p x p matrix [p=len(self)]
                                    containing the gramian values
        """
        p, w = leggauss(self.order, dtype=self.dtype)
        g = self._grid

        # linear transform grid-elements -> [-1,1]
        ak = np.repeat(0.5 * (g[1:]-g[:-1]), self.order)
        bk = np.repeat(0.5 * (g[1:]+g[:-1]), self.order)

        # integration grid
        nk = len(g) - 1
        pp = np.tile(p, nk)
        pp = ak * pp + bk

        # weights
        ww = np.tile(w, nk)
        N = len(ww)
        i = np.arange(N)
        W = scipy.sparse.coo_array((ak * ww, (i, i)), shape=(N, N))
        B = self.eval(pp)
        return B.T @ W @ B

    def __call__(self, x, p, deriv=0):
        if deriv == 0:
            B = self.eval(x)
        elif deriv == 1:
            B = self.deriv(x)
        else:
            B = self.deriv_m(x, m=deriv)
        return B @ p

    def linear_fit(self, x, y, w=None, beta=0):
        if x.shape != y.shape:
            raise ValueError('x and y must have the same shape')
        if w is not None and x.shape != w.shape:
            raise ValueError('x, y and w must have the same shape')

        # we now use cholmod, since it behaves much better than
        # scipy.sparse.linalg.spsolve when the size of the basis increases,
        # this is especially important in 2D (see below)
        J = self.eval(x)
        if w is not None:
            J.data *= w[J.row]
            yy = w * y
        else:
            yy = y

        JT = J.tocsr().T

        # TODO While https://github.com/scikit-sparse/scikit-sparse/pull/129 is
        # not merged and released, we want to ignore a false warning
        with warnings.catch_warnings():
            warnings.simplefilter(
                'ignore',
                category=sksparse.cholmod.CholmodTypeConversionWarning)
            factor = sksparse.cholmod.cholesky_AAt(JT, beta=beta)

        return factor(JT @ yy)
