"""Test of the bbf.filterlib.Filterlib class"""

import numpy as np
import pytest

from bbf.filterlib import FilterLib
import bbf.stellarlib.pickles


# issue 15
def test_flux_without_sensorid(filterlib):
    pickles = bbf.stellarlib.pickles.fetch()

    with pytest.raises(ValueError) as err:
        filterlib.flux(
            pickles,
            [54, 12],  # stars
            ['ztf::g'],  # bands
            x=np.zeros(10) + 100,
            y=np.zeros(10) + 100)
    assert 'Missing sensor_id' in str(err)


def test_flux(filterlib):
    pickles = bbf.stellarlib.pickles.fetch()

    flux = filterlib.flux(
        pickles,
        np.random.randint(len(pickles), size=2),
        ['ztf::g'],
        x=np.zeros(5) + 100,
        y=np.zeros(5) + 100,
        sensor_id=np.zeros(5) + 1)

    assert flux.shape == (2, 5)


@pytest.mark.parametrize('compression', (None, 'lzma', 'bzip2'))
def test_save_load(tmp_path, compression):
    flib = FilterLib()

    filename = tmp_path / 'flib.pkl'
    flib.save(filename, compression=compression)

    filename = filename.with_suffix({
        None: '.pkl',
        'lzma': '.pkl.xz',
        'bzip2': '.pkl.bz2'}[compression])
    flib2 = FilterLib.load(filename)

    assert flib.bandpass_names == flib2.bandpass_names
