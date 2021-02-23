# tests/test_data_unchanged.py

import os
from pathlib import Path

import pytest

import analysis


def test_data_is_unchanged():
    fp1 = Path("data/raw_data.csv")
    d1 = os.stat(fp1)
    analysis.main()
    fp2 = Path("data/raw_data.csv")
    d2 = os.stat(fp2)
    assert (
        d1.st_mode == d2.st_mode
        and d1.st_ino == d2.st_ino
        and d1.st_dev == d2.st_dev
        and d1.st_nlink == d1.st_nlink
        and d1.st_uid == d2.st_uid
        and d1.st_gid == d2.st_gid
        and d1.st_size == d2.st_size
        and d1.st_mtime == d2.st_mtime
        and d1.st_ctime == d2.st_ctime
    )
