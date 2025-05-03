# Pattern: Dual Path Grid DP

## Description

This pattern applies to grid/matrix problems where the objective involves finding an optimal path (or value) related to either:
1.  A single agent making a round trip (e.g., top-left to bottom-right and back).
2.  Two agents moving simultaneously through the grid, often starting at the same point and potentially interacting (e.g., collecting items).

The core idea is to transform the problem into one involving two simultaneous paths moving in the *same* direction (e.g., both from top-left to bottom-right) using only a restricted set of moves (typically right and down).

## Core Idea

Instead of tracking a complex round trip or two paths moving in potentially opposite directions, model two paths (Path 1 and Path 2) starting together at `(0, 0)` and both moving towards `(n-1, n-1)` using only down/right moves.

**Synchronization:** Both paths take the same number of steps `t`. If Path 1 is at `(r1, c1)` and Path 2 is at `(r2, c2)`, then `t = r1 + c1 = r2 + c2`.

**Interaction:** If the paths land on the same cell `(r, c)` at the same step `t`, any resource collection or state change at that cell usually happens only once.

## Dynamic Programming Approaches

Two main DP implementation strategies exist:

### 1. Bottom-Up (Tabulation)

*   **State:** Typically uses a 2D array `dp[r1][r2]` representing the maximum value after the *previous* step (`t-1`).
*   **Iteration:** Iterates through steps `t` from 1 to `max_steps` (e.g., `2n-2`). In each step, calculates a `new_dp[r1][r2]` for the current step `t` based on values in the `dp` table from step `t-1`.
*   **Transitions:** Check the 4 possible combinations of previous moves for Path 1 and Path 2 that could lead to the current `(r1, c1)` and `(r2, c2)`, looking up the corresponding states in the `dp` table (e.g., `dp[r1-1][r2-1]`, `dp[r1-1][r2]`, etc.).
*   **Complexity:**
    *   Time: O(N^3)
    *   Space: O(N^2) (when optimized to only store the current and previous step's states).

```python
# Conceptual Structure (Bottom-Up)
dp = [[-1] * n for _ in range(n)]
dp[0][0] = grid[0][0]
for t in range(1, max_steps + 1):
    new_dp = [[-1] * n for _ in range(n)]
    for r1 in range(n):
        for r2 in range(n):
            c1, c2 = t - r1, t - r2
            if is_invalid(grid, r1, c1, r2, c2):
                continue
            cherries = calculate_cherries(grid, r1, c1, r2, c2)
            max_prev = get_max_prev(dp, r1, r2) # Check 4 prev states in dp
            if max_prev != -1:
                new_dp[r1][r2] = max_prev + cherries
    dp = new_dp
result = max(0, dp[n-1][n-1])
```

### 2. Top-Down (Memoized Recursion)

*   **State:** Uses a recursive function. The state typically includes the number of steps `k` and the row indices `r1`, `r2` (e.g., `dfs(k, r1, r2)`), from which column indices `c1=k-r1`, `c2=k-r2` are derived. Alternatively, the state can use the coordinates of one path and the row index of the other (e.g., `dp(r1, c1, r2)`), deriving `c2 = r1 + c1 - r2`.
*   **Memoization:** Uses a cache (e.g., Python's `@functools.cache` or `@cache`, or a dictionary) to store results.
*   **Transitions:** The function calculates the result for the current state by recursively calling itself for the previous step (`k-1`) or by exploring the results of the next possible combined moves (DD, DR, RD, RR).
*   **Base Cases:** Define base cases for the start (`k=0` or `r1=c1=r2=c2=0`), destination, and invalid states (out of bounds, thorns).
*   **Optimization (Symmetry):** A crucial optimization is leveraging path symmetry. Since the two paths are often interchangeable, enforce a convention (e.g., `r1 <= r2`) in the state definition or add a check `if r1 > r2: return dp(...)` with swapped arguments or return an impossible value. This effectively prunes ~half the state space.
*   **Complexity:**
    *   Time: O(N^3)
    *   Space: O(N^3) (due to the memoization cache potentially storing all reachable states).

```python
# Conceptual Structure (Top-Down using k, r1, r2)
@cache # or @functools.cache
def dfs(k, r1, r2):
    # Optimization: if r1 > r2: return -inf # Pruning based on convention
    c1, c2 = k - r1, k - r2
    # ... Base cases for k=0, invalid indices, thorns ...

    prev = max(dfs(k-1, r1, r2), # RR
               dfs(k-1, r1-1, r2), # DR
               dfs(k-1, r1, r2-1), # RD
               dfs(k-1, r1-1, r2-1)) # DD

    # ... Calculate current cherries and return prev + cherries ...

# Conceptual Structure (Top-Down using i1, j1, i2)
@cache
def dp(i1, j1, i2):
    j2 = i1 + j1 - i2
    # Optimization: if i1 > i2: return dp(i2, j2, i1) # Canonicalize state
    # ... Base cases for destination, invalid indices, thorns ...

    # Explore next steps
    dd = dp(i1+1, j1, i2+1)
    dr = dp(i1+1, j1, i2)
    rd = dp(i1, j1+1, i2+1)
    rr = dp(i1, j1+1, i2)
    best = max(dd, dr, rd, rr)

    # ... Calculate current cherries and return best + cherries ...
```

## Comparison and Considerations

*   **Space:** Bottom-up (tabulation) with space optimization achieves better theoretical space complexity (O(N^2)) than top-down (memoization) (O(N^3)).
*   **Practical Speed:** Top-down (memoization) can sometimes be faster in practice, especially if:
    *   The state space is sparse (many states are unreachable due to obstacles).
    *   Optimizations like symmetry pruning (`r1 > r2`) are easily implemented.
    *   The memoization mechanism (like `@functools.cache`) is highly optimized.
*   **Implementation:** Top-down might feel more natural for some, directly mapping from the recursive relation. Bottom-up requires careful ordering of loops.

## Use Cases

*   Grid traversal problems involving a round trip where the return path depends on the state left by the first path (e.g., collecting items).
*   Problems involving two agents moving simultaneously on a grid.

## Example Application

*   LeetCode 741 - Cherry Pickup: [[../../../problems/0741_cherry_pickup/solution.md]]

## Related Concepts

*   [[../algorithms/dynamic_programming/dynamic_programming.md]] 