# test_plot.py

import os
from pathlib import Path

import pytest
import numpy as np

import analysis

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])
fig, ax = analysis.plot(x, y, "my_title", "my_x_axis_label", "my_y_axis_label")


def test_tensile_strength():
    expected = 10.0
    actual = analysis.get_tensile_strength(y, x)
    assert round(expected, 3) == round(actual, 3)


def test_plot_x_axis_label():
    assert ax.xaxis.label.get_text() == "my_x_axis_label"


def test_plot_y_axis_label():
    assert ax.yaxis.label.get_text() == "my_y_axis_label"


def test_plot_title_label():
    assert ax.title.get_text() == "my_title"
