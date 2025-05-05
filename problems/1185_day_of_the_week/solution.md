# Solution Explanation: LeetCode 1185 - Day of the Week

## 1. Problem Summary

Given a date (day, month, year), return the corresponding day of the week as a string (e.g., "Sunday", "Monday"). The date is guaranteed to be valid and within the range 1971-2100. January 1st, 1971 was a Friday.

## 2. Algorithmic Approach

This solution calculates the day of the week by determining the total number of days elapsed between a known reference date (January 1st, 1971, a Friday) and the target date. This calculation is performed **without using explicit loops** for years or months, instead relying on mathematical formulas and precomputed prefix sums.

This approach avoids using the built-in `datetime` library and avoids iterative counting.

## 3. Logic Explanation

1.  **Reference Date & Precomputation:**
    *   Reference: January 1st, 1971 was a Friday (index 5).
    *   `_day_names`: Stores output strings `["Sunday", ..., "Saturday"]`.
    *   `_is_leap(year)`: Helper function to check for leap years.
    *   `_count_leaps(year)`: Helper function that calculates the total number of leap years from year 1 up to (and including) `year` using the formula `y // 4 - y // 100 + y // 400`.
    *   `_days_prefix_sum_non_leap`, `_days_prefix_sum_leap`: Precomputed arrays where index `i` stores the total number of days from the start of the year up to the beginning of month `i+1` (for non-leap and leap years, respectively).

2.  **Calculate Days from Years (Formula):**
    *   Determine the number of full years passed between 1971 and the target year: `num_years_passed = year - 1971`.
    *   Calculate the number of leap years within that interval `[1971, year - 1]` using the helper function: `num_leaps = self._count_leaps(year - 1) - self._count_leaps(1970)`.
    *   Calculate the total days contributed by these full years: `days_from_years = num_years_passed * 365 + num_leaps`.

3.  **Calculate Days from Months (Prefix Sum):**
    *   Check if the target `year` is a leap year using `_is_leap(year)`.
    *   Select the appropriate prefix sum array (`_days_prefix_sum_leap` or `_days_prefix_sum_non_leap`).
    *   Get the total number of days from the start of the target year up to the beginning of the target `month`: `days_from_months = prefix_sum_array[month - 1]`.

4.  **Calculate Days from Day-of-Month:**
    *   The days elapsed within the target month are simply `days_from_day = day - 1` (since we count days *since* the start).

5.  **Calculate Total Elapsed Days:**
    *   Sum the days from the three parts: `total_days = days_from_years + days_from_months + days_from_day`.

6.  **Calculate Final Day Index:**
    *   The final day index is found by adding the `total_days` to the `reference_day_index` (5 for Friday) and taking the result modulo 7:
    *   `final_day_index = (reference_day_index + total_days) % 7`.

7.  **Return Result:** Return the day name string from `_day_names` using the `final_day_index`.

## 4. Complexity Analysis

*   **Time Complexity:** O(1). All calculations (leap year checks, formula application, array lookups, arithmetic) are constant time operations.
*   **Space Complexity:** O(1). We use a fixed amount of space for precomputed arrays and helper variables, independent of the input date.

## 5. Knowledge Base Links

*   This solution uses specific mathematical formulas and precomputation techniques (prefix sums) to avoid iteration.
    *   Mathematical Concept (Leap Year Calculation): [[../document/mathematical_concepts/calendar/leap_year_calculation.md]]
    *   Technique (Prefix Sum): [[../document/techniques/sequence/prefix_suffix_aggregates.md]]
    *   Optimization Comparison: [[../document/optimizations/date_time/day_of_week_calculation_strategies.md]] 