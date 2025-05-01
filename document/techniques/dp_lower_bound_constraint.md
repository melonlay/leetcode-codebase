# Technique: Enforcing Lower Bounds in DP Transitions

## Description

In some dynamic programming problems, the state value (or an intermediate calculation) must adhere to a strict lower bound (e.g., must be positive, non-negative, or greater than/equal to some threshold `B`).

A common way to enforce this during the DP transition is to use the `max()` function.

## Implementation Pattern

If a calculated intermediate value or the final DP state `dp[i]` must be at least `B`, the pattern is:

```python
# Example calculation leading to potential_value
potential_value = dp[i-1] + cost[i] # Or some other transition logic

# Enforce the lower bound B
dp[i] = max(B, potential_value)
```

## Use Cases & Examples

*   **Minimum Positive Value:** Ensuring a value remains strictly positive (lower bound `B = 1`).
    *   **Example:** LeetCode 174: Dungeon Game. The knight's health must always be `> 0`. When calculating the minimum health required *entering* a cell `dp[i][j]`, the transition involves `min_required_after - dungeon[i][j]`. To ensure the entering health is at least 1:
      `dp[i][j] = max(1, min_required_after - dungeon[i][j])`
*   **Minimum Non-Negative Value:** Ensuring a count, cost, or value remains non-negative (lower bound `B = 0`).
    *   **Example:** Problems involving counts or non-negative costs where a transition might mathematically result in a negative value that is conceptually invalid (e.g., taking more items than available might lead to a negative calculation that should be floored at 0).
      `dp[i] = max(0, dp[i-k] - cost)`

## Related Concepts

*   **Dynamic Programming:** This is a technique applied within DP transitions. See `../algorithms/dynamic_programming/dynamic_programming.md`.
*   **Problem Constraints:** This technique directly arises from specific problem constraints requiring minimum values. 