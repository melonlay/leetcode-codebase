# Solution for LeetCode 174: Dungeon Game

## Problem Summary

The goal is to find the minimum initial health a knight needs to travel from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)` of a 2D grid (`dungeon`). The knight can only move right or down. Each cell contains an integer representing health gain (positive) or loss (negative/zero). The knight's health must always be strictly greater than 0.

## Algorithmic Approach: Backward Dynamic Programming

A standard forward DP approach is difficult because knowing the minimum health to *reach* a cell isn't enough; we need to ensure survival *after* that cell. Therefore, a backward DP approach is more suitable.

We define `dp[i][j]` as the **minimum health the knight must have upon *entering* cell `(i, j)`** to guarantee survival and reach the princess at `(m-1, n-1)`.

### State Definition

*   `dp[i][j]`: Minimum health required when the knight is at cell `(i, j)`, just about to enter it.

### DP Table Initialization

We use a DP table `dp` of size `(m+1) x (n+1)`. The extra row and column act as sentinels to simplify boundary conditions.

*   **Base Case (Target):** To survive the journey *after* leaving the princess's cell `(m-1, n-1)`, the knight needs at least 1 health point. We initialize the virtual cells adjacent to the target to reflect this: `dp[m][n-1] = 1` and `dp[m-1][n] = 1`.
*   **Other Cells:** Initialize with `infinity`.

### Recurrence Relation (Transitions)

We fill the DP table iterating backward from `i = m-1` down to `0` and `j = n-1` down to `0`.

For cell `(i, j)`:

1.  **Minimum Health Needed *After Leaving* `(i, j)`:** The knight will move either down to `(i+1, j)` or right to `(i, j+1)`. To guarantee survival, they must have enough health for the *easier* of the two subsequent paths. So, the minimum health required *after* the effect of `dungeon[i][j]` is `min(dp[i+1][j], dp[i][j+1])`.

2.  **Minimum Health Needed *Before Effect* of `dungeon[i][j]`:** Let `min_health_needed_after = min(dp[i+1][j], dp[i][j+1])`. To have `min_health_needed_after` health *after* the current cell `(i, j)` applies its effect `dungeon[i][j]`, the health needed *before* the effect (i.e., upon entering the cell) is `min_health_needed_after - dungeon[i][j]`.

3.  **Ensuring Health > 0:** The knight's health must always be at least 1. If the calculated `health_needed_before_effect` is 0 or less, it means the knight gains enough health from this point onwards (or the current cell provides health) such that only 1 health point is necessary upon entering cell `(i, j)`. Therefore, the actual minimum health needed upon entering is:
    `dp[i][j] = max(1, min_health_needed_after - dungeon[i][j])`

### Final Answer

The minimum initial health required at the start `(0, 0)` is given by `dp[0][0]`.

## Knowledge Base References

*   The core technique is **Dynamic Programming**, specifically a **Bottom-Up (Tabulation)** approach applied **backward** from the target state. See `document/algorithms/dynamic_programming/dynamic_programming.md` for general DP principles.
*   This problem involves DP on a grid, calculating minimum values based on adjacent cells, which is a common DP pattern.
*   The state definition `dp[i][j]` representing the minimum requirement *entering* a cell from a future state is a key aspect of backward DP.

## Complexity Analysis

*   **Time Complexity:** O(m * n), where `m` is the number of rows and `n` is the number of columns. We visit each cell of the DP table once.
*   **Space Complexity:** O(m * n) for the DP table. (This could be optimized to O(n) or O(min(m,n)) by only storing the current and next row/column, but the O(m*n) solution is clearer). 