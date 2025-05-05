class Solution:
    # Precompute prefix sums for days in months
    _days_in_month_non_leap = [0, 31, 28, 31,
                               30, 31, 30, 31, 31, 30, 31, 30, 31]
    _days_prefix_sum_non_leap = [0] * 13
    for i in range(1, 13):
        _days_prefix_sum_non_leap[i] = _days_prefix_sum_non_leap[i -
                                                                 1] + _days_in_month_non_leap[i]

    _days_in_month_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _days_prefix_sum_leap = [0] * 13
    for i in range(1, 13):
        _days_prefix_sum_leap[i] = _days_prefix_sum_leap[i -
                                                         1] + _days_in_month_leap[i]

    _day_names = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    ]

    def _is_leap(self, year: int) -> bool:
        """Checks if a year is a leap year."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def _count_leaps(self, year: int) -> int:
        """Counts leap years from year 1 up to (and including) year y."""
        # Using integer division which acts like floor
        return year // 4 - year // 100 + year // 400

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """Calculates the day of the week using formulas, avoiding loops.

        Calculates days passed since Jan 1, 1971 (a Friday).
        Does not use the datetime library.

        Args:
            day: The day of the month.
            month: The month of the year.
            year: The year.

        Returns:
            The name of the day of the week.
        """
        # Reference: Jan 1, 1971 was a Friday (index 5)
        reference_day_index = 5

        # 1. Calculate days from full years passed since 1971 (up to year-1)
        # Number of years in the interval [1971, year - 1]
        num_years_passed = year - 1971
        # Number of leap years in the interval [1971, year - 1]
        num_leaps = self._count_leaps(year - 1) - self._count_leaps(1970)
        days_from_years = num_years_passed * 365 + num_leaps

        # 2. Calculate days from full months passed in the current year
        is_current_year_leap = self._is_leap(year)
        prefix_sum_days = self._days_prefix_sum_leap if is_current_year_leap else self._days_prefix_sum_non_leap
        days_from_months = prefix_sum_days[month - 1]

        # 3. Calculate days passed in the current month (excluding the start date)
        days_from_day = day - 1

        # 4. Total days elapsed since reference date
        total_days = days_from_years + days_from_months + days_from_day

        # 5. Calculate final index (0=Sunday, ..., 6=Saturday)
        final_day_index = (reference_day_index + total_days) % 7

        return self._day_names[final_day_index]
