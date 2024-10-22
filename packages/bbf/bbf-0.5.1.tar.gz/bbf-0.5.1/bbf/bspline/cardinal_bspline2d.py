"""2D-BSpline basis of arbitrary order, defined on a regular grid"""

import numpy as np

from bbf.bspline.bspline2d import BSpline2D
from bbf.bspline.cardinal_bspline import CardinalBSpline


class CardinalBSpline2D(BSpline2D):
    """2D-BSpline basis of arbitrary order, defined on a regular grid"""
    def __init__(
            self, xstart, xstop, xnum,
            ystart, ystop, ynum,
            xorder=4, yorder=4, dtype=np.float64):
        self.bx = CardinalBSpline(
            xstart, xstop, xnum, order=xorder, dtype=dtype)
        self.by = CardinalBSpline(
            ystart, ystop, ynum, order=yorder, dtype=dtype)
        self._dtype = dtype
