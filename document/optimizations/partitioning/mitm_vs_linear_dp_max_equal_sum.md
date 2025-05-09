# Optimization: Meet-in-the-Middle vs. Linear DP for Maximizing Equal Partition Sum

## Context

This document compares the Meet-in-the-Middle (MitM) approach against linear Dynamic Programming (DP) approaches for solving problems where the goal is to partition a set of N items into two disjoint subsets with equal sums, maximizing that common sum (e.g., LeetCode 956 - Tallest Billboard).

## Approach 1: Linear Dynamic Programming

*   **Method:** Process items one by one, maintaining a DP state mapping differences to values.
*   **State Options:**
    *   `dp[signed_diff] = max_taller_height`: [[../../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]]
    *   `dp[abs_diff] = max_shorter_height`: (Optimized state) [[../../optimizations/dynamic_programming/dp_state_comparison_equal_partition_sums.md]]
*   **Complexity (using optimized state):**
    *   Time: O(N * S) or potentially O(N * 3^N) depending on analysis (S = max sum, potentially limiting state space).
    *   Space: O(S) or O(3^N).
*   **Pros:** Conceptually simpler linear flow.
*   **Cons:** Can be too slow if N is moderately large (e.g., N=20) and S is large or the number of reachable states approaches 3^N.

## Approach 2: Meet-in-the-Middle (MitM)

*   **Method:**
    1.  Split items into two halves (size N/2).
    2.  Generate `(abs_diff, max_shorter_height)` maps (`d1`, `d2`) for each half using the optimized DP state logic.
    3.  Combine `d1` and `d2` by finding matching `abs_diff` keys (`k`) and calculating the max combined height `max(v1 + d2[k] + k)`. See [[../../techniques/divide_and_conquer/mitm_combine_diff_value_maps.md]].
*   **Pattern:** [[../../patterns/divide_and_conquer/meet_in_the_middle.md]]
*   **Complexity:**
    *   Generation: O(N/2 * 3^(N/2))
    *   Combination: O(3^(N/2))
    *   Overall Time: **O(N * 3^(N/2))** (Simplified)
    *   Overall Space: O(3^(N/2))
*   **Pros:** Exponentially faster than linear DP for moderate N (e.g., N > ~15). Complexity is independent of the sum S.
*   **Cons:** More complex implementation involving splitting, generation for both halves, and a specific combination step.

## Performance Comparison (Example: N=20)

*   **Linear DP (O(N*S)):** Can be up to ~ `20 * 5000 = 100k` inner loop ops per item, total `~2M` ops. If analyzed as `O(N * 3^N)`, it's `20 * 3^20` (infeasible).
*   **MitM (O(N * 3^(N/2))):** Roughly `10 * 3^10` (~600k ops). This is significantly faster than the potential `O(N*S)` upper bound and vastly faster than `O(N * 3^N)`.

## Recommendation

For the problem of maximizing the equal sum of two disjoint partitions:
*   If N is small (e.g., N <= 15), the simpler linear DP (using the optimized state `dp[abs_diff] = max_shorter_height`) might be sufficient and easier to implement.
*   If N is moderate (e.g., 15 < N <= 40), the **Meet-in-the-Middle approach is significantly faster** and generally required to pass time limits. 