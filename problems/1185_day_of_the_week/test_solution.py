import unittest
import time
import datetime
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def _reference_solution(self, day: int, month: int, year: int) -> str:
        """Reference implementation using the same datetime logic."""
        days = [
            "Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"
        ]
        weekday_index = datetime.date(year, month, day).weekday()
        target_index = (weekday_index + 1) % 7
        return days[target_index]

    # === Category 1: Provided Examples Verification ===
    def test_example_1(self):
        day, month, year = 31, 8, 2019
        expected = "Saturday"
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(self._reference_solution(day, month, year), expected)

    def test_example_2(self):
        day, month, year = 18, 7, 1999
        expected = "Sunday"
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(self._reference_solution(day, month, year), expected)

    def test_example_3(self):
        day, month, year = 15, 8, 1993
        expected = "Sunday"
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(self._reference_solution(day, month, year), expected)

    # === Category 2: Custom Small/Edge Case Validation ===
    def test_start_of_range(self):
        day, month, year = 1, 1, 1971  # Friday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Friday")

    def test_end_of_range(self):
        day, month, year = 31, 12, 2100  # Friday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Friday")

    def test_leap_day(self):
        day, month, year = 29, 2, 2000  # Tuesday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Tuesday")

    def test_day_before_leap(self):
        day, month, year = 28, 2, 2000  # Monday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Monday")

    def test_day_after_leap(self):
        day, month, year = 1, 3, 2000  # Wednesday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Wednesday")

    def test_non_leap_feb_28(self):
        day, month, year = 28, 2, 1971  # Sunday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Sunday")

    def test_non_leap_mar_1(self):
        day, month, year = 1, 3, 1971  # Monday
        expected = self._reference_solution(day, month, year)
        self.assertEqual(self.solution.dayOfTheWeek(
            day, month, year), expected)
        self.assertEqual(expected, "Monday")

    def test_various_dates(self):
        test_cases = [
            ((1, 1, 2000), "Saturday"),  # Jan 1st, 2000
            ((25, 12, 2023), "Monday"),  # Christmas 2023
            ((4, 7, 1976), "Sunday"),    # US Bicentennial
            ((14, 2, 2024), "Wednesday")  # Valentine's Day 2024
        ]
        for (d, m, y), expected_day_str in test_cases:
            with self.subTest(date=(d, m, y)):
                expected = self._reference_solution(d, m, y)
                self.assertEqual(self.solution.dayOfTheWeek(d, m, y), expected)
                self.assertEqual(expected, expected_day_str)

    # === Category 3: Large Constraint Stress Test (Performance) ===
    def test_performance_max_date(self):
        day, month, year = 31, 12, 2100
        start_time = time.time()
        result = self.solution.dayOfTheWeek(day, month, year)
        end_time = time.time()
        print(
            f"\nExecution Time (Max Date): {end_time - start_time:.6f} seconds")
        self.assertIsInstance(result, str)  # Basic type check
        self.assertIn(result, ["Sunday", "Monday", "Tuesday",
                      "Wednesday", "Thursday", "Friday", "Saturday"])


if __name__ == '__main__':
    unittest.main()
