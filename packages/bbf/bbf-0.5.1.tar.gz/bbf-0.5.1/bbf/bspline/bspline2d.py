"""2D B-spline bases"""

import warnings

import numpy as np
import scipy
import sksparse

from bbf.bspline.bspline import BSpline


class BSpline2D:
    """
    2D BSpline basis of arbitrary order,
    defined on an arbitrary grid

    The basis is the cross-product of two 1D BSpline bases, along x and y:

    .. math::
       B_{ij} = B_i(x) \\times B_j(y)
    """
    def __init__(self, gx, gy, x_order=4, y_order=4, dtype=np.float64):
        self.bx = BSpline(gx, order=x_order, dtype=dtype)
        self.by = BSpline(gy, order=y_order, dtype=dtype)
        self._dtype = dtype

    @property
    def dtype(self):
        return self._dtype

    def __len__(self):
        """
        return the size of the basis
        """
        return len(self.bx) * len(self.by)

    @property
    def nj(self):
        warnings.warn(
            "The property `basis.nj` is deprecated, use `len(basis)` instead",
            DeprecationWarning)

        return len(self)

    def astype(self, dtype):
        """Copies the BSpline2D to the specified data type

        The `dtype` must be either np.float32 or np.float64 or a ValueError is
        raised. If the requested `dtype` is the same as the actual spline, no
        copy is done.

        """
        if self.dtype == dtype:
            return self
        basis = BSpline2D.__new__(BSpline2D)
        basis.bx = self.bx.astype(dtype)
        basis.by = self.by.astype(dtype)
        basis._dtype = dtype
        return basis

    def _cross(self, N, ix, jx, vx, iy, jy, vy):
        """
        compute the cross-product:

        .. math::
           B_{ij}(x,y) = B_i(x) \times B_j(y)

        Args:
          N: (int)
             number of points (N=len(x))
          i: ndarray of ints
             a ndarray containing the row-indices in the jacobian matrix
          jx: ndarray of ints
              the column indices in the matrix returned by the x-basis
          vx: ndarray of floats,
              the values B_j(x)
          jy: ndarray of ints
              the column indices in the matrix returned by the y-basis
          vy: ndarray of floats
              the values B_j(y)

        Returns:
          J: (scipy.sparse.coo_matrix)
              the values of the cross-product as a (N,n) sparse jacobian matrix,
              [N is the number of points, n the size of the 2D-basis]

        Note:
          This implementation makes an assumption on how the return value
          of ``BSpline.eval'' is sorted internally.
          See the documentation of this routine above.

        TODO:
          One could gain ~ a factor 2 in execution time, by implementing
          the tile's and repeat's in C.

        """
        xo, yo = self.bx.order, self.by.order

        i_ = ix.reshape(-1, xo).repeat(yo, axis=1).ravel()
        jx_ = jx.reshape(-1, xo).repeat(yo, axis=1).ravel()
        vx_ = vx.reshape(-1, xo).repeat(yo, axis=1).ravel()
        jy_ = np.tile(jy.reshape(-1, yo), (1, xo)).ravel()
        vy_ = np.tile(vy.reshape(-1, yo), (1, xo)).ravel()
        data_ = vx_ * vy_
        j_ = jy_ * len(self.bx) + jx_
        return scipy.sparse.coo_matrix(
            (data_, (i_, j_)),
            shape=(N, len(self)),
            dtype=self.dtype)

    def eval(self, x, y):
        """
        evaluate and return the values of the basis functions for (x,y)

        Args:
          x: (ndarray of floats)
              x-coordinates of the entry points
          y: (ndarray of floats)
              y-coordinates of the entry points

        Returns:
          B: (scipy.sparse.coo_matrix)
              a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
              containing the basis values: B_{ij} = B_j(x_i)
        """
        if len(x) != len(y):
            raise ValueError('x and y should have the same length')
        N = len(x)

        Jx = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jy = self.by.eval(y)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        r = self._cross(N, ix, jx, vx, iy, jy, vy)
        return r

    def gradient(self, x, y):
        """
        evaluate and return the derivatives vs. x and y of the basis functions for (x,y)

        Args:
          x: (ndarray of floats)
              x-coordinates of the entry points
          y: (ndarray of floats)
              y-coordinates of the entry points

        Returns:
          dvdx: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j'(x_i) * B_j(y_i)
          dvdy: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j(x_i) * B_j'(y_i)
        """
        if len(x) != len(y):
            raise ValueError('x and y should have the same length')
        N = len(x)

        Jxp = self.bx.deriv(x)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy = self.by.eval(y)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx = self._cross(N, ix, jx, vx, iy, jy, vy)

        ix = jx = vx = None
        iy = jy = vy = None

        Jx = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jyp = self.by.deriv(y)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy = self._cross(N, ix, jx, vx, iy, jy, vy)

        return ddx, ddy

    def hessian(self, x, y):
        if len(x) != len(y):
            raise ValueError('x and y should have the same length')
        N = len(x)

        Jxp = self.bx.deriv_m(x, m=2)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy = self.by.eval(y)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx2 = self._cross(N, ix, jx, vx, iy, jy, vy)

        ix = jx = vx = None
        iy = jy = vy = None

        Jx = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jyp = self.by.deriv_m(y, m=2)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy2 = self._cross(N, ix, jx, vx, ix, jy, vy)

        ix = jx = vx = None
        iy = jy = vy = None

        Jxp = self.bx.deriv_m(x, m=1)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jyp = self.by.deriv_m(y, m=1)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddxy = self._cross(N, ix, jx, vx, ix, jy, vy)

        return ddx2, ddy2, ddxy

    def __call__(self, x, y, p, deriv=0):
        if deriv == 0:
            B = self.eval(x, y)
        elif deriv == 1:
            B = self.gradient(x, y)
        else:
            raise NotImplementedError('m>1 derivatives not implemented')
        return B @ p

    def linear_fit(self, x, y, v, w=None):
        """fit the basis coefficients on the data passed in argument

        Perform a least square fit of the basic coefficients.

        Args:
            x (ndarray of floats): x coordinates
            y (ndarray of floats): y coordinates
            v (ndarray of floats): values

        Returns:
            ndarray of floats: fit solution, i.e. basis coefficients

        .. note: ~ 12 seconds on a Intel(R) Core(TM) i5-2540M CPU @ 2.60GHz
                 for 10^6 values and a 10x10 basis. Dominated by the cholesky
                 factorization.
        """
        J = self.eval(x, y)
        if w is not None:
            J.data *= w[J.row]
            vv = w * v
        else:
            vv = v

        factor = sksparse.cholmod.cholesky_AAt(J.T)
        return factor(J.T @ vv)
