# LeetCode 9: Palindrome Number - Solution Explanation

## Problem Summary

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. The solution should ideally be done without converting the integer to a string.

## Algorithmic Approach

Instead of converting the number to a string or reversing the entire number (which risks integer overflow), we can reverse only the second half of the number and compare it with the first half.

## Logic Explanation

1.  **Edge Case Handling:**
    *   If `x` is negative, it cannot be a palindrome (due to the `-` sign). Return `False`.
    *   If `x` ends in 0 and `x` is not 0 itself (e.g., 10, 120), it cannot be a palindrome because a non-zero number cannot start with 0. Return `False`.
2.  **Reversing the Second Half:**
    *   Initialize `reversed_half = 0`.
    *   Initialize `original_num = x` (we modify `original_num` while preserving `x`).
    *   Use a `while` loop: `while original_num > reversed_half`.
        *   Inside the loop, extract the last digit of `original_num` (`digit = original_num % 10`).
        *   Append this `digit` to `reversed_half` (`reversed_half = reversed_half * 10 + digit`).
        *   Remove the last digit from `original_num` (`original_num //= 10`).
    *   This loop effectively stops when `reversed_half` has roughly the same number of digits (or one more for odd-length inputs) as the remaining `original_num`.
3.  **Comparison:**
    *   **Even Length:** If `x` had an even number of digits (e.g., 1221), the loop stops when `original_num` (12) equals `reversed_half` (12). The check `original_num == reversed_half` will be true.
    *   **Odd Length:** If `x` had an odd number of digits (e.g., 12321), the loop stops when `original_num` (12) is less than `reversed_half` (123). The middle digit (3) ends up as the last digit added to `reversed_half`. Since the middle digit doesn't affect the palindrome property, we can compare `original_num` with `reversed_half // 10` (123 // 10 = 12). The check `original_num == reversed_half // 10` will be true.
    *   Return `true` if either of these conditions (`original_num == reversed_half` or `original_num == reversed_half // 10`) is met, `false` otherwise.

## Knowledge Base References

*   **Handle Sign Separately Technique:** The initial check for negative numbers (`if x < 0`) aligns with the principle described in `document/techniques/handle_sign_separately.md`, although here it's a simple exclusion rather than processing the absolute value.
*   **Digit Manipulation:** The core loop uses standard techniques (`% 10` and `// 10`) for extracting and removing digits, similar to the integer reversal logic seen in Problem 7 (Reverse Integer) and discussed in `document/common_mistakes/integer_overflow_check.md` (though overflow is less of a concern here).

## Complexity Analysis

*   **Time Complexity:** O(log10(N)), where N is the input integer `x`. We process roughly half the digits of the number.
*   **Space Complexity:** O(1). Only a few variables are used. 