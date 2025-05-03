# Technique: DP State for Maximizing Equal Partition Sums

## Description

This technique utilizes a specific dynamic programming state formulation to solve problems where the goal is to partition a set of items (e.g., numbers) into two disjoint subsets (`Set1`, `Set2`) such that their sums are equal (`s1 == s2`), and this common sum (`s1`) is maximized. It keeps track of the maximum achievable sum for one subset given the difference between the two subsets.

This is particularly useful for problems like LeetCode 956: Tallest Billboard.

## Core Idea

*   **State:** `dp[diff] = max_s1`
    *   `diff`: The difference between the sum of the first subset and the second subset (`s1 - s2`).
    *   `max_s1`: The maximum achievable sum for the *first* subset (`s1`) when the difference between the subsets is exactly `diff`.
*   **Goal:** Find `dp[0]`, which represents the maximum `s1` when `s1 - s2 = 0`.

## Algorithm Steps (Tabulation)

1.  **Initialization:**
    *   `dp = {0: 0}`: Initialize the DP table (often a hash map/dictionary). A difference of 0 is achievable with a sum `s1 = 0` (using no items).
2.  **Iteration:** For each item `x` in the input set:
    *   Create a temporary copy `dp_next = dp.copy()` to store updates for the current iteration.
    *   Iterate through all existing `(diff, s1)` pairs in the `dp` table from the previous iteration.
    *   For each pair `(diff, s1)`:
        *   **Option 1: Add `x` to `Set1`:**
            *   `new_diff = diff + x`
            *   `new_s1 = s1 + x`
            *   Update `dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_s1)`
        *   **Option 2: Add `x` to `Set2`:**
            *   `new_diff = diff - x` (Since `s2` increases by `x`, the difference `s1 - s2` decreases by `x`)
            *   `new_s1 = s1` (The sum of the first set doesn't change in this case)
            *   Update `dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_s1)`
        *   **Option 3: Ignore `x`:** This is implicitly handled because `dp_next` starts as a copy of `dp`, carrying over previous states.
    *   After processing all `(diff, s1)` pairs for item `x`, update `dp = dp_next`.
3.  **Result:** After iterating through all items, the answer is `dp.get(0, 0)`.

## Complexity

Let `N` be the number of items and `S` be the maximum possible sum (or half the total sum, depending on the problem variant).
*   **Time Complexity:** O(N * S). The outer loop runs `N` times. The inner loop iterates through the `dp` table. The number of distinct `diff` values can range from `-S` to `+S`, making the size of `dp` roughly O(S).
*   **Space Complexity:** O(S) to store the `dp` table.

## Implementation Notes

*   Using a hash map (dictionary in Python) for `dp` is suitable because the `diff` keys can be sparse and include negative values.
*   The copy (`dp_next`) is crucial to ensure that updates within an iteration for item `x` are based on the state *before* considering `x`.

## Related Concepts

*   [[../../algorithms/dynamic_programming/dynamic_programming.md]] (General DP)
*   [[../../data_structures/hash_table_dict.md]] (For DP state storage)
*   Subset Sum Problem variations
*   Partition Problem variations

## Optimization Note

While this technique is correct, an alternative DP state formulation exists that uses the *absolute difference* and tracks the *shorter* height. This alternative reduces the state space size (from `[-S, S]` to `[0, S]`) and often leads to significantly better practical performance (~2x faster). See the comparison here: [[../../optimizations/dynamic_programming/dp_state_comparison_equal_partition_sums.md]].

Furthermore, for moderate N (e.g., N > ~15), a **Meet-in-the-Middle** approach significantly outperforms *any* linear DP approach by changing the exponential complexity base. See the comparison here: [[../../optimizations/partitioning/mitm_vs_linear_dp_max_equal_sum.md]]. 