"""Interface to Gaia spectra.

This interface relies on the existence of a calibrated version of the
Gaia DR3 spectra which has been made available on the CCIN2P3 at: 
/sps/ztf/data/calibrator/gaiaspectra

Files are indexed by healpix pixel ranges. 

Original files have been taken from the Gaia archive
https://cdn.gea.esac.esa.int/Gaia.

There are typically hundreds of thousand spectra in a given file, and
a few thousand files.

Given the high number of spectra, the stellar library is defined by a
some sky coordinate boundaries.
"""

import glob
import numpy as np
import os
import pandas as pd
import logging

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

from astroquery.gaia import GaiaClass
from astropy.table import Table
from gaiaxpy import calibrate
import healpy

from . import StellarLib
from .. import get_cache_dir, get_data_dir


def get_pixlist(cat, radius=1, level=8):
    """Return list of healpix pixel matching ra, dec coordinate of a
    given catalog.

    :param array cat: catalog with ra, dec
    :param int radius: query disc radius in degree
    :param int level: Gaia spectra are registered with healpix level 8 (nside=256)
    :return list pixlist: list of healpix pixels (in [0, 786431])
    """
    logging.debug(f"radius is {radius}")
    pixlist = []
    radius = np.radians(radius)
    nside = healpy.order2nside(level)
    for ra, dec in zip(cat["ra"], cat["dec"]):
        vec = healpy.ang2vec(ra, dec, lonlat=True)
        pixlist.append(
            healpy.query_disc(nside, vec, radius, inclusive=True, fact=4, nest=True)
        )
    pixlist = np.hstack(pixlist)
    return np.unique(pixlist)


def get_wave(gaia_dir):
    """Load Gaia spectra sampling.

    sampling is an output of gaiaxpy.calibrate
    :param str gaia_dir: location of calibrated spectra
    :return array wave: wavelength in nm
    """
    sampling = os.path.join(gaia_dir, "samplig_calibrated_spectra.txt")
    wave = np.loadtxt(sampling)
    return wave


def parse_md5sum(fn):
    """Use md5sum file to get the full list of files.

    :param str fn: md5sum file from https://cdn.gea.esac.esa.int/Gaia/gdr3/Spectroscopy/xp_continuous_mean_spectrum
    :return int list bins: first pixels
    :return str list ranges: list of pixel range used in filenames
    """
    with open(fn) as fid:
        lines = fid.readlines()
    ranges = [
        l.split("XpContinuousMeanSpectrum_")[-1].split(".csv.gz")[0] for l in lines
    ]
    bins = [int(b.split("-")[0]) for b in ranges]
    return bins, ranges


def get_pix_range(ra, dec, gaia_dir):
    """Return a list of pixel ranges matching indexing of gaia 36XX files.
    :param list ra:  ra
    :param list dec: dec
    :param str gaia_dir: location of calibrated spectra
    :return str list ranges: list of pixel range covered by sky corrdinates
    """
    pixlist = get_pixlist(
        pd.DataFrame({"ra": ra + ra, "dec": dec + dec[::-1]}),
        radius=max(float(np.diff(ra)), float(np.diff(dec))),
    )
    # todo span range
    md5sum = os.path.join(gaia_dir, "_MD5SUM.txt")
    if not os.path.exists(md5sum):
        url = "https://cdn.gea.esac.esa.int/Gaia/gdr3/Spectroscopy/xp_continuous_mean_spectrum/"
        os.system(f"wget {url}_MD5SUM.txt -O {md5sum}")

    bins, ranges = parse_md5sum(md5sum)
    f = [np.where(bins <= pix)[0][-1] for pix in pixlist]
    f = np.unique(f)
    logging.debug(f"pixlist: {pixlist}, selec: {np.array(ranges)[f]}")
    return [ranges[fi] for fi in f]


def get_ids(ra_min, ra_max, dec_min, dec_max, maxq=5000):
    """Return ids within given footprint

    :param float ra_min: min ra value in deg
    :param float ra_max: max ra value in deg
    :param float dec_min: min dec value in deg
    :param float dec_max: max dec value in deg
    :return dataframe ids: gaia source_id, ra, dec
    """
    gaia = GaiaClass(
        gaia_tap_server="https://gea.esac.esa.int/",
        gaia_data_server="https://gea.esac.esa.int/",
    )
    query = f"select TOP {maxq} source_id, ra, dec from gaiadr3.gaia_source where has_xp_continuous = 'True' and  ra <= {ra_max} and ra >= {ra_min} and dec <= {dec_max} and dec >= {dec_min}"
    job = gaia.launch_job_async(query, dump_to_file=False)
    ids = job.get_results()
    ids = pd.DataFrame(np.array(ids))
    return ids


def get_gaia_spectra(ids):
    """Return gaia spectra matching gaia ids."""
    gaia = GaiaClass(
        gaia_tap_server="https://gea.esac.esa.int/",
        gaia_data_server="https://gea.esac.esa.int/",
    )
    spectra = gaia.load_data(
        ids=ids["SOURCE_ID"],
        format="csv",
        data_release="Gaia DR3",
        data_structure="raw",
        retrieval_type="XP_CONTINUOUS",
        avoid_datatype_check=True,
    )
    data = spectra["XP_CONTINUOUS_RAW.csv"][0]
    return data


def retrieve_gaia_data(pixel_range, gaia_dir):
    """Load Gaia spectra.

    #todo: compute/save calibrated parquet file from original csv given by
    gaia archive.

    :param str pixel_range: pixel range
    :param str gaia_dir: location of calibrated spectra
    :return dataframe calibrated_spectra: source_id, flux, flux_error
    :return array sampling: wavelength in angstrom
    """
    cal_spectra_base = (
        f"XpContinuousMeanSpectrum_{pixel_range}_calibrated_spectra.parquet"
    )
    cal_spectra_fn = os.path.join(gaia_dir, "calibrated_spectra", cal_spectra_base)
    os.makedirs(os.path.dirname(cal_spectra_fn), exist_ok=True)
    if not os.path.exists(cal_spectra_fn):
        raise FileNotFoundError(cal_spectra_fn)
        # spectra_base = f"XpContinuousMeanSpectrum_{pixel_range}.csv.gz"
        # spectra_fn = os.path.join(gaia_dir,
        #                           "calibrated_spectra",
        #                           spectra_base)
        # url = "https://cdn.gea.esac.esa.int/Gaia/gdr3/Spectroscopy/xp_continuous_mean_spectrum/"
        # os.system(f"wget {url}{spectra_base} -O {spectra_fn}")
        # t = Table.read(spectra_fn, format='ascii.ecsv', guess=False).to_pandas()
        # spectra, sampling = calibrate(t)
        # spectra.to_parquet(cal_spectra_fn)
        # wave_fn = os.path.join(gaia_dir, "samplig_calibrated_spectra.txt")
        # if not os.exists(wave_fn):
        #     np.savetxt(wave_fn, sampling)
    else:
        calibrated_spectra = pd.read_parquet(cal_spectra_fn)
        sampling = get_wave(gaia_dir)

    calibrated_spectra["flux"] *= 100
    calibrated_spectra["flux_error"] *= 100
    return calibrated_spectra, sampling * 10


def fetch(basis=None, ra_bound=[], dec_bound=[], gaia_dir=None, on_the_fly=True):
    """Fetch some gaia spectra matching sky coordinate and return them in
    a StellarLib.

    :param BSpline (1D) or np.ndarray basis: the internal basis
    :param 2-elements list ra_bound: ra lower and upper bounds
    :param 2-elements list dec_bound: dec lower and upper bounds
    :param str gaia_dir: location of calibrated spectra
    :return stellarlib sps: a stellar lib object
    """
    if gaia_dir is None:
        gaia_dir = os.path.join(get_data_dir(), "gaia")
        os.makedirs(gaia_dir, exist_ok=True)

    ids = get_ids(*(ra_bound + dec_bound))
    logging.info(f"Selec {len(ids)} within footprint")

    if on_the_fly:
        logging.info(f"Retrieve spectra on the fly")
        filename = os.path.join(gaia_dir, "spectra.csv")
        try:
            os.remove(filename)
        except OSError:
            pass
        _spectra = get_gaia_spectra(ids)
        _spectra.write(filename)
        data, sampling = calibrate(filename, save_file=False)
        data = data.assign(ra=ids["ra"], dec=ids["dec"])
        data["flux"] *= 100
        data["flux_error"] *= 100
        data = data.set_index("source_id")  # needed to join
        sp = StellarLib(data, basis=basis, wave=sampling * 10, project=False)  # 2 nm
        sp.coeffs = sp.project(one_by_one=True)  # same_wave_grid projection not working
        return sp

    pix_range = get_pix_range(ra_bound, dec_bound, gaia_dir)
    logging.info(f"Footprint covers {len(pix_range)} pixel range(s)")
    ids = ids.set_index("SOURCE_ID")  # needed to join

    sps = []
    for pr in pix_range:
        logging.info(f"Fetching pixel range {pr}")
        data, sampling = retrieve_gaia_data(pr, gaia_dir)
        data = data.set_index("source_id")  # needed to join
        logging.info(f"{len(data)} spectra within pixel range")
        data = data.join(ids, how="inner")  # join is the fastest option
        data = data.assign(ra=ids["ra"][data.index], dec=ids["dec"][data.index])
        logging.info(f"Xcheck: {len(data)}")
        if len(data) == 0:
            continue
        sp = StellarLib(data, basis=basis, wave=sampling, project=False)
        sp.coeffs = sp.project(one_by_one=True)  # same_wave_grid projection not working
        sps.append(sp)

    # stacking stellar libs if more than 1 pixel range.
    for i in range(1, len(sps)):
        sps[0].stack(sps[i])
    return sps[0]
