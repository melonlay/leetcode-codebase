# LeetCode 7: Reverse Integer - Solution Explanation

## Problem Summary

Given a signed 32-bit integer `x`, reverse its digits. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return 0.

## Algorithmic Approach

The solution involves extracting digits from the original number, building the reversed number, handling the sign separately, and crucially, checking for potential integer overflow *before* it happens.

## Logic Explanation

1.  **Handle Sign:**
    *   Determine the sign of the input `x`. Store `sign = 1` if `x >= 0` and `sign = -1` if `x < 0`.
    *   Work with the absolute value of `x`: `x_abs = abs(x)`.
2.  **Digit Reversal Loop:**
    *   Initialize `reversed_num = 0`.
    *   Loop while `x_abs != 0`:
        *   Extract the last digit: `digit = x_abs % 10`.
        *   Remove the last digit: `x_abs //= 10`.
        *   **Pre-emptive Overflow Check:** This is the critical step. Before updating `reversed_num`, check if `reversed_num * 10 + digit` would exceed the maximum 32-bit signed integer (`INT_MAX = 2**31 - 1`). The check is:
            `if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):`
            If this condition is true, overflow would occur, so return 0 immediately.
            *Note: We only need to check against `INT_MAX` because if the reversed absolute value fits within `INT_MAX`, the negative version (`-reversed_num`) will also fit within `INT_MIN` (`-2**31`), except for the edge case where `x` is `INT_MIN` itself, but reversing `INT_MIN` always overflows `INT_MAX` anyway.* 
        *   Update the reversed number: `reversed_num = reversed_num * 10 + digit`.
3.  **Apply Sign:** After the loop, multiply the `reversed_num` by the original `sign`.
4.  **Return Result:** Return the final `sign * reversed_num`.

## Knowledge Base References

*   **Handle Sign Separately Technique:** The approach of determining the sign, working with the absolute value, and reapplying the sign at the end simplifies the core reversal logic. This is described in `document/techniques/handle_sign_separately.md`, which also uses this problem as an example.
*   **Integer Overflow Check:** The pre-emptive check before multiplying and adding the digit is crucial for adhering to the 32-bit constraint without relying on larger integer types. The strategy for this check is detailed in `document/common_mistakes/integer_overflow_check.md` (specifically the combined operation check), also using this problem as an example.

## Complexity Analysis

*   **Time Complexity:** O(log10(N)), where N is the absolute value of the input integer `x`. The number of iterations is proportional to the number of digits in `x`.
*   **Space Complexity:** O(1). We only use a few variables to store the sign, the reversed number, and the current digit. 