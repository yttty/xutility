from decimal import Decimal

import numpy as np
import pytest

from xutility import Cast


def test_cast_none():
    assert Cast(None, allow_none=True).to(Decimal) is None
    with pytest.raises(ValueError):
        Cast(None, allow_none=False)


def test_cast_decimal():
    assert Cast(1).to(Decimal) == Decimal(1)
    assert Cast(1.234).to(Decimal) == Decimal("1.234")
    assert Cast("1.234").to(Decimal) == Decimal("1.234")
    assert Cast(Decimal("1.234")).to(Decimal) == Decimal("1.234")

    assert Cast(1.234).to(Decimal, 2) == Decimal("1.23")
    assert Cast(1.234).to(Decimal, 2) == Decimal("1.23")
    assert Cast(1.235).to(Decimal, 2) == Decimal("1.24")
    assert Cast(1.235).to(Decimal, 2, "ROUND_DOWN") == Decimal("1.23")


def test_cast_str():
    assert Cast(1).to(str) == "1"
    assert Cast(1.234).to(str) == "1.234"
    assert Cast("1.234").to(str) == "1.234"
    assert Cast(Decimal("1.234")).to(str) == "1.234"

    assert Cast(1.234).to(str, 2) == "1.23"
    assert Cast(1.234).to(str, 2) == "1.23"
    assert Cast(1.235).to(str, 2) == "1.24"
    assert Cast(1.235).to(str, 2, "ROUND_DOWN") == "1.23"


def test_cast_float():
    assert Cast(1).to(float) == 1.0
    assert isinstance(Cast(1).to(float), float)
    assert Cast(1.234).to(float) == 1.234

    assert Cast(1.234).to(float, 2) == 1.23
    assert Cast(1.234).to(float, 2) == 1.23
    assert Cast(1.235).to(float, 2) == 1.24
    assert Cast(1.235).to(float, 2, "ROUND_DOWN") == 1.23


def test_cast_np_float64():
    assert Cast(1).to(np.float64) == 1.0
    assert isinstance(Cast(1).to(np.float64), np.float64)
    assert Cast(1.234).to(np.float64) == 1.234


def test_cast_int():
    assert Cast(1).to(int) == 1
    assert isinstance(Cast(1).to(int), int)
    assert Cast(1.234).to(int) == 1

    assert Cast("1.234").to(int) == 1
    assert Cast("1.234").to(int, rounding="ROUND_UP") == 2
