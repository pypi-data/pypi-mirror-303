"""Tests for the bbf.bspline.BSpline class"""

import numpy as np
import pytest

import bbf.bspline

# The `expected` arrays from the following tests have been computed with bbf at
# the commit 27adf5e3 (July, 2024):
# https://gitlab.in2p3.fr/lemaitre/bbf/-/tree/27adf5e331d2d434d5dc66ed7e2894fdc8bfe780.
# The tests below simply ensure the results are stable accross bbf versions.
# Below is the code snippet to generate the `expected` arrays.
#
#   from bbf.bspline import BSpline
#   import numpy as np
#   grid = np.asarray([0, 1, 4, 5], dtype=np.float64)
#   x = np.asarray([0.15, 0.3, 2, 3.2], dtype=np.float64)
#   s = BSpline(grid, order=4)
#   G = s.gram()
#   J0 = s.eval(x).toarray()
#   J1 = s.deriv(x).toarray()
#   J2 = s.deriv_m(x).toarray()
#   F = s.linear_fit(x, np.asarray([0.1, 0.2, 1, 3], dtype=np.float64), beta=1e-8)

@pytest.fixture
def basis():
    knots = np.asarray([0, 1, 4, 5], dtype=np.float64)
    return lambda dtype: bbf.bspline.BSpline(knots, order=4, dtype=dtype)


@pytest.fixture
def x():
    return np.asarray([0.15, 0.3, 2, 3.2], dtype=np.float64)


def test_bad_init():
    B = bbf.bspline.BSpline

    with pytest.raises(ValueError) as err:
        B([])
        assert 'need at least two unique points' in str(err)

    with pytest.raises(ValueError) as err:
        B([1])
        assert 'need at least two unique points' in str(err)

    with pytest.raises(ValueError) as err:
        B([1, 1, 1])
        assert 'need at least two unique points' in str(err)

    with pytest.raises(ValueError) as err:
        B([1, 2, 1])
        assert 'must be sorted' in str(err)

    with pytest.raises(ValueError) as err:
        B([1, 2, np.nan])
        assert 'should not have nans' in str(err)

    with pytest.raises(ValueError) as err:
        B([[1, 2], [3, 4]])
        assert 'must be one-dimensional' in str(err)

    with pytest.raises(ValueError) as err:
        B([1, 2], order=1)
        assert 'order must be greater or equal to 2' in str(err)

    with pytest.raises(ValueError) as err:
        B([1, 2], order=2, dtype=int)
        assert 'dtype must be' in str(err)


def test_basics(basis):
    B = basis(np.float64)
    assert B.dtype == np.float64
    assert B.order == 4
    assert B.degree == 3
    assert len(B) == 6
    assert B.nknots == 4
    assert B.range == (0, 5)
    assert np.allclose(B.grid, np.asarray([0, 1, 4, 5]))


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_gram(basis, dtype):
    expected = np.asarray([
        [3.96825397e-03, 3.03769841e-02, 7.26190476e-03, 5.95238095e-05, 0.00000000e+00, 0.00000000e+00],
        [3.03769841e-02, 5.12777778e-01, 3.64470238e-01, 7.13690476e-02, 4.33928571e-03, 0.00000000e+00],
        [7.26190476e-03, 3.64470238e-01, 6.50642857e-01, 3.81196429e-01, 7.13690476e-02, 5.95238095e-05],
        [5.95238095e-05, 7.13690476e-02, 3.81196429e-01, 6.50642857e-01, 3.64470238e-01, 7.26190476e-03],
        [0.00000000e+00, 4.33928571e-03, 7.13690476e-02, 3.64470238e-01, 5.12777778e-01, 3.03769841e-02],
        [0.00000000e+00, 0.00000000e+00, 5.95238095e-05, 7.26190476e-03, 3.03769841e-02, 3.96825397e-03]])

    result = basis(dtype).gram().toarray()
    assert result.dtype == dtype
    assert np.allclose(expected, result)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_eval(basis, x, dtype):
    expected = np.asarray([
        [1.02354167e-01, 7.46402083e-01, 1.51075000e-01, 1.68750000e-04, 0.00000000e+00, 0.00000000e+00],
        [5.71666667e-02, 7.29883333e-01, 2.11600000e-01, 1.35000000e-03, 0.00000000e+00, 0.00000000e+00],
        [0.00000000e+00, 1.33333333e-01, 5.50000000e-01, 3.00000000e-01, 1.66666667e-02, 0.00000000e+00],
        [0.00000000e+00, 8.53333333e-03, 2.40400000e-01, 5.73600000e-01, 1.77466667e-01, 0.00000000e+00]])

    result = basis(dtype).eval(x).toarray()
    assert result.dtype == dtype
    assert np.allclose(expected, result)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_deriv(basis, x, dtype):
    expected = np.asarray([
        [-0.36125 , -0.018625,  0.3765  ,  0.003375,  0.      ,  0.      ],
        [-0.245   , -0.1945  ,  0.426   ,  0.0135  ,  0.      ,  0.      ],
        [ 0.      , -0.2     , -0.15    ,  0.3     ,  0.05    ,  0.      ],
        [ 0.      , -0.032   , -0.294   ,  0.084   ,  0.242   ,  0.      ]])

    result = basis(dtype).deriv(x).toarray()
    assert result.dtype == dtype
    assert np.allclose(expected, result)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_deriv_m(basis, x, dtype):
    expected = np.asarray([
        [0., 0., 0.85, 0.15, 0., 0.],
        [0., 0. , 0.7 , 0.3 , 0. , 0.],
        [0. , 0. , 0. , 0.66666667, 0.33333333, 0.],
        [0., 0. ,0. , 0.26666667, 0.73333333, 0.]])

    result = basis(dtype).deriv_m(x).toarray()
    assert result.dtype == dtype
    assert np.allclose(expected, result)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_linear_fit(basis, x, dtype):
    expected = np.asarray(
        [-3.7772559 ,  0.85825059, -1.0244324 ,  4.65127131,  3.21739508, 0.])

    fit = basis(dtype).linear_fit(
        x,
        np.asarray([0.1, 0.2, 1, 3], dtype=np.float64),
        beta=1e-8)

    assert np.allclose(expected, fit)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
def test_linear_fit_weighted(basis, x, dtype):
    w = np.asarray([1, 1, 0, 1])
    expected = np.asarray(
        [0.05848361, -0.19117535,  1.56215506,  4.17807009,  1.29347119, 0.])

    fit = basis(dtype).linear_fit(
        x,
        np.asarray([0.1, 0.2, 1, 3], dtype=np.float64),
        w=w,
        beta=1e-8)

    assert np.allclose(expected, fit)


@pytest.mark.parametrize('dtype', (np.float32, np.float64))
@pytest.mark.parametrize('z, expected', (
    (0, np.asarray([
        [4.64257457e+04, 2.71043252e+05, 1.01721126e+05, 3.19626477e+02],
        [7.34661457e+05, 5.66282229e+06, 2.80328401e+06, 2.84467564e+04],
        [8.72660188e+05, 8.19458361e+06, 4.70913679e+06, 6.74411866e+04],
        [8.47010163e+04, 9.60477563e+05, 6.21673497e+05, 1.11869267e+04]])),
    (-0.1, np.asarray([
        [6.65200510e+04, 4.02345760e+05, 1.57146827e+05, 6.34809351e+02],
        [1.03651681e+06, 8.70814194e+06, 4.72785255e+06, 6.74059112e+04],
        [1.25626658e+06, 1.35239639e+07, 8.77044663e+06, 1.77370506e+05],
        [1.31649087e+05, 1.78402593e+06, 1.31866415e+06, 3.29057663e+04]])),
    (0.1, np.asarray([
        [4.45300411e+04, 2.69346995e+05, 1.05207292e+05, 4.25422841e+02],
        [6.79379181e+05, 5.57025111e+06, 2.94172159e+06, 3.78626328e+04],
        [7.81649425e+05, 8.00179227e+06, 4.97061586e+06, 8.97642193e+04],
        [7.31672949e+04, 9.31313245e+05, 6.58668664e+05, 1.48897994e+04]]))))
def test_lgram(dtype, z, expected):
    b1 = bbf.bspline.BSpline([0, 1], dtype=dtype)
    b2 = bbf.bspline.BSpline([0, 2.5], dtype=dtype)

    lgram = bbf.bspline.lgram(b1, b2, z=z).toarray()

    assert lgram.dtype == np.float64
    assert np.allclose(lgram, expected)
