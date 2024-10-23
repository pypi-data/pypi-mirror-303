"""Implementation of 1-D and 2-D B-spline bases.

.. note: on the grids on which the B-Splines are defined

      -----+------+--- ... --+-----+--- ... -----+-----+--
          -k    -k+1         0     1             N
                             [ specified by user ]
           [       internal, extended grid       ]

.. note::

    For simple interpolation, prefeer to use scipy.interpolation.BSpline. The
    reason we do not use them is (1) does not return the jacobian as a sparse
    matrix (2) slower on large arrays. The reason why we use our own version of
    bsplines, is precisely that we need the jacobian when training models, and
    since we have typically O(10^5 - 10^6) points and thousands of parameters,
    we need it as a sparse matrix.

"""


from .bspline import BSpline
from .bspline2d import BSpline2D
from .cardinal_bspline import CardinalBSpline
from .cardinal_bspline2d import CardinalBSpline2D
from .projector import Projector
from .utils import (
    leggauss,
    gram,
    lgram,
    integ,
    refine_grid)
