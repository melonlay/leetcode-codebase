# 956. Tallest Billboard

## Problem Summary

Given an array of integers `rods`, representing rod lengths, we need to find the largest possible height for a billboard. A billboard requires two steel supports of equal height. These supports are formed by welding together rods from the input array. Each rod can be used at most once, either in the left support or the right support.

We need to partition the `rods` into two disjoint subsets such that their sums are equal. The goal is to maximize this common sum. If no such partition is possible, return 0.

## Algorithmic Strategy

The problem asks us to find two disjoint subsets, say `Set1` and `Set2`, from the `rods` array such that `sum(Set1) == sum(Set2)` and `sum(Set1)` (or `sum(Set2)`) is maximized.

This can be viewed as a variation of the Partition Problem or the Subset Sum problem. We can use dynamic programming to solve this.

Let `dp[diff]` represent the maximum possible sum of the *first* support (`s1`) achievable for a given difference `diff = s1 - s2` between the two supports.

1.  **Initialization:** We start with `dp = {0: 0}`. This signifies that a difference of 0 between the two supports is initially possible with a height of 0 (using no rods).

2.  **Iteration:** We process each rod `r` from the `rods` array one by one. For each rod, we update the `dp` table based on the possibilities derived from the previous state:
    *   We create a copy (`dp_next`) of the current `dp` state to avoid modifying it while iterating.
    *   For each existing `(diff, s1)` pair in the current `dp`:
        *   **Option 1: Add rod `r` to the first support (`s1`).**
            *   The new sum of the first support becomes `new_s1 = s1 + r`.
            *   The new difference becomes `new_diff = (s1 + r) - s2 = diff + r`.
            *   We update `dp_next[new_diff]` to be the maximum of its current value (if any) and `new_s1`. `dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_s1)`.
        *   **Option 2: Add rod `r` to the second support (`s2`).**
            *   The sum of the first support `s1` remains unchanged (`new_s1 = s1`).
            *   The sum of the second support increases by `r`.
            *   The new difference becomes `new_diff = s1 - (s2 + r) = diff - r`.
            *   We update `dp_next[new_diff]` to be the maximum of its current value (if any) and `new_s1`. `dp_next[new_diff] = max(dp_next.get(new_diff, 0), new_s1)`.
        *   **Option 3: Do not use rod `r`.** This case is implicitly handled because `dp_next` starts as a copy of `dp`, so all previous states are carried forward.
    *   After considering all existing `(diff, s1)` pairs for the current rod `r`, we replace `dp` with `dp_next` to prepare for the next rod.

3.  **Result:** After iterating through all the rods, the final `dp` table contains the maximum possible `s1` for every achievable difference `diff`. We are interested in the case where the two supports have equal height, meaning the difference `diff` is 0. Therefore, the answer is the value stored in `dp[0]`. If `dp[0]` does not exist (meaning a difference of 0 was never achieved with a positive height), we return 0.

## Complexity Analysis

*   **Time Complexity:** `O(N * S)`, where `N` is the number of rods and `S` is the sum of all rod lengths. In each iteration (for `N` rods), we iterate through the current `dp` dictionary. The maximum possible difference is `S`, and the minimum is `-S`. In the worst case, the size of the `dp` dictionary can be proportional to `S`. Thus, the complexity is `O(N * S)`. Given the constraints `N <= 20` and `sum(rods) <= 5000`, this is efficient (approx. 20 * 5000 = 100,000 operations per rod update).
*   **Space Complexity:** `O(S)`, as the `dp` dictionary stores entries for differences ranging potentially from `-S` to `S`. The maximum number of keys is roughly `2*S + 1`.

**Note on Superior Approach:** While this linear DP approach works, a **Meet-in-the-Middle** strategy is significantly faster for the given constraints (N=20). It involves splitting the rods, running a DP variant (like the optimized `dp[abs_diff]=shorter_height` one) on each half, and then combining the results. This changes the complexity to roughly `O(N * 3^(N/2))`, which is much better.
*   Pattern: [[../patterns/divide_and_conquer/meet_in_the_middle.md]]
*   Optimization Comparison: [[../optimizations/partitioning/mitm_vs_linear_dp_max_equal_sum.md]]
*   Combination Technique Example: [[../techniques/divide_and_conquer/mitm_combine_diff_value_maps.md]]

## Knowledge Base Links

*   Core Concept: [[../algorithms/dynamic_programming/dynamic_programming.md]]
*   Data Structure Used: [[../data_structures/hash_table_dict.md]] (Implicitly, for the DP state)
*   Specific Technique: [[../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]]

**(Optimization Note):** An alternative DP state formulation (`dp[abs_diff] = max_shorter_height`) exists which reduces the state space and typically performs about twice as fast. See [[../optimizations/dynamic_programming/dp_state_comparison_equal_partition_sums.md]] for details. 