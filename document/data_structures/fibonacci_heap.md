# Data Structure: Fibonacci Heap

**Category:** Data Structure (`data_structures/`)

## Abstract Definition

The Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees. It has a better amortized running time for many operations compared to other priority queue structures like binary heaps or binomial heaps, particularly for `decrease_key`.

## Key Operations & Amortized Complexity

Assuming `n` elements:

*   **`insert(item)`:** O(1)
*   **`find_min()` / `peek_min()`:** O(1)
*   **`union(heap1, heap2)`:** O(1)
*   **`extract_min()`:** O(log n)
*   **`decrease_key(node, new_key)`:** O(1)
*   **`delete(node)`:** O(log n)

## Structure

*   A collection of trees satisfying the min-heap property.
*   Trees are not necessarily binary trees.
*   A pointer `min` points to the root with the minimum key.
*   Roots of the trees are linked together in a circular, doubly linked list (the root list).

The structure is more complex than a binary heap, involving operations like cascading cuts during `decrease_key` and linking trees of the same degree during `extract_min` to maintain the logarithmic amortized bounds.

## Use Cases

*   **Graph Algorithms:** Primarily used to speed up algorithms that rely heavily on `decrease_key` operations.
    *   **Dijkstra's Algorithm:** Improves time complexity to O(E + V log V).
    *   **Prim's Algorithm (MST):** Improves time complexity to O(E + V log V).

## Trade-offs vs. Binary Heap ([`heap_priority_queue.md`](./heap_priority_queue.md))

*   **Pros:** Faster amortized times for `insert`, `union`, `decrease_key`.
*   **Cons:**
    *   Much more complex to implement correctly.
    *   Higher constant factors in practice mean that for moderate input sizes, a simple binary heap (`heapq`) might be faster due to lower overhead.
    *   `delete` operation is less efficient than `extract_min`.
    *   Not typically available in standard libraries; usually requires a custom implementation.

## Conclusion

While theoretically important for achieving the best asymptotic complexities for certain algorithms like Dijkstra's and Prim's, Fibonacci heaps are often overkill in practice (especially in competitive programming or standard applications) unless the performance gain from the O(1) amortized `decrease_key` is critical for very large inputs or specific usage patterns. 