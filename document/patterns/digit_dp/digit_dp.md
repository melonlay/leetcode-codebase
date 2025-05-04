# Pattern: Digit DP (Standard)

## Description

Digit Dynamic Programming (Digit DP) is a technique used to count numbers within a given range `[L, R]` (or `[0, N]`) that satisfy a specific property related to their digits. The property often involves constraints on the sum of digits, the presence/absence of specific digits, divisibility rules, or other digit-based characteristics.

The core idea is to build the numbers digit by digit (usually from most significant to least significant) and use DP to keep track of the count of valid numbers formed so far, considering the constraints.

## Common Problem Type

Count the integers `x` such that `L <= x <= R` and `x` satisfies `Property(x)`.
This is often solved by calculating `count(0, R) - count(0, L-1)`. The main task is implementing the `count(0, N)` function.

## `count(0, N)` Function using Digit DP

We convert the upper bound `N` into a sequence of digits `digits = [d_k, d_{k-1}, ..., d_0]`. The DP state typically involves:

`dp(index, tight, state...)`

*   `index`: The current digit position being considered (from left/most significant `k` down to 0).
*   `tight`: A boolean flag indicating if we are restricted by the digits of `N`.
    *   If `True`, the current digit `d` can only range from `0` up to `digits[index]`. If we choose `d < digits[index]`, the `tight` constraint becomes `False` for subsequent positions. If we choose `d == digits[index]`, `tight` remains `True`.
    *   If `False`, the current digit `d` can range freely from `0` to `9` (or the base maximum). `tight` remains `False`.
*   `state...`: Additional state variables required by the specific `Property(x)`. Examples:
    *   `current_sum`: Tracks the sum of digits chosen so far.
    *   `leading_zeros`: A boolean flag to handle properties sensitive to leading zeros (e.g., distinct digits).
    *   `current_mod`: Tracks the number formed so far modulo some value `M` (for divisibility checks).
    *   `mask`: Bitmask representing digits used so far.

The function `dp` returns the count of valid numbers that can be formed from `index` down to 0, given the `tight` constraint and the current `state`.

## DP Transition

Inside `dp(index, tight, state...)`:

1.  **Base Case:** If `index < 0`, a valid number has been formed. Return 1.
2.  **Memoization:** Check if `dp[index][tight][state...]` has been computed. If so, return the stored value.
3.  **Loop:** Iterate through possible digits `d` for the current `index`.
    *   Determine the upper limit for `d`: `limit = digits[index]` if `tight` is True, else `9`.
    *   Loop `d` from `0` to `limit`.
4.  **Update State:** Calculate the `next_tight` constraint (`tight and (d == limit)`) and the `next_state` based on `d` and the current `state`.
5.  **Check Property:** Ensure the choice of `d` doesn't immediately violate the property (if applicable at this stage).
6.  **Recurse:** Add the result of the recursive call `dp(index - 1, next_tight, next_state...)` to the total count for the current state.
7.  **Store & Return:** Store the computed count in the memoization table and return it.

## Initialization

Start the process by calling `dp(k, True, initial_state...)`, where `k` is the index of the most significant digit of `N`.

## Complexity

*   **Time:** O(NumDigits * MaxTight * StateSpaceSize * Base). Often roughly O(log10(N) * StateSpaceSize * 10).
*   **Space:** O(log10(N) * StateSpaceSize) for the memoization table.

## Variations

*   **Digit DP with Carry:** For problems involving sums where carry matters across positions (like [[./digit_dp_carry_counts.md]]).
*   **Different Bases:** Can be adapted to bases other than 10.

## Foundational Concepts

*   [[../dynamic_programming/dynamic_programming.md]]
*   [[../../techniques/recursion/memoization.md]] 