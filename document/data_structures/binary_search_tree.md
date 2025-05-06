# Binary Search Tree (BST)

**Category:** Data Structures

## Description

A Binary Search Tree is a node-based binary tree data structure which has the following key properties:

1.  The left subtree of a node contains only nodes with keys lesser than the node's key.
2.  The right subtree of a node contains only nodes with keys greater than the node's key.
3.  The left and right subtree each must also be a binary search tree.
4.  There must be no duplicate nodes (in a simple BST, though variations exist).

BSTs allow for efficient searching, insertion, and deletion operations on average.

## Operations

### 1. Search

To search for a value, start at the root. Compare the search value with the node's key:
*   If equal, the node is found.
*   If less, move to the left child.
*   If greater, move to the right child.
Repeat until the value is found or a `None`/NIL leaf is reached.

*   **Time Complexity:** O(log N) on average, O(N) in the worst case (skewed tree).
*   **Space Complexity:** O(log N) average / O(N) worst for recursion stack, O(1) for iterative.

### 2. Insertion

To insert a value, search for the value until a `None`/NIL leaf is reached. Insert the new node at that position.

*   **Time Complexity:** O(log N) on average, O(N) in the worst case.
*   **Space Complexity:** O(log N) average / O(N) worst for recursion stack, O(1) for iterative.

### 3. Deletion

Deleting a node is more complex, involving three cases for the node to be deleted:
*   **Case 1: Node has no children (leaf node):** Simply remove the node.
*   **Case 2: Node has one child:** Replace the node with its child.
*   **Case 3: Node has two children:**
    *   Find the inorder successor (smallest node in the right subtree) or inorder predecessor (largest node in the left subtree).
    *   Copy the successor's/predecessor's key to the node being deleted.
    *   Recursively delete the successor/predecessor (which will fall into Case 1 or 2).

*   **Time Complexity:** O(log N) on average, O(N) in the worst case.
*   **Space Complexity:** O(log N) average / O(N) worst for recursion stack, O(1) for iterative.

## Complexity

| Operation | Average Case | Worst Case | Space (Worst) |
| :-------- | :----------- | :--------- | :------------ |
| Search    | O(log N)     | O(N)       | O(N)*         |
| Insert    | O(log N)     | O(N)       | O(N)*         |
| Delete    | O(log N)     | O(N)       | O(N)*         |

\* O(1) space if implemented iteratively.

The worst-case O(N) complexity occurs when the tree becomes degenerate (skewed), resembling a linked list.

## Use Cases & Trade-offs

*   **Advantages:** Simple to implement. Efficient average-case performance. Enables inorder traversal to retrieve elements in sorted order.
*   **Disadvantages:** Performance degrades to O(N) on unbalanced trees.
*   **Common Uses:** Symbol tables, searching, sorting (via inorder traversal). Often serves as the basis for more complex balanced trees.

## Related Concepts

*   [[red_black_tree.md]]
*   [[avl_tree.md]]
*   [[splay_tree.md]]
*   [[../techniques/tree/tree_traversal.md]] (Assumed - needs creation/verification)
*   Self-Balancing BSTs (general concept) 