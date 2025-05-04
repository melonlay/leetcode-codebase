# LeetCode 296: Best Meeting Point - Solution Explanation

## Problem Summary

Given an `m x n` binary grid where `1` represents a house and `0` represents empty land, find a meeting point `(p_r, p_c)` such that the sum of Manhattan distances from all houses to the meeting point is minimized. Return the minimum total distance.

Manhattan Distance: `distance(p1, p2) = |p1.row - p2.row| + |p1.col - p2.col|`

## Algorithmic Approach: Median Property + Dimension Decoupling

This problem leverages two key mathematical insights:

1.  **Manhattan Distance Decoupling:** The total Manhattan distance can be separated into independent row and column components:
    `Sum(|r_i - p_r| + |c_i - p_c|) = Sum(|r_i - p_r|) + Sum(|c_i - p_c|)`.
    Minimizing the total distance is equivalent to minimizing the sum of row distances and the sum of column distances independently.
    *   **Reference:** `[[../document/mathematical_concepts/geometry/manhattan_distance_optimization.md]]`

2.  **Median Minimizes L1 Norm:** In 1D, the point `m` that minimizes the sum of absolute differences `Sum(|x_i - m|)` is the median of the points `x_i`.
    *   **Reference:** `[[../document/mathematical_concepts/statistics/median_l1_norm_minimization.md]]`

Therefore, the optimal meeting point `(p_r, p_c)` has `p_r` as the median of all house row coordinates and `p_c` as the median of all house column coordinates.

## Logic Explanation

1.  **Collect Coordinates:** Iterate through the `grid`. Collect all row coordinates `r` where `grid[r][c] == 1` into a list `rows`. Collect all corresponding column coordinates `c` into a list `cols`.
    *   The `rows` list will naturally be sorted because we iterate through the grid row by row.
    *   The `cols` list will *not* necessarily be sorted.
2.  **Sort Column Coordinates:** Sort the `cols` list: `cols.sort()`.
3.  **Calculate Minimum Row Distance:** Use the efficient two-pointer pairing method on the sorted `rows` list to calculate `Sum(|r_i - median(rows)|)`. This method calculates the minimum sum directly without needing the median value itself.
    *   Reference: See calculation technique in `[[../document/mathematical_concepts/statistics/median_l1_norm_minimization.md]]`.
    *   Call helper `_calculate_min_distance_1d(rows)`.
4.  **Calculate Minimum Column Distance:** Apply the same two-pointer pairing method to the now-sorted `cols` list to calculate `Sum(|c_i - median(cols)|)`.
    *   Call helper `_calculate_min_distance_1d(cols)`.
5.  **Total Minimum Distance:** Return the sum of the minimum row distance and minimum column distance.

## `_calculate_min_distance_1d` Helper

This helper function takes a *sorted* list of 1D coordinates.
1.  Initialize `total_distance = 0`.
2.  Use two pointers `low = 0`, `high = len(coords) - 1`.
3.  While `low < high`:
    *   Add the difference between the outermost points: `total_distance += coords[high] - coords[low]`.
    *   Move pointers inward: `low += 1`, `high -= 1`.
4.  Return `total_distance`.

## Knowledge Base References

*   **Core Math Concept:** [[../document/mathematical_concepts/statistics/median_l1_norm_minimization.md]] (Explains why median minimizes L1 distance and the efficient calculation method).
*   **Manhattan Distance Property:** [[../document/mathematical_concepts/geometry/manhattan_distance_optimization.md]] (Explains dimension decoupling).
*   **Calculation Technique:** [[../document/patterns/two_pointers.md]] (General pattern applied in `_calculate_min_distance_1d`).

## Complexity Analysis

Let `R` be the number of rows, `C` be the number of columns, and `H` be the number of houses.

*   **Time Complexity:** O(R * C + H log H).
    *   O(R * C) to iterate through the grid and collect coordinates.
    *   O(H log H) to sort the column coordinates.
    *   O(H) to calculate the 1D distances using the two-pointer method.
*   **Space Complexity:** O(H) to store the row and column coordinate lists.

``` 