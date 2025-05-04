# Technique: Find Boundary Pointer in Sorted Array with Relative Constraint

## 1. Description

This technique uses the [[../../patterns/two_pointers.md]] pattern to efficiently find a specific boundary pointer (e.g., the leftmost or rightmost index) for each element in a **sorted array** that satisfies a relative constraint.

It's commonly used as a sub-step when transforming an implicit graph on sorted data into a derived tree structure (see [[../../patterns/graph/implicit_graph_to_tree_transformation.md]]).

## 2. Core Algorithm (Leftmost Pointer Example)

**Problem:** Given a sorted array `vals` and a constraint value `k` (e.g., `maxDiff`), for each index `i`, find the **smallest** index `p` (the "leftmost pointer") such that `vals[i]` and `vals[p]` satisfy the constraint (e.g., `vals[i] - vals[p] <= k`).

**Algorithm (O(N) Time):**

1.  **Initialization:**
    *   Initialize the result array `parent_ptr = [0] * n` (where `n` is the length of `vals`).
    *   Initialize a second pointer `left_ptr = 0`.
2.  **Iteration:** Iterate through the array with the main pointer `i` from `0` to `n-1`:
    *   **Advance `left_ptr`:** While the constraint is violated between `vals[i]` and `vals[left_ptr]` (e.g., `vals[i] - vals[left_ptr] > k`):
        *   Increment `left_ptr`.
    *   **Assign Result:** The current `left_ptr` is now the smallest index satisfying the constraint for `i`. Assign `parent_ptr[i] = left_ptr`.
3.  **Return `parent_ptr`.**

**Correctness:** Since both `i` and `left_ptr` only move forward, and `vals` is sorted, the `while` loop efficiently finds the correct leftmost boundary for each `i`. Each pointer traverses the array at most once.

## 3. Variations

*   **Rightmost Pointer:** A similar logic can be applied to find the largest index `p` satisfying a constraint, potentially iterating `i` from right-to-left or using a different `while` loop condition.
*   **Different Constraints:** The `while` loop condition changes based on the specific constraint (`>= k`, `|vals[i] - vals[p]| <= k`, etc.).

## 4. Complexity

*   **Time Complexity:** O(N) - Each pointer (`i` and `left_ptr`) iterates through the array at most once.
*   **Space Complexity:** O(N) to store the result array `parent_ptr` (or O(1) if results can be processed online).

## 5. Use Cases

*   Calculating parent pointers for the [[../graph_traversal/dfs_derived_tree_path_query.md]] technique.
*   Preprocessing step in algorithms operating on sorted data with range constraints.

## 6. Related Concepts

*   [[../../patterns/two_pointers.md]]
*   [[../../patterns/graph/implicit_graph_to_tree_transformation.md]]
*   Sorting 