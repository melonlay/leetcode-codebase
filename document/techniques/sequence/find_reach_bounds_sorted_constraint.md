# Technique: Find Reach Bounds in Sorted Array with Relative Constraint

## 1. Description

This technique uses [[../../algorithms/searching/binary_search.md]] (specifically functions like Python's `bisect_left` and `bisect_right`) to efficiently find the farthest reachable bounds (leftmost and rightmost indices) for each element in a **sorted array** that satisfy a relative constraint.

It's commonly used as a sub-step for precomputing single-step jumps in algorithms like [[../binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]].

## 2. Core Algorithm (Farthest Left/Right Reach Example)

**Problem:** Given a sorted array `vals` and a constraint value `k` (e.g., `maxDiff`), for each index `i`:
*   Find the **largest** index `fr` (farthest right) such that `vals[fr] <= vals[i] + k`.
*   Find the **smallest** index `fl` (farthest left) such that `vals[fl] >= vals[i] - k`.

**Algorithm (O(N log N) Time):**

1.  **Initialization:**
    *   Initialize result arrays `farthest_right = [0] * n` and `farthest_left = [0] * n`.
2.  **Iteration:** Iterate through the array with index `i` from `0` to `n-1`:
    *   **Calculate Farthest Right (`fr`):**
        *   Find the insertion point for `vals[i] + k` in `vals` using `bisect_right`. This gives an index `idx_r` such that all elements *before* it are `<= vals[i] + k`.
        *   The largest index satisfying the condition is `fr = idx_r - 1`. Handle edge cases (e.g., if `idx_r` is 0).
        *   Store `farthest_right[i] = fr`.
    *   **Calculate Farthest Left (`fl`):**
        *   Find the insertion point for `vals[i] - k` in `vals` using `bisect_left`. This gives an index `idx_l` such that all elements *at or after* it are `>= vals[i] - k`.
        *   The smallest index satisfying the condition is `fl = idx_l`. Handle edge cases.
        *   Store `farthest_left[i] = fl`.
3.  **Return `farthest_left`, `farthest_right`.**

## 3. Complexity

*   **Time Complexity:** O(N log N) - The loop runs N times, and each iteration performs binary searches (`bisect`) which take O(log N) time.
*   **Space Complexity:** O(N) to store the result arrays.

## 4. Use Cases

*   Calculating single-step reach (`fr`, `fl`) for [[../binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]].
*   Preprocessing step in algorithms needing reachability information based on constraints in sorted data.

## 5. Related Concepts

*   [[../../algorithms/searching/binary_search.md]] (`bisect` module)
*   [[../binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]]
*   Sorting 