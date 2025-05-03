# Technique: 2D Dependency Reduction to LIS

## Description

Some problems, particularly in dynamic programming, involve finding an optimal subset or sequence from 2D data points `(x, y)` where the selection of a point `(x_i, y_i)` depends on previously selected points satisfying constraints in *both* dimensions (e.g., needing both `x_j < x_i` and `y_j < y_i`).

A common technique to solve these efficiently is to reduce the 2D dependency problem to a 1D Longest Increasing Subsequence (LIS) problem.

## Core Idea

1.  **Sort by One Dimension:** Sort the 2D data points primarily based on one dimension, say `x`. If `x` values are equal, use the *other* dimension `y` as a tie-breaker (the tie-breaking order might be crucial - often descending `y` for ascending `x`, or vice-versa, depending on the exact LIS variant needed).
    *   Example: Sort points `(x, y)` such that if `p_i = (x_i, y_i)` and `p_j = (x_j, y_j)`, then `i < j` implies `x_i <= x_j`. If `x_i == x_j`, then `y_i > y_j` (for a standard increasing subsequence on `y`).

2.  **Extract Second Dimension:** Create a new 1D sequence containing only the values of the *second* dimension (`y`) from the sorted points.

3.  **Solve LIS on Second Dimension:** Apply a standard LIS algorithm (either the O(n log n) Patience Sorting/Binary Search method or the O(n^2) DP method) on this 1D sequence of `y` values.

## Why it Works

By sorting primarily based on the first dimension (`x`), we ensure that when we process the `y` values in the resulting 1D sequence, any element `y_j` appearing *before* `y_i` in this sequence corresponds to an original point `(x_j, y_j)` where `x_j <= x_i`.

The LIS algorithm applied to the `y` sequence then finds the longest subsequence where `y_j < y_i` (for standard LIS). Combining these conditions:

*   Sorting guarantees `x_j <= x_i`.
*   LIS guarantees `y_j < y_i`.

This effectively finds the longest chain of points where both dimensions are increasing (or satisfy the required relationship). The careful sorting (especially the tie-breaker on `y` when `x` values are equal) ensures that points with the same `x` coordinate but larger `y` values don't incorrectly extend a subsequence based only on the `x` order. For example, if we sort ascending `x` then descending `y`, and run LIS on `y`, we prevent picking `(3, 5)` then `(3, 4)` because `5` would come before `4` in the y-sequence, and LIS requires `y_j < y_i`.

## Applications

*   **Russian Doll Envelopes (LeetCode 354):** Find the maximum number of envelopes that can be nested inside each other (`w_j < w_i`, `h_j < h_i`). Sort by width `w` (ascending), then height `h` (descending). Find LIS on the heights `h`.
*   **Maximum Height by Stacking Cuboids (LeetCode 1691):** Similar principle after normalizing cuboid dimensions and sorting.
*   Certain variants of maximum point subset problems on a 2D plane.

## Complexity

*   **Sorting:** O(n log n), where `n` is the number of points.
*   **LIS:** O(n log n) using the efficient algorithm.
*   **Overall:** O(n log n).

## Implementation Notes

*   The sorting order (primary key, secondary key, ascending/descending) is critical and depends on the specific problem constraints (e.g., `<` vs `<=`, increasing vs. non-decreasing).
*   Choose the appropriate LIS algorithm (O(n log n) is usually preferred).

## Related Concepts

*   [Algorithm: Longest Increasing Subsequence (LIS)](../../algorithms/dynamic_programming/longest_increasing_subsequence.md) (*Assumed link*)
*   Sorting Algorithms
*   Dynamic Programming 