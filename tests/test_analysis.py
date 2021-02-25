# tests/test_analysis.py

import numpy as np

import analysis

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])


def test_tensile_strength():
    expected = 10.0
    actual = analysis.get_tensile_strength(y, x)
    assert round(expected, 3) == round(actual, 3)


def test_total_extension():
    expected = 3 - 1
    actual = analysis.get_total_extension(y, x)
    assert round(expected, 3) == round(actual, 3)
