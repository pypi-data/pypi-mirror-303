"""
"""

import numpy as np
import sncosmo


def retrieve_bandpass_model(name, version=None, average=False, radius=None):
    """get the bandpass or the bandpass interpolator from sncosmo"""
    # if average set to True, we explicitely want the averaged version of the
    # bandpasses
    if average and radius is None:
        return sncosmo.bandpasses._BANDPASSES.retrieve(name)

    if average and radius is not None:
        return sncosmo.bandpasses.get_bandpass(name, radius=radius)

    # otherwise, we want the variable version, unless it does not exists, in
    # which case we look into _BANDPASSES
    try:
        return sncosmo.bandpasses._BANDPASS_INTERPOLATORS.retrieve(name)
    except:
        return sncosmo.bandpasses._BANDPASSES.retrieve(name)


def check_bandpass_type(interp):
    """check whether interpolator is XY or radial and return a grid

    Will be replaced by isinstance() when XYBandpassInterpolator and
    RadialBandpassInterplator are implemented in sncosmo.

    """
    if isinstance(interp, sncosmo.bandpasses.Bandpass):
        return 'bandpass'

    x_min, x_max = interp.minpos(), interp.maxpos()
    if (
            isinstance(x_min, tuple) and len(x_min) == 2 and
            isinstance(x_max, tuple) and len(x_max) == 2
    ):
        return 'xy'

    if isinstance(x_min, float) and isinstance(x_max, float):
        return 'radial'

    raise ValueError(
        'do not know how to interpret interpolator minpos/maxpos')


def check_interp_xy_range(interp, size=10):
    """check whether interpolator is XY or radial and return a grid

    Will be replaced by isinstance() when XYBandpassInterpolator and
    RadialBandpassInterplator are implemented in sncosmo.

    """
    x_min, x_max = interp.minpos(), interp.maxpos()
    if isinstance(x_min, tuple) and len(x_min) == 2 and \
       isinstance(x_max, tuple) and len(x_max) == 2:
        xx = np.linspace(x_min[0], x_max[0], size)
        yy = np.linspace(x_min[0], x_max[0], size)
        return xx, yy
    elif isinstance(x_min, float) and isinstance(x_max, float):
        rad = np.linspace(x_min, x_max, size)
        return rad,
    raise ValueError(
        'do not know how to interpret interpolator minpos/maxpos')
