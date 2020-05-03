# test_plot.py

import pytest
import analysis
import numpy as np
import os
from pathlib import Path

x = np.array([1, 2, 3])
y = np.array([6, 7, 10])
fig, ax = analysis.plot(x, y, 'my_title', 'my_x_axis_label', 'my_y_axis_label')


def test_tensile_strength():
    expected = 10.0
    actual = analysis.get_tensile_strength(y,x)
    assert round(expected,3) == round(actual,3)

def test_plot_x_axis_label():
    assert ax.xaxis.label.get_text() == 'my_x_axis_label'

def test_plot_y_axis_label():
    assert ax.yaxis.label.get_text() == 'my_y_axis_label'

def test_plot_title_label():
    assert ax.title.get_text() == 'my_title'

def test_get_info():
    version_dict = analysis.get_info()
    assert version_dict['Python_major_version']>=3
    assert version_dict['Python_minor_version']>=6

def test_data_is_unchanged():
    fp1 = Path('data/raw_data.csv')
    d1 = os.stat(fp1)
    analysis.main()
    fp2 = Path('data/raw_data.csv')
    d2 = os.stat(fp2)
    assert d1 == d2
