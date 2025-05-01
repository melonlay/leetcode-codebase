# LeetCode 25: Reverse Nodes in k-Group - Solution Explanation

## Problem Summary

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k`, then the left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Algorithmic Approach

This problem is solved using an **Iterative Linked List Segment Reversal** algorithm. We process the list in segments of size `k`. For each segment, we first check if it contains at least `k` nodes. If it does, we reverse that segment in place. If it doesn't (i.e., it's the final, potentially shorter segment), we leave it as is.

A dummy node is used before the actual head to simplify handling the connections, especially for the first segment.

## Logic Explanation

1.  **Edge Case Handling:**
    *   If the list is empty (`not head`) or `k` is 1 (no reversal needed), return the original `head`.
2.  **Initialization:**
    *   Create a `dummy = ListNode(0)` and set `dummy.next = head`. This simplifies connecting the first reversed group.
    *   Initialize `prev_group_tail = dummy`. This pointer always points to the tail node of the *previous* processed group (or the dummy node initially), which needs to be connected to the head of the *next* reversed group.
    *   Initialize `current_node = head`. This pointer marks the start of the potential next group to be reversed.
3.  **Main Iteration Loop (`while True`):**
    *   **Identify Segment End:** Starting from `current_node`, traverse up to `k` nodes. Use a `kth_node` pointer and a `count`. If a full group of `k` nodes is found, `kth_node` will point to the node *after* the k-th node (the start of the next segment), and `count` will be `k`.
    *   **Check Segment Validity:**
        *   If `count == k`: A full segment of `k` nodes exists.
        *   If `count < k`: Not enough nodes remain for a full group. Break the loop.
    *   **Reverse the k-Group (if valid):**
        *   Store the start of the next segment: `next_segment_start = kth_node`.
        *   Store the head of the current group: `group_head = current_node` (this will become the tail after reversal).
        *   Perform standard iterative linked list reversal for the `k` nodes starting from `curr = current_node`. The crucial detail is initializing the reversal's `prev` pointer to `next_segment_start`. After reversing `k` times, `prev` will point to the new head of the reversed segment.
    *   **Reconnect List:**
        *   Connect the previous segment's tail to the new head of the reversed segment: `prev_group_tail.next = prev`.
        *   Connect the new tail of the reversed segment (which was `group_head`) to the start of the next segment: `group_head.next = next_segment_start`.
    *   **Advance Pointers for Next Iteration:**
        *   Update `prev_group_tail` to the tail of the *just reversed* segment: `prev_group_tail = group_head`.
        *   Update `current_node` to start the search for the next group: `current_node = next_segment_start`.
4.  **Return Result:** Return `dummy.next`, which points to the head of the modified list.

## Knowledge Base References

*   **Iterative Linked List Segment Reversal:** The entire solution follows this algorithm. The steps for initialization (using a dummy node), segment identification, in-place reversal, reconnection, and pointer advancement are detailed in `document/algorithms/linked_list/iterative_segment_reversal.md`. This document also lists LeetCode 25 as a specific application.
*   **Linked List Data Structure:** Requires understanding of basic linked list nodes and pointer manipulation (`document/data_structures/linked_list.md`).
*   **Dummy Head Node:** The use of `dummy` is crucial for simplifying the logic, especially connecting the first segment back to the start.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the total number of nodes in the list. Although there's a loop for reversal inside the main loop, each node is effectively visited and processed a constant number of times (once for finding the k-th node, once during reversal).
*   **Space Complexity:** O(1). The reversal is done in-place using a few pointers. 