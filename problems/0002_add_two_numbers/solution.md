# LeetCode 2: Add Two Numbers - Solution Explanation

## Problem Summary

Given two non-empty linked lists representing two non-negative integers where the digits are stored in reverse order, add the two numbers and return the sum as a linked list in the same format.

## Algorithmic Approach

The solution simulates the process of manual addition, starting from the least significant digit (the head of the lists). It iterates through both lists concurrently, adding corresponding digits along with any carry from the previous step, and constructs a new linked list for the result.

## Logic Explanation

1.  **Initialization:**
    *   Create a `dummy_head = ListNode(0)`. This simplifies the process of adding the first node to the result list, as we can always append to `current.next`.
    *   Initialize `current = dummy_head` to keep track of the last node in the result list.
    *   Initialize `carry = 0` to store the carry-over value (0 or 1).
2.  **Iteration:** Use a `while` loop that continues as long as there are nodes left in either input list (`l1` or `l2`) or there is a non-zero `carry`.
3.  **Get Values:** Inside the loop, get the values of the current nodes from `l1` and `l2`. If a list has been exhausted (`l1` or `l2` is `None`), treat its value as 0.
4.  **Calculate Sum and Digit:** Calculate the `total_sum` of the two digits and the `carry`. The new `carry` for the next iteration is `total_sum // 10`, and the `digit` to be added to the result list is `total_sum % 10`.
5.  **Create New Node:** Create a new `ListNode` with the calculated `digit` and append it to the result list: `current.next = ListNode(digit)`.
6.  **Advance Pointers:** Move the `current` pointer to the newly added node (`current = current.next`). Advance `l1` and `l2` to their next nodes if they exist.
7.  **Return Result:** After the loop finishes, the complete sum is stored in the list starting from `dummy_head.next`. Return `dummy_head.next`.

## Knowledge Base References

*   **Linked List Data Structure:** The solution fundamentally operates on linked lists. Basic node structure and traversal are described in `document/data_structures/linked_list.md`.
*   **Dummy Head Node:** The use of a `dummy_head` is a common technique in linked list manipulations (mentioned in contexts like `document/algorithms/linked_list/iterative_segment_reversal.md`) to simplify edge cases, particularly handling the insertion of the very first node without special checks.

## Complexity Analysis

*   **Time Complexity:** O(max(M, N)), where M and N are the lengths of the input lists `l1` and `l2`. The loop iterates at most max(M, N) + 1 times.
*   **Space Complexity:** O(max(M, N)). The length of the new result list is at most max(M, N) + 1 (to accommodate a potential final carry). 