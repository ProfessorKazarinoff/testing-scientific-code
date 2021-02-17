# test_dependancies.py

import platform
import sys

import pytest

import numpy as np
import pandas as pd
import matplotlib as mpl


def test_python_version():
    expected = "3.8.3"
    actual = platform.python_version()
    assert actual == expected


def test_numpy_version():
    expected = "1.18.5"
    actual = np.__version__
    assert actual == expected


def test_pandas_version():
    expected = "1.0.5"
    actual = pd.__version__
    assert actual == expected


def test_matplotlib_version():
    expected = "3.2.2"
    actual = mpl.__version__
    assert actual == expected


def test_system_encoding():
    expected = "utf-8"
    actual = sys.getfilesystemencoding()
    assert actual == expected
