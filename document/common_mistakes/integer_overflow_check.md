# Common Mistake: Not Checking for Integer Overflow Pre-emptively

## Context

When performing arithmetic operations, especially multiplication or addition within a loop, on numbers that might approach the boundaries of their data type (e.g., a 32-bit signed integer), it's crucial to check for potential overflow *before* the operation occurs if the environment restricts the use of larger data types to hold intermediate results.

Directly performing the operation and then checking if the result has wrapped around or exceeded the limit is often not feasible or reliable, especially under strict environment constraints like those sometimes found in LeetCode problems.

## Pre-emptive Check Strategy

Let `MAX_VAL` be the maximum value for the integer type and `MIN_VAL` be the minimum value.

### 1. Addition (`current_val + addition`)

*   **Positive Overflow:** Before calculating `result = current_val + addition`, check:
    `if current_val > MAX_VAL - addition:`
    `   # Overflow will occur`
*   **Negative Overflow:** Before calculating `result = current_val + addition` (where `addition` could be negative, or `current_val` is negative), check:
    `if current_val < MIN_VAL - addition:`
    `   # Overflow will occur`

### 2. Multiplication (`current_val * factor`)

*   **Positive Overflow:** Assuming `current_val` and `factor` are positive. Before calculating `result = current_val * factor`, check:
    `if current_val > MAX_VAL // factor:`
    `   # Overflow will occur`
*   **Negative Overflow:** Assuming `current_val` is negative and `factor` is positive. Before calculating `result = current_val * factor`, check:
    `if current_val < MIN_VAL // factor:`
    `   # Overflow will occur`
    (Note: Integer division `//` behavior with negative numbers needs care, `math.ceil(MIN_VAL / factor)` might be needed depending on language/rounding)

### 3. Combined Operation (e.g., `current_val * 10 + digit`)

This is common when building numbers from digits, like in the "Reverse Integer" problem (LeetCode 7).

*   **Positive Overflow Check (`MAX_VAL = 2147483647`):**
    Before `result = current_val * 10 + digit`:
    `if current_val > MAX_VAL // 10 or (current_val == MAX_VAL // 10 and digit > MAX_VAL % 10):`
    `    # Overflow will occur`
    (Example: `MAX_VAL % 10` is 7 for 32-bit signed int)

*   **Negative Overflow Check (`MIN_VAL = -2147483648`):**
    Before `result = current_val * 10 + digit` (where the intended final result is negative, often handled by reversing the positive absolute value and negating later):
    If constructing a positive `rev_abs` from `abs(x)` and `INT_MIN` is involved, the check often simplifies. If `rev_abs` doesn't overflow `INT_MAX` when constructed, then `-rev_abs` generally won't overflow `INT_MIN` (unless `rev_abs == abs(INT_MIN)` which has specific conditions).
    A direct check before `result = negative_current_val * 10 - digit` (where digit is positive) would be:
    `limit = MIN_VAL // 10`
    `if negative_current_val < limit or (negative_current_val == limit and digit > abs(MIN_VAL % 10)):`
    `    # Overflow will occur`
    (Example: `abs(MIN_VAL % 10)` is 8 for 32-bit signed int)

## Example: LeetCode 7 - Reverse Integer

The solution involves building the reversed integer `rev` from digits `pop` of `abs(x)`.

```python
INT_MAX = 2**31 - 1
rev = 0
while x_abs != 0:
    pop = x_abs % 10
    x_abs //= 10

    # Pre-emptive positive overflow check
    if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
        return 0 # Indicate overflow

    rev = rev * 10 + pop
# Apply sign later
```

Failure to perform these pre-emptive checks can lead to incorrect results or runtime errors in environments without automatic arbitrary-precision integers. 