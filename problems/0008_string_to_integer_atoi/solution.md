# LeetCode 8: String to Integer (atoi) - Solution Explanation

## Problem Summary

Implement the `atoi` function, which converts a string to a 32-bit signed integer. The function should follow these steps:
1. Discard leading whitespace characters.
2. Check for an optional `+` or `-` sign.
3. Read consecutive digits until a non-digit character or the end of the string is reached.
4. Convert the digits to an integer.
5. If no digits were read, return 0.
6. If the integer is outside the 32-bit signed range `[-2^31, 2^31 - 1]`, clamp it to the range.

## Algorithmic Approach

The solution requires **Strict Sequential Parsing** based on the rules defined. We iterate through the string, maintaining an implicit state (expecting whitespace, then sign, then digits). Crucially, we must handle potential integer overflows *before* they occur during digit accumulation and clamp the final result.

## Logic Explanation

1.  **Initialization:**
    *   Define `INT_MAX = 2**31 - 1` and `INT_MIN = -2**31`.
    *   Initialize `index = 0` to track the current position in the string `s`.
    *   Initialize `sign = 1` (default positive).
    *   Initialize `result = 0` to store the accumulated integer value.
2.  **Skip Leading Whitespace (State 1):**
    *   Use a `while` loop to advance `index` as long as it's within bounds and `s[index]` is a space.
3.  **Check for Sign (State 2):**
    *   If `index` is still within bounds:
        *   If `s[index]` is `'-'`, set `sign = -1` and increment `index`.
        *   Else if `s[index]` is `'+'`, just increment `index`.
4.  **Read Digits and Handle Overflow (State 3):**
    *   Use a `while` loop that continues as long as `index` is within bounds and `s[index]` is a digit.
    *   Inside the loop:
        *   Get the integer value of the digit: `digit = int(s[index])`.
        *   **Pre-emptive Overflow Check:** Before updating `result`, check if `result * 10 + digit` would exceed the limits. The check focuses on `INT_MAX`:
            `if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):`
            If overflow would occur, return `INT_MAX` if `sign` is positive, or `INT_MIN` if `sign` is negative. This effectively handles clamping.
        *   Accumulate the digit: `result = result * 10 + digit`.
        *   Increment `index`.
    *   The loop stops automatically at the first non-digit character.
5.  **Final Result (State 4):**
    *   Apply the determined `sign` to the accumulated `result`: `return sign * result`.

## Knowledge Base References

*   **Strict Sequential Parsing Pattern:** The step-by-step processing (whitespace -> sign -> digits -> stop) is the core of this pattern, which is essential for `atoi`. This is detailed in `document/patterns/strict_sequential_parsing.md`, including an `atoi` example.
*   **Integer Overflow Check:** The pre-emptive check within the digit accumulation loop prevents exceeding the 32-bit integer limits and handles clamping. This specific check is detailed in `document/common_mistakes/integer_overflow_check.md`.
*   **(Implicit) Handle Sign Separately Technique:** Although not explicitly separated like in Problem 7, the logic implicitly follows this by determining the sign first and applying it only at the end. `document/techniques/handle_sign_separately.md` describes this general idea.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the relevant parts of the string at most once.
*   **Space Complexity:** O(1). We only use a few variables for the index, sign, and result. 