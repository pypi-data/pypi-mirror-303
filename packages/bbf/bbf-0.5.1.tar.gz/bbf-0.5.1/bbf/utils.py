"""Miscellaneous utility functions"""

import numpy as np


def check_sequence(x, cond):
    """Returns True if `x` is a sequence and all `e` in `x` satisfies `cond(e)`

    Returns False otherwise.

    """
    try:
        return all(cond(e) for e in x)
    except TypeError:
        # x is not a sequence
        return False


def is_list_of_callables(x):
    """Returns True if `x` is a sequence of callables, False otherwise"""
    return check_sequence(x, callable)


def sort_bands_by_mean_wavelength(tr):
    """sort the transmissions in ascending wavelength order

    Parameters
    ----------
    tr: list of `sncosmo.Bandpass`
        List or dictionary of `sncosmo` transmissions

    Returns
    -------
    If `tr` is a dictionary, a list of dictionary keys that sort the
    transmissions in ascending wavelength order.

    If `tr`` is a list (or can be converted to a list), a list of indices that
    allow to sort the transmissions in ascending wavelength order.

    """
    if isinstance(tr, dict):
        trans_db = tr
    else:
        try:
            tr = list(tr)
        except TypeError as exc:
            raise ValueError(f"don't know how to handle {type(tr)} ") from exc
        trans_db = dict(zip([t.name for t in tr], tr))

    wl = np.array([trans_db[k].wave_eff for k in trans_db])
    iband = np.argsort(wl)
    if not isinstance(tr, dict):
        return iband

    keys = np.array(list(trans_db.keys()))
    ordered_keys = keys[iband]
    return ordered_keys
