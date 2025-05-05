# Pattern: Dynamic Programming for 2xN Grid Tiling

## Problem Class

This pattern applies to problems asking for the number of ways to completely tile a `2 x N` rectangular grid using a given set of tile shapes (e.g., dominoes, trominoes, custom shapes). The tiles can often be rotated. The goal is typically to find the total count of valid tilings, often modulo a large number.

**Example Problems:**
*   LeetCode 790: Domino and Tromino Tiling
*   LeetCode 1185: Day of the Week (Conceptually similar state transitions, though simpler)
*   Problems involving tiling with 1x1 and 2x2 squares, etc.

## Approach: Dynamic Programming

These problems exhibit optimal substructure and overlapping subproblems, making dynamic programming a suitable approach. We build the solution for a `2 x n` grid based on solutions for smaller grid widths.

### State Definition & Recurrence Derivation Technique

The core idea is to define DP states based on the configuration of the boundary after column `i`.
A common and powerful technique involves defining states for fully covered columns and partially covered columns:

*   `f[i]` = Number of ways to **fully tile** the `2 x i` grid.
*   `g[i]` = (Optional, depends on tiles) Number of ways to tile the `2 x i` grid such that the **top cell** `(i, 0)` is uncovered, but all other cells up to column `i` are covered.
*   `h[i]` = (Optional, depends on tiles) Number of ways to tile the `2 x i` grid such that the **bottom cell** `(i, 1)` is uncovered, but all other cells up to column `i` are covered.

By symmetry, if both `g` and `h` states are needed, often `g[i] = h[i]`.

**Transitions:**
The crucial step is to derive the transition equations based on the **specific allowed tile shapes**. For each state (e.g., `f[i]`, `g[i]`), consider all possible ways the last tile(s) could be placed to achieve that state, based on the valid states of the preceding columns (`i-1`, `i-2`, etc.).

*   **Example Transition Logic (Conceptual):**
    *   To get `f[i]`: How can tiles cover columns `i` (and potentially `i-1`) ending in a fully covered column `i`? This might involve placing tiles vertically in column `i` (from state `f[i-1]`), placing tiles horizontally across `i-1` and `i` (from state `f[i-2]`), or placing specific tiles that fill gaps from partially covered states (`g[i-1]`, `h[i-1]`).
    *   To get `g[i]`: How can tiles cover columns up to `i` leaving only `(i, 0)` uncovered? This depends on placing tiles that end in this specific configuration.

**Goal:** The ultimate goal is usually to find a recurrence relation for `f[i]`. Sometimes this involves solving a system of recurrences for `f`, `g`, and `h` and then simplifying, or directly deriving the recurrence for `f[i]` if possible.

### Base Cases

Define base cases for the smallest grid sizes (e.g., `n=0`, `n=1`, `n=2`) needed to start the recurrence. `dp[0]` often represents the single way to tile an empty grid (1).

### Complexity

*   **Time:** Typically O(N), as the recurrence usually depends on a constant number of previous states.
*   **Space:** O(N) if storing the full DP table. Often reducible to O(1) using the fixed-window space optimization technique if the recurrence only depends on states `i-1` to `i-k` for a constant `k`.

## Example Application (LC 790: Domino & Tromino Tiling)

*   **Tiles:** 2x1 dominoes, L-shaped trominoes.
*   **States:** Using the `f`, `g`, `h` state derivation leads to the coupled system:
    *   `f[i] = f[i-1] + f[i-2] + g[i-1] + h[i-1]`
    *   `g[i] = f[i-1] + h[i-1]`
    *   `h[i] = f[i-1] + g[i-1]`
*   **Simplified Recurrence for `f[i]` (let `dp[i]=f[i]`):**
    \[ dp[i] = 2 \cdot dp[i-1] + dp[i-3] \]
*   **Base Cases:** `dp[0]=1`, `dp[1]=1`, `dp[2]=2`.

## Implementation Notes

*   Always carefully consider the exact tile placements allowed when deriving transitions.
*   Apply modulo arithmetic if the counts can be large.
*   Consider space optimization techniques.

## Related Concepts

*   **Algorithm:** [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   **Technique (Space Optimization):** [[../../techniques/dynamic_programming/fixed_window_dp_space_optimization.md]] 