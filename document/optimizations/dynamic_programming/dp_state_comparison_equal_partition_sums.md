# Optimization: DP State Comparison for Maximizing Equal Partition Sums

## Context

This document compares two different dynamic programming state formulations for solving problems where the goal is to partition a set into two disjoint subsets with equal sums, maximizing that common sum (e.g., LeetCode 956 - Tallest Billboard). Both approaches have the same asymptotic time complexity O(N * S) but differ significantly in constant factors and practical performance due to state space size.

See the base technique documented in [[../../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]].

## State Formulation 1: Signed Difference & Taller Height (Baseline)

*   **State:** `dp[signed_diff] = max_taller_height`
    *   `signed_diff`: The signed difference `s1 - s2`. Can range from `-S` to `+S`.
    *   `max_taller_height`: The maximum height of the *taller* partition (`s1` if `s1 >= s2`, or `s2` if `s2 > s1`, although the linked technique uses `s1` consistently for simplicity) achievable for the given `signed_diff`.
*   **Transitions (for item `x`):**
    *   Add `x` to Set1: `new_diff = signed_diff + x`, `new_taller = max_taller_height + x` (if `x` added to original `s1`) -> update `dp[new_diff]`
    *   Add `x` to Set2: `new_diff = signed_diff - x`, `new_taller = max_taller_height` (if `x` added to original `s2` and `s1` was taller) -> update `dp[new_diff]`
    *   *(Note: The exact update logic depends slightly on always tracking `s1` vs. tracking the genuinely taller one, but the state space remains the primary factor. The linked technique tracks `s1`.)*
*   **Result:** `dp[0]` (which will store the max `s1` when `s1=s2`).
*   **KB File:** [[../../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]]

## State Formulation 2: Absolute Difference & Shorter Height (Optimized)

*   **State:** `dp[abs_diff] = max_shorter_height`
    *   `abs_diff`: The absolute difference `abs(s1 - s2)`. Ranges from `0` to `S`.
    *   `max_shorter_height`: The maximum height of the *shorter* partition achievable for the given `abs_diff`.
*   **Transitions (for item `x`, previous state `diff, s` where `s` = shorter height):**
    *   **Option 1: Add `x` to Taller Side:**
        *   `new_diff = diff + x`
        *   `new_shorter = s`
        *   Update `dp[new_diff] = max(dp.get(new_diff, 0), new_shorter)`.
    *   **Option 2: Add `x` to Shorter Side:**
        *   Calculate new difference: `d = abs(diff - x)`
        *   Calculate new shorter height: `val = s + min(diff, x)`
        *   Update `dp[d] = max(dp.get(d, 0), val)`.
    *   ***Implementation Detail:*** *Option 2 can also be implemented using an `if/else` check instead of `abs()` and `min()` which might offer a slight performance edge:* 
        ```python
        # Inside the loop iterating through previous dp states (diff, s)
        # For current item x:
        if x >= diff:
            # Add x to shorter side, new shorter is s + diff
            new_diff = x - diff
            new_shorter = s + diff
            dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_shorter)
        else: # x < diff
            # Add x to shorter side, new shorter is s + x
            new_diff = diff - x
            new_shorter = s + x
            dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_shorter)
        ```
*   **Result:** `dp[0]` (which stores the max shorter height when diff=0, hence the max equal height).

## Performance Comparison

| Feature         | State 1 (Signed Diff, Taller H) | State 2 (Abs Diff, Shorter H) |
|-----------------|-----------------------------------|---------------------------------|
| State Keys      | `signed_diff` (-S to +S)          | `abs_diff` (0 to S)             |
| Max Keys        | ~ 2S + 1                          | ~ S + 1                         |
| Inner Loop Work | Iterates up to ~2S items          | Iterates up to ~S items         |
| **Performance** | Baseline                          | **Significantly Faster (~2x)**  |

The primary reason **State Formulation 2 is faster** is the **reduced state space**. By using the absolute difference, the `dp` dictionary only needs to store entries for non-negative differences. This effectively halves the maximum number of entries compared to using signed differences. Since the core computation involves iterating through the `dp` dictionary for each input item, reducing the dictionary size directly translates to faster execution time.

## Recommendation

For problems fitting this pattern (maximizing equal partition sums), **State Formulation 2 (`dp[abs_diff] = max_shorter_height`) is strongly recommended** for better performance due to its smaller state space.

## Related Concepts

*   [[../../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]] (Describes State Formulation 1)
*   [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   [[../../data_structures/hash_table_dict.md]] 