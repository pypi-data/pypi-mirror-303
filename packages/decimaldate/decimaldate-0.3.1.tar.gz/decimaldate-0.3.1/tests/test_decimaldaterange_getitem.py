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
__getitem__
"""


def test_getitem_all() -> None:
    assert sut[0] == dd_10_21
    assert sut[1] == dd_10_22
    assert sut[2] == dd_10_23
    assert sut[3] == dd_10_24
    assert sut[4] == dd_10_25


def test_getitem_zero_returns_start() -> None:
    assert sut[0] == sut_start_incl
    assert sut[-0] == sut_start_incl


def test_getitem_minus_one_returns_last_before_stop() -> None:
    assert sut[-1] == sut_stop_excl.previous(1)


def test_getitem_minus_len_returns_start() -> None:
    assert sut[-len(sut)] == sut_start_incl


def test_getitem() -> None:
    assert sut[1] == sut_start_incl.next(1)
    assert sut[-2] == sut_stop_excl.previous(2)


def test_getitem_outside_raises_index_error() -> None:

    with pytest.raises(expected_exception=IndexError):
        _ = sut[len(sut)]

    with pytest.raises(expected_exception=IndexError):
        _ = sut[-(len(sut) + 1)]

    with pytest.raises(expected_exception=IndexError):
        _ = sut[100_000_000]

    with pytest.raises(expected_exception=IndexError):
        _ = sut[-100_000_000]


def test_getitem_invalid_type_raises_type_error() -> None:
    with pytest.raises(expected_exception=TypeError):
        _ = sut["3"]  # type: ignore[index]


def test_getitem_empty_sequence_raises_index_error(today_as_decimaldate_int) -> None:
    # WHEN
    _sut: DecimalDateRange = DecimalDateRange(
        today_as_decimaldate_int, today_as_decimaldate_int
    )
    # THEN
    assert list(_sut) == []
    with pytest.raises(expected_exception=IndexError):
        _ = _sut[0]


#
#
#


def test_getitem_1_7_1():
    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 1)

    # THEN

    assert len(_sut) == 6
    assert list(_sut) == [dd_10_01, dd_10_02, dd_10_03, dd_10_04, dd_10_05, dd_10_06]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = sut[-6]

    assert _sut[-5] == dd_10_02
    assert _sut[-4] == dd_10_03
    assert _sut[-3] == dd_10_04
    assert _sut[-2] == dd_10_05
    assert _sut[-1] == dd_10_06

    assert _sut[0] == dd_10_01

    assert _sut[1] == dd_10_02
    assert _sut[2] == dd_10_03
    assert _sut[3] == dd_10_04
    assert _sut[4] == dd_10_05
    assert _sut[5] == dd_10_06

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[6]


def test_getitem_1_7_2():
    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 2)

    # THEN

    assert len(_sut) == 3
    assert list(_sut) == [dd_10_01, dd_10_03, dd_10_05]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-4]

    assert _sut[-3] == dd_10_01
    assert _sut[-2] == dd_10_03
    assert _sut[-1] == dd_10_05

    assert _sut[0] == dd_10_01

    assert _sut[1] == dd_10_03
    assert _sut[2] == dd_10_05

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[3]


def test_getitem_1_7_3():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 3)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_01, dd_10_04]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_01
    assert _sut[-1] == dd_10_04

    assert _sut[0] == dd_10_01

    assert _sut[1] == dd_10_04

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_1_7_4():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 4)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_01, dd_10_05]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_01
    assert _sut[-1] == dd_10_05

    assert _sut[0] == dd_10_01

    assert _sut[1] == dd_10_05

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_1_7_5():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 5)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_01, dd_10_06]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_01
    assert _sut[-1] == dd_10_06

    assert _sut[0] == dd_10_01

    assert _sut[1] == dd_10_06

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_1_7_6():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 6)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_01]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_01

    assert _sut[0] == dd_10_01

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]


def test_getitem_1_7_7():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 7)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_01]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_01

    assert _sut[0] == dd_10_01

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]


def test_getitem_1_7_365():

    # WHEN

    _sut = DecimalDateRange(dd_10_01, dd_10_07, 365)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_01]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_01

    assert _sut[0] == dd_10_01

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]


#
#
#


def test_getitem_7_1_1():
    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -1)

    # THEN

    assert len(_sut) == 6
    assert list(_sut) == [dd_10_07, dd_10_06, dd_10_05, dd_10_04, dd_10_03, dd_10_02]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = sut[-6]

    assert _sut[-5] == dd_10_06
    assert _sut[-4] == dd_10_05
    assert _sut[-3] == dd_10_04
    assert _sut[-2] == dd_10_03
    assert _sut[-1] == dd_10_02

    assert _sut[0] == dd_10_07

    assert _sut[1] == dd_10_06
    assert _sut[2] == dd_10_05
    assert _sut[3] == dd_10_04
    assert _sut[4] == dd_10_03
    assert _sut[5] == dd_10_02

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[6]


def test_getitem_7_1_2():
    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -2)

    # THEN

    assert len(_sut) == 3
    assert list(_sut) == [dd_10_07, dd_10_05, dd_10_03]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-4]

    assert _sut[-3] == dd_10_07
    assert _sut[-2] == dd_10_05
    assert _sut[-1] == dd_10_03

    assert _sut[0] == dd_10_07

    assert _sut[1] == dd_10_05
    assert _sut[2] == dd_10_03

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[3]


def test_getitem_7_1_3():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -3)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_07, dd_10_04]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_07
    assert _sut[-1] == dd_10_04

    assert _sut[0] == dd_10_07

    assert _sut[1] == dd_10_04

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_7_1_4():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -4)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_07, dd_10_03]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_07
    assert _sut[-1] == dd_10_03

    assert _sut[0] == dd_10_07

    assert _sut[1] == dd_10_03

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_7_1_5():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -5)

    # THEN

    assert len(_sut) == 2
    assert list(_sut) == [dd_10_07, dd_10_02]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-3]

    assert _sut[-2] == dd_10_07
    assert _sut[-1] == dd_10_02

    assert _sut[0] == dd_10_07

    assert _sut[1] == dd_10_02

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[2]


def test_getitem_7_1_6():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -6)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_07]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_07

    assert _sut[0] == dd_10_07

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]


def test_getitem_7_1_7():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -7)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_07]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_07

    assert _sut[0] == dd_10_07

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]


def test_getitem_7_1_365():

    # WHEN

    _sut = DecimalDateRange(dd_10_07, dd_10_01, -365)

    # THEN

    assert len(_sut) == 1
    assert list(_sut) == [dd_10_07]

    # ---

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[-2]

    assert _sut[-1] == dd_10_07

    assert _sut[0] == dd_10_07

    with pytest.raises(
        expected_exception=IndexError,
    ):
        _ = _sut[1]
