# AVL Tree

**Category:** Data Structures

## Description

An AVL Tree (named after its inventors Adelson-Velsky and Landis) is a self-balancing binary search tree. It was the first such data structure to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done using tree rotations.

This strict balancing ensures that the tree's height remains logarithmic with respect to the number of nodes, guaranteeing O(log N) worst-case performance for search, insertion, and deletion.

## Core Properties

1.  **BST Property:** It maintains the standard Binary Search Tree properties (left child < parent < right child).
2.  **Balance Factor Property:** For every node in the tree, the **balance factor**, defined as `height(right subtree) - height(left subtree)`, must be in the range `[-1, 0, 1]`. A node with a balance factor outside this range is considered unbalanced.

## Operations

### 1. Search

Searching is performed exactly like in a standard Binary Search Tree (BST).
*   **Time Complexity:** O(log N) due to the strictly balanced height.
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative.

### 2. Insertion

Insertion starts like a standard BST insertion. After inserting the new node, traverse back up the tree from the new node's parent to the root, updating heights and checking balance factors.

If an unbalanced node is found (balance factor becomes -2 or +2), perform the appropriate single or double rotation to restore the balance.

*   **Single Rotations:** Used when the imbalance is caused by an insertion into the "outer" subtree (left-left or right-right case).
    *   Left-Left imbalance: Requires a single Right Rotation.
    *   Right-Right imbalance: Requires a single Left Rotation.
*   **Double Rotations:** Used when the imbalance is caused by an insertion into the "inner" subtree (left-right or right-left case).
    *   Left-Right imbalance: Requires a Left Rotation followed by a Right Rotation.
    *   Right-Left imbalance: Requires a Right Rotation followed by a Left Rotation.

Only one rotation (single or double) is needed per insertion to restore balance for the entire tree.

*   **Time Complexity:** O(log N). BST insertion is O(log N), height updates and checks are O(log N), and rotations are O(1).
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative (if height management allows).

### 3. Deletion

Deletion starts like a standard BST deletion. After removing the node (or its successor/predecessor), traverse back up the tree from the parent of the removed node to the root, updating heights and checking balance factors.

If an unbalanced node is found, perform the appropriate rotation(s). Unlike insertion, deletion might require multiple rotations (up to O(log N)) along the path to the root to restore balance throughout the tree.

*   **Time Complexity:** O(log N). BST deletion is O(log N), updates and checks are O(log N), and rotations take O(log N) in total worst-case for deletion.
*   **Space Complexity:** O(log N) for recursion stack, O(1) for iterative.

## Balancing Mechanisms

AVL trees rely solely on [[../techniques/tree/tree_rotations.md]] (Left, Right, and combinations forming double rotations) to maintain the balance factor property.

## Complexity

| Operation | Average Case | Worst Case | Space (Worst) |
| :-------- | :----------- | :--------- | :------------ |
| Search    | O(log N)     | O(log N)   | O(log N)*     |
| Insert    | O(log N)     | O(log N)   | O(log N)*     |
| Delete    | O(log N)     | O(log N)   | O(log N)*     |

\* O(1) space if implemented iteratively.

## Use Cases & Trade-offs

*   **Advantages:** Stricter balance guarantees faster lookups compared to Red-Black Trees in theory (due to potentially smaller height). Conceptually simpler balancing rules than Red-Black Trees (only balance factor).
*   **Disadvantages:** Insertions and deletions can be slower than Red-Black Trees due to the higher frequency of rotations required to maintain the strict balance. Implementation requires storing and updating heights or balance factors.
*   **Common Uses:** Situations where lookups are the dominant operation and insertion/deletion frequency is lower, or where strict height balance is critical.

## Related Concepts

*   [[binary_search_tree.md]]
*   [[red_black_tree.md]]
*   [[splay_tree.md]]
*   [[../techniques/tree/tree_rotations.md]]
*   [[../optimizations/tree/red_black_vs_avl.md]] 