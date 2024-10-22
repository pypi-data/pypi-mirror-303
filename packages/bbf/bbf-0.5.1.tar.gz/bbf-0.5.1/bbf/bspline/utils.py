"""Utility functions related to B-splines"""

import functools

import numpy as np
import scipy


def _init_ijB(size, dtype=np.float64):
    """Initializes empty arrays (i, j, B) for a COO sparse matrix"""
    return (
        np.zeros((size,), dtype=np.int32),
        np.zeros((size,), dtype=np.int32),
        np.zeros((size,), dtype=dtype))


def refine_grid(grid, scale=0.5):
    dx = (grid[1:] - grid[:-1]).min()
    xmin, xmax = grid.min(), grid.max()
    N = int(np.floor((xmax - xmin) / (scale * dx)))
    return np.linspace(xmin, xmax, N)


@functools.cache
def leggauss(deg, dtype=np.float64):
    """A cached version of Gauss-Legendre quadrature"""
    x, y = np.polynomial.legendre.leggauss(deg)
    return x.astype(dtype), y.astype(dtype)


def gram(basis1, basis2, dtype=np.float64):
    r"""
    Compute the gramian matrix of elements of the two (different) bases
    ``basis1`` and ``basis2``.

    .. math::  G_{ij} = \int B_i(x) C_j(x) dx

    where B_i and C_j are elements of the two bases.

    """
    # Gaussian quadrature points and weights
    deg = basis1.order + basis2.order
    p, w = leggauss(deg, dtype=dtype)

    # points -- use the basis grids !
    x1 = np.linspace(basis1.range[0], basis1.range[1], basis1.n_knots+1, dtype=dtype)
    x2 = np.linspace(basis2.range[0], basis2.range[1], basis2.n_knots+1, dtype=dtype)
    x = np.hstack((x1,x2)) ; x.sort() ; x = np.unique(x)
    nk = len(x)-1
    ak = np.repeat(0.5*(x[1:]-x[:-1]), deg)
    bk = np.repeat(0.5*(x[1:]+x[:-1]), deg)
    pp = np.tile(p, nk)
    pp = ak * pp + bk

    # weights
    ww = np.tile(w, nk)
    N = len(ww)
    i = np.arange(N)
    W = scipy.sparse.coo_array((ak * ww, (i,i)), shape=(N,N), dtype=dtype)

    B1 = basis1.astype(dtype).eval(pp)
    B2 = basis2.astype(dtype).eval(pp)
    return B1.T @ W @ B2


def lgram(spectrum_basis, filter_basis, z=0, lambda_power=1):
    """Compute the :math:`\\lambda-`Gramian of both bases.

    When computing broadband fluxes, using transmission functions as
    spectra developed on spline bases, one needs to compute the
    following quantities:

    .. math::
         G_{ij} = \\int B_i(\\lambda) B_j(\\lambda) \\lambda d\\lambda

    This function computes the G-matrix above, and returns it as a
    sparse matrix. The spectrum basis may be shifted by a factor
    (1+z), for example:

    .. math::
         G_{ij} = \\int B_i(\\lambda) B_j(\\lambda / (1+z)) \\lambda d\\lambda

    """
    # Gaussian quadrature points and weights
    deg = spectrum_basis.order + filter_basis.order
    p, w = leggauss(deg)

    # points -- use the basis grids !
    if z > 0.:
        x1 = spectrum_basis.grid * (1.+z)
    else:
        x1 = spectrum_basis.grid / (1.-z)
    x2 = filter_basis.grid
    x = np.hstack((x1,x2)) ; x.sort() ; x = np.unique(x)
    nk = len(x)-1
    ak = np.repeat(0.5*(x[1:]-x[:-1]), deg)
    bk = np.repeat(0.5*(x[1:]+x[:-1]), deg)
    pp = np.tile(p, nk)
    pp = ak*pp + bk

    # weights
    ww = np.tile(w, nk)
    N = len(ww)
    i = np.arange(N)

    A_hc = 50341170.081942275 / (1.+z) ** 2
    W = scipy.sparse.coo_array(
        (ak * ww * A_hc * np.power(pp, lambda_power), (i,i)),
        shape=(N,N))

    B1 = spectrum_basis.eval(pp / (1.+ np.abs(z)))
    B2 = filter_basis.eval(pp)
    return B1.T @ W @ B2


def integ(basis, n=0):
    r"""
    Compute the integral (of n-th moments) of the spline basis functions.

    .. math::
       I_i^{[n]} = \int x^n B_i(x) dx

    Args:
      basis (bspline basis): 1-D bspline basis to integrate
      n (int): moment order

    Returns:
      a vector of length `len(basis)` containing the n-th moment of each function.
    """
    g = basis.grid
    aa = np.matrix(0.5 * (g[1:]-g[:-1]))
    bb = np.matrix(0.5 * (g[1:]+g[:-1]))
    nk = len(g) - 1

    x, w = leggauss(basis.order + n)

    xx = np.array(np.dot(aa.T, np.matrix(x)) + bb.T).flatten().squeeze()
    dx = np.array(np.dot(aa.T, np.matrix(np.ones(len(x))))).flatten().squeeze()

    J = basis.eval(xx)
    w = np.tile(w, nk) * xx**n * dx
    i,j = np.zeros(len(w)), np.arange(len(w))
    W = scipy.sparse.coo_array((w, (i,j)), shape=(1, len(w)))

    I = (W @ J).tocoo()

    return I.data[I.col]
