import pytest

from decimaldate import DecimalDate

"""
__eq__
"""


def test_dunder_equality_true(
    today_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    sut: DecimalDate = DecimalDate.today()
    # THEN
    assert today_dd == sut


def test_dunder_equality_false(
    today_as_decimaldate_int: int,
    future_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    sut: DecimalDate = DecimalDate(future_as_decimaldate_int)
    # THEN
    assert not today_dd == sut  # NOSONAR


def test_equality_ident(
    today_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    sut: DecimalDate = today_dd
    # THEN
    assert today_dd == sut


def test_equality_same_value(
    today_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today1_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    today2_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    # THEN
    assert today1_dd == today2_dd


def test_equality_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    assert today.as_int() == today_as_decimaldate_int
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today == today_as_decimaldate_int  # NOSONAR


"""
__ne__
"""


def test_dunder_non_equality_true(
    today_as_decimaldate_int: int,
    future_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    sut: DecimalDate = DecimalDate(future_as_decimaldate_int)
    # THEN
    assert today_dd != sut


def test_dunder_non_equality_false(
    today_as_decimaldate_int: int,
) -> None:
    # GIVEN
    today_dd: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # WHEN
    sut: DecimalDate = DecimalDate.today()
    # THEN
    assert not today_dd != sut  # NOSONAR


def test_dunder_non_equality_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today != today_as_decimaldate_int  # NOSONAR


"""
__gt__
"""


def test_dunder_greater_than(
    today_as_decimaldate_int: int,
    past_as_decimaldate_int: int,
) -> None:
    # GIVEN
    # WHEN
    # THEN
    # fmt: off
    assert not DecimalDate(today_as_decimaldate_int) == DecimalDate(past_as_decimaldate_int)  # NOSONAR
    assert not DecimalDate(today_as_decimaldate_int) < DecimalDate(past_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(today_as_decimaldate_int) > DecimalDate(past_as_decimaldate_int)  # NOSONAR
    # fmt: on


def test_dunder_greater_than_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today > today_as_decimaldate_int  # NOSONAR


"""
__ge__
"""


def test_dunder_greater_than_or_equal(
    today_as_decimaldate_int: int,
    past_as_decimaldate_int: int,
) -> None:
    # GIVEN
    # WHEN
    # THEN
    # fmt: off
    assert not DecimalDate(today_as_decimaldate_int) == DecimalDate(past_as_decimaldate_int)  # NOSONAR
    assert not DecimalDate(today_as_decimaldate_int) < DecimalDate(past_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(today_as_decimaldate_int) > DecimalDate(past_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(today_as_decimaldate_int) >= DecimalDate(past_as_decimaldate_int)  # NOSONAR
    # fmt: on


def test_dunder_greater_than_or_equal_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today >= today_as_decimaldate_int  # NOSONAR


"""
__lt__
"""


def test_dunder_less_than(
    today_as_decimaldate_int: int,
    past_as_decimaldate_int: int,
) -> None:
    # GIVEN
    # WHEN
    # THEN
    # fmt: off
    assert not DecimalDate(past_as_decimaldate_int) == DecimalDate(today_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(past_as_decimaldate_int) < DecimalDate(today_as_decimaldate_int)  # NOSONAR
    assert not DecimalDate(past_as_decimaldate_int) > DecimalDate(today_as_decimaldate_int)  # NOSONAR
    # fmt: on


def test_dunder_less_than_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today < today_as_decimaldate_int  # NOSONAR


"""
__le__
"""


def test_dunder_less_than_or_equal(
    today_as_decimaldate_int: int,
    past_as_decimaldate_int: int,
) -> None:
    # GIVEN
    # WHEN
    # THEN
    # fmt: off
    assert not DecimalDate(past_as_decimaldate_int) == DecimalDate(today_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(past_as_decimaldate_int) < DecimalDate(today_as_decimaldate_int)  # NOSONAR
    assert DecimalDate(past_as_decimaldate_int) <= DecimalDate(today_as_decimaldate_int)  # NOSONAR
    # fmt: on


def test_dunder_less_than_or_equal_unsupported_type_raises_typeerror(
    today_as_decimaldate_int,
) -> None:
    # WHEN
    today = DecimalDate.today()
    # THEN
    with pytest.raises(
        expected_exception=TypeError,
    ):
        today <= today_as_decimaldate_int  # NOSONAR
