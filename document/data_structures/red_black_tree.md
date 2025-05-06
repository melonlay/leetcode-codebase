# Red-Black Tree

**Category:** Data Structures

## Description

A Red-Black Tree is a self-balancing binary search tree where each node has an extra bit for storing color ("red" or "black"). By enforcing constraints on node colors during insertions and deletions, Red-Black Trees ensure that the tree remains approximately balanced, guaranteeing logarithmic time complexity for search, insert, and delete operations.

It is a useful data structure for implementing associative arrays, priority queues, and other dynamic sets.

## Core Properties

Red-Black Trees maintain the standard properties of a binary search tree, plus the following specific rules:

1.  **Node Color:** Every node is either red or black.
2.  **Root Property:** The root node is always black.
3.  **Leaf Property:** All leaves (NIL nodes, typically represented by `None` or a sentinel node) are considered black.
4.  **Red Node Property:** If a node is red, then both its children must be black. (Corollary: A red node cannot have a red parent).
5.  **Black-Height Property:** Every simple path from a given node to any of its descendant leaves contains the same number of black nodes. This number is called the "black-height" of the node.

These properties ensure that the longest path from the root to any leaf is no more than twice as long as the shortest path, keeping the tree balanced.

## Operations

### 1. Search

Searching is performed exactly like in a standard Binary Search Tree (BST). The colors do not affect the search logic.
*   **Time Complexity:** O(log N) due to the balanced nature.
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative.

### 2. Insertion

Insertion starts like a standard BST insertion. The new node is always added as a leaf and colored **red**. Coloring it red minimizes the chance of violating the black-height property (Rule 5).

After insertion, the tree might violate the Red Node Property (Rule 4 - a red node might now have a red parent) or the Root Property (Rule 2 - if the tree was empty and the new node is the root).

To restore the properties, a "fixup" process is applied, which involves:

*   **Recoloring:** Changing the colors of nodes (e.g., parent, grandparent, uncle).
*   **Rotations:** Restructuring the tree locally using [[../techniques/tree/tree_rotations.md]] (left and right rotations) to maintain the BST property while fixing color violations.

There are specific cases to handle during the fixup, primarily based on the color of the new node's *uncle*.

*   **Time Complexity:** O(log N). The initial BST insertion is O(log N), and the fixup involves at most two rotations and traversing up the tree (O(log N)).
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative.

### 3. Deletion

Deletion is more complex. It starts with a standard BST deletion.

*   If the node to delete has zero or one child, it's removed directly.
*   If it has two children, it's typically replaced by its inorder successor (which has at most one child), and then the successor is removed.

The complexity arises when a **black** node is removed (or replaced by a black child). Removing a black node can violate the Black-Height Property (Rule 5) and potentially the Red Node Property (Rule 4 if the node replacing the deleted one is red and its new parent is also red) or the Root Property (Rule 2).

A "fixup" process, similar to insertion but with more cases, is required. This often involves considering a node as "double-black" temporarily and propagating this status up the tree, performing recoloring and [[../techniques/tree/tree_rotations.md]] to resolve it.

*   **Time Complexity:** O(log N). BST deletion is O(log N), and the fixup involves at most three rotations and traversing up the tree (O(log N)).
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative.

## Balancing Mechanisms

### Rotations

Uses [[../techniques/tree/tree_rotations.md]] (Left and Right) in combination with recoloring during insertion and deletion fixups.

### Recoloring

Changing the colors of nodes is fundamental to maintaining the Red-Black properties, often done in conjunction with rotations.

## Complexity

| Operation | Average Case | Worst Case | Space (Worst) |
| :-------- | :----------- | :--------- | :------------ |
| Search    | O(log N)     | O(log N)   | O(log N)*     |
| Insert    | O(log N)     | O(log N)   | O(log N)*     |
| Delete    | O(log N)     | O(log N)   | O(log N)*     |

\* O(1) space if implemented iteratively.

## Use Cases & Trade-offs

Refer to [[../optimizations/tree/red_black_vs_avl.md]] for a detailed comparison.

*   **Advantages:** Guarantees logarithmic time for main operations. Generally faster insertions/deletions than AVL trees due to fewer rotations on average.
*   **Disadvantages:** More complex implementation rules than standard BSTs or AVL trees. Slightly less balanced than AVL trees in the worst case.
*   **Common Uses:** `std::map`, `std::set` in C++, `TreeMap`, `TreeSet` in Java, Completely Fair Scheduler (CFS) in Linux kernel.

## Related Concepts

*   [[binary_search_tree.md]]
*   [[avl_tree.md]]
*   [[../techniques/tree/tree_rotations.md]]
*   [[../optimizations/tree/red_black_vs_avl.md]] 