##############
  Change Log
##############

==========
  Latest
==========

New Features
------------

* None.

Other Changes
-------------

* None.

Bugfixes
--------

* None.

======================
  0.3.1 (2024-10-21)
======================

New Features
------------

* Added static method ``DecimalDate.randrange()``.

Other Changes
-------------

* Updates to documentation.

Bugfixes
--------

* None.

======================
  0.3.0 (2024-10-17)
======================

New Features
------------

* Added static method ``DecimalDate.from_ymd()``.
* Added static method ``DecimalDateRange.range_month_of_year_and_month()``.
* Added static method ``DecimalDateRange.range_month_of_decimal_date()``.

Other Changes
-------------

* Updates to documentation.

Bugfixes
--------

* None.

======================
  0.2.4 (2024-10-14)
======================

New Features
------------

* Added static method ``DecimalDate.diff_days()``.

Other Changes
-------------

* Proper calculate ``DecimalDateRange.last()``
* Proper calculate ``DecimalDateRange.length()``
* Proper calculate ``DecimalDateRange.__contains__()`` (``in``)
* Updates to documentation.

Bugfixes
--------

* None.

======================
  0.2.3 (2024-10-10)
======================

New Features
------------

* Added ``DecimalDateRange.has_empty_sequence()`` simplifying internal logic.

Other Changes
-------------

* Updates to documentation.

Bugfixes
--------

* None.

======================
  0.2.2 (2024-10-08)
======================

New Features
------------

* | Implemented inversal of start and stop arguments in ``range()`` and step argument other than ``1`` and ``-1`` in same.
  | **Note**: The implementation of additions to ``range()`` are naive and slow; made to satisfy the creation of unit tests for later release of improvements.

Other Changes
-------------

* Updates to documentation.
* Improved unit tests.
* Unit testing ``count()`` outstanding in 0.2.1.

Bugfixes
--------

* None.

======================
  0.2.1 (2024-10-08)
======================

New Features
------------

* Added ``count()`` - not yet unit tested

Other Changes
-------------

* Updates to documentation.
* Removed dependency of deprecated ``pytest-freezegun``.

Bugfixes
--------

* None.

=======================
  0.2.0 (2024-10-03)
=======================

New Features
------------

* None.

Other Changes
-------------

* Ready for Python 3.13.
* Updates to documentation.

Bugfixes
--------

* None.

=======================
  0.1.12 (2024-09-27)
=======================

New Features
------------

* New convenience methods: 
  
    - ``weekday()``, 
    - ``isoweekday()``, and 
    - ``isoformat()``

    similar to ``datetime``'s methods.

* Now constructor: ``try_initialize()`` that returns ``None`` 
  instead of raising error when failing to initialize.

Other Changes
-------------

* Updates to documentation.
* | Added ``datetime.date`` as a valid argument type to ``__init__``.
  | Includes the method ``as_date()`` and unit tests.

Bugfixes
--------

* None.

======================
  0.1.11 (2024-09-25)
======================

New Features
------------

* None.

Other Changes
-------------

* Updates to documentation.
* Use ``__slots__`` to improve resource use and immutability.
* Use ``__all__`` to manage exports from module

Bugfixes
--------

* ``range()`` raises ``ValueError`` if argument value for step is ``0``.

======================
  0.1.10 (2024-09-23)
======================

New Features
------------

* None.

Other Changes
-------------

* Updates to documentation.

Bugfixes
--------

* None.

======================
  0.1.9 (2024-09-20)
======================

New Features
------------

* None.

Other Changes
-------------

* Updates to documentation.
* Added the file ``MANIFEST.in`` to make the build include the ``LICENSE`` file.

Bugfixes
--------

* None.

======================
  0.1.8 (2024-09-18)
======================

New Features
------------

* None.

Other Changes
-------------

* Minor updates to documentation.
* Added `py.typed` to support typing (see `PEP-561 <https://peps.python.org/pep-0561/#packaging-type-information>`_).

Bugfixes
--------

* None.

======================
  0.1.7 (2024-09-18)
======================

Initial release.
