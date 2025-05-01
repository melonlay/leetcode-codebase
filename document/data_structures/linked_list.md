# Linked List

## Description

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (called a *node*) contains:

1.  Data (the value stored in the node).
2.  A pointer (or link) to the next node in the sequence.

The first node is called the *head*, and the last node typically points to `null` (or `None` in Python) to indicate the end of the list.

## Types

*   **Singly Linked List:** Each node points only to the next node.
*   **Doubly Linked List:** Each node points to both the next and the previous node.
*   **Circular Linked List:** The last node points back to the head node.

## Common Operations

*   **Traversal:** Visiting each node in the list, usually starting from the head.
*   **Insertion:** Adding a new node (at the beginning, end, or middle).
*   **Deletion:** Removing a node.
*   **Search:** Finding a node with a specific value.

## Complexity (Singly Linked List)

*   **Access (by index):** O(n) - requires traversing from the head.
*   **Search:** O(n) - requires traversing in the worst case.
*   **Insertion (at beginning):** O(1)
*   **Insertion (at end):** O(n) if tail pointer is not maintained, O(1) if it is.
*   **Deletion (at beginning):** O(1)
*   **Deletion (given node reference):** O(1)
*   **Deletion (by value):** O(n) - requires search first.

## Use Cases

*   Implementing stacks and queues.
*   When dynamic size is needed and insertions/deletions are frequent (especially at the beginning).
*   Representing sequences where random access is not a primary requirement.

## Python Snippet (Singly Linked List Node)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example Usage (Creating 1 -> 2 -> 3)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
``` 