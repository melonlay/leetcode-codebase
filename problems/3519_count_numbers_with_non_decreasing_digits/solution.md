# 3519. Count Numbers with Non-Decreasing Digits

## Problem Summary

Given two integers `l` and `r` (represented as decimal strings) and a base `b`, find the count of integers `x` such that `l <= x <= r`, and the digits of `x` in base `b` are in non-decreasing order (from most significant to least significant). Return the count modulo `10^9 + 7`.

## Approach: Digit DP

This problem asks for a count of numbers within a range satisfying a specific digit-based property (non-decreasing digits in base `b`). This is a classic application of **Digit Dynamic Programming (Digit DP)**.

1.  **Range Counting:** The standard way to count in a range `[l, r]` is to compute `count(<= r) - count(<= l-1)`. We define a helper function `count_le(num, b)` that counts all integers `x` from 0 up to `num` (inclusive) whose base-`b` digits are non-decreasing.

2.  **`count_le(num, b)` using Digit DP:**
    *   Convert the upper bound `num` into its string representation `s` in base `b`.
    *   Use a recursive DP function `solve(index, prev_digit, is_less, is_leading)` with memoization.
    *   **State Variables:**
        *   `index`: The current digit position we are considering in `s` (from left to right, 0-indexed).
        *   `prev_digit`: The value of the digit placed at `index - 1`. Used to enforce the non-decreasing constraint. It's 0 if `is_leading` is true.
        *   `is_less`: A boolean flag. If `True`, the number prefix we've built so far is already strictly smaller than the corresponding prefix of `s`. This means we can place any digit up to `b-1` from now on. If `False`, we are still bounded by the digits of `s`, so the current digit cannot exceed `s[index]`.
        *   `is_leading`: A boolean flag. If `True`, we are currently placing leading zeros. This affects the `prev_digit` constraint (it doesn't apply) and allows us to count numbers shorter than `s` implicitly.
    *   **Base Case:** If `index == len(s)`, we have successfully constructed a valid non-decreasing number. Return 1.
    *   **Transitions:** Iterate through possible digits `d` for the current `index`. The upper bound for `d` is `s[index]` if `is_less` is false, otherwise `b-1`. Check if the non-decreasing constraint (`d >= prev_digit` unless `is_leading`) is met. Recursively call `solve` for `index + 1`, updating `prev_digit`, `is_less`, and `is_leading` accordingly. Sum the results modulo `10^9 + 7`.
    *   **Memoization:** Store the results of `solve(state)` to avoid redundant computations.

3.  **Final Calculation:** The final answer is `(count_le(r_int, b) - count_le(l_int - 1, b) + MOD) % MOD`.

## Implementation Details

*   A helper function `_to_base_b(n, b)` is used for base conversion.
*   The `solve` function is implemented recursively with a dictionary `memo` for memoization, nested inside `_count_le` to ensure the cache is cleared for each call to `_count_le`.
*   The modulo operation is applied at each addition step within the DP to prevent overflow.

## Complexity Analysis

*   **Time Complexity:** Let `N = max(r_int)`. Converting to base `b` takes `O(log_b N)` time. Precomputation for factorials/inverses takes `O(MaxN)` where `MaxN` is the maximum value needed (`~log_b N + b`). The `_count_le` function involves loops proportional to `log_b N` and `b`. Each loop iteration involves `nCr` calculation which is `O(1)` with precomputation. The overall time complexity is dominated by the loops in `_count_le`, resulting in `O(log_b N * b + Precomputation)`. This is efficient.
*   **Space Complexity:** `O(MaxN)` for the precomputed arrays and `O(log_b N)` for the recursion stack during base conversion (if implemented recursively) or the digit list. Overall `O(MaxN)` or `O(log_b N + b)`.

## Knowledge Base Links

*   [[../patterns/digit_dp/digit_dp.md]] (Alternative Approach)
*   [[../optimizations/counting/digit_dp_vs_combinatorics_non_decreasing.md]] (Approach Comparison)
*   [[../mathematical_concepts/combinatorics/combinations_with_repetition.md]] (Core Technique)
*   [[../techniques/combinatorics/iterative_nCr_modulo.md]] (Implementation Detail)
*   [[../common_mistakes/implementation/precomputation_array_size_base_conversion.md]] (Potential Pitfall) 