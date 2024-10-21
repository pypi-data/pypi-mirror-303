from datetime import datetime, timedelta

import pytest


def _datetime_as_int(dt: datetime) -> int:
    """
    _summary_

    :param dt: a ``datetime``
    :type dt: is a datetime object
    :return: datetime argument on the form ``yyyymmdd``.
    :rtype: int
    """
    return dt.year * 1_00_00 + dt.month * 1_00 + dt.day


@pytest.fixture(scope="module")
def future_as_decimaldate_int() -> int:
    """
    Adds three days to today's date and return
    an integer representation on the form ``yyyymmdd``.
    """
    today: datetime = datetime.today()  # no tzinfo
    delta: timedelta = timedelta(days=3)
    future_date: datetime = today + delta
    return _datetime_as_int(future_date)


@pytest.fixture(scope="module")
def past_as_decimaldate_int() -> int:
    """
    Subtracts three days from today's date and return
    an integer representation on the form ``yyyymmdd``.
    """
    today: datetime = datetime.today()  # no tzinfo
    delta: timedelta = timedelta(days=3)
    past_date: datetime = today - delta
    return _datetime_as_int(past_date)


@pytest.fixture(scope="module")
def today_as_decimaldate_int() -> int:
    """
    Today's date as integer representation on the form ``yyyymmdd``.
    """
    today: datetime = datetime.today()  # no tzinfo
    return _datetime_as_int(today)
