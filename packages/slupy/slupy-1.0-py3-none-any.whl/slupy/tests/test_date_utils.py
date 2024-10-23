from datetime import date, datetime, timezone
import unittest

from slupy.dates import functions, utils


class TestDateUtils(unittest.TestCase):

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
        self.date_obj_1: date = date(year=2019, month=2, day=25)  # month with 28 days
        self.date_obj_2: date = date(year=2020, month=2, day=25)  # month with 29 days
        self.date_obj_3: date = date(year=2020, month=12, day=25)  # month with 31 days
        self.date_obj_4: date = date(year=2020, month=4, day=25)  # month with 30 days

    def test_is_first_day_of_month(self):
        self.assertTrue(
            utils.is_first_day_of_month(date(year=2019, month=2, day=1)),
        )
        self.assertTrue(
            not utils.is_first_day_of_month(date(year=2019, month=2, day=2)),
        )

    def test_is_last_day_of_month(self):
        self.assertTrue(
            utils.is_last_day_of_month(date(year=2019, month=2, day=28)),
        )
        self.assertTrue(
            utils.is_last_day_of_month(date(year=2020, month=2, day=29)),
        )
        self.assertTrue(
            not utils.is_last_day_of_month(date(year=2020, month=2, day=28)),
        )
        self.assertTrue(
            utils.is_last_day_of_month(date(year=2020, month=6, day=30)),
        )
        self.assertTrue(
            not utils.is_last_day_of_month(date(year=2020, month=12, day=30)),
        )
        self.assertTrue(
            utils.is_last_day_of_month(date(year=2020, month=12, day=31)),
        )

    def test_is_first_day_of_year(self):
        self.assertTrue(
            utils.is_first_day_of_year(date(year=2019, month=1, day=1)),
        )
        self.assertTrue(
            not utils.is_first_day_of_year(date(year=2019, month=1, day=2)),
        )

    def test_is_last_day_of_year(self):
        self.assertTrue(
            utils.is_last_day_of_year(date(year=2019, month=12, day=31)),
        )
        self.assertTrue(
            not utils.is_last_day_of_year(date(year=2019, month=12, day=30)),
        )

    def test_get_first_day_of_current_month(self):
        self.assertEqual(
            utils.get_first_day_of_current_month(self.date_obj_1),
            date(year=2019, month=2, day=1),
        )

    def test_get_last_day_of_current_month(self):
        self.assertEqual(
            utils.get_last_day_of_current_month(self.date_obj_1),
            date(year=2019, month=2, day=28),
        )
        self.assertEqual(
            utils.get_last_day_of_current_month(self.date_obj_2),
            date(year=2020, month=2, day=29),
        )
        self.assertEqual(
            utils.get_last_day_of_current_month(self.date_obj_3),
            date(year=2020, month=12, day=31),
        )
        self.assertEqual(
            utils.get_last_day_of_current_month(self.date_obj_4),
            date(year=2020, month=4, day=30),
        )

    def test_get_first_day_of_next_month(self):        
        self.assertEqual(
            utils.get_first_day_of_next_month(self.date_obj_3),
            date(year=2021, month=1, day=1),
        )

    def test_is_february_29th(self):
        self.assertTrue(
            utils.is_february_29th(date(year=2020, month=2, day=29)),
        )
        self.assertTrue(
            not utils.is_february_29th(date(year=2020, month=2, day=28)),
        )

    def test_get_day_of_month_suffix(self):
        # cases whose suffix should not be 'th'
        io = [
            (1, "st"),
            (2, "nd"),
            (3, "rd"),
            (21, "st"),
            (22, "nd"),
            (23, "rd"),
            (31, "st"),
        ]
        for input_, output in io:
            self.assertEqual(
                utils.get_day_of_month_suffix(input_),
                output,
            )

        # cases whose suffix should be 'th'
        suffix_should_be_th = sorted(
            list(set(range(1, 31 + 1)).difference(set([day_of_month for day_of_month, _ in io]))),
            reverse=False,
        )
        for day_of_month in suffix_should_be_th:
            self.assertEqual(
                utils.get_day_of_month_suffix(day_of_month),
                "th",
            )

    def test_get_small_and_big_dates(self):
        small = date(year=2020, month=1, day=25)
        big = date(year=2020, month=1, day=26)

        self.assertEqual(
            utils.get_small_and_big_dates(small, big),
            (small, big),
        )
        self.assertEqual(
            utils.get_small_and_big_dates(big, small),
            (small, big),
        )
        self.assertEqual(
            utils.get_small_and_big_dates(small, small),
            (small, small),
        )
        self.assertEqual(
            utils.get_small_and_big_dates(big, big),
            (big, big),
        )

    def test_compare_day_and_month(self):
        self.assertEqual(
            utils.compare_day_and_month(
                date(year=2020, month=1, day=25),
                date(year=2016, month=3, day=16),
            ),
            "<",
        )
        self.assertEqual(
            utils.compare_day_and_month(
                date(year=2016, month=3, day=16),
                date(year=2020, month=1, day=25),
            ),
            ">",
        )
        self.assertEqual(
            utils.compare_day_and_month(
                date(year=2016, month=4, day=20),
                date(year=2020, month=4, day=20),
            ),
            "==",
        )

    def test_update_year(self):
        date_1 = date(year=2020, month=2, day=20)
        self.assertEqual(
            utils.update_year(date_1, to_year=date_1.year + 4),
            date(year=2024, month=2, day=20)
        )

        date_2 = date(year=2020, month=2, day=29)
        self.assertEqual(
            utils.update_year(date_2, to_year=date_2.year + 4),
            date(year=2024, month=2, day=29)
        )
        self.assertEqual(
            utils.update_year(date_2, to_year=date_2.year + 5),
            date(year=2025, month=3, day=1)
        )

    def test_update_month(self):
        date_1 = date(year=2020, month=2, day=20)
        self.assertEqual(
            utils.update_month(date_1, to_month=6),
            date(year=2020, month=6, day=20),
        )
        self.assertEqual(
            utils.update_month(date_1, to_month=12),
            date(year=2020, month=12, day=20),
        )

        date_2 = date(year=2020, month=2, day=29)
        self.assertEqual(
            utils.update_month(date_2, to_month=12),
            date(year=2020, month=12, day=29),
        )
        self.assertEqual(
            utils.update_month(date_2, to_month=3),
            date(year=2020, month=3, day=29),
        )
        self.assertEqual(
            utils.update_month(date_2, to_month=4),
            date(year=2020, month=4, day=29),
        )

        date_3 = date(year=2020, month=3, day=31)
        self.assertEqual(
            utils.update_month(date_3, to_month=12),
            date(year=2020, month=12, day=31),
        )
        self.assertEqual(
            utils.update_month(date_3, to_month=2),
            date(year=2020, month=2, day=29),
        )
        self.assertEqual(
            utils.update_month(date_3, to_month=4),
            date(year=2020, month=4, day=30),
        )

        date_4 = date(year=2019, month=3, day=31)
        self.assertEqual(
            utils.update_month(date_4, to_month=2),
            date(year=2019, month=2, day=28),
        )

        date_5 = date(year=2019, month=1, day=29)
        self.assertEqual(
            utils.update_month(date_5, to_month=3),
            date(year=2019, month=3, day=29),
        )
        self.assertEqual(
            utils.update_month(date_5, to_month=3, jump_to_end=True),
            date(year=2019, month=3, day=31),
        )
        self.assertEqual(
            utils.update_month(date_5, to_month=4),
            date(year=2019, month=4, day=29),
        )
        self.assertEqual(
            utils.update_month(date_5, to_month=4, jump_to_end=True),
            date(year=2019, month=4, day=30),
        )

    def test_compute_absolute_date_difference(self):
        self.assertEqual(
            utils.compute_absolute_date_difference(
                date(year=2020, month=1, day=11),
                date(year=2020, month=6, day=28),
            ),
            (0, 169),
        )
        self.assertEqual(
            utils.compute_absolute_date_difference(
                date(year=2021, month=6, day=28),
                date(year=2020, month=1, day=11),
            ),
            (1, 168),
        )
        self.assertEqual(
            utils.compute_absolute_date_difference(
                date(year=2020, month=6, day=28),
                date(year=2021, month=1, day=11),
            ),
            (0, 197),
        )
        self.assertEqual(
            utils.compute_absolute_date_difference(
                date(year=2019, month=1, day=11),
                date(year=2020, month=6, day=28),
            ),
            (1, 169),
        )
        self.assertEqual(
            utils.compute_absolute_date_difference(
                date(year=2019, month=1, day=11),
                date(year=2021, month=6, day=28),
            ),
            (2, 168),
        )

    def test_compute_date_difference(self):
        self.assertEqual(
            utils.compute_date_difference(
                date(year=2020, month=1, day=11),
                date(year=2020, month=6, day=28),
            ),
            (0, -169),
        )
        self.assertEqual(
            utils.compute_date_difference(
                date(year=2019, month=1, day=11),
                date(year=2020, month=6, day=28),
            ),
            (-1, -169),
        )
        self.assertEqual(
            utils.compute_date_difference(
                date(year=2019, month=1, day=11),
                date(year=2021, month=6, day=28),
            ),
            (-2, -168),
        )
        self.assertEqual(
            utils.compute_date_difference(
                date(year=2021, month=6, day=28),
                date(year=2020, month=1, day=11),
            ),
            (1, 168),
        )
        self.assertEqual(
            utils.compute_date_difference(
                date(year=2020, month=6, day=28),
                date(year=2020, month=1, day=11),
            ),
            (0, 169),
        )

    def test_is_leap_year(self):
        self.assertTrue(
            utils.is_leap_year(2000),
        )
        self.assertTrue(
            not utils.is_leap_year(2001),
        )
        self.assertTrue(
            not utils.is_leap_year(2010),
        )
        self.assertTrue(
            not utils.is_leap_year(2100),
        )

    def test_get_day_of_week(self):
        self.assertEqual(
            utils.get_day_of_week(date(year=1996, month=6, day=28), shorten=False),
            "Friday",
        )
        self.assertEqual(
            utils.get_day_of_week(date(year=1996, month=6, day=28), shorten=True),
            "Fri",
        )

    def test_offset_between_datetimes(self):
        self.assertEqual(
            functions.offset_between_datetimes(
                start=date(year=2000, month=1, day=21),
                end=date(year=2000, month=1, day=27),
                offset_kwargs=dict(days=1),
                ascending=True,
                as_string=True,
            ),
            [
                "2000-01-21",
                "2000-01-22",
                "2000-01-23",
                "2000-01-24",
                "2000-01-25",
                "2000-01-26",
                "2000-01-27",
            ],
        )

    def test_get_datetime_buckets(self):
        self.assertEqual(
            functions.get_datetime_buckets(
                start=date(year=2000, month=1, day=1),
                num_buckets=5,
                offset_kwargs=dict(weeks=1),
                ascending=True,
                as_string=True,
            ),
            [
                ("2000-01-01", "2000-01-07"),
                ("2000-01-08", "2000-01-14"),
                ("2000-01-15", "2000-01-21"),
                ("2000-01-22", "2000-01-28"),
                ("2000-01-29", "2000-02-04"),
            ],
        )

        self.assertEqual(
            functions.get_datetime_buckets(
                start=date(year=2000, month=1, day=1),
                num_buckets=5,
                offset_kwargs=dict(weeks=1),
                ascending=False,
                as_string=True,
            ),
            [
                ('1999-11-28', '1999-12-04'),
                ('1999-12-05', '1999-12-11'),
                ('1999-12-12', '1999-12-18'),
                ('1999-12-19', '1999-12-25'),
                ('1999-12-26', '2000-01-01'),
            ],
        )

    def test_compute_date_difference_in_years(self):
        num_places = 10

        date_1 = date(year=2020, month=6, day=28)
        date_2 = date(year=2020, month=1, day=11)
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_1, date_2),
            round(169 / 366, num_places),
            places=num_places,
        )

        date_1, date_2 = date_2, date_1
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_1, date_2),
            round(169 / 366, num_places) * -1,
            places=num_places,
        )

        date_3 = date(year=2021, month=5, day=25)
        date_4 = date(year=2021, month=5, day=15)
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_3, date_4),
            round(10 / 365, num_places),
            places=num_places,
        )

        date_5 = date(year=2020, month=5, day=15)
        date_6 = date(year=2019, month=5, day=16)
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_5, date_6),
            round(365 / 366, num_places),
            places=num_places,
        )

        date_7 = date(year=2020, month=5, day=17)
        date_8 = date(year=2019, month=5, day=16)
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_7, date_8),
            round(1 + (1 / 365), num_places),
            places=num_places,
        )

        date_9 = date(year=2019, month=5, day=17)
        date_10 = date(year=2018, month=5, day=16)
        self.assertAlmostEqual(
            functions.compute_date_difference_in_years(date_9, date_10),
            round(1 + (1 / 366), num_places),
            places=num_places,
        )

    def test_compute_date_difference_in_weeks_and_days(self):
        date_1 = date(year=2020, month=6, day=28)
        date_2 = date(year=2020, month=1, day=11)
        self.assertEqual(
            functions.compute_date_difference_in_weeks_and_days(date_1, date_2),
            (24, 1),
        )

        date_1, date_2 = date_2, date_1
        self.assertEqual(
            functions.compute_date_difference_in_weeks_and_days(date_1, date_2),
            (-24, -1),
        )

        date_3 = date(year=2019, month=6, day=28)
        date_4 = date(year=2019, month=1, day=11)
        self.assertEqual(
            functions.compute_date_difference_in_weeks_and_days(date_3, date_4),
            (24, 0),
        )

        date_3, date_4 = date_4, date_3
        self.assertEqual(
            functions.compute_date_difference_in_weeks_and_days(date_3, date_4),
            (-24, 0),
        )

        date_5 = date(year=2020, month=6, day=26)
        date_6 = date(year=2020, month=1, day=11)
        self.assertEqual(
            functions.compute_date_difference_in_weeks_and_days(date_5, date_6),
            (23, 6),
        )

