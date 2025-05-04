# LeetCode 23: Merge k Sorted Lists - Solution Explanation

## Problem Summary

Given an array of `k` linked-lists `lists`, where each linked list is sorted in ascending order, merge all the linked lists into one sorted linked list and return it.

## Algorithmic Approach: K-Way Merge using Min-Heap

This problem is a direct application of the **K-Way Merge** algorithm, efficiently implemented using a **Min Heap** (Priority Queue).

The heap is used to efficiently find the smallest node among the current heads of all `k` lists.

## Logic Explanation

The detailed algorithm is described in the Knowledge Base:
*   **Reference:** `[[../document/algorithms/merging/k_way_merge_heap.md]]`

Here is a summary matching the code:

1.  **Initialization:**
    *   Create a min-heap `min_heap`.
    *   Initialize a `counter` to 0 (used for stable tie-breaking in the heap when node values are equal).
    *   Iterate through the input `lists`. For each non-null head node `head`:
        *   Push `(head.val, counter, head)` onto the `min_heap`. The tuple stores the value (for sorting), the counter (for tie-breaking), and the node itself.
        *   Increment `counter`.
    *   Create a `dummy` head node for the result list and a `current` pointer initialized to `dummy`.
2.  **Heap Processing:**
    *   While `min_heap` is not empty:
        *   Pop the element with the smallest value: `val, idx, node = heapq.heappop(min_heap)`.
        *   Append this `node` to the result list: `current.next = node`.
        *   Advance the `current` pointer: `current = current.next`.
        *   **Add Next Node:** If the popped `node` has a successor (`node.next` is not null):
            *   Push the successor onto the heap: `heapq.heappush(min_heap, (node.next.val, counter, node.next))`.
            *   Increment `counter`.
3.  **Return Result:** Return `dummy.next`, which is the head of the merged sorted linked list.

## Knowledge Base References

*   **Core Algorithm:** `[[../document/algorithms/merging/k_way_merge_heap.md]]` (Explains the K-Way Merge pattern and heap usage).
*   **Data Structures:**
    *   `[[../document/data_structures/heap_priority_queue.md]]` (Details on heaps and `heapq`).
    *   `[[../document/data_structures/linked_list.md]]` (Basic linked list concepts).

## Complexity Analysis

Let `N` be the total number of nodes across all `k` lists.

*   **Time Complexity:** O(N log k). Initial heap creation is O(k log k). Each node is pushed onto and popped from the heap once, with each operation taking O(log k). Total time is dominated by heap operations on N nodes.
*   **Space Complexity:** O(k). The heap stores at most `k` nodes (one from each list) at any time. 