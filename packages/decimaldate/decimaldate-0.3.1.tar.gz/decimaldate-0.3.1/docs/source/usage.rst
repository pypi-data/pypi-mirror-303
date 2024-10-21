.. _PyPI: https://pypi.org/
.. _python-dateutil: https://dateutil.readthedocs.io/

#########
  Usage
#########

================
  Installation
================

First install package using ``pip``:

.. code:: bash

    python3 - m pip install decimaldate

===============
  DecimalDate
===============

.. note::

   The ``datetime`` objects used internally and being exposed by method calls
   ignores time (hours, minutes, and seconds) and are *not* timezone aware.

``DecimalDate`` has utility and convenience methods,
but for more advanced use,
like determine if a date is a Saturday,
or the difference in days between two dates,
you can use the methods of ``datetime``.

>>> from decimaldate import DecimalDate
>>> DecimalDate.today().as_datetime() - DecimalDate.yesterday().as_datetime()
datetime.timedelta(days=1)

For more complex ``datetime`` computations see python-dateutil_,

Initialization
--------------

No argument or ``None``
    Will use today's date:
        
    .. code:: python
       
       DecimalDate()
       DecimalDate(None)

``int``
    >>> from decimaldate import DecimalDate
    >>> DecimalDate(20240911)
    DecimalDate(20240911)

``str``
    >>> from decimaldate import DecimalDate
    >>> DecimalDate("20240911")
    DecimalDate(20240911)

``decimaldate``
    >>> from decimaldate import DecimalDate
    >>> from datetime import datetime
    >>> DecimalDate(datetime.today()) == DecimalDate.today()
    True

Representation
--------------

``repr()``
    >>> from decimaldate import DecimalDate
    >>> repr(DecimalDate(2024_09_11))
    DecimalDate(20240911)

``int()``
    >>> from decimaldate import DecimalDate
    >>> int(DecimalDate(2024_09_11))
    20240911

``str()``
    >>> from decimaldate import DecimalDate
    >>> str(DecimalDate(2024_09_11))
    '20240911'


Comparisons
-----------

The usual comparison operators are available:
  
  - equality, ``==``
  
    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() == DecimalDate.yesterday()
    False
  
  - inequality, ``!=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() != DecimalDate.yesterday()
    True
  
  - less-than, ``<``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() < DecimalDate.yesterday()
    False

  - less-than-or-equal, ``<=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() <= DecimalDate.yesterday()
    False

  - greater-than, ``>``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() > DecimalDate.yesterday()
    True

  - greater-than-or-equal, ``>=``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today() >= DecimalDate.yesterday()
    True

Instance Methods
----------------

``year()``
    The year of date as an integer (1-9999).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).year()
    2024

``month()``
    The month of date as an integer (1-12).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).month()
    9

``day()``
    The day of date as an integer (1-31).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).day()
    11

``weekday()``
    The day of the week as an integer (0-6), where Monday == ``0`` ... Sunday == ``6``.

    >>> from decimaldate import DecimalDate
    >>> FRIDAY = 4
    >>> DecimalDate(2024_09_27).weekday() == FRIDAY
    True

``isoweekday()``
    The day of the week as an integer (1-7), where Monday == ``1`` ... Sunday == ``7``.

    >>> from decimaldate import DecimalDate
    >>> ISO_FRIDAY = 5
    >>> DecimalDate(2024_09_27).isoweekday() == ISO_FRIDAY
    True

``isoformat()``
    The decimal date as a ``str`` formatted according to ISO (yyyy-mm-dd) and *not* including time or timezone.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_27).isoformat()
    '2024-09-27'

``last_day_of_month()``
    The last day of date's month as an integer (1-31).

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).last_day_of_month()
    30

``start_of_month()``
    A new ``DecimalDate`` instance with the date of start-of-month.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).start_of_month()
    DecimalDate(20240901)

``end_of_month()``
    A new ``DecimalDate`` instance with the date of end-of-month.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).end_of_month()
    DecimalDate(20240930)

``split()``
    Splits date into constituent year, month, and day as a tuple of integers.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).split()
    (2024, 9, 11)

``clone()``
    A new ``DecimalDate`` instance identical to original.

    >>> from decimaldate import DecimalDate
    >>> dd = DecimalDate(2024_09_11)
    >>> clone = dd.clone()
    >>> dd == clone
    True
    >>> dd is dd
    True
    >>> dd is clone
    False

    .. note:: 
        As ``DecimalDate`` is immutable, you should consider assignment instead.

``next()``
    A new ``DecimalDate`` instance with the day after.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next()
    DecimalDate(20240912)

    If ``next()`` is given an argument it will return value days forward.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

    A negative argument is simlar to ``previous()``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(-42)
    DecimalDate(20240731)

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

``previous()``
    A new ``DecimalDate`` instance with the day before.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous()
    DecimalDate(20240910)

    If ``previous()`` is given an argument it will return value days back.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(42)
    DecimalDate(20240731)

    A negative argument is simlar to ``next()``

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).previous(-42)
    DecimalDate(20241023)

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).next(42)
    DecimalDate(20241023)

As other types
--------------

``as_int()``
    ``int`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_int()
    20240911

    Similar to ``ìnt()``

    >>> from decimaldate import DecimalDate
    >>> int(DecimalDate(2023_01_17))
    20230117

``as_str()``
    ``str`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_str()
    '20240911'

    Similar to ``str()``

    >>> from decimaldate import DecimalDate
    >>> str(DecimalDate(2023_01_17))
    '20230117'

    There is an optional argument for separator.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_str('-')
    '2024-09-11'

``as_date()``
    ``datetime.date`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_27).as_date()
    datetime.date(2024, 9, 27)

    The returned ``date`` has no time (hours, minutes, and seconds) and is *not* TimeZone aware.

``as_datetime()``
    ``datetime.datetime`` representation.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate(2024_09_11).as_datetime()
    datetime.datetime(2024, 9, 11, 0, 0)

    The returned ``datetime`` has no time (hours, minutes, and seconds) and is *not* TimeZone aware.

    The ``datetime`` representation is convenient to calculate the difference in days between two dates,
    or to determine if a date is a Saturday.

Class Methods
-------------

``today()``
    A new ``DecimalDate`` instance with today's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.today()

``yesterday()``
    A new ``DecimalDate`` instance with yesterday's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.yesterday()

``tomorrow()``
    A new ``DecimalDate`` instance with tomorrows's date.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.tomorrow()

``range()``
    Return an object that produces a sequence of ``DecimalDate`` objects
    from ``start`` (inclusive) to ``stop`` (exclusive)
    by one day.

    Valid argument types are (except``None``) identical to ``DecimalDate``.

    >>> for dd in DecimalDate.range(2023_05_04, 2023_05_07):
    >>>     print(dd.as_str('.'))
    2023.05.04
    2023.05.05
    2023.05.06

    See ``DecimalDateRange``.

``count()``
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


``try_instantiate()``
    A new instance of ``DecimalDate`` if successful; otherwise ``None``.

    If no argument is given then uses today's date.

    .. note:: 
        No errors will be raised.
    
    >>> from decimaldate import DecimalDate
    >>> DecimalDate.try_instantiate() == DecimalDate(None)
    True
    >>> DecimalDate.try_instantiate(None) == DecimalDate.today()
    True

    An invalid date will return ``None``.

    >>> from decimaldate import DecimalDate
    >>> print(DecimalDate.try_instantiate(2024_27_09))
    None

    A valid date will instantiate a new ``DecimalDate``.

    >>> from decimaldate import DecimalDate
    >>> print(DecimalDate.try_instantiate("2024_09_27"))
    20240927


``diff_days``
    Difference in days between two decimal dates.

    >>> from decimaldate import DecimalDate
    >>> dd1 = DecimalDate(2024_03_01)
    >>> dd2 = DecimalDate(2024_03_07)
    >>> diff = DecimalDate.diff_days(dd1, dd2)
    >>> diff
    6
    >>> dd1.next(diff) == dd2
    True

    If the dates are identical the diffenrence is ``0``.

    >>> from decimaldate import DecimalDate
    >>> dd = DecimalDate(2024_03_01)
    >>> DecimalDate.diff_days(dd, dd)
    0

``from_ymd``
    A new ``DecimalDate`` from arguments: year, month, and day.

    >>> DecimalDate.from_ymd(2021,2,14)
    DecimalDate(20210214)


``randrange``
    A new ``DecimalDate`` instance randomly selected from ``range(start, stop, step)``.

    .. note:: 

        | Similar to ``random.randrange``.
        | See https://docs.python.org/3/library/random.html#random.randrange.

    .. warning:: 

        As the method internally uses the ``random`` module (https://docs.python.org/3/library/random.html),
        the same warning applies:

        The pseudo-random generators of this module should not be used for security purposes.

    >>> from decimaldate import DecimalDate
    >>> DecimalDate.randrange(2024_01_01, 2024_01_02, 1)
    DecimalDate(20240101)

    if step is 0 then raises ``ValueError``.

    if start/stop and step goes in "opposite directions" then raises ``ValueError``.

====================
  DecimalDateRange
====================

Intended use is by using the ``DecimalDate`` static method ``range()``.

.. code:: python

   DecimalDate.range(start, stop)

.. code:: python

   DecimalDateRange(start, stop)

will behave identically.

Creation
--------

``DecimalDateRange``
    >>> from decimaldate import DecimalDate, DecimalDateRange
    >>> for dd in DecimalDateRange(DecimalDate(2024_02_14), DecimalDate(2024_02_17)):
    >>>     print(dd)
    20240214
    20240215
    20240216

Representation
--------------

``repr()``
    >>> from decimaldate import DecimalDate, DecimalDateRange
    >>> repr(DecimalDateRange(DecimalDate(2024_02_14), DecimalDate(2024_02_17), 3))
    DecimalDateRange(20240214, 20240217, 3)

Instance Methods
----------------

``start()``
    Start of sequence as called when initializing.

    >>> from decimaldate import DecimalDateRange
    >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
    >>> rng.start()
    DecimalDate(20241001)

``stop()``
    Stop of sequence as called when initializing.

    Often different from the last ``DecimalDate`` in the sequence.

    >>> from decimaldate import DecimalDateRange
    >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
    >>> rng.stop()
    DecimalDate(20241101)
    >>> rng.last()
    DecimalDate(20241029)

``step()``
    Step of sequence as called when initializing.

    >>> from decimaldate import DecimalDateRange
    >>> rng = DecimalDateRange(2024_10_01, 2024_11_01, 4)
    >>> rng.step()
    4
    
``length()``
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

``last()``
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

``has_empty_sequence()``
    Convenience method similar to ``ddr.last() is None``.

    An empty sequence happens if start and stop date are identical
    or the step is not going the same "direction"" as the start to stop.  

    This behaviour is similar to the regular ``range()``.
    
    >>> from decimaldate import DecimalDate
    >>> ddr = DecimalDate.range(2023_01_23, 2023_01_23)
    >>> ddr.has_empty_sequence()
    True
    >>> len(ddr)
    0
    >>> list(ddr)
    []
    >>> ddr[0]
    # ... IndexError

    >>> from decimaldate import DecimalDateRange
    >>> ddr = DecimalDateRange(2023_01_01, 2024_01_01, 7)
    >>> ddr.has_empty_sequence()
    False

    >>> from decimaldate import DecimalDateRange
    >>> ddr = DecimalDateRange(2023_01_01, 2024_01_01, -7)
    >>> ddr.has_empty_sequence()
    True

    >>> from decimaldate import DecimalDateRange
    >>> ddr = DecimalDateRange(2024_01_01, 2023_01_01, 14)
    >>> ddr.has_empty_sequence()
    True

    >>> from decimaldate import DecimalDateRange
    >>> ddr = DecimalDateRange(2024_01_01, 2023_01_01, -14)
    >>> ddr.has_empty_sequence()
    False


``range_month_of_year_and_month``
    A Decimal date range starting with the first day of the month, and ends (inclusive) with the last day of the month.

    >>> from decimaldate import DecimalDateRange
    >>> DecimalDateRange.range_month_of_year_and_month(2024, 2)
    DecimalDateRange(20240201, 20240301, 1)

    .. note:: 

        The end date of a range is exclusive, so will be the first day of *next* month.

``range_month_of_decimal_date``
    A Decimal date range starting with the first day of the month, and ends (inclusive) with the last day of the month.

    >>> from decimaldate import DecimalDateRange
    >>> DecimalDateRange.range_month_of_decimal_date(2024_05_18)
    DecimalDateRange(20240501, 20240601, 1)

    .. note:: 

        The end date of a range is exclusive, so will be the first day of *next* month.
