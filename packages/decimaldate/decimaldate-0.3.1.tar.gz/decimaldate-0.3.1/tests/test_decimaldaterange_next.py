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


"""
next()
"""


def test_next_1_7_1() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 1)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    assert next(it) == dd_10_02
    assert next(it) == dd_10_03
    assert next(it) == dd_10_04
    assert next(it) == dd_10_05
    assert next(it) == dd_10_06
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_2() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 2)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    assert next(it) == dd_10_03
    assert next(it) == dd_10_05
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_3() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 3)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    assert next(it) == dd_10_04
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_4() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 4)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    assert next(it) == dd_10_05
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_5() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 5)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    assert next(it) == dd_10_06
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_6() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 6)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_1_7_7() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_01, dd_10_07, 7)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_01
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_1() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -1)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    assert next(it) == dd_10_06
    assert next(it) == dd_10_05
    assert next(it) == dd_10_04
    assert next(it) == dd_10_03
    assert next(it) == dd_10_02
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_2() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -2)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    assert next(it) == dd_10_05
    assert next(it) == dd_10_03
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_3() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -3)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    assert next(it) == dd_10_04
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_4() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -4)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    assert next(it) == dd_10_03
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_5() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -5)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    assert next(it) == dd_10_02
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_6() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -6)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)


def test_next_7_1_7() -> None:
    # GIVEN
    _sut: DecimalDateRange = DecimalDateRange(dd_10_07, dd_10_01, -7)
    # WHEN
    it = iter(_sut)
    # THEN
    assert next(it) == dd_10_07
    with pytest.raises(expected_exception=StopIteration):
        _ = next(it)
