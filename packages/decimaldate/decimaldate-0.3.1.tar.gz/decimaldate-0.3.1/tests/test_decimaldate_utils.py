from typing import Literal

import pytest

from decimaldate import DecimalDate

dd: Literal[20231102] = 2023_11_02
ds: Literal["20231102"] = "20231102"

"""
split
"""


def test_split_str_returns_ymd() -> None:
    # GIVEN
    sut: DecimalDate = DecimalDate(ds)
    # WHEN
    sut_y, sut_m, sut_d = sut.split()
    # THEN
    assert sut_y == 2023
    assert sut_m == 11
    assert sut_d == 2


def test_split_int_returns_ymd() -> None:
    # GIVEN
    sut: DecimalDate = DecimalDate(dd)
    # WHEN
    sut_y, sut_m, sut_d = sut.split()
    # THEN
    assert sut_y == 2023
    assert sut_m == 11
    assert sut_d == 2


"""
clone
"""


def test_clone_equal_value() -> None:
    # GIVEN
    _dd: DecimalDate = DecimalDate(dd)
    # WHEN
    sut = _dd.clone()
    # THEN
    assert sut == _dd


def test_clone_not_equal_reference() -> None:
    # GIVEN
    _dd: DecimalDate = DecimalDate(dd)
    # WHEN
    sut = _dd.clone()
    # THEN
    assert sut == _dd
    assert sut is not _dd


def test_clone_internals() -> None:
    # GIVEN
    dd_int_29: int = 2024_09_29
    dd_int_30: int = 2023_09_30
    _dd: DecimalDate = DecimalDate(dd_int_30)

    # WHEN
    dd_clone = _dd.clone()
    # abuse mangled member variable to verify instance variables are not shared
    dd_clone._DecimalDate__dd_int = dd_int_29  # type: ignore[attr-defined]

    # THEN
    assert _dd.as_int() == dd_int_30
    assert dd_clone.as_int() == dd_int_29
    assert _dd != dd_clone


"""
next
"""


def test_next_31daymonth_1nexts_as_expected() -> None:
    # GIVEN
    _ds: Literal["20220430"] = "20220430"
    # WHEN
    sut: DecimalDate = DecimalDate(_ds)
    # THEN
    assert "20220501" == sut.next().as_str()


def test_next_31daymonth_2nexts_as_expected() -> None:
    # GIVEN
    _ds: Literal["20220430"] = "20220430"
    # WHEN
    sut: DecimalDate = DecimalDate(_ds)
    # THEN
    assert "20220502" == sut.next().next().as_str()


def test_next_30daymonth_1nexts_as_expected() -> None:
    # GIVEN
    _ds: Literal["20220330"] = "20220330"
    # WHEN
    sut: DecimalDate = DecimalDate(_ds)
    # THEN
    assert "20220331" == sut.next().as_str()


def test_next_30daymonth_2nexts_as_expected() -> None:
    # GIVEN
    _ds: Literal["20220330"] = "20220330"
    # WHEN
    sut: DecimalDate = DecimalDate(_ds)
    # THEN
    assert "20220401" == sut.next().next().as_str()


def test_next_next_is_two_days_previous() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.next().next() == sut.next(2)


def test_next_multiple_next() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.next(43).next(7) == sut.next(43 + 7)


def test_next_zero_is_identical() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.next(0) == sut


def test_next_none_raises_typeerror() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    with pytest.raises(expected_exception=TypeError):
        _ = sut.next(None)  # type: ignore[arg-type]  # NOSONAR


"""
previous
"""


def testprevious_31daymonth_1previous_as_expected() -> None:
    # GIVEN
    _ds: Literal["2019_11_01"] = "2019_11_01"
    # WHEN
    sut: DecimalDate = DecimalDate(_ds)
    # THEN
    assert "20191031" == sut.previous().as_str()


def test_previous_31daymonth_2previous_as_expected() -> None:
    # GIVEN
    ds: Literal["2019_11_02"] = "2019_11_02"
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert "20191031" == sut.previous().previous().as_str()


def test_previous_30daymonth_1previous_as_expected() -> None:
    # GIVEN
    ds: Literal["2021_10_01"] = "2021_10_01"
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert "20210930" == sut.previous().as_str()


def test_previous_30daymonth_2previous_as_expected() -> None:
    # GIVEN
    ds: Literal["2021_10_02"] = "2021_10_02"
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert "20210930" == sut.previous().previous().as_str()


def test_previous_next_is_next_previous() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.previous().next() == sut.next().previous()
    assert sut.next().previous() == sut.previous().next()


def test_previous_previous_is_two_days_previous() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.previous().previous() == sut.previous(2)


def test_previous_multiple_previous() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.previous(43).previous(7) == sut.previous(43 + 7)


def test_previous_zero_is_identical() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.previous(0) == sut


def test_previous_none_raises_typeerror() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    with pytest.raises(expected_exception=TypeError):
        _ = sut.previous(None)  # type: ignore[arg-type]  # NOSONAR


#
#
#


def test_previous_next_are_symetrical() -> None:
    # GIVEN
    delta: int = 7
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.previous(delta) == sut.next(-delta)
    assert sut.previous(-delta) == sut.next(delta)


"""
tomorrow
"""


def test_tomorrow(
    today_as_decimaldate_int: int,
) -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # THEN
    assert sut.as_int() == today_as_decimaldate_int
    assert DecimalDate.tomorrow() == sut.next()


"""
yesterday
"""


def test_yesterday(
    today_as_decimaldate_int: int,
) -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(today_as_decimaldate_int)
    # THEN
    assert sut.as_int() == today_as_decimaldate_int
    assert DecimalDate.yesterday() == sut.previous()


"""
year
"""


def test_year() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.year() == 2023


"""
month
"""


def test_month() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.month() == 11


"""
day
"""


def test_day() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.day() == 2


"""
last_day_of_month
"""


@pytest.mark.parametrize(
    "sut,expected",
    [
        pytest.param(DecimalDate("2023_01_06"), 31),
        pytest.param(DecimalDate("2023_02_06"), 28),
        pytest.param(DecimalDate("2024_02_06"), 29),
    ],
)
def test_last_day_of_month(sut: DecimalDate, expected: int) -> None:
    assert sut.last_day_of_month() == expected


"""
start_of_month
"""


@pytest.mark.parametrize(
    "sut,expected",
    [
        pytest.param(DecimalDate("2023_01_01"), DecimalDate("2023_01_01")),
        pytest.param(DecimalDate("2023_01_06"), DecimalDate("2023_01_01")),
        pytest.param(DecimalDate("2024_12_31"), DecimalDate("2024_12_01")),
    ],
)
def test_start_of_month(sut: DecimalDate, expected: DecimalDate) -> None:
    assert sut.start_of_month() == expected


"""
end_of_month
"""


@pytest.mark.parametrize(
    "sut,expected",
    [
        pytest.param(DecimalDate("2023_01_06"), DecimalDate("2023_01_31")),
        pytest.param(DecimalDate("2023_02_06"), DecimalDate("2023_02_28")),
        pytest.param(DecimalDate("2024_02_06"), DecimalDate("2024_02_29")),
        pytest.param(DecimalDate("2024_12_31"), DecimalDate("2024_12_31")),
    ],
)
def test_end_of_month(sut: DecimalDate, expected: DecimalDate) -> None:
    assert sut.end_of_month() == expected


"""
weekday
"""


def test_weekday() -> None:
    # GIVEN
    FRIDAY: Literal[4] = 4
    # WHEN
    wd: int = DecimalDate(2024_09_27).weekday()
    # THEN
    assert wd == FRIDAY


"""
isoweekday
"""


def test_isoweekday() -> None:
    # GIVEN
    ISO_FRIDAY: Literal[5] = 5
    # WHEN
    iso_wd: int = DecimalDate(2024_09_27).isoweekday()
    # THEN
    assert iso_wd == ISO_FRIDAY


"""
isoformat
"""


def test_isoformat() -> None:
    # WHEN
    iso: str = DecimalDate(2024_09_27).isoformat()
    # THEN
    assert iso == "2024-09-27"


"""
try_instantiate
"""


def test_try_instantiate_none_is_today() -> None:
    # WHEN
    dd: DecimalDate | None = DecimalDate.try_instantiate(None)
    # THEN
    assert dd == DecimalDate.today()


def test_try_instantiate_no_arg_is_today() -> None:
    # WHEN
    dd: DecimalDate | None = DecimalDate.try_instantiate()
    # THEN
    assert dd == DecimalDate.today()


def test_try_instantiate_bad_is_none() -> None:
    # GIVEN
    bad_date: Literal[20242709] = 2024_27_09
    # WHEN
    dd: DecimalDate | None = DecimalDate.try_instantiate(bad_date)
    # THEN
    assert dd is None


def test_try_instantiate_good_is_ok() -> None:
    # GIVEN
    good_date: Literal[20240927] = 2024_09_27
    # WHEN
    dd: DecimalDate | None = DecimalDate.try_instantiate(good_date)
    # THEN
    assert str(dd) == str(good_date)


"""
diff_days
"""


@pytest.mark.parametrize(
    "dd1,dd2,expected",
    [
        pytest.param(2023_12_11, 2023_12_11, 0),
        pytest.param(2023_12_11, 2023_12_12, 1),
        pytest.param(2023_12_12, 2023_12_11, -1),
    ],
)
def test_diff_days(dd1: int, dd2: int, expected: int) -> None:
    assert DecimalDate.diff_days(dd1, dd2) == expected


def test_diff_days_next() -> None:
    # GIVEN
    dd1: DecimalDate = DecimalDate(2024_03_01)
    dd7: DecimalDate = DecimalDate(2024_03_07)
    # WHEN
    diff: int = DecimalDate.diff_days(dd1, dd7)
    # THEN
    assert dd1.next(diff) == dd7


def test_diff_days_left_is_none_raise_type_error() -> None:
    dd_left: DecimalDate | None = None
    dd_right: DecimalDate | None = DecimalDate(2024_03_01)
    with pytest.raises(TypeError):
        _ = DecimalDate.diff_days(dd_left, dd_right)  # type: ignore[arg-type]


def test_diff_days_right_is_none_raise_type_error() -> None:
    dd_left: DecimalDate | None = DecimalDate(2024_03_01)
    dd_right: DecimalDate | None = None
    with pytest.raises(TypeError):
        _ = DecimalDate.diff_days(dd_left, dd_right)  # type: ignore[arg-type]


"""
from_ymd
"""


def test_from_ymd() -> None:
    # GIVEN
    dd: DecimalDate = DecimalDate(2021_02_14)
    # WHEN
    year = dd.year()
    month = dd.month()
    day = dd.day()
    sut = DecimalDate.from_ymd(year, month, day)
    # THEN
    assert year == 2021
    assert month == 2
    assert day == 14
    assert sut == dd
