from decimaldate import DecimalDate, DecimalDateRange

###

"""
range_month_from_decimal_date
"""


def test_range_month_from_decimal_date_may_month() -> None:
    # WHEN
    sut: DecimalDateRange = DecimalDateRange.range_month_of_decimal_date(2024_05_18)
    list_sut = list(sut)
    # THEN
    assert len(sut) == 31  # May has 31 days
    assert list_sut[0] == DecimalDate(2024_05_01)  # First
    assert list_sut[-1] == DecimalDate(2024_05_31)  # Last


def test_range_month_from_decimal_date_february_not_leap_year() -> None:
    # GIVEN
    valentines_day = 2023_02_14
    # WHEN
    sut: DecimalDateRange = DecimalDateRange.range_month_of_decimal_date(valentines_day)
    list_sut = list(sut)
    # THEN
    assert len(sut) == 28
    assert list_sut[0] == DecimalDate(2023_02_01)  # First
    assert list_sut[-1] == DecimalDate(2023_02_28)  # Last


def test_range_month_from_decimal_date_february_leap_year() -> None:
    # GIVEN
    valentines_day = 2024_02_14
    # WHEN
    sut: DecimalDateRange = DecimalDateRange.range_month_of_decimal_date(valentines_day)
    list_sut = list(sut)
    # THEN
    assert len(sut) == 29
    assert list_sut[0] == DecimalDate(2024_02_01)  # First
    assert list_sut[-1] == DecimalDate(2024_02_29)  # Last
