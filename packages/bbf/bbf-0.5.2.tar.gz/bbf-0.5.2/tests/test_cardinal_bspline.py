"""Tests for the bbf.bspline.{CardinalBSpline,CardinalBSpline2D} classes"""

import numpy as np
import pytest

from bbf.bspline import (
    BSpline, BSpline2D, CardinalBSpline, CardinalBSpline2D)


# those two tests ensure we get the same result using BSpline and
# CardinalBSpline in 1d and 2d.

def test_1d():
    x = np.asarray([0.15, 0.3, 2, 3.2], dtype=np.float64)
    n = 10
    start = 0
    stop = 4

    s1 = BSpline(np.linspace(start, stop, n+1))
    s2 = CardinalBSpline(start, stop, n)
    assert s1 != s2
    assert s2 == s2
    assert s2.astype(np.float32) != s2

    assert np.allclose(s1.gram().toarray(), s2.gram().toarray())
    assert np.allclose(s1.eval(x).toarray(), s2.eval(x).toarray())
    assert np.allclose(s1.deriv(x).toarray(), s2.deriv(x).toarray())
    assert np.allclose(s1.deriv_m(x).toarray(), s2.deriv_m(x).toarray())


def test_2d():
    x = np.asarray([0.15, 0.3, 2, 3.2], dtype=np.float64)
    y = np.asarray([0.1, 0.25, 0.9, 1.7], dtype=np.float64)

    n = 5
    xstart = 0
    xstop = 4
    ystart = 0
    ystop = 2

    s1 = BSpline2D(
        np.linspace(xstart, xstop, n+1),
        np.linspace(ystart, ystop, n+1))
    s2 = CardinalBSpline2D(xstart, xstop, n, ystart, ystop, n)
    assert s1 != s2
    assert s2 == s2
    assert s2.astype(np.float32) != s2

    assert np.allclose(s1.eval(x, y).toarray(), s2.eval(x, y).toarray())
