# LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings - Solution Explanation

## Problem Summary

Given an m x n grid of characters and a pattern string, we need to count the number of cells `(r, c)` that belong to *both* a horizontal substring match and a vertical substring match of the pattern. The horizontal and vertical reads wrap row-wise and column-wise, respectively, but do not wrap around the entire grid boundary (bottom to top or last column to first).

## Algorithmic Approach: KMP + Difference Array

The core idea is to find all horizontal and vertical matches using the efficient Knuth-Morris-Pratt (KMP) algorithm and then determine which grid cells are covered by *both* types of matches. A naive approach of marking every cell for every match can lead to Time Limit Exceeded (TLE) if there are many overlapping matches (O(num_matches * L) complexity).

This optimized solution uses KMP combined with Difference Arrays (a sweep-line concept) to efficiently calculate cell coverage in O(m*n) time after finding the matches.

1.  **Flatten the Grid:** Convert the 2D grid into 1D strings using Row-Major and Column-Major orders as described in [[document/techniques/matrix/grid_flattening.md]].
    *   `text_h`: Row-Major flattened string.
    *   `text_v`: Column-Major flattened string.
2.  **KMP Preprocessing:** Compute the LPS array for the `pattern` using the method described in [[document/algorithms/string/kmp.md]].
3.  **KMP Search:**
    *   Run KMP search (see [[document/algorithms/string/kmp.md]]) on `text_h` to get `indices_h`.
    *   Run KMP search on `text_v` to get `indices_v`.
4.  **Calculate Horizontal Coverage (Difference Array):**
    *   Use the Difference Array technique [[document/techniques/sequence/difference_array.md]] on `indices_h` to calculate the `coverage_h` boolean array (size `m*n`), indicating which row-major indices are covered.
5.  **Calculate Vertical Coverage (Difference Array):**
    *   Similarly, use the Difference Array technique on `indices_v` to calculate the `coverage_v` boolean array, indicating which column-major indices are covered.
6.  **Count Overlaps:**
    *   Iterate through grid cells `(r, c)`.
    *   Convert `(r, c)` to both row-major `idx_h` and column-major `idx_v` using the formulas in [[document/techniques/matrix/grid_flattening.md]].
    *   If `coverage_h[idx_h]` is `True` AND `coverage_v[idx_v]` is `True`, increment the final count.
7.  **Return Counter:** The final count.

## Implementation Details

The solution uses helper functions for KMP. The main `countCells` function implements the flattening, KMP search, difference array calculations, and the final overlap counting, including the necessary index conversions.

## Knowledge Base References

*   **Core Algorithm:** [[document/algorithms/string/kmp.md]]
*   **Optimization Technique:** [[document/techniques/sequence/difference_array.md]]
*   **Matrix Handling:** [[document/techniques/matrix/grid_flattening.md]]
*   **Related Pattern:** [[document/patterns/matrix/dimension_reduction_matrix_to_1d.md]]

## Complexity Analysis

*   **Time Complexity:** O(m * n + L)
*   **Space Complexity:** O(m * n + L) 