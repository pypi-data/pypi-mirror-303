from datetime import date
from unittest import TestCase

from guilib.dates.generators import create_days
from guilib.dates.generators import next_first_of_the_month


class TestDateTimeAxis(TestCase):
    def test_create_days(self) -> None:
        begin = date(2024, 3, 1)
        end = date(2024, 6, 1)
        step = 1

        expected: list[date] = [date(2024, m, 1) for m in (3, 4, 5, 6)]
        actual = list(create_days(begin, end, step=step))
        self.assertListEqual(expected, actual)

    def test_next_first_of_the_month(self) -> None:
        for day, expected in [
            (date(2024, 3, 1), date(2024, 4, 1)),
            (date(2024, 11, 1), date(2024, 12, 1)),
            (date(2024, 12, 1), date(2025, 1, 1)),
            (date(2024, 3, 17), date(2024, 4, 1)),
            (date(2024, 3, 31), date(2024, 4, 1)),
        ]:
            with self.subTest(day=day, expected=expected):
                actual = next_first_of_the_month(day)
                self.assertEqual(expected, actual)
