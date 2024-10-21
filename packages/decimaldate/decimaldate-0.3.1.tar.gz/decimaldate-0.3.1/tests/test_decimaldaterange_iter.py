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
__iter__
"""


def test_iter_ident_is_empty() -> None:
    # sequence 'end' is exclusive
    assert len(DecimalDateRange(dd_10_07, dd_10_07)) == 0


@pytest.mark.parametrize(
    "start,stop,step,expected,is_in,is_in_expected",
    [
        # - 0 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            1,
            [dd_10_01, dd_10_02, dd_10_03, dd_10_04, dd_10_05, dd_10_06],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, 1))
        # [1, 2, 3, 4, 5, 6]
        # - 1 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            -1,
            [],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, -1))
        # []
        # - 2 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -1,
            [dd_10_07, dd_10_06, dd_10_05, dd_10_04, dd_10_03, dd_10_02],
            dd_10_07,
            True,
        ),
        # >>> list(range(7, 1, -1))
        # [7, 6, 5, 4, 3, 2]
        # - 3 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            1,
            [],
            dd_10_07,
            False,
        ),
        # >>> list(range(7, 1, 1))
        # []
        # - 4 -
        pytest.param(
            dd_10_04,
            dd_10_04,
            1,
            [],
            dd_10_07,
            False,
        ),
        # >>> list(range(4, 4, 1))
        # []
        # - 5 -
        pytest.param(
            dd_10_04,
            dd_10_04,
            -1,
            [],
            dd_10_07,
            False,
        ),
        # >>> list(range(4, 4, -1))
        # []
        # - 6 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            5,
            [dd_10_01, dd_10_06],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, 5))
        # [1, 6]
        # - 7 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            6,
            [dd_10_01],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, 6))
        # [1]
        # - 8 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            7,
            [dd_10_01],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, 7))
        # [1]
        # - 9 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            42,
            [dd_10_01],
            dd_10_07,
            False,
        ),
        # >>> list(range(1, 7, 42))
        # [1]
        # - 10 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -5,
            [dd_10_07, dd_10_02],
            dd_10_07,
            True,
        ),
        # >>> list(range(7, 1, -5))
        # [7, 2]
        # - 11 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -6,
            [dd_10_07],
            dd_10_07,
            True,
        ),
        # >>> list(range(7, 1, -6))
        # [7]
        # - 12 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -7,
            [dd_10_07],
            dd_10_07,
            True,
        ),
        # >>> list(range(7, 1, -7))
        # [7]
        # - 13 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -42,
            [dd_10_07],
            dd_10_07,
            True,
        ),
        # >>> list(range(7, 1, -42))
        # [7]
        # - 14 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            2,
            [dd_10_01, dd_10_03, dd_10_05],
            dd_10_07,
            False,
        ),
        # - 15 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            3,
            [dd_10_01, dd_10_04],
            dd_10_07,
            False,
        ),
        # - 16 -
        pytest.param(
            dd_10_01,
            dd_10_07,
            4,
            [dd_10_01, dd_10_05],
            dd_10_07,
            False,
        ),
        # - 17 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -2,
            [dd_10_07, dd_10_05, dd_10_03],
            dd_10_07,
            True,
        ),
        # - 18 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -3,
            [dd_10_07, dd_10_04],
            dd_10_07,
            True,
        ),
        # - 19 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -4,
            [dd_10_07, dd_10_03],
            dd_10_07,
            True,
        ),
        # - 20 -
        pytest.param(
            dd_10_07,
            dd_10_01,
            -5,
            [dd_10_07, dd_10_02],
            dd_10_03,
            False,
        ),
    ],
)
def test_iter(
    start: DecimalDate,
    stop: DecimalDate,
    step: int,
    expected: list[DecimalDate],
    is_in: DecimalDate,
    is_in_expected: bool,
) -> None:
    # GIVEN
    ddrange: DecimalDateRange = DecimalDateRange(start, stop, step)
    # THEN
    assert list(ddrange) == expected
    assert len(ddrange) == len(expected)
    assert (is_in in ddrange) == is_in_expected
