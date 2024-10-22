
from importlib.resources import files

import pandas

from bbf.stellarlib import StellarLib


def fetch(basis=None):
    """
    """
    path = files(__package__).joinpath('data', 'pickles.parquet')
    data = pandas.read_parquet(path)
    # if basis is None:
    #     wave = data.iloc[0].wave
    #     grid = np.arange(wave.min(), wave.max()+bin_width, bin_width)
    #     return StellarLib(data, basis=None, grid=grid)
    return StellarLib(data, basis=basis)
