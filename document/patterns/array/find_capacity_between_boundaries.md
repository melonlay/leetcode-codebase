# Pattern: Find Capacity Between Boundaries

## Description

This pattern addresses problems where you need to calculate the total capacity (e.g., area, volume) that can be contained or trapped between varying boundaries defined by elements in an array.

The quintessential example is calculating trapped rainwater in an elevation map, but the core idea can apply to similar scenarios involving finding contained quantities limited by surrounding values.

## Core Problem Structure

Given an array `H` representing heights or boundary levels:

For each position `i`, the capacity it can hold is determined by the *minimum* of the highest boundary to its left (`max_left`) and the highest boundary to its right (`max_right`), minus the height at the position itself (`H[i]`).

Capacity at `i` = `max(0, min(max_left, max_right) - H[i])`

The total capacity is the sum of capacities at all relevant positions.

## Common Solution Approaches

1.  **Two Pointers (Inward Moving):**
    *   **Idea:** Use two pointers, `left` and `right`, moving inwards. Maintain `left_max` and `right_max` encountered so far.
    *   **Logic:** At each step, process the side with the lower height (`H[left]` vs `H[right]`). If `H[left] < H[right]`, the capacity at `left` is limited by `left_max` (since `right_max` is guaranteed to be at least `H[right]`). Calculate water `max(0, left_max - H[left])` and move `left` inward. Update `left_max` if needed. Symmetric logic applies if `H[right] <= H[left]`.
    *   **Complexity:** O(n) Time, O(1) Space.
    *   **Reference:** [Pattern: Two Pointers](../../patterns/two_pointers.md)
    *   **Example:** Optimal solution for Trapping Rain Water ([Problem 42](../../../problems/0042_trapping_rain_water/solution.md)).

2.  **Dynamic Programming (Prefix/Suffix Max):**
    *   **Idea:** Precompute the `max_left` for all `i` and `max_right` for all `i`.
    *   **Logic:**
        1. Calculate `prefix_max` array: `prefix_max[i] = max(H[0...i])`.
        2. Calculate `suffix_max` array: `suffix_max[i] = max(H[i...n-1])`.
        3. Iterate from `i = 0` to `n-1`. Calculate capacity at `i` as `max(0, min(prefix_max[i], suffix_max[i]) - H[i])`. Sum these capacities.
    *   **Complexity:** O(n) Time (3 passes), O(n) Space (for prefix/suffix arrays).
    *   **Reference:** [[../../../techniques/sequence/prefix_suffix_aggregates.md]]

3.  **Monotonic Stack (Decreasing):**
    *   **Idea:** Use a decreasing monotonic stack to store indices of bars. When a taller bar `H[i]` is encountered, it acts as a right boundary for the bars popped from the stack.
    *   **Logic:** Iterate `i` from 0 to `n-1`.
        *   While stack is not empty and `H[i] > H[stack.top()]`:
            *   Pop `top_idx` (index of the bar being processed).
            *   If stack is now empty, break (no left boundary).
            *   `left_boundary_idx = stack.top()`.
            *   Bounded height: `h = min(H[left_boundary_idx], H[i]) - H[top_idx]`.
            *   Width: `w = i - left_boundary_idx - 1`.
            *   Add `w * h` to total trapped water.
        *   Push current index `i` onto the stack.
    *   **Complexity:** O(n) Time (each index pushed/popped once), O(n) Space (for stack).
    *   **Reference:** [[../../../techniques/sequence/monotonic_queue.md]] (covers general monotonic stack/queue concept).

## When to Use

*   When the problem involves calculating a contained area/volume based on surrounding heights or boundaries in a 1D array.
*   Look for phrasing like "trapped water", "container with most water" (though that one has a simpler two-pointer logic), or finding capacity limited by walls.

## Tradeoffs

*   **Two Pointers:** Most space-efficient (O(1)) for the 1D case.
*   **DP (Prefix/Suffix Max):** Conceptually simple passes for 1D, but requires extra O(n) space.
*   **Monotonic Stack:** O(n) time and space for 1D, can be less intuitive.
*   **Heap-based (for 2D):** Necessary for the 2D version ([Problem 407](../../../problems/0407_trapping_rain_water_ii/solution.md)). Standard approach uses O(M*N) space (heap + visited). An optimization combines the heap with DFS and modifies the input array in-place for visited tracking, potentially reducing heap operations and saving explicit visited space.
    *   **Reference (Heap+DFS Algorithm):** [[../../../algorithms/graph_search/heap_dfs_boundary_fill.md]]
    *   **Reference (Comparison):** [[../../../optimizations/grid_traversal/heap_dfs_vs_bfs_boundary_fill.md]]

## Strategy Comparison (1D Case)

See [[../../optimizations/array/trapping_rain_water_1d_strategies.md]] for a comparison of the Time/Space tradeoffs and implementation details of the Two Pointers, DP, and Monotonic Stack approaches for the 1D problem. 