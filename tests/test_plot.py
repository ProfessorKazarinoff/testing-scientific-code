# tests/test_plot.py

import pytest
import numpy as np
import matplotlib

import analysis

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])
fig, ax = analysis.plot(x, y, "my_title", "my_x_axis_label", "my_y_axis_label","plot.png")


def test_plot_x_axis_label():
    assert ax.xaxis.label.get_text() == "my_x_axis_label"


def test_plot_y_axis_label():
    assert ax.yaxis.label.get_text() == "my_y_axis_label"


def test_plot_title_label():
    assert ax.title.get_text() == "my_title"


def test_figure_object():
    assert type(fig) == matplotlib.figure.Figure

def test_save_png(tmpdir):
    file = tmpdir.join('plot.png')
    analysis.plot(x, y, "my_title", "my_x_axis_label", "my_y_axis_label",file.strpath)

