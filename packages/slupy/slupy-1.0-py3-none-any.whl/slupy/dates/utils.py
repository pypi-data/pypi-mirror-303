from __future__ import annotations

from datetime import date, datetime
import math
from typing import Any, Dict, Literal, Optional, Tuple, Union

from slupy.core import checks, conversions
from slupy.dates import constants
from slupy.dates.time_conversions import TimeUnitConverter


def is_date_object(x: Any, /) -> bool:
    return isinstance(x, date) and x.__class__ is date


def is_datetime_object(x: Any, /) -> bool:
    return isinstance(x, datetime) and x.__class__ is datetime


def is_date_or_datetime_object(x: Any, /) -> bool:
    return is_date_object(x) or is_datetime_object(x)


def get_timetaken_dictionary(*, num_seconds: Union[int, float]) -> Dict[str, Union[int, float]]:
    """
    Returns dictionary having the keys: ['weeks', 'days', 'hours', 'minutes', 'seconds', 'milliseconds'] containing the time elapsed.

    >>> get_timetaken_dictionary(num_seconds=3725.4292)
    >>> get_timetaken_dictionary(num_seconds=885354.128129)
    """
    assert checks.is_non_negative_number(num_seconds), "Param `num_seconds` must be a non-negative number"
    weeks, remainder = divmod(num_seconds, TimeUnitConverter.SECONDS_PER_WEEK)
    days, remainder = divmod(remainder, TimeUnitConverter.SECONDS_PER_DAY)
    hours, remainder = divmod(remainder, TimeUnitConverter.SECONDS_PER_HOUR)
    minutes, remainder = divmod(remainder, TimeUnitConverter.SECONDS_PER_MINUTE)
    seconds = math.floor(remainder)
    milliseconds = (remainder - seconds) * TimeUnitConverter.MILLISECONDS_PER_SECOND
    milliseconds = round(milliseconds, 6)

    dictionary_time_taken = {
        "weeks": conversions.integerify_if_possible(weeks),
        "days": conversions.integerify_if_possible(days),
        "hours": conversions.integerify_if_possible(hours),
        "minutes": conversions.integerify_if_possible(minutes),
        "seconds": conversions.integerify_if_possible(seconds),
        "milliseconds": conversions.integerify_if_possible(milliseconds),
    }
    return dictionary_time_taken


def get_timetaken_fstring(*, num_seconds: Union[int, float], shorten_unit: Optional[bool] = False) -> str:
    """Returns f-string containing the elapsed time"""
    dict_time_taken = get_timetaken_dictionary(num_seconds=num_seconds)
    dict_unit_shortener = {
        "weeks": "w",
        "days": "d",
        "hours": "h",
        "minutes": "m",
        "seconds": "s",
        "milliseconds": "ms",
    }
    time_taken_components = [
        f"{value} {dict_unit_shortener.get(unit, unit) if shorten_unit else unit}"
        for unit, value in dict_time_taken.items() if value != 0
    ]
    if not time_taken_components:
        return "0 s" if shorten_unit else "0 seconds"
    time_taken_fstring = ", ".join(time_taken_components)
    return time_taken_fstring


def is_first_day_of_month(dt_obj: Union[datetime, date], /) -> bool:
    """Checks if the given date/datetime object represents the first day of any month"""
    return dt_obj.day == 1


def is_last_day_of_month(dt_obj: Union[datetime, date], /) -> bool:
    """Checks if the given date/datetime object represents the last day of any month"""
    if dt_obj.month in constants.MONTHS_HAVING_30_DAYS:
        return dt_obj.day == 30
    if dt_obj.month in constants.MONTHS_HAVING_31_DAYS:
        return dt_obj.day == 31
    return dt_obj.day == 29 if is_leap_year(dt_obj.year) else dt_obj.day == 28


def is_first_day_of_year(dt_obj: Union[datetime, date], /) -> bool:
    """Checks if the given date/datetime object represents the first day of any year"""
    return dt_obj.month == 1 and dt_obj.day == 1


def is_last_day_of_year(dt_obj: Union[datetime, date], /) -> bool:
    """Checks if the given date/datetime object represents the last day of any year"""
    return dt_obj.month == 12 and dt_obj.day == 31


def get_first_day_of_current_month(dt_obj: Union[datetime, date], /) -> Union[datetime, date]:
    """Returns a new date/datetime object having the first day of the current month"""
    return dt_obj.replace(day=1)


def get_last_day_of_current_month(dt_obj: Union[datetime, date], /) -> Union[datetime, date]:
    """Returns a new date/datetime object having the last day of the current month"""
    current_month = dt_obj.month
    if current_month in constants.MONTHS_HAVING_30_DAYS:
        return dt_obj.replace(day=30)
    elif current_month in constants.MONTHS_HAVING_31_DAYS:
        return dt_obj.replace(day=31)
    return dt_obj.replace(day=29) if is_leap_year(dt_obj.year) else dt_obj.replace(day=28)


def get_first_day_of_next_month(dt_obj: Union[datetime, date], /) -> Union[datetime, date]:
    """Returns a new date/datetime object having the first day of the next month"""
    if dt_obj.month == 12:
        return dt_obj.replace(year=dt_obj.year + 1, month=1, day=1)
    return dt_obj.replace(month=dt_obj.month + 1, day=1)


def is_february_29th(x: Union[datetime, date], /) -> bool:
    """Checks if the given date/datetime object represents February 29th (of any year)"""
    return x.month == 2 and x.day == 29


def get_day_of_month_suffix(day_of_month: int, /) -> Literal["st", "nd", "rd", "th"]:
    """Returns the suffix of the given `day_of_month`"""
    assert checks.is_integer(day_of_month) and 1 <= day_of_month <= 31, "Param `day_of_month` must be between [1, 31]"
    mapper: Dict[int, Literal["st", "nd", "rd", "th"]] = {
        1: "st",
        2: "nd",
        3: "rd",
        21: "st",
        22: "nd",
        23: "rd",
        31: "st",
    }
    suffix = mapper.get(day_of_month, "th")
    return suffix


def get_small_and_big_dates(x: date, y: date, /) -> Tuple[date, date]:
    """
    Returns tuple having `(small_date, big_date)` after comparing `x` and `y`. Ensures that `small_date` <= `big_date`.
    Returns new instances of the date objects.
    """
    a = x.replace()
    b = y.replace()
    if a > b:
        return (b, a)
    if a < b:
        return (a, b)
    return (a, b)


def compare_day_and_month(a: date, b: date, /) -> Literal["<", ">", "=="]:
    """
    Compares only the day and month of the given date objects.
        - If a < b, returns '<'
        - If a > b, returns '>'
        - If a == b, returns '=='
    """
    if a.month < b.month:
        return "<"
    if a.month > b.month:
        return ">"
    if a.day < b.day:
        return "<"
    if a.day > b.day:
        return ">"
    return "=="


def update_year(date_obj: date, /, *, to_year: int, leap_forward: Optional[bool] = True) -> date:
    """
    Returns new date object with the updated year.

    Parameters:
        - date_obj: The date object.
        - to_year (int): The year to jump to.
        - leap_forward (bool): This is for cases where the `date_obj` given falls on February 29th and `to_year` is
        not a leap year. If set to `True` - will update date to March 1st; if `False` - will update date to February 28th.
    """
    if is_february_29th(date_obj) and not is_leap_year(to_year):
        kwargs = dict(month=3, day=1) if leap_forward else dict(month=2, day=28)
        new_date = date_obj.replace(year=to_year, **kwargs)
    else:
        new_date = date_obj.replace(year=to_year)
    return new_date


def update_month(date_obj: date, /, *, to_month: int, jump_to_end: Optional[bool] = False) -> date:
    """
    Returns new date object with the updated month.

    Parameters:
        - date_obj: The date object.
        - to_month (int): The month to jump to.
        - jump_to_end (bool): Used for cases where the day of month is one of: [29, 30, 31]. If set to `True`, jumps
        to the last day of the month.
    """
    day_of_month = date_obj.day
    if 1 <= day_of_month <= 28:
        return date_obj.replace(month=to_month)

    # For cases where `day_of_month` is one of: [29, 30, 31]
    if to_month in constants.MONTHS_HAVING_30_DAYS:
        day_of_month_computed = day_of_month if day_of_month < 30 else 30
    elif to_month in constants.MONTHS_HAVING_31_DAYS:
        day_of_month_computed = day_of_month
    else:
        day_of_month_computed = 29 if is_leap_year(date_obj.year) else 28

    new_date = date_obj.replace(month=to_month, day=day_of_month_computed)
    if jump_to_end:
        new_date = get_last_day_of_current_month(new_date)
    return new_date


def compute_absolute_date_difference(d1: date, d2: date, /) -> Tuple[int, int]:
    """Computes the absolute date-difference, and returns a tuple of (years, days)"""
    if d1 == d2:
        return (0, 0)
    d1_copy = d1.replace()
    d2_copy = d2.replace()
    if d2_copy < d1_copy:
        d1_copy, d2_copy = d2_copy, d1_copy  # ensure that d2_copy > d1_copy
    year_difference = d2_copy.year - d1_copy.year
    operator = compare_day_and_month(d2_copy, d1_copy)
    d1_is_on_leap_day = is_february_29th(d1_copy)
    if operator == ">":
        d1_copy = update_year(d1_copy, to_year=d2_copy.year, leap_forward=False)
    elif operator == "<":
        year_difference -= 1
        d1_copy = update_year(d1_copy, to_year=d2_copy.year - 1, leap_forward=False)
    elif operator == "==":
        return (year_difference, 0)
    day_difference = (d2_copy - d1_copy).days
    if d1_is_on_leap_day:
        day_difference -= 1
    return (year_difference, day_difference)


def compute_date_difference(a: date, b: date, /) -> Tuple[int, int]:
    """Computes the date-difference as `a - b`, and returns a tuple of (years, days)"""
    years, days = compute_absolute_date_difference(a, b)
    if a < b:
        years *= -1
        days *= -1
    return (years, days)


def is_leap_year(year: int, /) -> bool:
    assert isinstance(year, int), "Param `year` must be of type 'int'"
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return True if year % 400 == 0 else False


def get_day_of_week(
        dt_obj: Union[datetime, date],
        /,
        *,
        shorten: Optional[bool] = False,
    ) -> str:
    """
    Returns the day of the week.
    Day of week options when `shorten` is set to False: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].
    Day of week options when `shorten` is set to True: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].
    """
    if shorten:
        return dt_obj.strftime("%a")
    return dt_obj.strftime("%A")

