from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Literal, Union

from slupy.core import checks
from slupy.dates import constants, utils


class TimeTravel:
    """
    Class that represents a time-traveller.

    Instance methods:
        - add()
        - copy()
        - diff_for_humans()
        - subtract()

    Properties:
        - dtype
        - initial_value
        - value
    """

    def __init__(self, origin: Union[datetime, date], /) -> None:
        assert utils.is_date_or_datetime_object(origin), "Param must be of type 'date' or 'datetime'"
        self._initial_value = origin.replace()  # make a copy
        self._value = origin.replace()  # make a copy
        self._dtype: Literal["DATE", "DATETIME"] = (
            "DATETIME" if isinstance(self._value, datetime) else "DATE"
        )

    def __str__(self) -> str:
        return self._value_as_string()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value='{self._value_as_string()}')"

    def copy(self) -> TimeTravel:
        """Returns a copy (new instance) of the `TimeTravel` object"""
        return TimeTravel(self.value)

    @property
    def initial_value(self) -> Union[datetime, date]:
        return self._initial_value

    @initial_value.setter
    def initial_value(self, obj) -> None:
        raise NotImplementedError("Not allowed to set the `initial_value` property")

    def _value_as_string(self) -> str:
        """Returns the string representation of the `value` property"""
        if self.dtype == "DATETIME":
            return self.value.strftime(constants.DATETIME_FORMAT)
        return self.value.strftime(constants.DATE_FORMAT)

    @property
    def value(self) -> Union[datetime, date]:
        return self._value

    @value.setter
    def value(self, obj) -> None:
        assert utils.is_date_or_datetime_object(obj), "Param must be of type 'date' or 'datetime'"
        self._value = obj

    @property
    def dtype(self) -> Literal["DATE", "DATETIME"]:
        return self._dtype

    @dtype.setter
    def dtype(self, obj) -> None:
        raise NotImplementedError("Not allowed to set the `dtype` property")

    def _add_years(self, *, years: int = 0) -> TimeTravel:
        updated_year = self.value.year + years
        self.value = utils.update_year(self.value, to_year=updated_year, leap_forward=True)
        return self

    def _subtract_years(self, *, years: int = 0) -> TimeTravel:
        updated_year = self.value.year - years
        self.value = utils.update_year(self.value, to_year=updated_year, leap_forward=False)
        return self

    def _compute_day_of_month_after_travelling(self, *, to_year: int, to_month: int, day_of_month: int) -> int:
        """
        Used for cases where day-of-month could be 29, 30, 31.
        Returns the day-of-month to use [1-31].
        """
        assert checks.is_positive_integer(day_of_month) and 29 <= day_of_month <= 31, (
            "Param `day_of_month` must be one of: [29, 30, 31]"
        )
        if to_month in constants.MONTHS_HAVING_30_DAYS:
            return day_of_month if day_of_month < 30 else 30
        elif to_month in constants.MONTHS_HAVING_31_DAYS:
            return day_of_month
        return 29 if utils.is_leap_year(to_year) else 28

    def _add_months(self, *, months: int = 0) -> TimeTravel:
        diff_years, diff_months = divmod(months, constants.NUM_MONTHS_PER_YEAR)
        if diff_years > 0:
            self = self._add_years(years=diff_years)
        if diff_months == 0:
            return self
        updated_month = (
            (self.value.month + diff_months) % constants.NUM_MONTHS_PER_YEAR
            if self.value.month + diff_months > constants.NUM_MONTHS_PER_YEAR else
            self.value.month + diff_months
        )
        updated_year = (
            self.value.year + 1
            if self.value.month + diff_months > constants.NUM_MONTHS_PER_YEAR else
            self.value.year
        )
        if 1 <= self.value.day <= 28:
            self.value = self.value.replace(year=updated_year, month=updated_month)
        else:
            day_of_month = self._compute_day_of_month_after_travelling(
                to_year=updated_year,
                to_month=updated_month,
                day_of_month=self.value.day,
            )
            self.value = self.value.replace(year=updated_year, month=updated_month, day=day_of_month)
        return self

    def _subtract_months(self, *, months: int = 0) -> TimeTravel:
        diff_years, diff_months = divmod(months, constants.NUM_MONTHS_PER_YEAR)
        if diff_years > 0:
            self = self._subtract_years(years=diff_years)
        if diff_months == 0:
            return self
        updated_month = (
            constants.NUM_MONTHS_PER_YEAR - abs(self.value.month - diff_months)
            if self.value.month - diff_months <= 0 else
            self.value.month - diff_months
        )
        updated_year = self.value.year - 1 if self.value.month - diff_months < 0 else self.value.year
        if 1 <= self.value.day <= 28:
            self.value = self.value.replace(year=updated_year, month=updated_month)
        else:
            day_of_month = self._compute_day_of_month_after_travelling(
                to_year=updated_year,
                to_month=updated_month,
                day_of_month=self.value.day,
            )
            self.value = self.value.replace(year=updated_year, month=updated_month, day=day_of_month)
        return self

    def add(
            self,
            *,
            years: int = 0,
            months: int = 0,
            weeks: int = 0,
            days: int = 0,
            hours: int = 0,
            minutes: int = 0,
            seconds: int = 0,
            milliseconds: int = 0,
            microseconds: int = 0,
        ) -> TimeTravel:
        """Returns the same `TimeTravel` instance after modifying it in-place"""
        assert checks.is_non_negative_integer(years), "Param `years` must be a non-negative integer"
        assert checks.is_non_negative_integer(months), "Param `months` must be a non-negative integer"
        assert checks.is_non_negative_integer(weeks), "Param `weeks` must be a non-negative integer"
        assert checks.is_non_negative_integer(days), "Param `days` must be a non-negative integer"
        assert checks.is_non_negative_integer(hours), "Param `hours` must be a non-negative integer"
        assert checks.is_non_negative_integer(minutes), "Param `minutes` must be a non-negative integer"
        assert checks.is_non_negative_integer(seconds), "Param `seconds` must be a non-negative integer"
        assert checks.is_non_negative_integer(milliseconds), "Param `milliseconds` must be a non-negative integer"
        assert checks.is_non_negative_integer(microseconds), "Param `microseconds` must be a non-negative integer"
        if self.dtype == "DATE":
            assert checks.is_zero_or_none(hours), "Param `hours` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(minutes), "Param `minutes` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(seconds), "Param `seconds` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(milliseconds), "Param `milliseconds` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(microseconds), "Param `microseconds` must not be passed when a date-object is used"
        self = self._add_years(years=years)
        self = self._add_months(months=months)
        self.value += timedelta(
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            milliseconds=milliseconds,
            microseconds=microseconds,
        )
        return self

    def subtract(
            self,
            *,
            years: int = 0,
            months: int = 0,
            weeks: int = 0,
            days: int = 0,
            hours: int = 0,
            minutes: int = 0,
            seconds: int = 0,
            milliseconds: int = 0,
            microseconds: int = 0,
        ) -> TimeTravel:
        """Returns the same `TimeTravel` instance after modifying it in-place"""
        assert checks.is_non_negative_integer(years), "Param `years` must be a non-negative integer"
        assert checks.is_non_negative_integer(months), "Param `months` must be a non-negative integer"
        assert checks.is_non_negative_integer(weeks), "Param `weeks` must be a non-negative integer"
        assert checks.is_non_negative_integer(days), "Param `days` must be a non-negative integer"
        assert checks.is_non_negative_integer(hours), "Param `hours` must be a non-negative integer"
        assert checks.is_non_negative_integer(minutes), "Param `minutes` must be a non-negative integer"
        assert checks.is_non_negative_integer(seconds), "Param `seconds` must be a non-negative integer"
        assert checks.is_non_negative_integer(milliseconds), "Param `milliseconds` must be a non-negative integer"
        assert checks.is_non_negative_integer(microseconds), "Param `microseconds` must be a non-negative integer"
        if self.dtype == "DATE":
            assert checks.is_zero_or_none(hours), "Param `hours` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(minutes), "Param `minutes` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(seconds), "Param `seconds` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(milliseconds), "Param `milliseconds` must not be passed when a date-object is used"
            assert checks.is_zero_or_none(microseconds), "Param `microseconds` must not be passed when a date-object is used"
        self = self._subtract_years(years=years)
        self = self._subtract_months(months=months)
        self.value -= timedelta(
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
            milliseconds=milliseconds,
            microseconds=microseconds,
        )
        return self

    def diff_for_humans(self) -> str:
        """
        Returns a string having a human-readable format of the difference between `value` and `initial_value`.
        Computes it as `value` - `initial_value`.
        """
        difference_in_seconds = (self.value - self.initial_value).total_seconds()
        timetaken_fstring = utils.get_timetaken_fstring(
            num_seconds=abs(difference_in_seconds),
            shorten_unit=False,
        )
        if difference_in_seconds == 0:
            return timetaken_fstring
        sign = "(+)" if difference_in_seconds > 0 else "(-)"
        return f"{sign} {timetaken_fstring}"

