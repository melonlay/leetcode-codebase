# LeetCode 23: Merge k Sorted Lists - Solution Explanation

## Problem Summary

Given an array of `k` linked-lists `lists`, where each linked list is sorted in ascending order, merge all the linked lists into one sorted linked list and return it.

## Algorithmic Approach

The most efficient way to merge `k` sorted lists is using a **Min-Heap (Priority Queue)**. This approach is often referred to as K-Way Merge.

1.  We add the head node of each of the `k` lists to a min-heap.
2.  We repeatedly extract the node with the minimum value from the heap.
3.  This extracted node is the next node in our final merged list.
4.  If the extracted node has a `next` node in its original list, we add that `next` node to the heap.
5.  We continue this process until the heap is empty.

To handle the case where nodes in the heap might have the same value (leading to comparison issues if `ListNode` objects themselves are not directly comparable in the required way), we store tuples `(value, counter, node)` in the heap. The `counter` acts as a unique tie-breaker.

## Logic Explanation

1.  **Initialization:**
    *   Create an empty min-heap `min_heap`.
    *   Initialize a `counter = 0` for tie-breaking.
    *   Iterate through the input `lists`.
    *   For each non-empty `head` node in `lists`, push a tuple `(head.val, counter, head)` onto the `min_heap`. Increment the `counter` after each push to ensure uniqueness.
    *   Create a `dummy = ListNode()` to serve as the starting point for the merged list.
    *   Initialize `current = dummy` to keep track of the tail of the merged list.
2.  **Merging Loop:**
    *   While `min_heap` is not empty:
        *   Pop the smallest element from the heap using `heapq.heappop(min_heap)`. This returns the tuple `(val, idx, node)` where `node` has the smallest value currently in the heap.
        *   Append this `node` to the merged list: `current.next = node`.
        *   Advance the tail pointer: `current = current.next`.
        *   If the popped `node` has a `next` node (`node.next` is not `None`), push the next node's tuple `(node.next.val, counter, node.next)` onto the heap. Increment the `counter`.
3.  **Return Result:** After the loop, the merged list is complete. Return `dummy.next`, which points to the head of the merged sorted list.

## Knowledge Base References

*   **K-Way Merge using Min-Heap:** The core algorithm is described in `document/algorithms/merging/k_way_merge_heap.md`. This includes the heap initialization, extraction loop, and importantly, the use of tuples `(value, counter, node)` to handle non-comparable items (like `ListNode` objects with the same `val`) in Python's `heapq`.
*   **Linked List Data Structure:** Basic linked list operations and the `ListNode` definition are fundamental. See `document/data_structures/linked_list.md`.
*   **Dummy Head Node:** Using a `dummy` node simplifies adding the first node to the result list.

## Complexity Analysis

*   **Time Complexity:** O(N log k), where N is the *total* number of nodes across all `k` lists. Each node is pushed onto and popped from the heap once. Heap operations take O(log k) time, as the heap size is at most `k`.
*   **Space Complexity:** O(k). The space is dominated by the min-heap, which stores at most one node from each of the `k` lists at any time. 