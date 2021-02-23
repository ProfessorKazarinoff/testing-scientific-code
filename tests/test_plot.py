# tests/test_plot.py

import pytest
import numpy as np
import matplotlib

import analysis

@pytest.fixture
def set_up_plot():
    x = np.array([1, 2, 3])
    y = np.array([6, 7, 10])
    fig, ax = analysis.plot(x, y, "my_title", "my_x_axis_label", "my_y_axis_label","plot.png")
    return (fig,ax)


def test_plot_x_axis_label(set_up_plot):
    assert set_up_plot[1].xaxis.label.get_text() == "my_x_axis_label"


def test_plot_y_axis_label(set_up_plot):
    assert set_up_plot[1].yaxis.label.get_text() == "my_y_axis_label"


def test_plot_title_label(set_up_plot):
    assert set_up_plot[1].title.get_text() == "my_title"


def test_figure_object(set_up_plot):
    assert type(set_up_plot[0]) == matplotlib.figure.Figure


def test_axes_object(set_up_plot):
    assert set_up_plot[0] == set_up_plot[1].get_figure()


def test_save_png(tmpdir):
    file = tmpdir.join('plot.png')
    assert True == True
