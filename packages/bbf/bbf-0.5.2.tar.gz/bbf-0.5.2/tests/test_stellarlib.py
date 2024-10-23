import numpy as np

import bbf.stellarlib.gaia
import bbf.stellarlib.pickles
from bbf import SpecMagsys


# inspired by examples/gaia.py with 3 random observations
def test_gaia(filterlib):
    stars = [0, 0, 10]
    bands = ['ztf::g', 'ztf::r', 'ztf::I']
    x = [1914.06596272, 1431.41444064, 1387.35061568]
    y = [2653.92928505, 2711.83844245, 643.04916354]
    sensor_id = [19, 9, 13]

    gaia = bbf.stellarlib.gaia.fetch(
        ra_bound=[36, 36.1],
        dec_bound=[-4.2, -4])
    mags = SpecMagsys().mag(filterlib, gaia, stars, bands, x, y, sensor_id)

    assert np.allclose([17.75314192, 16.964202, 12.88735661], mags)


def test_pickles(filterlib):
    pickles = bbf.stellarlib.pickles.fetch()
    fluxes = filterlib.flux(pickles, [1, 4, 5], ['ztf::g', 'ztf::g', 'ztf::r'])
    assert np.allclose(
        fluxes,
        np.asarray([3.39769617e+14, 2.48825753e+14, 4.25911990e+14]))
