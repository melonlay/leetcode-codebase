# Greedy Approach for K Limited Operations (Heap-based)

**Applies Pattern:** [[../../../patterns/array/k_limited_operations.md|Pattern: K-Limited Operations on Arrays]]

**Paradigm:** [[../greedy.md|Greedy Algorithms]]
**Data Structure:** [[../../../data_structures/heap_priority_queue.md|Heap/Priority Queue]]
**Alternative:** [[../dynamic_programming/array/k_limited_operations_dp.md|DP Approach]]

## Problem Pattern Context

This approach is often applicable to the **K-Limited Operations** pattern when:
1. The goal is to maximize/minimize a value by performing at most `k` discrete operations.
2. Individual operations have identifiable start/end points and values.
3. A concept of "merging" adjacent optimal operations exists, typically by identifying and cancelling an intermediate segment with low/negative value (a "cost").

This frequently provides a faster alternative to O(N*k) DP, especially for large `k`.

## Heap-based Greedy Approach

**Core Idea:**
Greedily select the best possible actions up to `k` times using a heap. An "action" can be:
1. Performing the single highest-value operation currently available.
2. Identifying the highest "cost" (or smallest gain) intermediate segment whose cancellation enables merging two adjacent high-value operations.

A min-heap stores potential actions, prioritized by value/cost (using negative values for max-heap behavior).

**Algorithm Steps (Generalized):**

1. **`find_best_change(start, end, direction)` Helper:**
    * Scans sequence segment `[start...end]`.
    * `direction=1`: Finds max positive value operation, returns `(value, op_start, op_end)`.
    * `direction=-1`: Finds max "cost" operation (e.g., smallest gain or largest loss), returns `(cost_magnitude, cost_start, cost_end)`.

2. **Heap Initialization:**
    * Find the best initial operation (`direction=1`) over the whole sequence.
    * Push `(-value, 0, op_start, op_end, n-1, 1)` onto min-heap.

3. **Main Loop (Repeat `k` times or until heap empty):**
    * Pop the best action (highest value or highest cost-to-cancel).
    * Let popped item be `(neg_val_or_cost, interval_start, op_start, op_end, interval_end, direction)`.
    * **If `direction == 1` (Valuable Operation):**
        * Add value (`-neg_val_or_cost`) to total.
        * Increment operations count.
        * **Split and Add Potential Actions:**
            * Find max *cost* (`d=-1`) *within* `op_start+1` to `op_end-1`. If found, push `(-cost_magnitude, ..., -1)`.
            * Find max *value* (`d=1`) *before* `op_start-1`. If found, push `(-value, ..., 1)`.
            * Find max *value* (`d=1`) *after* `op_end+1`. If found, push `(-value, ..., 1)`.
    * **If `direction == -1` (Cost Cancellation / Merge):**
        * No direct value added, no operation count incremented.
        * Find max *value* (`d=1`) within the *entire merged interval* `interval_start` to `interval_end`. If found, push `(-value, ..., 1)`.

4. **Problem-Specific Optimizations:** Look for optimizations based on the problem constraints (e.g., large `k`).

## Complexity
*   **Time:** Typically O(N log N) or similar logarithmic dependency, often faster than O(N*k) DP.
*   **Space:** O(N) for the heap worst case.

## Implementation Notes
*   Requires careful definition of the `find_best_change` function and the interval logic for the specific problem.
*   Using `direction=-1` to represent the merge-enabling cost segment is crucial. 