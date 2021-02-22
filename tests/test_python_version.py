# tests/test_python_version.py

from pathlib import Path
import platform

import pytest


def test_python_version():
    rt_fp = Path(Path.cwd(),'runtime.txt')
    with open(rt_fp,'r') as f:
        v = f.readline().strip().split("-")[1]
    expected = v
    actual = platform.python_version()
    assert actual == expected
