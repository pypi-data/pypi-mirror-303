"""Unit tests for __version__.py
"""

import bobleesj.release


def test_package_version():
    """Ensure the package version is defined and not set to the initial placeholder."""
    assert hasattr(bobleesj.release, "__version__")
    assert bobleesj.release.__version__ != "0.0.0"
