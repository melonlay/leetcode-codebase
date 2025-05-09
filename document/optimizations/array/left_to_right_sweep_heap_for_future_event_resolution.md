# Optimization: Left-to-Right Sweep with Heap for Future Event Resolution

## 1. Problem Type Addressed

This technique is highly effective for problems where:
1.  Queries involve conditions that depend on elements appearing *later* in a sequence (i.e., to the right during a left-to-right sweep).
2.  We need to find the *leftmost* element `j` (the sweep index) that satisfies a pre-determined condition for an active query.
3.  Queries can be "activated" when the sweep reaches a certain index.

A prime example is LeetCode 2940 ("Find Building Where Alice And Bob Can Meet"), specifically the part where `a < b` and `heights[a] >= heights[b]`. The task becomes finding the leftmost `j > b` such that `heights[j] > heights[a]`. Here, `b` is the activation index for the query, and `heights[a]` is the threshold.

## 2. Core Idea & Algorithm Steps

The approach involves a left-to-right sweep over the main data array, using a min-priority queue (heap) to manage active queries waiting for a future element to satisfy their condition.

1.  **Query Preprocessing & Grouping (Activation Map):
    *   Iterate through each raw query. Simplify or immediately resolve if possible.
        *   _Example (LeetCode 2940):_ If `a==b`, result is `a`. If `heights[a] < heights[b]` (assuming `a<b`), result is `b` because Alice can see Bob at `b`, and Bob is already there.
    *   For queries that cannot be immediately resolved and require searching to the right:
        *   Identify an **activation index** `s` (e.g., index `b` in the example).
        *   Determine the **condition value** `v` that a future element `element[j]` (where `j > s`) must satisfy (e.g., `element[j] > v`, where `v = heights[a]` in the example).
        *   Store these pending queries, grouped by their activation index `s`. A dictionary `queries_activated_at[s] = list_of[(condition_value, original_query_idx)]` is suitable.

2.  **Left-to-Right Sweep with Min-Heap:**
    *   Initialize an empty `min_heap`. This heap will store `(condition_value, original_query_idx)` for queries that have been activated but not yet resolved. It's ordered by `condition_value`.
    *   Initialize `results` array for all queries (e.g., with -1).
    *   Iterate with current index `j` from `0` to `n-1` (where `n` is the array size):
        *   **Step A: Resolve Active Queries:**
            *   While the `min_heap` is not empty AND `element[j]` satisfies the condition for the query at the top of the heap (e.g., `element[j] > min_heap[0][0]` for a "greater than" condition):
                *   Pop `(resolved_value, query_idx)` from `min_heap`.
                *   Set `results[query_idx] = j`. Since we are sweeping left-to-right, this `j` is the leftmost element satisfying the condition for this query.
        *   **Step B: Activate New Queries:**
            *   If index `j` is an activation index for some queries (i.e., `j` is in `queries_activated_at`):
                *   For each `(condition_value, original_query_idx)` in `queries_activated_at[j]`:
                    *   Push `(condition_value, original_query_idx)` onto the `min_heap`.

3.  **Return `results`.**

## 3. Data Structure Details

*   **Activation Map (`queries_activated_at`):** Typically a `defaultdict(list)` mapping an index `s` to a list of tuples, where each tuple contains the necessary information for a query that becomes active when the sweep reaches `s`.
*   **Min-Heap (`min_heap`):** Stores tuples like `(condition_value, original_query_idx)`. The heap property ensures that the query with the "easiest" condition to satisfy (e.g., smallest threshold for a `>` condition) is always at the top.

## 4. Complexity

*   **Time Complexity:**
    *   Query Preprocessing: O(Q) where Q is the number of queries.
    *   Sweep: N iterations.
        *   Heap Operations: Each query is pushed onto the heap once and popped once. Each heap operation is O(log Q). Total O(Q log Q).
        *   Accessing `queries_activated_at`: O(Q) total across all `j`.
    *   Overall: **O(N + Q log Q)**.
*   **Space Complexity:** O(Q + N) in worst case for `queries_activated_at` (if all queries activate at different points) and O(Q) for the heap.

## 5. Advantages

*   **Conceptual Simplicity:** The L-R sweep directly corresponds to finding the "leftmost" satisfying element.
*   **Efficiency:** Often very fast in practice, especially in Python, due to efficient heap operations and direct logic.
*   **Direct Handling of "Future" Conditions:** Well-suited for problems where an event/query at index `s` depends on finding something at `j > s`.

## 6. Comparison with Right-to-Left Sweep + Monotonic Stack

*   For problems like LeetCode 2940, this L-R sweep with a heap for pending query conditions can be more direct and performant than a R-L sweep with a monotonic stack that then requires binary searching on that stack for each query.
The L-R sweep resolves queries as soon as the condition is met by the current `element[j]`, naturally finding the leftmost.

## 7. Related Concepts

*   [[../../patterns/sweep_line.md]] (though this is a 1D sweep)
*   [[../../data_structures/heap_priority_queue.md]]
*   Offline Query Processing 