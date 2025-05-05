# Mathematical Concept: Leap Year Calculation (Gregorian Calendar)

## Definition

A leap year in the Gregorian calendar system is a year that contains an extra day, February 29th. This adjustment helps synchronize the calendar year with the solar year.

## Rule

A year is a leap year if it meets the following conditions:

1.  The year is evenly divisible by 4.
2.  **UNLESS** the year is evenly divisible by 100, **THEN** it is **NOT** a leap year.
3.  **UNLESS** the year is also evenly divisible by 400, **THEN** it **IS** a leap year.

## Implementation (Python Check)

```python
def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Or as a single boolean expression:
def is_leap_compact(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

## Counting Leap Years Up To Year `y`

To efficiently calculate the number of leap years between year 1 and year `y` (inclusive), we can use the inclusion-exclusion principle based on the rules:

`count = floor(y / 4) - floor(y / 100) + floor(y / 400)`

In Python, using integer division (`//`) achieves the floor operation:

```python
def count_leaps(year: int) -> int:
    """Counts leap years from year 1 up to (and including) year y."""
    if year < 1:
        return 0
    return year // 4 - year // 100 + year // 400
```

This formula allows calculating the number of leap years in an interval `[start, end]` efficiently as `count_leaps(end) - count_leaps(start - 1)`.

## Applicability

*   Date and time calculations.
*   Problems involving calendar logic (e.g., finding the day of the week, calculating durations).
*   Simulation problems spanning multiple years. 