# Data Structure: Heap (Priority Queue)

## Abstract Definition

A **Priority Queue** is an abstract data type similar to a regular queue or stack, but where each element additionally has a "priority" associated with it. Elements are served based on their priority; elements with higher priority (or lower, depending on convention) are served before elements with lower priority.

A **Heap** (specifically a **Binary Heap**) is a specialized tree-based data structure that satisfies the heap property and is a common, efficient way to *implement* a priority queue.

*   **Min-Heap:** The value of each node is less than or equal to the value of its children. The root holds the minimum value.
*   **Max-Heap:** The value of each node is greater than or equal to the value of its children. The root holds the maximum value.

Heaps are typically implemented using arrays for efficiency.

## Key Operations & Complexity

Assuming a heap with `n` elements:

*   **`insert(item)` / `push(item)`:** Adds an item, maintaining the heap property. Time: O(log n).
*   **`extract_min()` / `pop_min()` (for Min-Heap):** Removes and returns the smallest item (root). Time: O(log n).
*   **`extract_max()` / `pop_max()` (for Max-Heap):** Removes and returns the largest item (root). Time: O(log n).
*   **`peek_min()` / `find_min()` (for Min-Heap):** Returns the smallest item without removing it. Time: O(1).
*   **`peek_max()` / `find_max()` (for Max-Heap):** Returns the largest item without removing it. Time: O(1).
*   **`heapify(list)`:** Converts an arbitrary list into a heap in-place. Time: O(n).

## Common Implementation: Array-Based Binary Heap

A binary heap can be efficiently represented using a list or array where:
*   The root is at index 0.
*   For a node at index `i`:
    *   Its left child is at index `2*i + 1`.
    *   Its right child is at index `2*i + 2`.
    *   Its parent is at index `(i - 1) // 2`.

This allows traversing the tree structure using simple arithmetic operations.

## Python's `heapq` Module

Python's standard library `heapq` module provides an efficient implementation of a **min-heap** using regular lists.

*   **`heapq.heappush(heap, item)`:** Pushes `item` onto the `heap` list.
*   **`heapq.heappop(heap)`:** Pops and returns the smallest item from the `heap` list.
*   **`heapq.heapify(x)`:** Transforms list `x` into a min-heap, in-place.
*   **`heapq.heappushpop(heap, item)`:** Pushes `item`, then pops and returns the smallest. More efficient than separate push and pop.
*   **`heapq.heapreplace(heap, item)`:** Pops and returns smallest, then pushes `item`. More efficient than separate pop and push.
*   To get the smallest item without popping: Access `heap[0]` (if heap is not empty).

*Note:* To implement a max-heap using `heapq`, store negated values or use custom comparison wrappers.

## Use Cases

*   **Priority Scheduling:** Operating systems, event simulation.
*   **Graph Algorithms:** Dijkstra's algorithm (shortest path), Prim's algorithm (minimum spanning tree).
*   **Merging:** K-Way Merge (see `../algorithms/merging/k_way_merge_heap.md`).
*   **Order Statistics:** Finding the k-th smallest/largest element efficiently.
*   **Huffman Coding:** Used in building the optimal prefix code tree.

## Handling Non-Comparable Items / Stability

If storing items that are not directly comparable (like objects without `__lt__`) or if stability is needed (preserving order of equal priority items), store tuples:
`(priority, sequence_count, item)`
*   `priority`: The main value to heapify by.
*   `sequence_count`: A unique, increasing counter to act as a tie-breaker.
*   `item`: The actual data.

See `../algorithms/merging/k_way_merge_heap.md` for an example of this technique. 