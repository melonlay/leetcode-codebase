# Solution for 790. Domino and Tromino Tiling

## Problem Summary

Given an integer `n`, find the number of ways to tile a `2 x n` board using two types of tiles:
1.  A 2x1 domino tile.
2.  An L-shaped tromino tile (which covers 3 squares).
The tiles can be rotated. Every square must be covered. Return the answer modulo `10^9 + 7`.

## Approach: Dynamic Programming

This problem has optimal substructure and overlapping subproblems, making it suitable for dynamic programming. We want to find the number of ways to tile a `2 x n` board based on the ways to tile smaller boards.

Let `dp[i]` be the number of ways to fully tile a `2 x i` board.

### Deriving the Recurrence

We can derive a recurrence relation by considering the state of the rightmost columns. A common approach involves defining multiple DP states representing fully tiled boards and partially tiled boards (e.g., with one cell uncovered in the last column).

Let:
*   `f[i]` = ways to fully tile `2 x i`.
*   `g[i]` = ways to tile `2 x i` with the top cell `(i, 0)` uncovered.
*   `h[i]` = ways to tile `2 x i` with the bottom cell `(i, 1)` uncovered.

By symmetry, `g[i] = h[i]`. The transitions are:
*   `f(i) = f(i-1) + f(i-2) + g(i-1) + h(i-1)`
*   `g(i) = f(i-1) + h(i-1)`
*   `h(i) = f(i-1) + g(i-1)`

Substituting `g=h`, we get:
*   `f(i) = f(i-1) + f(i-2) + 2*g(i-1)`
*   `g(i) = f(i-1) + g(i-1)`

Through algebraic manipulation or by observing the pattern for small `n`, these can be simplified into a single recurrence relation for the number of ways to fully tile the `2 x i` board (`dp[i] = f[i]`):

\[ dp[i] = 2 \cdot dp[i-1] + dp[i-3] \]

### Base Cases

We need the first few values to start the recurrence:
*   `dp[0] = 1` (One way to tile an empty board: do nothing)
*   `dp[1] = 1` (One vertical domino)
*   `dp[2] = 2` (Two vertical dominoes or two horizontal dominoes)

Using the recurrence:
*   `dp[3] = 2 * dp[2] + dp[0] = 2 * 2 + 1 = 5` (Matches example)

### Implementation Details

We can calculate `dp[n]` iteratively. Since `dp[i]` only depends on `dp[i-1]` and `dp[i-3]`, we only need to store the last three values to achieve O(1) space complexity.

We initialize variables representing `dp[i-1]`, `dp[i-2]`, and `dp[i-3]` based on the values for `n=0, 1, 2`, and iterate from `i = 3` up to `n`. In each step, we calculate the new `dp[i]` and update the three state variables. Remember to perform all additions modulo `10^9 + 7`.

## Complexity Analysis

*   **Time Complexity:** O(n) - We iterate from 3 to `n`, performing constant-time calculations in each step.
*   **Space Complexity:** O(1) - We only store a fixed number of variables (`dp_i_1`, `dp_i_2`, `dp_i_3`) regardless of `n`.

## Knowledge Base Connection

*   **Algorithm:** [[../algorithms/dynamic_programming/dynamic_programming.md]] - The solution uses the iterative (tabulation) dynamic programming approach with space optimization.
*   **Pattern:** [[../patterns/grid_tiling/2xn_tiling_dp.md]] - The problem fits the general 2xN tiling DP pattern.
*   **Technique:** [[../techniques/dynamic_programming/fixed_window_dp_space_optimization.md]] - The O(1) space implementation uses this technique.
*   The specific recurrence relation `dp[i] = 2*dp[i-1] + dp[i-3]` is derived from the pattern's state transition logic applied to dominoes and trominoes, as detailed in the pattern's example application section. 