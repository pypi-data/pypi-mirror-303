from datetime import date, datetime, timezone
import unittest

from slupy.dates.time_travel import TimeTravel


class TestTimeTravel(unittest.TestCase):

    def setUp(self) -> None:
        self.datetime_obj: datetime = datetime(
            year=2020,
            month=5,
            day=25,
            hour=17,
            minute=30,
            second=0,
            tzinfo=timezone.utc,
        )
        self.date_obj: date = date(year=2020, month=5, day=25)

    def test_diff_for_humans(self):
        time_travel = TimeTravel(self.datetime_obj)
        self.assertEqual(
            time_travel.diff_for_humans(),
            "0 seconds",
        )
        time_travel.add(weeks=5, days=5, hours=3, minutes=45, seconds=30, milliseconds=500)
        time_travel.subtract(weeks=1)
        time_travel.add(hours=2)
        self.assertEqual(
            time_travel.diff_for_humans(),
            "(+) 4 weeks, 5 days, 5 hours, 45 minutes, 30 seconds, 500 milliseconds",
        )

    def test_initial_value(self):
        time_travel = TimeTravel(self.date_obj)
        self.assertEqual(time_travel.initial_value, self.date_obj)
        self.assertEqual(time_travel.value, self.date_obj)
        time_travel.add(days=5).subtract(years=5)
        self.assertEqual(time_travel.initial_value, self.date_obj)
        self.assertNotEqual(time_travel.value, self.date_obj)

    def test_value_copy_in_initializer(self):
        time_travel = TimeTravel(self.datetime_obj)
        self.assertEqual(time_travel.value, self.datetime_obj)
        self.assertIsNot(time_travel.value, self.datetime_obj)
        self.assertNotEqual(id(time_travel.value), id(self.datetime_obj))

    def test_dtype(self):
        self.assertEqual(TimeTravel(self.datetime_obj).dtype, "DATETIME")
        self.assertEqual(TimeTravel(self.date_obj).dtype, "DATE")
        with self.assertRaises(AssertionError):
            TimeTravel("Some object that is neither 'date' not 'datetime'")

    def test_add_for_datetime(self):
        time_travel = TimeTravel(self.datetime_obj)
        time_travel.add(years=2)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2022,
                month=5,
                day=25,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(months=32)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=1,
                day=25,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(weeks=2)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=2,
                day=8,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(days=50)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=3,
                day=30,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(hours=100)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=4,
                day=3,
                hour=21,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(minutes=100)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=4,
                day=3,
                hour=23,
                minute=10,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(seconds=300)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=4,
                day=3,
                hour=23,
                minute=15,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(milliseconds=5000)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=4,
                day=3,
                hour=23,
                minute=15,
                second=5,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.add(microseconds=5_000_000)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2025,
                month=4,
                day=3,
                hour=23,
                minute=15,
                second=10,
                tzinfo=timezone.utc,
            ),
        )

    def test_subtract_for_datetime(self):
        time_travel = TimeTravel(self.datetime_obj)
        time_travel.subtract(years=2)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2018,
                month=5,
                day=25,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(months=32)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=9,
                day=25,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(weeks=2)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=9,
                day=11,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(days=50)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=23,
                hour=17,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(hours=100)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=19,
                hour=13,
                minute=30,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(minutes=100)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=19,
                hour=11,
                minute=50,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(seconds=300)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=19,
                hour=11,
                minute=45,
                second=0,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(milliseconds=5000)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=19,
                hour=11,
                minute=44,
                second=55,
                tzinfo=timezone.utc,
            ),
        )
        time_travel.subtract(microseconds=5_000_000)
        self.assertEqual(
            time_travel.value,
            datetime(
                year=2015,
                month=7,
                day=19,
                hour=11,
                minute=44,
                second=50,
                tzinfo=timezone.utc,
            ),
        )

    def test_add_for_date(self):
        time_travel = TimeTravel(self.date_obj)
        time_travel.add(years=2)
        self.assertEqual(
            time_travel.value,
            date(year=2022, month=5, day=25),
        )
        time_travel.add(months=32)
        self.assertEqual(
            time_travel.value,
            date(year=2025, month=1, day=25),
        )
        time_travel.add(weeks=2)
        self.assertEqual(
            time_travel.value,
            date(year=2025, month=2, day=8),
        )
        time_travel.add(days=50)
        self.assertEqual(
            time_travel.value,
            date(year=2025, month=3, day=30),
        )
        with self.assertRaises(AssertionError):
            time_travel.add(hours=10)
        with self.assertRaises(AssertionError):
            time_travel.add(minutes=10)
        with self.assertRaises(AssertionError):
            time_travel.add(seconds=10)
        with self.assertRaises(AssertionError):
            time_travel.add(milliseconds=10)
        with self.assertRaises(AssertionError):
            time_travel.add(microseconds=10)

    def test_subtract_for_date(self):
        time_travel = TimeTravel(self.date_obj)
        time_travel.subtract(years=2)
        self.assertEqual(
            time_travel.value,
            date(year=2018, month=5, day=25),
        )
        time_travel.subtract(months=32)
        self.assertEqual(
            time_travel.value,
            date(year=2015, month=9, day=25),
        )
        time_travel.subtract(weeks=2)
        self.assertEqual(
            time_travel.value,
            date(year=2015, month=9, day=11),
        )
        time_travel.subtract(days=50)
        self.assertEqual(
            time_travel.value,
            date(year=2015, month=7, day=23),
        )
        with self.assertRaises(AssertionError):
            time_travel.subtract(hours=10)
        with self.assertRaises(AssertionError):
            time_travel.subtract(minutes=10)
        with self.assertRaises(AssertionError):
            time_travel.subtract(seconds=10)
        with self.assertRaises(AssertionError):
            time_travel.subtract(milliseconds=10)
        with self.assertRaises(AssertionError):
            time_travel.subtract(microseconds=10)

    def test_yearly_corner_cases_for_date(self):
        # adding/subtracting by `years` from February 29th
        date_obj = date(year=2020, month=2, day=29)

        time_travel_1 = TimeTravel(date_obj)
        time_travel_1.add(years=1)
        self.assertEqual(
            time_travel_1.value,
            date(year=2021, month=3, day=1),
        )
        time_travel_1.subtract(years=1)
        self.assertEqual(
            time_travel_1.value,
            date(year=2020, month=3, day=1),
        )

        time_travel_2 = TimeTravel(date_obj)
        time_travel_2.subtract(years=1)
        self.assertEqual(
            time_travel_2.value,
            date(year=2019, month=2, day=28),
        )
        time_travel_2.add(years=1)
        self.assertEqual(
            time_travel_2.value,
            date(year=2020, month=2, day=28),
        )

    def test_monthly_corner_cases_for_date(self):
        # case 1 - adding/subtracting by `months` from February 29th
        date_obj_1 = date(year=2020, month=2, day=29)

        time_travel_1 = TimeTravel(date_obj_1)
        time_travel_1.add(months=1)
        self.assertEqual(
            time_travel_1.value,
            date(year=2020, month=3, day=29),
        )
        time_travel_1.subtract(months=1)
        self.assertEqual(
            time_travel_1.value,
            date(year=2020, month=2, day=29),
        )

        time_travel_2 = TimeTravel(date_obj_1)
        time_travel_2.subtract(months=1)
        self.assertEqual(
            time_travel_2.value,
            date(year=2020, month=1, day=29),
        )
        time_travel_2.add(months=1)
        self.assertEqual(
            time_travel_2.value,
            date(year=2020, month=2, day=29),
        )

        # case 2 - adding/subtracting by `months` across February 29th
        date_obj_2 = date(year=2020, month=1, day=31)

        time_travel_3 = TimeTravel(date_obj_2)
        time_travel_3.add(months=1)
        self.assertEqual(
            time_travel_3.value,
            date(year=2020, month=2, day=29),
        )
        time_travel_3.add(months=1)
        self.assertEqual(
            time_travel_3.value,
            date(year=2020, month=3, day=29),
        )

        # case 3 - adding/subtracting by `months` jumping over February 29th
        date_obj_3 = date(year=2020, month=1, day=31)
        time_travel_4 = TimeTravel(date_obj_3)
        time_travel_4.add(months=2)
        self.assertEqual(
            time_travel_4.value,
            date(year=2020, month=3, day=31),
        )
        time_travel_4.add(months=1)
        self.assertEqual(
            time_travel_4.value,
            date(year=2020, month=4, day=30),
        )

        # case 4 - adding/subtracting by `months` onto February 28th/29th
        time_travel_4.subtract(months=2)
        self.assertEqual(
            time_travel_4.value,
            date(year=2020, month=2, day=29),
        )
        time_travel_4.subtract(months=12)
        self.assertEqual(
            time_travel_4.value,
            date(year=2019, month=2, day=28),
        )

