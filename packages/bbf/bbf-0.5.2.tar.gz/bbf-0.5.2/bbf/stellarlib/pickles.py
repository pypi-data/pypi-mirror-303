
import importlib.resources

import pandas

from bbf.stellarlib import StellarLib


def fetch(basis=None):
    """
    """
    filename = (
        importlib.resources.files(__package__) / 'data' / 'pickles.parquet')
    if not filename.is_file():
        raise ValueError(f'file not found: {filename}')

    return StellarLib(pandas.read_parquet(filename), basis=basis)
