import pytest

from decimaldate import DecimalDate, DecimalDateRange

###

dd_09_29: DecimalDate = DecimalDate(2024_09_29)
dd_09_30: DecimalDate = DecimalDate(2024_09_30)

dd_10_01: DecimalDate = DecimalDate(2024_10_01)
dd_10_02: DecimalDate = DecimalDate(2024_10_02)
dd_10_03: DecimalDate = DecimalDate(2024_10_03)
dd_10_04: DecimalDate = DecimalDate(2024_10_04)
dd_10_05: DecimalDate = DecimalDate(2024_10_05)
dd_10_06: DecimalDate = DecimalDate(2024_10_06)
dd_10_07: DecimalDate = DecimalDate(2024_10_07)
dd_10_08: DecimalDate = DecimalDate(2024_10_08)
dd_10_09: DecimalDate = DecimalDate(2024_10_09)
dd_10_10: DecimalDate = DecimalDate(2024_10_10)

dd_10_11: DecimalDate = DecimalDate(2024_10_11)
dd_10_12: DecimalDate = DecimalDate(2024_10_12)
dd_10_13: DecimalDate = DecimalDate(2024_10_13)
dd_10_14: DecimalDate = DecimalDate(2024_10_14)
dd_10_15: DecimalDate = DecimalDate(2024_10_15)
dd_10_16: DecimalDate = DecimalDate(2024_10_16)
dd_10_17: DecimalDate = DecimalDate(2024_10_17)
dd_10_18: DecimalDate = DecimalDate(2024_10_18)
dd_10_19: DecimalDate = DecimalDate(2024_10_19)
dd_10_20: DecimalDate = DecimalDate(2024_10_20)

dd_10_21: DecimalDate = DecimalDate(2024_10_21)
dd_10_22: DecimalDate = DecimalDate(2024_10_22)
dd_10_23: DecimalDate = DecimalDate(2024_10_23)
dd_10_24: DecimalDate = DecimalDate(2024_10_24)
dd_10_25: DecimalDate = DecimalDate(2024_10_25)
dd_10_26: DecimalDate = DecimalDate(2024_10_26)
dd_10_27: DecimalDate = DecimalDate(2024_10_27)
dd_10_28: DecimalDate = DecimalDate(2024_10_28)
dd_10_29: DecimalDate = DecimalDate(2024_10_29)
dd_10_30: DecimalDate = DecimalDate(2024_10_30)
dd_10_31: DecimalDate = DecimalDate(2024_10_31)

dd_11_01: DecimalDate = DecimalDate(2024_11_01)


sut_start_incl = dd_10_21
sut_stop_excl = dd_10_26
sut: DecimalDateRange = DecimalDateRange(sut_start_incl, sut_stop_excl)


"""
__contains__
"""


def test_contains() -> None:
    # THEN
    assert dd_10_01 not in sut
    assert dd_10_20 not in sut
    assert dd_10_21 in sut
    assert dd_10_22 in sut
    assert dd_10_23 in sut
    assert dd_10_24 in sut
    assert dd_10_25 in sut
    assert dd_10_26 not in sut
    assert dd_11_01 not in sut


def test_contains_invalid_type_raises_typeerror() -> None:
    with pytest.raises(expected_exception=TypeError):
        _ = "3" in sut  # type: ignore[operator]


def test_contains_1_7_1() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 1)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 in sut
    assert dd_10_03 in sut
    assert dd_10_04 in sut
    assert dd_10_05 in sut
    assert dd_10_06 in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_2() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 2)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 in sut
    assert dd_10_04 not in sut
    assert dd_10_05 in sut
    assert dd_10_06 not in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_3() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 3)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_4() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 4)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 in sut
    assert dd_10_06 not in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_5() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 5)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_6() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 6)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_1_7_7() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 7)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 not in sut
    assert dd_10_08 not in sut


def test_contains_7_1_1() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -1)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 in sut
    assert dd_10_03 in sut
    assert dd_10_04 in sut
    assert dd_10_05 in sut
    assert dd_10_06 in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_2() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -2)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 not in sut
    assert dd_10_03 in sut
    assert dd_10_04 not in sut
    assert dd_10_05 in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_3() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -3)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_4() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -4)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 not in sut
    assert dd_10_03 in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_5() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -5)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_6() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -6)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


def test_contains_7_1_7() -> None:
    # GIVEN
    sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -7)
    # THEN
    assert dd_09_30 not in sut
    assert dd_10_01 not in sut
    assert dd_10_02 not in sut
    assert dd_10_03 not in sut
    assert dd_10_04 not in sut
    assert dd_10_05 not in sut
    assert dd_10_06 not in sut
    assert dd_10_07 in sut
    assert dd_10_08 not in sut


# ---


def test_contains_min_seg_pos() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2023_12_17)
    # WHEN
    _sut = DecimalDateRange(dd, dd.next(), 1)
    # THEN
    assert len(_sut) == 1
    assert dd in _sut


def test_contains_min_seg_neg() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2023_12_17)
    # WHEN
    _sut = DecimalDateRange(dd, dd.previous(), -1)
    # THEN
    assert len(_sut) == 1
    assert dd in _sut
