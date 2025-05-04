# LeetCode 363: Max Sum of Rectangle No Larger Than K - Solution Explanation

## Problem Summary

Given an `m x n` matrix `matrix` and an integer `k`, find the maximum sum of a rectangle in the matrix such that its sum is no larger than `k`. It is guaranteed that such a rectangle exists.

## Algorithmic Approach: 2D to 1D Reduction + Max Subarray Sum <= k

The problem asks for the maximum sum of a submatrix (rectangle) under a constraint `k`. A naive approach checking all possible rectangles would be too slow (O(M^2 * N^2) for sum calculation, or O(M^2 * N^2 * M*N) without prefix sums).

The solution uses two main ideas:

1.  **Dimension Reduction:** Reduce the 2D problem to multiple 1D problems by iterating through all possible pairs of boundary columns (or rows) and calculating the sum of elements within those boundaries for each row (or column). See [[../document/patterns/matrix/dimension_reduction_matrix_to_1d.md]].
2.  **Max Subarray Sum <= k (1D):** For each generated 1D array (representing sums across rows for fixed columns, or vice-versa), find the maximum sum of any contiguous subarray whose sum is less than or equal to `k`. This subproblem is solved using prefix sums and binary search. See [[../document/techniques/sequence/prefix_sum_difference_constraint.md]].

## Logic Explanation

1.  **Dimension Optimization:** Determine the smaller dimension (`N`) and larger dimension (`M`) between rows and columns. The algorithm iterates O(N^2) times over the smaller dimension for better performance.
2.  **Outer Loops (Dimension N):** Iterate through all possible start (`i`) and end (`j`) boundaries along the smaller dimension (`N`).
3.  **Calculate 1D Array (`sums_in_m`):** For each `(i, j)` pair, calculate a 1D array `sums_in_m` of size `M`. `sums_in_m[idx]` stores the sum of elements in `matrix` along the dimension `M` at index `idx`, accumulated over the range `[i, j]` of dimension `N`. This is done efficiently by adding the contribution of the `j`-th column/row to the sums calculated for the `(i, j-1)` range.
4.  **Solve 1D Subproblem:** Call a helper function `_find_max_subarray_sum_le_k(sums_in_m, k)` on the generated 1D array.
5.  **`_find_max_subarray_sum_le_k` Logic:**
    *   Initialize `max_s = -inf`, `prefix_sum = 0`, `seen_sums = [0]` (sorted list of seen prefix sums).
    *   Iterate through the 1D array `arr` (which is `sums_in_m`):
        *   Update `prefix_sum += x`.
        *   We need `max(prefix_sum - prev_s)` such that `prefix_sum - prev_s <= k`.
        *   This requires finding the smallest `prev_s` in `seen_sums` such that `prev_s >= prefix_sum - k`.
        *   Use `idx = bisect.bisect_left(seen_sums, prefix_sum - k)` to find this `prev_s` (which is `seen_sums[idx]` if `idx < len(seen_sums)`).
        *   If found, update `max_s = max(max_s, prefix_sum - seen_sums[idx])`.
        *   Insert `prefix_sum` into the sorted list `seen_sums` using `bisect.insort(seen_sums, prefix_sum)`.
    *   Return `max_s`.
6.  **Update Overall Max:** Update the overall `max_sum` found across all 1D subproblems: `max_sum = max(max_sum, current_max_1d)`.
7.  **Early Exit:** If `max_sum == k`, return `k` immediately.
8.  **Return `max_sum`.**

## Knowledge Base References

*   **Overall Structure:** [[../document/patterns/matrix/dimension_reduction_matrix_to_1d.md]] (Explains reducing 2D matrix problems by iterating boundaries in one dimension).
*   **1D Subproblem Technique:** [[../document/techniques/sequence/prefix_sum_difference_constraint.md]] (Details finding max/min/count of subarray sums satisfying constraints using prefix sums and auxiliary structures like sorted lists or hash maps).
*   **Foundation:** [[../document/techniques/sequence/prefix_suffix_aggregates.md]] (Basic prefix sums).
*   **Implementation Detail:** [[../document/algorithms/searching/binary_search.md]] (Basis for `bisect` module). The technique document discusses complexity implications of using `bisect` vs. structures like `SortedList`.

## Complexity Analysis

Let `M = max(rows, cols)` and `N = min(rows, cols)`.
*   **Time Complexity:** O(N^2 * M^2) using `list + bisect.insort` for the 1D subproblem.
    *   Outer loops: O(N^2).
    *   Calculating `sums_in_m`: O(M) per iteration.
    *   `_find_max_subarray_sum_le_k`: O(M^2) because `bisect.insort` on a list is O(M).
    *   Total: O(N^2 * (M + M^2)) = O(N^2 * M^2).
    *   **(Optimized):** If `_find_max_subarray_sum_le_k` used a Balanced BST or `SortedList`, its complexity would be O(M log M), making the overall complexity O(N^2 * M log M).
*   **Space Complexity:** O(M) - Primarily for storing `sums_in_m` and `seen_sums` within the 1D subproblem solver. 