# Technique: Fixed-Window DP Space Optimization

## Concept

This technique optimizes the space complexity of dynamic programming solutions where the calculation of the current state `dp[i]` only depends on a fixed number of immediately preceding states (e.g., `dp[i-1]`, `dp[i-2]`, ..., `dp[i-k]`, where `k` is a small constant).

Instead of storing the entire DP array (or matrix) of size O(N) (or larger), we only need to keep track of the last `k` states required for the next calculation. This reduces the space complexity from O(N) (or more) down to O(k), which is often O(1) if `k` is constant.

## How It Works

1.  **Identify Dependency Window:** Analyze the DP recurrence relation to determine the maximum 'lookback' required. For example, in `dp[i] = dp[i-1] + dp[i-2]`, the window size `k` is 2. In `dp[i] = 2*dp[i-1] + dp[i-3]`, the window size `k` is 3 (we need `i-1` and `i-3`).
2.  **Initialize Variables:** Create a fixed number of variables (usually `k`) to store the necessary base case values.
3.  **Iterate and Update:** Loop from the first state not covered by base cases up to the target state `n`.
    *   Calculate the `current_dp` value using the stored variables representing the previous states according to the recurrence.
    *   Update the variables by shifting the values: the variable for `dp[i-k]` is discarded, `dp[i-k+1]` takes its place, and so on, until `dp[i-1]` takes the place of `dp[i-2]`, and the newly calculated `current_dp` becomes the new `dp[i-1]`.
4.  **Result:** After the loop finishes, the variable representing the most recent state (`dp[n]`) holds the final answer.

## Example (LeetCode 790 - Domino/Tromino Tiling)

*   **Recurrence:** `dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD`
*   **Dependency Window:** Need `i-1` and `i-3`. `k=3`.
*   **Variables:** `dp_i_1` (stores `dp[i-1]`), `dp_i_2` (stores `dp[i-2]`), `dp_i_3` (stores `dp[i-3]`).
*   **Initialization (for i=3):** `dp_i_1 = dp[2]`, `dp_i_2 = dp[1]`, `dp_i_3 = dp[0]`.
*   **Iteration (i=3 to n):**
    ```python
    # Calculate dp[i]
    dp_curr = (2 * dp_i_1 + dp_i_3) % MOD
    # Update states for next iteration (i+1)
    dp_i_3 = dp_i_2 # Old dp[i-2] becomes new dp[i-3] for next step
    dp_i_2 = dp_i_1 # Old dp[i-1] becomes new dp[i-2] for next step
    dp_i_1 = dp_curr # Current dp[i] becomes new dp[i-1] for next step
    ```
*   **Result:** `dp_i_1` after the loop.

## Complexity

*   **Time:** Remains the same as the O(N) space DP, typically O(N).
*   **Space:** Reduced to O(k), which is O(1) if `k` is constant.

## When to Use

*   When solving DP problems iteratively (tabulation).
*   When the recurrence `dp[i]` only depends on states within a fixed, small window `dp[i-1]` to `dp[i-k]`.
*   When space complexity is a constraint (e.g., to avoid Memory Limit Exceeded errors).

## Related Concepts

*   **Algorithm:** [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   **Pattern Example:** [[../patterns/grid_tiling/2xn_tiling_dp.md]] (Uses this optimization) 