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
__init__
"""


def test_init_none_none_raises_valueerror() -> None:
    with pytest.raises(
        expected_exception=ValueError,
        match=r".*None.*",
    ):
        _ = DecimalDateRange(None, None)  # type: ignore[arg-type]


def test_init_dd_none_raises_valueerror() -> None:
    with pytest.raises(
        expected_exception=ValueError,
        match=r".*None.*",
    ):
        _ = DecimalDateRange(dd_10_29, None)  # type: ignore[arg-type]


def test_init_none_dd_raises_valueerror() -> None:
    with pytest.raises(
        expected_exception=ValueError,
        match=r".*None.*",
    ):
        _ = DecimalDateRange(None, dd_10_29)  # type: ignore[arg-type]


def test_init_no_arguments_raises_typeerror() -> None:
    with pytest.raises(
        expected_exception=TypeError,
        match=r".*missing 2 required positional arguments.*",
    ):
        _ = DecimalDateRange()  # type: ignore[arg-type, call-arg]


def test_init_none_raises_typeerror() -> None:
    with pytest.raises(
        expected_exception=TypeError,
        match=r".*missing 1 required positional argument.*",
    ):
        _ = DecimalDateRange(None)  # type: ignore[arg-type, call-arg]


def test_init_one_argument_raises_typeerror() -> None:
    with pytest.raises(
        expected_exception=TypeError,
        match=r".*missing 1 required positional argument.*",
    ):
        _ = DecimalDateRange(dd_10_29)  # type: ignore[call-arg]


def test_init_argument_types() -> None:
    # WHEN
    rng: DecimalDateRange = DecimalDateRange(2024_10_21, "20241026")
    # THEN
    assert list(rng) == list(sut)


def test_init_argument_order() -> None:
    # GIVEN
    start: DecimalDate = dd_10_05
    stop: DecimalDate = dd_10_08
    # THEN
    assert len(DecimalDateRange(start, stop, 1)) == 3
    assert len(DecimalDateRange(stop, start, 1)) == 0


def test_init_step_zero_raises_value_error() -> None:
    """
    Tests range argument ``step=0`` raises ``ValueError``.
    """
    with pytest.raises(
        expected_exception=ValueError,
        match=r".*step.*",
    ):
        _: DecimalDateRange = DecimalDateRange(2024_10_21, "20241026", 0)


def test_init_step_none_raises_value_error() -> None:
    """
    Tests range argument ``step=None`` raises ``ValueError``.
    """
    with pytest.raises(
        expected_exception=ValueError,
        match=r".*step.*",
    ):
        _: DecimalDateRange = DecimalDateRange(2024_10_21, "20241026", None)  # type: ignore[arg-type]


def test_init_step_str_raises_type_error() -> None:
    """
    Tests range argument ``step=None`` raises ``TypeError``.
    """
    with pytest.raises(
        expected_exception=TypeError,
        match=r".*step.*",
    ):
        _: DecimalDateRange = DecimalDateRange(2024_10_21, "20241026", "1")  # type: ignore[arg-type]


def test_str() -> None:
    # GIVEN
    step: int = 7
    # WHEN
    _sut: DecimalDateRange = DecimalDateRange(sut_start_incl, sut_stop_excl, step)
    # THEN
    assert (
        repr(_sut)
        == f"DecimalDateRange({sut_start_incl.as_int()}, {sut_stop_excl.as_int()}, {step})"
    )


"""
list()
"""


def test_list() -> None:
    # GIVEN
    expected: list[DecimalDate] = [
        dd_10_21,
        dd_10_22,
        dd_10_23,
        dd_10_24,
        dd_10_25,
    ]
    # THEN
    assert list(sut) == expected
