# Optimization: 1D Trapping Rain Water Strategies

**Related Pattern:** [[../../patterns/array/find_capacity_between_boundaries.md]]

## Context

The 1D Trapping Rain Water problem (e.g., LeetCode 42) asks to calculate the amount of water trapped between vertical bars represented by an array of heights.

Capacity at `i` = `max(0, min(max_left[i], max_right[i]) - height[i])`

Several approaches exist with the same optimal O(n) time complexity, but they differ in space complexity and implementation details.

## Strategies Compared

1.  **Two Pointers (Inward Moving)**
    *   **Logic:** Maintain `left`, `right` pointers, `left_max`, `right_max`. Process the shorter side (`height[left]` vs `height[right]`). Calculate trapped water based on the corresponding `max` (`left_max` or `right_max`). Move the pointer of the shorter side inward. See [[../../patterns/array/find_capacity_between_boundaries.md]] for detailed logic.
    *   **Time:** O(n) - Single pass.
    *   **Space:** O(1).
    *   **Pros:** Most space-efficient, conceptually elegant once the invariant (processing the shorter side is safe) is understood.
    *   **Cons:** The logic/invariant might be slightly less immediately obvious than the DP approach.

2.  **Dynamic Programming (Prefix/Suffix Max)**
    *   **Logic:**
        1. Calculate `prefix_max` array (max height from left up to `i`).
        2. Calculate `suffix_max` array (max height from right up to `i`).
        3. Iterate again, calculating trapped water at `i` using `min(prefix_max[i], suffix_max[i]) - height[i]`.
    *   **Time:** O(n) - Three passes.
    *   **Space:** O(n) - For the two max arrays.
    *   **Pros:** Conceptually straightforward, directly implements the `min(max_left, max_right)` formula.
    *   **Cons:** Requires extra space.
    *   **Reference:** [[../sequence/prefix_suffix_aggregates.md]]

3.  **Monotonic Stack (Decreasing)**
    *   **Logic:** Maintain a stack storing indices of bars in decreasing height order. Iterate through the heights. If the current bar `height[i]` is taller than the bar at `stack.top()`:
        *   Pop `top_idx` from the stack.
        *   If the stack is not empty, the popped bar `height[top_idx]` is bounded by the current bar `height[i]` (right boundary) and the new stack top `stack.top()` (left boundary).
        *   Calculate width: `w = i - stack.top() - 1`.
        *   Calculate bounded height: `h = min(height[i], height[stack.top()]) - height[top_idx]`.
        *   Add `w * h` to total water.
        *   Repeat popping while `height[i]` > `height[stack.top()]`.
        *   Push `i` onto the stack.
    *   **Time:** O(n) - Each index pushed/popped at most once.
    *   **Space:** O(n) - For the stack in the worst case (e.g., decreasing heights).
    *   **Pros:** Solves the problem in a single pass (conceptually).
    *   **Cons:** Can be less intuitive to implement correctly compared to the other two. Logic relies on finding the bounding walls when a bar is popped.
    *   **Reference:** [[../sequence/monotonic_queue.md]] (covers general monotonic stack/queue concept).

## Recommendation

*   For optimal **space complexity**, the **Two Pointers** approach is preferred (O(1) space).
*   For conceptual **simplicity** in directly applying the formula, the **DP (Prefix/Suffix Max)** approach is very clear, at the cost of O(n) space.
*   The **Monotonic Stack** approach is also efficient but often considered less intuitive for this specific problem compared to the others.

All three achieve O(n) time complexity. 