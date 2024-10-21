import pytest

from decimaldate import DecimalDate


def test_randrange_ident_raises_value_error() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2014_02_14)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd, dd)


def test_randrange_step_not_int_raises_type_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # GIVEN
    bad_float_step: float = 1.0
    # THEN
    with pytest.raises(TypeError):
        _ = DecimalDate.randrange(dd1, dd2, bad_float_step)  # type: ignore[arg-type] # NOSONAR


def test_randrange_step_0_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd1, dd2, 0)
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd2, dd1, 0)


def test_randrange_pos_dir_pos_step_is_ok() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    _ = DecimalDate.randrange(dd1, dd2, 1)


def test_randrange_pos_dir_neg_step_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd1, dd2, -1)


def test_randrange_neg_dir_pos_step_raises_value_error() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    with pytest.raises(ValueError):
        _ = DecimalDate.randrange(dd2, dd1, 1)


def test_randrange_neg_dir_neg_step_is_ok() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    _ = DecimalDate.randrange(dd2, dd1, -1)


def test_randrange_min_range() -> None:
    """Try a lot with a range that can only ever give one value back."""
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = dd1.next()
    # THEN
    for _ in range(200):
        assert DecimalDate.randrange(dd1, dd2) == dd1


def test_randrange() -> None:
    """Try a lot and see if all values are in expected range.

    This can never be a definitive test but there are enough tries
    that it should give confidence.
    """
    # GIVEN
    dd1: DecimalDate = DecimalDate(2014_02_14)
    dd2: DecimalDate = DecimalDate(2014_06_05)
    # THEN
    for _ in range(5000):
        assert dd1 <= DecimalDate.randrange(dd1, dd2) < dd2
