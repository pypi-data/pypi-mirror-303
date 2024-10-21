import pytest

from decimaldate import DecimalDate


def test_count_step_0_raises_value_error() -> None:
    it = iter(DecimalDate.count(step=0))
    with pytest.raises(expected_exception=ValueError):
        _ = next(it)


def test_count_step_none_raises_type_error() -> None:
    it = iter(DecimalDate.count(step=None))  # type: ignore[arg-type]  # NOSONAR
    with pytest.raises(expected_exception=TypeError):
        _ = next(it)


def test_count_step_1(today_as_decimaldate_int) -> None:
    # GIVEN
    step = 1
    # WHEN
    it = iter(DecimalDate.count(step=step))
    # THEN
    assert next(it).as_int() == today_as_decimaldate_int
    assert (
        next(it).as_int() == DecimalDate(today_as_decimaldate_int).next(step).as_int()
    )


def test_count_step_neg1(today_as_decimaldate_int) -> None:
    # GIVEN
    step = -1
    # WHEN
    it = iter(DecimalDate.count(step=step))
    # THEN
    assert next(it).as_int() == today_as_decimaldate_int
    assert (
        next(it).as_int() == DecimalDate(today_as_decimaldate_int).next(step).as_int()
    )


def test_count_step_17(today_as_decimaldate_int) -> None:
    # GIVEN
    step = 17
    # WHEN
    it = iter(DecimalDate.count(step=step))
    # THEN
    assert next(it).as_int() == today_as_decimaldate_int
    assert (
        next(it).as_int() == DecimalDate(today_as_decimaldate_int).next(step).as_int()
    )


def test_count_step_neg17(today_as_decimaldate_int) -> None:
    # GIVEN
    step = -17
    # WHEN
    it = iter(DecimalDate.count(step=step))
    # THEN
    assert next(it).as_int() == today_as_decimaldate_int
    assert (
        next(it).as_int() == DecimalDate(today_as_decimaldate_int).next(step).as_int()
    )
