"""Interface to the CalSpec spectral library

We use the external module getCalspec, developped and maintained by Jeremy
Neveu

"""

import sys
import glob
import logging

import numpy as np
import pandas
import getCalspec

from bbf import get_cache_dir
from bbf.bspline import BSpline
from bbf.stellarlib import StellarLib


logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO)


def fetch(basis=None, bin_width=10, rebuild=False):
    """fetch the calspec spectra and return them in a StellarLib

    TODO:
      - we need to version the various releases of the CALSPEC library
      - we need an option to return either the models, or the STIS data
      - add a kill list or a selection (?)
    """
    # there might be a cached version of the library
    cache_dir = get_cache_dir()
    cache_version = glob.glob(str(cache_dir.joinpath('calspec_*.parquet')))
    if len(cache_version) > 0:
        if not rebuild:
            logging.info(f'calspec: reading from {cache_dir}')
            sp = StellarLib.from_parquet(cache_dir.joinpath('calspec'), basis=basis)
            return sp

    # otherwise, re-read all spectra from getCalspec
    logging.info(f'calspec: rebuilding library with getCalspec')
    df = getCalspec.getCalspec.getCalspecDataFrame()
    data = {'name': [], 'star_name': [], 'wave': [], 'flux': [], 'fluxerr': [], 'fluxerrsys': []}
    for i, star_name in enumerate(df.Star_name):
        try:
            d = df.iloc[i]
            # fetch data *before* adding in into data, otherwise,
            # we may end up with an inconsistent structure
            # exceptions may happen here, since calspec format
            # is not always very consistent
            spec = getCalspec.Calspec(star_name).get_spectrum_numpy()
            wave = np.array(spec['WAVELENGTH']).astype(np.float64)
            flux = np.array(spec['FLUX']).astype(np.float64)
            staterror = np.array(spec['STATERROR']).astype(np.float64)
            syserror = np.array(spec['SYSERROR']).astype(np.float64)
            # OK, now fill the structure
            data['wave'].append(wave)
            data['flux'].append(flux)
            data['fluxerr'].append(staterror)
            data['fluxerrsys'].append(syserror)
            data['name'].append(d.Name)
            data['star_name'].append(star_name)
        except:
            logging.warning(f'unable to fetch: {star_name}')
            print(sys.exc_info())
            continue

    # stuff all that into a DataFrame
    data = pandas.DataFrame(data)

    # TODO: simplify this
    sp = StellarLib(data, basis=basis)

    # write it to cache for future use
    logging.info(f'caching to: {cache_dir}')
    sp.to_parquet(cache_dir.joinpath('calspec'))

    return sp
