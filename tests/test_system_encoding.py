# tests/test_system_encoding.py

import sys


def test_system_encoding():
    expected = "utf-8"
    actual = sys.getfilesystemencoding()
    assert actual == expected
