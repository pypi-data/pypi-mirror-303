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
last()
"""


def test_last_october_1() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 1)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_02,
        dd_10_03,
        dd_10_04,
        dd_10_05,
        dd_10_06,
        dd_10_07,
        dd_10_08,
        dd_10_09,
        dd_10_10,
        dd_10_11,
        dd_10_12,
        dd_10_13,
        dd_10_14,
        dd_10_15,
        dd_10_16,
        dd_10_17,
        dd_10_18,
        dd_10_19,
        dd_10_20,
        dd_10_21,
        dd_10_22,
        dd_10_23,
        dd_10_24,
        dd_10_25,
        dd_10_26,
        dd_10_27,
        dd_10_28,
        dd_10_29,
        dd_10_30,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_2() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 2)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_03,
        dd_10_05,
        dd_10_07,
        dd_10_09,
        dd_10_11,
        dd_10_13,
        dd_10_15,
        dd_10_17,
        dd_10_19,
        dd_10_21,
        dd_10_23,
        dd_10_25,
        dd_10_27,
        dd_10_29,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_3() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 3)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_04,
        dd_10_07,
        dd_10_10,
        dd_10_13,
        dd_10_16,
        dd_10_19,
        dd_10_22,
        dd_10_25,
        dd_10_28,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_4() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 4)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_05,
        dd_10_09,
        dd_10_13,
        dd_10_17,
        dd_10_21,
        dd_10_25,
        dd_10_29,
    ]
    assert list(_sut)[-1] == dd_10_29
    assert _sut.last() == dd_10_29


def test_last_october_5() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 5)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_06,
        dd_10_11,
        dd_10_16,
        dd_10_21,
        dd_10_26,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_6() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 6)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_07,
        dd_10_13,
        dd_10_19,
        dd_10_25,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_7() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 7)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_08,
        dd_10_15,
        dd_10_22,
        dd_10_29,
    ]
    assert list(_sut)[-1] == dd_10_29
    assert _sut.last() == dd_10_29


def test_last_october_8() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 8)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_09,
        dd_10_17,
        dd_10_25,
    ]
    assert list(_sut)[-1] == dd_10_25
    assert _sut.last() == dd_10_25


def test_last_october_9() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 9)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_10,
        dd_10_19,
        dd_10_28,
    ]
    assert list(_sut)[-1] == dd_10_28
    assert _sut.last() == dd_10_28


def test_last_october_10() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 10)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_11,
        dd_10_21,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_11() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 11)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_12,
        dd_10_23,
    ]
    assert list(_sut)[-1] == dd_10_23
    assert _sut.last() == dd_10_23


def test_last_october_12() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 12)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_13,
        dd_10_25,
    ]
    assert list(_sut)[-1] == dd_10_25
    assert _sut.last() == dd_10_25


def test_last_october_13() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 13)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_14,
        dd_10_27,
    ]
    assert list(_sut)[-1] == dd_10_27
    assert _sut.last() == dd_10_27


def test_last_october_14() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 14)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_15,
        dd_10_29,
    ]
    assert list(_sut)[-1] == dd_10_29
    assert _sut.last() == dd_10_29


def test_last_october_15() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 15)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_16,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_16() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 16)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_17,
    ]
    assert list(_sut)[-1] == dd_10_17
    assert _sut.last() == dd_10_17


def test_last_october_17() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 17)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_18,
    ]
    assert list(_sut)[-1] == dd_10_18
    assert _sut.last() == dd_10_18


def test_last_october_18() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 18)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_19,
    ]
    assert list(_sut)[-1] == dd_10_19
    assert _sut.last() == dd_10_19


def test_last_october_19() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 19)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_20,
    ]
    assert list(_sut)[-1] == dd_10_20
    assert _sut.last() == dd_10_20


def test_last_october_20() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 20)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_21,
    ]
    assert list(_sut)[-1] == dd_10_21
    assert _sut.last() == dd_10_21


def test_last_october_21() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 21)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_22,
    ]
    assert list(_sut)[-1] == dd_10_22
    assert _sut.last() == dd_10_22


def test_last_october_22() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 22)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_23,
    ]
    assert list(_sut)[-1] == dd_10_23
    assert _sut.last() == dd_10_23


def test_last_october_23() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 23)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_24,
    ]
    assert list(_sut)[-1] == dd_10_24
    assert _sut.last() == dd_10_24


def test_last_october_24() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 24)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_25,
    ]
    assert list(_sut)[-1] == dd_10_25
    assert _sut.last() == dd_10_25


def test_last_october_25() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 25)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_26,
    ]
    assert list(_sut)[-1] == dd_10_26
    assert _sut.last() == dd_10_26


def test_last_october_26() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 26)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_27,
    ]
    assert list(_sut)[-1] == dd_10_27
    assert _sut.last() == dd_10_27


def test_last_october_27() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 27)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_28,
    ]
    assert list(_sut)[-1] == dd_10_28
    assert _sut.last() == dd_10_28


def test_last_october_28() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 28)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_29,
    ]
    assert list(_sut)[-1] == dd_10_29
    assert _sut.last() == dd_10_29


def test_last_october_29() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 29)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_30,
    ]
    assert list(_sut)[-1] == dd_10_30
    assert _sut.last() == dd_10_30


def test_last_october_30() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 30)
    # THEN
    assert list(_sut) == [
        dd_10_01,
        dd_10_31,
    ]
    assert list(_sut)[-1] == dd_10_31
    assert _sut.last() == dd_10_31


def test_last_october_31() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 31)
    # THEN
    assert list(_sut) == [
        dd_10_01,
    ]
    assert list(_sut)[-1] == dd_10_01
    assert _sut.last() == dd_10_01


def test_last_october_32() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 32)
    # THEN
    assert list(_sut) == [
        dd_10_01,
    ]
    assert list(_sut)[-1] == dd_10_01
    assert _sut.last() == dd_10_01


def test_last_october_365() -> None:
    # WHEN
    _sut = DecimalDateRange(dd_10_01, dd_11_01, 365)
    # THEN
    assert list(_sut) == [
        dd_10_01,
    ]
    assert list(_sut)[-1] == dd_10_01
    assert _sut.last() == dd_10_01


# ---


def test_last_min_seq_pos() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2023_12_17)
    # WHEN
    _sut = DecimalDateRange(dd, dd.next())
    it = iter(_sut)
    # THEN
    assert len(_sut) == 1
    assert next(it) == dd


def test_last_min_seq_neg() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2023_12_17)
    # WHEN
    _sut = DecimalDateRange(dd, dd.previous(), -1)
    it = iter(_sut)
    # THEN
    assert len(_sut) == 1
    assert next(it) == dd
