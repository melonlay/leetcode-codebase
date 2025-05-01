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
    *   **Reference:** [Technique: Prefix/Suffix Maximums](../../techniques/array/prefix_suffix_max.md)

3.  **Monotonic Stack:**
    *   **Idea:** Use a decreasing monotonic stack to store indices of bars. When a taller bar is encountered, it forms a boundary, allowing calculation of trapped water for bars popped from the stack.
    *   **Logic:** Iterate through heights. If the current bar is taller than the stack top, pop the top, calculate water trapped using the new top and current bar as boundaries, and add to total. Push the current bar's index.
    *   **Complexity:** O(n) Time (each index pushed/popped once), O(n) Space (for stack).
    *   **Reference:** [Technique: Monotonic Queue/Stack](../../techniques/monotonic_queue.md) (*Assuming link*) - This problem often uses a stack variant.

## When to Use

*   When the problem involves calculating a contained area/volume based on surrounding heights or boundaries in a 1D array.
*   Look for phrasing like "trapped water", "container with most water" (though that one has a simpler two-pointer logic), or finding capacity limited by walls.

## Tradeoffs

*   **Two Pointers:** Most space-efficient (O(1)) for the 1D case.
*   **DP (Prefix/Suffix Max):** Conceptually simple passes for 1D, but requires extra O(n) space.
*   **Monotonic Stack:** O(n) time and space for 1D, can be less intuitive.
*   **Heap-based (for 2D):** Necessary for the 2D version ([Problem 407](../../../problems/0407_trapping_rain_water_ii/solution.md)). Standard approach uses O(M*N) space (heap + visited). An optimization combines the heap with DFS and modifies the input array in-place for visited tracking, potentially reducing heap operations and saving explicit visited space. 