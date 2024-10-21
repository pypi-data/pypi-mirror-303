from typing import Literal

import pytest

from decimaldate import DecimalDate

dd: Literal[20231102] = 2023_11_02
ds: Literal["20231102"] = "20231102"

"""
as_int
"""


def test_as_int_integer_is_equal() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(dd)
    # THEN
    assert dd == sut.as_int()


def test_as_int_string_is_equal() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert dd == sut.as_int()


"""
as_str
"""


def test_as_str_default_separator_has_no_separator() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert ds == sut.as_str()


@pytest.mark.parametrize(
    "separator,expected",
    [
        pytest.param("-", "2023-11-02"),
        pytest.param(".", "2023.11.02"),
        pytest.param("", "20231102"),
        pytest.param(None, "20231102"),
    ],
)
def test_as_str_with_separator(
    separator: None | str,
    expected: str,
) -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert sut.as_str(separator) == expected
