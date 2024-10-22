"""Defines pytest fixtures"""

import pytest
import lemaitre.bandpasses


@pytest.fixture
def filterlib():
    return lemaitre.bandpasses.get_filterlib()
