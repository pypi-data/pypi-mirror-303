from typing import Literal

from decimaldate import DecimalDate

dd: Literal[20231102] = 2023_11_02
ds: Literal["20231102"] = "20231102"


"""
__str__
"""


def test_dunder_str_integer_prints_integer() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(dd)
    expected: str = str(dd)
    actual: str = str(sut)
    # THEN
    assert expected == actual


def test_dunder_str_string_prints_integer() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert int(ds) == sut.as_int()
    assert ds == str(sut)


"""
__repr__
"""


def test_dunder_repr_str() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(ds)
    # THEN
    assert repr(sut) == f"DecimalDate({ds})"


def test_dunder_repr_int() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(dd)
    # THEN
    assert repr(sut) == f"DecimalDate({dd})"


"""
__int__
"""


def test_dunder_int_integer() -> None:
    # WHEN
    sut: DecimalDate = DecimalDate(dd)
    # THEN
    assert dd == sut.as_int()
    assert dd == int(sut)
