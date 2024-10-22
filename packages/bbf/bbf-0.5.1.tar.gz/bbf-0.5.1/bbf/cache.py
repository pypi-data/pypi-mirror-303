"""Access to a cache directory"""

import os
import pathlib

import platformdirs


def _get_cache_dir(env_variable, platformdirs_func):
    # environment variable overrides default platformdirs
    cache_dir = os.environ.get(env_variable)

    if cache_dir is None:
        cache_dir = pathlib.Path(platformdirs_func('bbf'))
    else:
        cache_dir = pathlib.Path(cache_dir)

    if not cache_dir.is_dir():
        if cache_dir.exists():
            raise RuntimeError(f"{cache_dir} not a directory")
        cache_dir.mkdir(parents=True)

    return cache_dir


def get_cache_dir():
    """Return a default location for caching stuff as a pathlib.Path object

    The cache directory is defined after the environment variable BBF_CACHE_DIR
    if existing, or is determined as a platform dependent location otherwise.

    """
    return _get_cache_dir("BBF_CACHE_DIR", platformdirs.user_cache_dir)


def get_data_dir():
    """Return a default location for caching stuff as a pathlib.Path object

    The data directory is defined after the environment variable BBF_DATA_DIR
    if existing, or is determined as a platform dependent location otherwise.

    """
    return _get_cache_dir("BBF_DATA_DIR", platformdirs.user_data_dir)
