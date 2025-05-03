# Optimization: Dual Path Grid DP - Top-Down vs Bottom-Up

## Context

When implementing the **Dual Path Grid DP pattern** (see [[../../patterns/matrix/dual_path_grid_dp.md]]), two primary dynamic programming approaches are common: Top-Down (Memoized Recursion) and Bottom-Up (Tabulation).

While both solve the same problem with the same asymptotic time complexity (O(N^3)), they have different space complexities and practical performance characteristics worth comparing.

## Approach Comparison

1.  **Bottom-Up (Tabulation with O(N^2) Space):**
    *   **Implementation:** Iterates through steps `t`, calculating `new_dp[r1][r2]` based on the previous step's `dp[r1][r2]`. Requires only two layers (current and previous) of the DP state, reducing space.
    *   **Space Complexity:** O(N^2)
    *   **Time Complexity:** O(N^3)
    *   **Pros:** Best theoretical space complexity.
    *   **Cons:** Iterates through all possible `(r1, r2)` pairs at each step, potentially doing unnecessary work if many states are unreachable (e.g., due to many thorns in the grid). Implementing symmetry pruning (`r1 <= r2`) might require slightly more complex loop bounds or checks.

2.  **Top-Down (Memoized Recursion):**
    *   **Implementation:** Uses a recursive function `dp(state...)` with memoization (e.g., `@cache`).
    *   **Space Complexity:** O(N^3) (Worst-case for the memoization cache).
    *   **Time Complexity:** O(N^3)
    *   **Pros:**
        *   **Sparse State Efficiency:** Naturally explores only reachable states. Can be significantly faster in practice if the grid contains many obstacles, avoiding computation for unreachable `(r1, r2)` pairs.
        *   **Symmetry Pruning:** Easily implements symmetry optimization (e.g., checking `if r1 > r2: ...`) which prunes ~half the state space, reducing the constant factor of the time complexity.
        *   **Implementation:** Can feel more direct, mapping closely to the recursive state definition.
    *   **Cons:** Higher theoretical space complexity. Python recursion depth limits could be a concern for extremely large N (though typically not for N=50).

## Recommendation

*   For grids where the state space is dense (few obstacles) and memory is highly constrained, the **Bottom-Up O(N^2) space** approach is preferable.
*   For grids that might be sparse (many obstacles) or when implementation simplicity is valued, the **Top-Down O(N^3) space** approach, especially with **symmetry pruning**, is often faster in practice and easier to code correctly.

Given typical competitive programming constraints and Python's efficient `@cache`, the Top-Down approach with symmetry pruning is frequently a strong choice for this pattern.

## Related Concepts

*   **Pattern:** [[../../patterns/matrix/dual_path_grid_dp.md]]
*   **Algorithm:** [[../../algorithms/dynamic_programming/dynamic_programming.md]] 