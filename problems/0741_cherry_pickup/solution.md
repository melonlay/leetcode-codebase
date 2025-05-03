# Solution Explanation: 741. Cherry Pickup

## Problem Summary

Given an `n x n` grid containing empty cells (0), cherries (1), or thorns (-1), find the maximum number of cherries collectable by:
1.  Traveling from `(0, 0)` to `(n-1, n-1)` moving only right or down.
2.  Traveling back from `(n-1, n-1)` to `(0, 0)` moving only left or up.

Picked cherries turn into empty cells (0). Thorns block paths.

## Approach: Dynamic Programming (Dual Paths)

The core idea is to reframe the problem from a single path going down-right and then up-left into **two paths starting simultaneously from `(0, 0)` and moving towards `(n-1, n-1)` using only down and right moves.**

Why this works:
*   A path from `(0, 0)` to `(n-1, n-1)` (down/right) and back (up/left) covers the same set of cells as two independent paths from `(0, 0)` to `(n-1, n-1)` (down/right), assuming the paths can overlap.
*   The constraint that a picked cherry becomes 0 is naturally handled: if both paths land on the same cherry cell `(r, c)` at the same time, they collect it only once.

**State:**
We use dynamic programming. A naive state `dp[r1][c1][r2][c2]` (max cherries with path 1 at `(r1, c1)` and path 2 at `(r2, c2)`) would be O(n^4), which is feasible but can be optimized.

Notice that both paths take the same number of steps `t` to reach their respective positions: `t = r1 + c1 = r2 + c2`.
We can optimize the state to depend on the number of steps `t` and the row positions `r1` and `r2`. The columns `c1 = t - r1` and `c2 = t - r2` can be derived.

*   `dp[t][r1][r2]`: Maximum cherries collected after `t` steps, with path 1 at row `r1` (column `t-r1`) and path 2 at row `r2` (column `t-r2`). This leads to O(n^3) time and space.

**Space Optimization:**
To calculate the state for step `t`, we only need the results from step `t-1`. We can reduce the space complexity to O(n^2) by using only two 2D DP tables (one for the previous step `t-1`, one for the current step `t`) or by updating a single 2D DP table in place carefully (often easier to implement with a `new_dp` table copied after each step `t`).

Let `dp[r1][r2]` represent the maximum cherries collected when path 1 is at row `r1` and path 2 is at row `r2` *after the previous step `t-1`*. We calculate `new_dp[r1][r2]` for the current step `t` based on the values in `dp`.

**Transitions:**
For each step `t` from 1 to `2n-2` (total steps required to reach `(n-1, n-1)`), we calculate `new_dp[r1][r2]` for all valid pairs `(r1, r2)`:

1.  Calculate `c1 = t - r1` and `c2 = t - r2`.
2.  Check validity: `0 <= r1, c1, r2, c2 < n` and `grid[r1][c1] != -1` and `grid[r2][c2] != -1`.
3.  Determine cherries gained at this step: `cherries = grid[r1][c1]` (if `r1 == r2` and `c1 == c2`) or `cherries = grid[r1][c1] + grid[r2][c2]` (if paths are on different cells).
4.  Find the maximum cherries from the previous step (`t-1`) by considering the four possible previous states that could lead to the current `(r1, c1)` and `(r2, c2)`:
    *   Path 1 came from `(r1-1, c1)`, Path 2 came from `(r2-1, c2)` -> Check `dp[r1-1][r2-1]`
    *   Path 1 came from `(r1-1, c1)`, Path 2 came from `(r2, c2-1)` -> Check `dp[r1-1][r2]`
    *   Path 1 came from `(r1, c1-1)`, Path 2 came from `(r2-1, c2)` -> Check `dp[r1][r2-1]`
    *   Path 1 came from `(r1, c1-1)`, Path 2 came from `(r2, c2-1)` -> Check `dp[r1][r2]`
5.  Let `max_prev_cherries` be the maximum value among the valid previous states (`!= -1`).
6.  If `max_prev_cherries != -1`, update `new_dp[r1][r2] = max_prev_cherries + cherries`.
7.  After iterating through all `r1, r2`, set `dp = new_dp` for the next step.

**Base Case:**
*   Initialize `dp` table with `-1` (representing unreachable states).
*   `dp[0][0] = grid[0][0]` for the state before step `t=1`.

**Result:**
*   The final answer is `dp[n-1][n-1]` after completing `t = 2n-2` steps.
*   If `dp[n-1][n-1]` is still `-1`, it means the end is unreachable, so return 0.

## Complexity Analysis

*   **Time Complexity:** O(n^3)
    *   We iterate through `t` from 1 to `2n-2` (O(n) steps).
    *   Inside each step, we iterate through `r1` from 0 to `n-1` (O(n)) and `r2` from 0 to `n-1` (O(n)).
    *   The transitions inside the loops take O(1) time.
    *   Total time = O(n * n * n) = O(n^3).
*   **Space Complexity:** O(n^2)
    *   We use a 2D DP table of size `n x n` to store the results for the current/previous step.

## Knowledge Base Connection

This solution uses the **Dynamic Programming** paradigm. The core idea involves transforming the round trip into two simultaneous paths, a specific pattern now documented in the Knowledge Base:
*   **Pattern:** [[../patterns/matrix/dual_path_grid_dp.md]]

The general principles of DP state definition, transitions, base cases, and space optimization are outlined in:
*   **Algorithm:** [[../algorithms/dynamic_programming/dynamic_programming.md]]

The transformation of the problem into two simultaneous paths is a key insight specific to this problem type. 