# tests/test_dependencies.py

from pathlib import Path

import matplotlib as mpl
import numpy as np
import pandas as pd

fp = Path(Path.cwd(), "requirements.txt")
with open(fp, "r") as f:
    v = f.readlines()
d = {}
for l in v:
    r = l.split("==")[0]
    ver = l.split("==")[1].strip()
    d[r] = ver


def test_numpy_version():
    expected = d["numpy"]
    actual = np.__version__
    assert actual == expected


def test_pandas_version():
    expected = d["pandas"]
    actual = pd.__version__
    assert actual == expected


def test_matplotlib_version():
    expected = d["matplotlib"]
    actual = mpl.__version__
    assert actual == expected
