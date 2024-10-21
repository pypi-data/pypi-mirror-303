import pytest

from decimaldate import DecimalDate, DecimalDateRange

"""
__highest_multiple_of
"""


@pytest.mark.parametrize(
    "arg,div,expected",
    [
        pytest.param(7, 1, 7),
        pytest.param(7, 2, 6),
        pytest.param(7, 3, 6),
        pytest.param(7, 4, 4),
        pytest.param(7, 5, 5),
        pytest.param(7, 6, 6),
        pytest.param(7, 7, 7),
        pytest.param(7, 8, 0),
    ],
)
def test_highest_multiple_of(arg, div, expected) -> None:
    assert DecimalDateRange._DecimalDateRange__highest_multiple_of(arg, div) == expected  # type: ignore[attr-defined]


"""
__get_length_of_sequence
"""

dd_start: DecimalDate = DecimalDate(2024_05_01)
dd_stop: DecimalDate = DecimalDate(2024_05_07)


def test_get_length_of_sequence_step_0_raises_value_error() -> None:
    with pytest.raises(ValueError):
        _ = DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_start,
            dd_stop,
            0,
        )


def test_get_length_of_sequence_ident_is_0() -> None:
    assert (
        DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_start,
            dd_start,
            1,
        )
        == 0
    )


def test_get_length_of_sequence_direction_good_neg() -> None:
    assert (
        DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_stop,
            dd_start,
            -1,
        )
        == 6
    )


def test_get_length_of_sequence_direction_good_pos() -> None:
    assert (
        DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_start,
            dd_stop,
            1,
        )
        == 6
    )


def test_get_length_of_sequence_direction_bad_neg_is_0() -> None:
    assert (
        DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_stop,
            dd_start,
            1,
        )
        == 0
    )


def test_get_length_of_sequence_direction_bad_pos_is_0() -> None:
    assert (
        DecimalDateRange._DecimalDateRange__get_length_of_sequence(  # type: ignore[attr-defined]
            dd_start,
            dd_stop,
            -1,
        )
        == 0
    )


"""
__get_last_in_sequence
"""


def test_get_last_in_sequence_step_0_raises_value_error() -> None:
    with pytest.raises(ValueError):
        _ = DecimalDateRange._DecimalDateRange__get_last_in_sequence(  # type: ignore[attr-defined]
            dd_start,
            dd_stop,
            0,
        )
