from __future__ import annotations

import random
from collections.abc import Generator
from datetime import date, datetime, timedelta
from typing import Any, Literal, NoReturn, Self, TypeAlias

DecimalDateInitTypes: TypeAlias = int | str | datetime | date
"""
The regular types (excluding ``None`` and ``DecimalDate``)
that can be given as argument to 'init' methods.
"""


__all__ = [
    "DecimalDate",
    "DecimalDateRange",
]
""" Objects exposed in module. """
#
# DecimalDate
#


class DecimalDate(object):
    """
    A class to represent a decimal date on the form ``yyyymmdd``.

    The class assumes *only* a Gregorian (went into effect in October 1582) calendar
    with: year, month, and day.

    Only dates that are valid for ``datetime.date`` are accepted.

    Used and exposed``datetime.date`` and ``datetime.datetime`` objects
    in this class are *naive* (meaning *not* TimeZone aware)!

    Examples::

        DecimalDate()              # today's date
        DecimalDate(None)          # today's date
        DecimalDate(20231225)
        DecimalDate("20230518")
        DecimalDate(date.today())
        DecimalDate(datetime.today())

    Objects of this type are immutable.
    """

    # replace __dict__ : optimization and improving immutability
    __slots__ = (
        "_DecimalDate__dd_int",
        "_DecimalDate__dd_str",
        "_DecimalDate__dd_datetime",
        "_DecimalDate__dd_date",
        "_DecimalDate__year",
        "_DecimalDate__month",
        "_DecimalDate__day",
    )

    @staticmethod
    def __split(dd: int) -> tuple[int, int, int]:
        """
        A tuple with the constituent year, month, and day ``(yyyy, mm, dd)``
        from the argument decimal date on the form ``yyyymmdd``

        :param dd: A decimal date on the form ``yyyymmdd``.
        :type dd: int
        :return: A tuple with (year, month, day).
        :rtype: tuple[int, int, int]
        """
        yyyy, remain = divmod(dd, 1_00_00)
        mm, dd = divmod(remain, 1_00)
        return yyyy, mm, dd

    @staticmethod
    def __today_as_int() -> int:
        """
        Today's date as an integer on the form ``yyyymmdd``.\\
        The date is *not* TimeZone aware.

        :return: Today's date on the form ``yyyymmdd``.
        :rtype: int
        """
        today: date = date.today()  # no tzinfo
        return DecimalDate.__date_as_int(today)

    @staticmethod
    def __datetime_as_int(_datetime: datetime) -> int:
        """
        Returns an integer on the form ``yyyymmdd`` from the argument ``datetime``.

        >>> DecimalDate.__datetime_as_int(datetime.today())
        20240906

        :param _datetime: A ``datetime.datetime``.
        :type _datetime: datetime
        :return: Decimal date integer on the form ``yyyymmdd``.
        :rtype: int
        """
        return DecimalDate.__date_as_int(_datetime.date())

    @staticmethod
    def __date_as_int(_date: date) -> int:
        """
        Returns an integer on the form ``yyyymmdd`` from the argument ``date``.

        >>> DecimalDate.__date_as_int(date.today())
        20240906

        :param _date: A ``datetime.date``.
        :type _date: date
        :return: Decimal date integer on the form ``yyyymmdd``.
        :rtype: int
        """
        return DecimalDate.__ymd_as_int(_date.year, _date.month, _date.day)

    @staticmethod
    def __int_as_datetime(dd: int) -> datetime:
        """
        Returns a ``datetime`` from the argument ``int`` on the form ``yyyymmdd``.

        :param dd: A decimal date on the form ``yyyymmdd``.
        :type dd: int
        :return: ``datetime`` representing the argument ``yyyymmdd``.
        :rtype: datetime
        """
        year, month, day = DecimalDate.__split(dd)
        return datetime(year, month, day)

    @staticmethod
    def __ymd_as_int(year: int, month: int, day: int) -> int:
        return year * 1_00_00 + month * 1_00 + day

    @staticmethod
    def __start_of_month(dt: datetime) -> datetime:
        """
        Start date of a year and month taken from the argument.\\
        The day will always be ``1``.

        >>> DicimalDate(DecimalDate.__start_of_month(DecimalDate("2024_02_06").as_datetime()))
        DecimalDate(20240201)

        :param dt: A ``datetime`` object.
        :type dt: datetime
        :return: start date of year and month (day will always be 1).
        :rtype: datetime
        """
        return dt.replace(day=1)  # new datetime

    @staticmethod
    def __end_of_month(dt: datetime) -> datetime:
        """
        End date of a year and month taken from the argument.

        >>> DicimalDate(DecimalDate.__end_of_month(DecimalDate("2024_02_06").as_datetime()))
        DecimalDate(20240229)

        :param dt: A ``datetime``.
        :type dt: datetime
        :return: end date of year and month.
        :rtype: datetime
        """
        # The day 28 exists in every month and 4 days later is always next month
        next_month: datetime = dt.replace(day=28) + timedelta(days=4)
        # Subtract day of next month gives last day of original month
        return next_month - timedelta(days=next_month.day)

    @staticmethod
    def __last_day_of_month(dt: datetime) -> int:
        """
        End day (1-31) of a year and month taken from the argument.

        >>> DecimalDate("2024_02_06")
        29

        :param dt: A ``datetime.datetime``.
        :type dt: datetime
        :return: End day (1-31)
        :rtype: int
        """
        return DecimalDate.__end_of_month(dt).day

    @staticmethod
    def __parse_int_value_from_argument(
        dd: DecimalDateInitTypes | DecimalDate | None,
    ) -> int:
        """
        Integer value of argument.

        The function returns an integer but does not validate the integer as a valid date.

        :param dd: A decimal date representation in one of the valid argument types.
        :type dd: DecimalDateInitTypes | DecimalDate | None
        :raises ValueError: If argument cannot be represented as an integer.
        :raises TypeError: If argument is not one of the valid argument types.
        :return: Integer value parsed from the argument.
                 The value is not guaranteed to be a valid date.
        :rtype: int
        """
        if dd is None:
            # Use the default today's date
            return DecimalDate.__today_as_int()

        elif isinstance(dd, int):
            return dd

        elif isinstance(dd, str):
            try:
                return int(dd)
            except ValueError as e_info:
                raise ValueError(f"argument {dd} is not a valid literal.") from e_info

        elif isinstance(dd, datetime):
            return DecimalDate.__datetime_as_int(dd)

        elif isinstance(dd, date):
            return DecimalDate.__date_as_int(dd)

        elif isinstance(dd, DecimalDate):
            return dd.as_int()

        else:
            raise TypeError(
                f"argument {dd} is not a valid literal on the form `yyyymmdd`."
            )

    #
    # Initialization
    #

    def __init__(
        self: Self,
        dd: DecimalDateInitTypes | Self | None = None,
    ) -> None:
        """
        Construct an immutable ``DecimalDate`` instance.

        If argument is not present or ``None``, then use today's date.

        :param dd: date representation on the form ``yyyymmdd`` or a ``datetime``, defaults to ``None``
        :type dd: DecimalDateInitTypes | Self | None, optional
        :raises ValueError: If not a valid date, that can be represented on the form ``yyyymmdd``.
        :raises TypeError: If argument type is not valid (``None``, ``DecimalDate``, ``int``, ``str``, ``datetime``).
        """

        #
        # Instance variables
        # These have been placed in `__slots__`
        #

        self.__dd_int: int
        """ Internal instance value of the decimal date as an ``int`` on the form ``yyyymmdd``. """

        self.__dd_str: str
        """ Internal instance value of the decimal date as a ``str`` on the form ``"yyyymmdd"``. """

        self.__dd_datetime: datetime
        """ Internal instance value of the decimal date as a ``datetime.datetime``. """

        self.__year: int
        """ Internal instance value of the year (1-9999). """

        self.__month: int
        """ Internal instance value of the month (1-12). """

        self.__day: int
        """ Internal instance value of the day (1-31). """

        # ---

        # Raises error if an integer can not be inferred
        self.__dd_int = DecimalDate.__parse_int_value_from_argument(dd)

        # If not a valid Gregorian date, then the following raises `ValueError`
        try:
            self.__dd_datetime = DecimalDate.__int_as_datetime(self.__dd_int)
        except ValueError as e_info:
            raise ValueError(
                f"argument {dd} is not a valid literal on the form `yyyymmdd`."
            ) from e_info

        self.__dd_str = str(self.__dd_int)

        self.__year, self.__month, self.__day = DecimalDate.__split(self.__dd_int)

    #
    # Comparisons
    #

    __UNSUPPORTED_OPERAND_TYPE: Literal["Unsupported operand type."] = (
        "Unsupported operand type."
    )

    def __eq__(self: Self, other: object) -> bool:
        """
        The equality operator, ``==``.

        :param other: the DecimalDate object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int == other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __ne__(self: Self, other: object) -> bool:
        """
        The inequality operator, ``!=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int != other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __gt__(self: Self, other: object) -> bool:
        """
        The greater-than operator, ``>``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int > other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __ge__(self: Self, other: object) -> bool:
        """
        The greater-than-or-equal operator, ``>=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int >= other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __lt__(self: Self, other: object) -> bool:
        """
        The less-than operator, ``<``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int < other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    def __le__(self: Self, other: object) -> bool:
        """
        The less-than-or-equal operator, ``<=``.

        :param other: Is the ``DecimalDate`` object to compare with.
        :type other: object
        :raises TypeError: If the object compared to is not a ``DecimalDate``.
        :return: ``True`` or ``False`` depending on the comparison.
        :rtype: bool
        """
        if isinstance(other, DecimalDate):
            return self.__dd_int <= other.__dd_int
        else:
            raise TypeError(DecimalDate.__UNSUPPORTED_OPERAND_TYPE)

    #
    # repr, str, int
    #

    def __repr__(self: Self) -> str:
        """
        When called by built-in ``repr()`` method returning a machine readable representation of ``DecimalDate``.

        >>> DecimalDate("2023_01_06")
        DecimalDate(20230106)

        :return: machine readable representation of this instance.
        :rtype: str
        """
        return f"DecimalDate({self.__dd_int})"

    def __str__(self: Self) -> str:
        """
        When ``str()`` is called on an instance of ``DecimalDate``.

        >>> str(DecimalDate(2023_01_06))
        '20230106'

        :return: string representation of this instance.
        :rtype: str
        """
        return self.__dd_str

    def __int__(self: Self) -> int:
        """
        When ``int()`` is called on an instance of ``DecimalDate``.

        >>> int(DecimalDate("2023_01_06"))
        20230106

        :return: integer representation of this instance.
        :rtype: int
        """
        return self.__dd_int

    #
    # convenience and utils
    #

    def year(self: Self) -> int:
        """
        Year (1-9999).

        >>> DecimalDate("2023_01_06").year()
        2023

        :return: Year (1-9999).
        :rtype: int
        """
        return self.__year

    def month(self: Self) -> int:
        """
        Month (1-12).

        >>> DecimalDate("2023_01_06").month()
        1

        :return: Month (1-12).
        :rtype: int
        """
        return self.__month

    def day(self: Self) -> int:
        """
        Day (1-31).

        >>> DecimalDate("2023_01_06").day()
        6

        :return: Day (0-31).
        :rtype: int
        """
        return self.__day

    def last_day_of_month(self: Self) -> int:
        """
        Day (28-31).

        >>> DecimalDate("2023_01_06").last_day_of_month()
        31

        >>> DecimalDate("2023_02_06").last_day_of_month()
        28

        >>> DecimalDate("2024_02_06").last_day_of_month()  # leap year
        29

        :return: Day (28-31).
        :rtype: int
        """
        return DecimalDate.__last_day_of_month(self.as_datetime())

    def weekday(self: Self) -> int:
        """
        The day of the week as an integer (0-6), where Monday == ``0`` ... Sunday == ``6``.

        See also ``isoweekday()``.

        :return: Day of the week (0-6)
        :rtype: int
        """
        return self.as_datetime().weekday()

    def isoweekday(self: Self) -> int:
        """
        The day of the week as an integer (1-7), where Monday == ``1`` ... Sunday == ``7``.

        See also ``weekday()``.

        :return: Day of the week (1-7)
        :rtype: int
        """
        return self.as_datetime().isoweekday()

    def isoformat(self: Self) -> str:
        """
        The decimal date formatted according to ISO ``yyyy-mm-dd``.

        >>> from decimaldate import DecimalDate
        >>> DecimalDate(2024_09_27).isoformat()
        '2024-09-27'

        To create a ``DecimalDate``from an ISO formatted date,
        use ``datetime.date.fromisoformat()`` or ``datetime.datetime.fromisoformat``.

        >>> from datetime import date
        >>> from decimaldate import DecimalDate
        >>> DecimalDate(date.fromisoformat('2024-09-27'))
        DecimalDate(20240927)

        :return: String representation formatted according to ISO.
        :rtype: str
        """
        return self.as_date().isoformat()

    def start_of_month(self: Self) -> DecimalDate:
        """
        The start date of the month and year of this instance.\\
        The day will always be ``1``.

        :return:  A new ``DecimalDate`` with the value of start-of-month.
        :rtype: DecimalDate
        """
        month_start: datetime = DecimalDate.__start_of_month(self.as_datetime())
        return DecimalDate(month_start)

    def end_of_month(self: Self) -> DecimalDate:
        """
        The end date of the month and year of this instance.\\
        For February the end day will be ``28`` or ``29`` depending on leap year.

        >>> DecimalDate("2023_01_06")
        DecimalDate(20230131)

        >>> DecimalDate("2023_02_06")
        DecimalDate(20230228)

        >>> DecimalDate("2024_02_06")
        DecimalDate(20240229)

        :return: A new ``DecimalDate`` with the value of end-of-month.
        :rtype: DecimalDate
        """
        return DecimalDate(DecimalDate.__end_of_month(self.as_datetime()))

    def split(self: Self) -> tuple[int, int, int]:
        """
        Return this object's integer value on the form ``yyyymmdd``
        as integer values for: year, month and day.

        >>> yyyy, mmm, dd = DecimalDate(2021_02_17).split()
        >>> print(yyyy, mmm, dd)
        2021 2 17

        :return: year, month, and day.
        :rtype: tuple[int, int, int]
        """
        return (self.__year, self.__month, self.__day)

    def clone(self: Self) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance identical to original.

        Note that ``DecimalDate`` is immutable, so consider a regular assignment.

        >>> today = DecimalDate().today()
        >>> today.clone() == today
        True

        >>> today = DecimalDate().today()
        >>> today.clone() is today
        False

        :return: A new ``DecimalDate`` instance identical to original.
                 But not same reference.
        :rtype: DecimalDate
        """
        return DecimalDate(self.as_int())

    def next(self: Self, delta_days: int = 1) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance ``delta_days`` days in the future.

        * The default argument value of ``1`` is the day after.
        * If the argument value is ``0`` then it the date of this instance.
        * If the argument is negative (<0) then it will be days in the past (opposite of future).

        :param delta_days: days in the future, defaults to ``1``.
        :type delta_days: int, optional
        :raises TypeError: if ``delta_days`` is not an ``int``.
        :return: A new ``DecimalDate`` offset with argument days.
        :rtype: DecimalDate
        """
        if not isinstance(delta_days, int):
            raise TypeError("argument for `next` is not `int`")
        next_date: datetime = self.as_datetime() + timedelta(delta_days)
        return DecimalDate(next_date)

    def previous(self: Self, delta_days: int = 1) -> DecimalDate:
        """
        Creates a new ``DecimalDate`` instance ``delta_days`` days in the past.

        * The default argument value of ``1`` is the day before.
        * If the argument value is ``0`` then it the date of this instance.
        * If the argument is negative (<0) then it will be days in the future (opposite of past).

        :param delta_days: days in the past, defaults to ``1``.
        :type delta_days: int, optional
        :raises TypeError: if ``delta_days`` is not an ``int``
        :return: A new ``DecimalDate`` offset with argument days.
        :rtype: DecimalDate
        """
        if not isinstance(delta_days, int):
            raise TypeError("argument for `previous` is not `int`")
        return self.next(-delta_days)

    #
    # As ...
    #

    def as_int(self: Self) -> int:
        """
        This ``DecimalDate`` instance's date as a ``int`` object on the form ``yyyymmdd``.

        Convenience method similar to ``int()``.

        >>> DecimalDate(2023_04_18).as_int()
        20230418

        >>> dd = DecimalDate(2023_04_18)
        >>> int(dd) == dd.as_int()
        True

        :return: Integer representation on the form ``yyyymmdd``.
        :rtype: int
        """
        return self.__dd_int

    def as_str(
        self: Self,
        sep: str | None = None,
    ) -> str:
        """
        This ``DecimalDate`` instance's date with an optional separator as a ``str`` object.

        >>> DecimalDate(2023_04_18).as_str()
        '20230418'

        >>> DecimalDate(2023_04_18).as_str('.')
        '2023.04.18'

        :param sep: Optional separator, defaults to ``None``.
        :type sep: str | None, optional
        :return: String representation on the form ``"yyyymmdd"``.
                 Or if separator then on the form ``"yyyy_mm_dd"`` where ``_`` is the separator.
        :rtype: str
        """
        if not sep:
            # None or empty string, then return the internal string value
            return self.__dd_str
        yyyy, mm, dd = self.split()
        return f"{yyyy:04d}{sep}{mm:02d}{sep}{dd:02d}"

    def as_date(self: Self) -> date:
        """
        This ``DecimalDate`` instance's date as a ``datetime.date`` object.

        :return: ``datetime.date`` representation.
        :rtype: date
        """
        return self.__dd_datetime.date()

    def as_datetime(self: Self) -> datetime:
        """
        This ``DecimalDate`` instance's date as a ``datetime.datetime`` object.

        :return: ``datetime.datetime`` representation.
        :rtype: datetime
        """
        return self.__dd_datetime

    #
    #
    #

    @classmethod
    def try_instantiate(
        cls,
        dd: DecimalDateInitTypes | DecimalDate | None = None,
    ):
        """
        A new instance of ``DecimalDate`` if successful;
        otherwise ``None``.

        If no argument is given then uses today's date.

        >>> dd: DecimalDate = DecimalDate.try_instantiate(2024_27_09)
        >>> if dd:
        >>>     print(f"success {dd}")
        >>> else:
        >>>     print(f"failure {dd}")
        success 20240927

        >>> dd: DecimalDate = DecimalDate.try_instantiate(2024_09_27)
        >>> if dd:
        >>>     print(f"success {dd}")
        >>> else:
        >>>     print(f"failure {dd}")
        failure None

        >>> DecimalDate.try_instantiate() == DecimalDate.today()
        True
        """

        try:
            return cls(dd)
        except (ValueError, TypeError):
            return None

    @classmethod
    def today(cls):
        """
        Todays's date as a ``DecimalDate`` instance.
        """
        return cls(cls.__today_as_int())

    @classmethod
    def yesterday(cls):
        """
        Yesterdays's date as a ``DecimalDate`` instance.
        """
        return cls.today().previous()

    @classmethod
    def tomorrow(cls):
        """
        Tomorrow's date as a ``DecimalDate`` instance.
        """
        return cls.today().next()

    @staticmethod
    def range(
        start_inclusive: DecimalDate | DecimalDateInitTypes,
        stop_exclusive: DecimalDate | DecimalDateInitTypes,
        step: int = 1,
        /,
    ) -> DecimalDateRange:
        """
        Return an object that produces a sequence of ``DecimalDate`` objects
        from ``start`` (inclusive) to ``stop`` (exclusive)
        by one day.

        Valid argument types are (except``None``) identical to ``DecimalDate``.

        >>> for dd in DecimalDate.range(2023_05_04, 2023_05_07):
        >>>     print(dd.as_str('.'))
        2023.05.04
        2023.05.05
        2023.05.06

        Similar to https://docs.python.org/3.8/library/functions.html#func-range.

        :param start_inclusive: Sequence start (inclusive).
        :type start_inclusive: DecimalDate | int | str | datetime
        :param stop_exclusive: Sequence stop (exclusive).
        :type stop_exclusive: DecimalDate | int | str | datetime
        :param step: difference between objects in range, defaults to 1
        :type step: int, optional
        :return: _description_
        :rtype: DecimalDateRange
        """
        return DecimalDateRange(start_inclusive, stop_exclusive, step)

    @classmethod
    def count(
        cls,
        start: DecimalDate | DecimalDateInitTypes | None = None,
        step: int = 1,
    ) -> Generator[DecimalDate, Any, NoReturn]:
        """
        Make an iterator that returns evenly spaced decimal dates beginning with start.

        >>> from decimaldate import DecimalDate
        >>> for idx, dd in enumerate(DecimalDate.count(2024_03_01, 7)):
        >>>     if idx >= 6:
        >>>         break
        >>>     print(idx, dd.isoformat())
        0 2024-03-01
        1 2024-03-08
        2 2024-03-15
        3 2024-03-22
        4 2024-03-29
        5 2024-04-05

        Similar to ``itertools.count()``.
        https://docs.python.org/3/library/itertools.html#itertools.count
        intended for ``zip()`` and ``map()``.

        The iterator will continue until it reaches beyond valid ``decimal.date``values;
        eg. less than 1-01-01 (``datetime.MINYEAR``) or greater than 9999-12-31 (``datetime.MAXYEAR``)
        and then raise ``OverflowError``.

        To get the length of the sequence use ``len(dd)`` or ``dd.length()``.

        :param start: The starting decimal date, defaults to ``None``. If no argument or ``None`` uses todays's date as start.
        :type start: DecimalDate | DecimalDateInitTypes, optional
        :param step: difference in day between dates in sequence, defaults to 1
        :type step: int, optional
        :raises TypeError: if ``start``is not a valid argument type for ``DecimalDate`` .
        :raises ValueError: if ``start``is not a valid date.
        :raises TypeError: if ``step``is not an integer.
        :raises ValueError: if ``step``is ``0``.
        :raises: OverflowError when generator reaches beyound valid ``datetime.date`` values (e.g. 9999-12-31).
        :yield: a sequence of evenly spaced decimal dates.
        :rtype: Generator[DecimalDate, Any, NoReturn]
        """
        if not isinstance(step, int):
            raise TypeError("count step argument is not an `int`.")
        if step == 0:
            raise ValueError("count step argument is 0.")

        dd: DecimalDate = cls(start)
        while True:
            # intentionally never stops
            yield dd
            dd = dd.next(step)

    @staticmethod
    def diff_days(
        arg_left: DecimalDate | DecimalDateInitTypes,
        arg_right: DecimalDate | DecimalDateInitTypes,
    ) -> int:
        """
        Difference in days between two decimal dates.

        Result can be positive, 0, or negative.

        No time or TimeZone is considered.

        >>> from decimaldate import DecimalDate
        >>> dd1 = DecimalDate(2024_03_01)
        >>> dd2 = DecimalDate(2024_03_07)
        >>> diff = DecimalDate.diff_days(dd1, dd2)
        >>> diff
        6
        >>> dd1.next(diff) == dd2
        True

        If the dates are identical the difference is ``0``.

        >>> from decimaldate import DecimalDate
        >>> dd = DecimalDate(2024_03_01)
        >>> DecimalDate.diff_days(dd, dd)
        0

        :param arg_left: valid decimal date
        :type arg_left: DecimalDate | DecimalDateInitTypes
        :param arg_right: valid decimal date
        :type arg_right: DecimalDate | DecimalDateInitTypes
        :raises TypeError: if any argument is ``None``.
        :return: difference in days.
        :rtype: int
        """
        if arg_left is None or arg_right is None:
            raise TypeError("argument is None")

        dt_right: datetime = DecimalDate(arg_right).as_datetime()
        dt_left: datetime = DecimalDate(arg_left).as_datetime()

        return (dt_right - dt_left).days

    @staticmethod
    def from_ymd(year: int, month: int, day: int) -> DecimalDate:
        ymd: int = DecimalDate.__ymd_as_int(int(year), int(month), int(day))
        return DecimalDate(ymd)

    @staticmethod
    def __randrange(
        start_inclusive: DecimalDate,
        stop_exclusive: DecimalDate,
        step: int,
    ) -> DecimalDate:
        diff_days: int = DecimalDate.diff_days(start_inclusive, stop_exclusive)
        rnd_day: int = random.randrange(0, diff_days, step)
        return start_inclusive.next(rnd_day)

    @staticmethod
    def randrange(
        start_inclusive: DecimalDate | DecimalDateInitTypes,
        stop_exclusive: DecimalDate | DecimalDateInitTypes,
        step: int = 1,
        /,
    ) -> DecimalDate:
        """
        Return a randomly selected element from range(start, stop, step).

        As the method internally uses https://docs.python.org/3/library/random.html,
        the same warning applies:\\
        *The pseudo-random generators of this module should not be used for security purposes.*

        >>> from decimaldate import DecimalDate
        >>> DecimalDate.randrange(2024_01_01, 2024_01_02)
        DecimalDate(20240101)

        :param start_inclusive: range start (inclusive)
        :type start_inclusive: DecimalDate | DecimalDateInitTypes
        :param stop_exclusive: range stop (exclusive)
        :type stop_exclusive: DecimalDate | DecimalDateInitTypes
        :param step: difference between objects in range, defaults to ``1``
        :type step: int, optional
        :raises TypeError: if ``step`` is not an integer
        :raises ValueError: if ``step`` is ``0``
        :raises ValueError: if start date equals stop date
        :raises ValueError: if "direction" of arguments and ``step`` are not matching
        :return: randomly selected element from range
        :rtype: DecimalDate
        """
        if not isinstance(step, int):
            raise TypeError("randrange step argument is not an `int`.")
        if step == 0:
            raise ValueError("randrange step argument is 0.")

        dd_start: DecimalDate = DecimalDate(start_inclusive)
        dd_stop: DecimalDate = DecimalDate(stop_exclusive)

        EMPTY_RANGE: str = "randrange empty range"

        #
        # start_inclusive == stop_exclusive
        #

        if dd_start == dd_stop:
            raise ValueError(EMPTY_RANGE)

        #
        # start_inclusive < stop_exclusive
        #

        if dd_start < dd_stop:
            if step < 0:
                raise ValueError(EMPTY_RANGE)

            return DecimalDate.__randrange(dd_start, dd_stop, step)

        #
        # start_inclusive > stop_exclusive
        #

        if step > 0:
            raise ValueError(EMPTY_RANGE)

        return DecimalDate.__randrange(dd_start, dd_stop, step)


#
# DecimalDateRange
#


class DecimalDateRange(object):
    """
    Return an object that produces a sequence of ``DecimalDate`` objects
    from ``start`` (inclusive) to ``stop`` (exclusive)

    Valid argument types are (except``None``) identical to ``DecimalDate``.

    >>> for dd in DecimalDateRange(2023_05_04, 2023_05_07, 1):
    >>>     print(dd.as_str('.'))
    2023.05.04
    2023.05.05
    2023.05.06

    Objects of this type are immutable.
    """

    @staticmethod
    def __highest_multiple_of(arg: int, div: int) -> int:  # NOSONAR
        """
        Returns the highest multiple of ``0*div``, ``1*div``, ``2*div``, ``3*div`` ...  that is less than or equal to ``arg``.

        >>> highest_multiple_of(7, 1)
        7
        >>> highest_multiple_of(7, 3)
        6
        >>> highest_multiple_of(23, 10)
        20
        >>> highest_multiple_of(23, 40)
        0

        :param arg: number to find the largest number that is a multiple of divider.
        :type arg: int
        :param div: divider
        :type div: int
        :return: largest number that is a multiple of divider.
        :rtype: int
        """
        return (arg // div) * div

    @staticmethod
    def __get_last_in_sequence(
        start_inclusive: DecimalDate,
        stop_exclusive: DecimalDate,
        step: int,
    ) -> DecimalDate | None:

        # sanity check
        if step == 0:
            raise ValueError("argument step 0 is not valid.")

        #
        # start == stop
        #

        if start_inclusive == stop_exclusive:
            return None

        #
        # start < stop
        #

        if start_inclusive < stop_exclusive:
            if step < 0:
                return None
            return start_inclusive.next(
                DecimalDateRange.__highest_multiple_of(
                    DecimalDate.diff_days(start_inclusive, stop_exclusive.previous()),
                    step,
                )
            )

        #
        # start > stop
        #

        if step > 0:
            return None
        return start_inclusive.next(
            DecimalDateRange.__highest_multiple_of(
                DecimalDate.diff_days(start_inclusive, stop_exclusive.next()),
                step,
            )
        )

    @staticmethod
    def __get_length_of_sequence(
        start_inclusive: DecimalDate,
        stop_exclusive: DecimalDate,
        step: int,
    ) -> int:

        # sanity check
        if step == 0:
            raise ValueError("argument step 0 is not valid.")

        #
        # start == stop
        #

        if start_inclusive == stop_exclusive:
            return 0

        #
        # start < stop
        #

        if start_inclusive < stop_exclusive:
            if step < 0:
                return 0
            return (
                DecimalDate.diff_days(
                    start_inclusive,
                    stop_exclusive.previous(),
                )
                // step
            ) + 1

        #
        # start > stop
        #

        if step > 0:
            return 0
        return (
            DecimalDate.diff_days(
                start_inclusive,
                stop_exclusive.next(),
            )
            // step
        ) + 1

    # replace __dict__ : optimization and improving immutability
    __slots__ = (
        "_DecimalDateRange__start",
        "_DecimalDateRange__stop",
        "_DecimalDateRange__step",
        "_DecimalDateRange__length",
        "_DecimalDateRange__last",
    )

    def __init__(
        self: Self,
        start_inclusive: DecimalDate | DecimalDateInitTypes,
        stop_exclusive: DecimalDate | DecimalDateInitTypes,
        step: int = 1,
        /,
    ) -> None:
        """
        Return an object that produces a sequence of ``DecimalDate`` objects
        from ``start`` (inclusive) to ``stop`` (exclusive)
        by ``step`` days.

        Valid argument types for ``start`` and ``stop``
        are identical to ``DecimalDate`` excepting ``None`` ('today').

        Start is expected to be before Stop or the sequence will be empty.

        >>> for dd in DecimalDateRange(2023_05_04, 2023_05_07, 1):
        >>>     print(dd.as_str('.'))
        2023.05.04
        2023.05.05
        2023.05.06

        :param start: Sequence start (inclusive).
        :type start: DecimalDate | int | str | datetime
        :param stop: Sequence stop (exclusive).
        :type stop: DecimalDate | int | str | datetime
        :param step: Sequence step, defaults to ``1``
        :type step: int, optional
        :raises ValueError: If any argument is ``None``
        :raises TypeError: If step argument is not instance of ``int``
        :raises ValueError: If step argument is ``0``
        """
        if start_inclusive is None:
            raise ValueError("DecimalDateRange argument start is None.")
        if stop_exclusive is None:
            raise ValueError("DecimalDateRange argument stop is None.")
        if step is None:
            raise ValueError("DecimalDateRange argument step is None.")
        if not isinstance(step, int):
            raise TypeError("DecimalDateRange argument step is not an `int`.")

        #
        # Instance variables
        # These have been placed in ``__slots__``
        #

        self.__start: DecimalDate
        """ The start of the decimal date range (*inclusive*). """

        self.__stop: DecimalDate
        """ The end of the decimal date range (*exclusive*). """

        self.__step: int
        """ The steps between items in the decimal date range from
        start (*inclusive*) to end (*exclusive*).

        A value of ``1`` will return every date in the decimal date range.
        """

        self.__last: DecimalDate | None
        """ Internal instance value of the last ``DecimalDate`` object in the sequence.

        If ``None`` then sequence is empty.
        """

        self.__length: int
        """ Internal instance value of the length of the range.

        The range start is *inclusive*.\\
        The range stop is *exclusive*.
        """

        #

        self.__start = DecimalDate(start_inclusive)
        self.__stop = DecimalDate(stop_exclusive)
        self.__step = step

        if self.__step == 0:
            raise ValueError("DecimalDateRange argument step 0 is not valid.")

        self.__last = DecimalDateRange.__get_last_in_sequence(
            self.__start,
            self.__stop,
            self.__step,
        )
        # If ``None`` then sequence is empty.

        self.__length = (
            0
            if self.__last is None
            else DecimalDateRange.__get_length_of_sequence(
                self.__start,
                self.__stop,
                self.__step,
            )
        )

    def __repr__(self: Self) -> str:
        """
        When called by built-in ``repr()`` method returning a machine readable representation of ``DecimalDateRange``.

        >>> from decimaldate import DecimalDateRange
        >>> DecimalDateRange("2023_01_06", 2023_02_17)
        DecimalDateRange(20230106, 20230217, 1)

        :return: machine readable representation of this instance.
        :rtype: str
        """
        return f"DecimalDateRange({self.start().as_int()}, {self.stop().as_int()}, {self.step()})"

    def __iter__(self: Self) -> Generator[DecimalDate, Any, None]:
        """
        Return an object that produces a sequence of ``DecimalDate``
        from start (inclusive) to stop (exclusive) by step.

        Behave similar to regular ``range()`` but for ``DecimalDate``:

        :yield: next ``DecimalDate`` in generator sequence.
        :rtype: Generator[DecimalDate, Any, None]
        """

        if self.has_empty_sequence():
            return

        _current: DecimalDate = self.__start

        if self.__start < self.__stop:
            while _current < self.__stop:
                yield _current
                _current = _current.next(self.__step)  # go forward

        else:
            while _current > self.__stop:
                yield _current
                _current = _current.next(self.__step)  # go back

    def __len__(self: Self) -> int:
        """
        The length operator, ``len()``.

        >>> len(DecimalDateRange(DecimalDate(2023_11_11), DecimalDate(2023_11_15)))
        4

        :return: Length of sequence.
        :rtype: int
        """
        return self.__length

    def __contains__(self: Self, dd_contains: DecimalDate) -> bool:
        """
        The containment-check operator, ``in``.

        >>> DecimalDate(2023_11_16) in DecimalDateRange(
        >>>     DecimalDate(2023_11_11), DecimalDate(2023_11_22)
        >>> )
        True
        """
        if not isinstance(dd_contains, DecimalDate):
            raise TypeError(
                "DecimalDateRange contains argument is not a `DecimalDate`."
            )

        #
        # start == stop
        #

        if self.has_empty_sequence():
            return False

        #
        # start < stop
        #

        if self.__start < self.__stop:

            if dd_contains < self.__start:
                return False
            if dd_contains >= self.__stop:
                return False

        #
        # start > stop
        #

        else:

            if dd_contains > self.__start:
                return False
            if dd_contains <= self.__stop:
                return False

        # ---

        diff: int = DecimalDate.diff_days(self.__start, dd_contains)
        return (diff % self.__step) == 0

    def __getitem__(self: Self, index: int) -> DecimalDate:
        """
        The index operator, ``[]``.

        >>> DecimalDateRange(2023_05_04, 2023_05_07)[2]
        DecimalDate(20230506)

        The 0 index is 2023_05_04, 1 is 2023_05_05, and 2 is 2023_05_06

        :param index: index into range [0..len[.
        :type index: int
        :raises TypeError: If index is not an ``int``.
        :raises IndexError: If index is outside sequence [0..len[ or [-len..0[.
        :raises RuntimeError: If failed to compare index.
        :return: Object at index in sequence.
        :rtype: DecimalDate
        """
        if not isinstance(index, int):
            raise TypeError("DecimalDateRange index argument is not an `int`.")

        if self.has_empty_sequence():
            raise IndexError(
                f"DecimalDateRange object index {index} into empty sequence"
            )

        if index == 0:
            return self.__start

        if index > 0:
            if self.__length <= index:
                raise IndexError(
                    f"DecimalDateRange object index {index} out of range: [0..{self.__length}[."
                )

            return self.__start.next(index * self.__step)

        if index < 0:
            if index < -self.__length:
                raise IndexError(
                    f"DecimalDateRange object index {index} out of range: [-{self.__length}..0[."
                )

            return self.__last.next((1 + index) * self.__step)  # type: ignore[union-attr]
            # self.__last is not None (-> empty sequence) so it is safe to ignore mypy error

        # To make `mypy` not complain about missing return statement -> exclude from coverage
        raise RuntimeError("Failure to compare index argument")  # pragma: no cover

    # ---

    def start(self: Self) -> DecimalDate:
        """
        Start of sequence as called when initializing.

        >>> from decimaldate import DecimalDateRange
        >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
        >>> rng.start()
        DecimalDate(20241001)

        :return: start of sequence.
        :rtype: DecimalDate
        """
        return self.__start

    def stop(self: Self) -> DecimalDate:
        """
        Stop of sequence as called when initializing.

        Often different from the last ``DecimalDate`` in the sequence.

        >>> from decimaldate import DecimalDateRange
        >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
        >>> rng.stop()
        DecimalDate(20241101)
        >>> rng.last()
        DecimalDate(20241029)

        :return: stop of sequence.
        :rtype: DecimalDate
        """
        return self.__stop

    def step(self: Self) -> int:
        """
        Step of sequence as called when initializing.

        >>> from decimaldate import DecimalDateRange
        >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
        >>> rng.step()
        4

        :return: step of sequence.
        :rtype: int
        """
        return self.__step

    def length(self: Self) -> int:
        """
        Length of sequence.

        Identical to ``len()``.

        >>> from decimaldate import DecimalDateRange
        >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
        >>> list(rng)
        [DecimalDate(20241001), DecimalDate(20241005), DecimalDate(20241009), DecimalDate(20241013), DecimalDate(20241017), DecimalDate(20241021), DecimalDate(20241025), DecimalDate(20241029)]
        >>> rng.length()
        8
        >>> len(rng)
        8

        >>> from decimaldate import DecimalDate, DecimalDateRange
        >>> rng = DecimalDateRange(DecimalDate.today(), DecimalDate.today())
        >>> list(rng)
        []
        >>> rng.length()
        0
        >>> len(rng)
        0

        :return: length of sequence.
        :rtype: int
        """
        return self.__length

    def last(self: Self) -> DecimalDate | None:
        """
        Last ``DecimalDate`` in sequence.

        Often different from the ``stop`` argument.

        If the sequence is empty; then returns ``None``.

        >>> from decimaldate import DecimalDateRange
        >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
        >>> list(rng)
        [DecimalDate(20241001), DecimalDate(20241005), DecimalDate(20241009), DecimalDate(20241013), DecimalDate(20241017), DecimalDate(20241021), DecimalDate(20241025), DecimalDate(20241029)]
        >>> rng.last()
        DecimalDate(20241029)
        >>> rng.stop()
        DecimalDate(20241101)

        :return: Last ``DecimalDate`` in sequence or ``None`` if empty.
        :rtype: DecimalDate | None
        """
        return self.__last

    def has_empty_sequence(self: Self) -> bool:
        return self.last() is None

    @staticmethod
    def range_month_of_year_and_month(year: int, month: int) -> DecimalDateRange:
        """
        A Decimal date range starting with the first day of the month, and ends (inclusive) with the last day of the month.

        >>> from decimaldate import DecimalDateRange
        >>> DecimalDateRange.range_month_of_year_and_month(2024, 2)
        DecimalDateRange(20240201, 20240301, 1)

        :param year: 'year' of the range
        :type year: int
        :param month: 'month' of the range
        :type month: int
        :return: a new ``DecimalDateRange`` including start end end of argument year and month
        :rtype: DecimalDateRange
        """
        # The first day of this month
        start_inclusive: DecimalDate = DecimalDate.from_ymd(int(year), int(month), 1)

        # The first day of following month - range will end by including last day of this month
        stop_exclusive: DecimalDate = start_inclusive.end_of_month().next()

        # Every day between start and stop
        step: int = 1

        return DecimalDateRange(start_inclusive, stop_exclusive, step)

    @staticmethod
    def range_month_of_decimal_date(
        dd: DecimalDate | DecimalDateInitTypes | None = None,
    ) -> DecimalDateRange:
        """
        A Decimal date range starting with the first day of the month, and ends (inclusive) with the last day of the month.

        >>> from decimaldate import DecimalDateRange
        >>> DecimalDateRange.range_month_of_decimal_date(2024_05_18)
        DecimalDateRange(20240501, 20240601, 1)

        :param dd: if no argument or ``None`` then use today's date
        :type dd: DecimalDate | DecimalDateInitTypes | None
        :return: a new ``DecimalDateRange`` including start end end of argument decimal date
        :rtype: DecimalDateRange
        """
        _dd = DecimalDate(dd)
        year: int = _dd.year()
        month: int = _dd.month()
        return DecimalDateRange.range_month_of_year_and_month(year, month)
