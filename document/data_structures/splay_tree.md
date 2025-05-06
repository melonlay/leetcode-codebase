# Splay Tree

**Category:** Data Structures

## Description

A Splay Tree is a self-balancing binary search tree with the additional property that recently accessed elements are quick to access again. It achieves this by performing a special "splaying" operation whenever a node is accessed (for searching, insertion, or deletion). Splaying restructures the tree by moving the accessed node to the root through a sequence of tree rotations.

Unlike AVL or Red-Black trees, Splay Trees do not use an explicit balance factor or color constraints. Instead, the splaying operation itself provides an *amortized* O(log N) time complexity for all standard BST operations.

## Core Properties

1.  **BST Property:** It maintains the standard Binary Search Tree properties.
2.  **Splaying Mechanism:** After a node `x` is accessed (searched, inserted, or involved in deletion), a sequence of specific rotation steps (zig, zig-zig, zig-zag) is applied to move `x` to the root of the tree.

## The Splay Operation

The splaying operation on node `x` consists of repeating the following steps until `x` is the root:

Let `p` be the parent of `x` and `g` be the grandparent of `x` (if it exists).

1.  **Zig Step:** If `p` is the root, perform a single rotation on the edge between `x` and `p` to make `x` the root.
    *   If `x` is the left child, perform a Right Rotation at `p`.
    *   If `x` is the right child, perform a Left Rotation at `p`.

2.  **Zig-Zig Step:** If `p` is not the root and both `x` and `p` are left children (or both are right children) of their respective parents (`g` and `p`).
    *   **Left-Left Case:** Rotate the edge between `g` and `p` first (Right Rotation at `g`), then rotate the edge between `p` and `x` (Right Rotation at `p`).
    *   **Right-Right Case:** Rotate the edge between `g` and `p` first (Left Rotation at `g`), then rotate the edge between `p` and `x` (Left Rotation at `p`).

3.  **Zig-Zag Step:** If `p` is not the root and `x` is a right child while `p` is a left child (or vice-versa).
    *   **Left-Right Case:** Rotate the edge between `p` and `x` first (Left Rotation at `p`), then rotate the edge between the new parent (`g`) and `x` (Right Rotation at `g`).
    *   **Right-Left Case:** Rotate the edge between `p` and `x` first (Right Rotation at `p`), then rotate the edge between the new parent (`g`) and `x` (Left Rotation at `g`).

These steps utilize [[../techniques/tree/tree_rotations.md]].

## Operations

*   **Search:** Perform a standard BST search for the target key. If found, splay the found node to the root. If not found, splay the *last accessed node* (the node where the search terminated) to the root.
*   **Insertion:** Insert the new node `x` using standard BST insertion. Then, splay `x` to the root.
*   **Deletion:** Search for the node `x` to delete, which splays `x` (or the last node accessed if `x` not found) to the root. If `x` was found and is now the root:
    *   Remove `x`.
    *   This splits the tree into two subtrees: L (left) and R (right).
    *   Find the maximum element (`max_L`) in the left subtree L.
    *   Splay `max_L` to the root of L.
    *   Make R the right child of the new root (`max_L`) of L.
    *   The root of L is the new root of the combined tree.

## Complexity (Amortized)

Splay trees have a remarkable property: while a single operation can take O(N) time in the worst case (e.g., accessing nodes sequentially in a skewed manner before splaying), any sequence of `M` operations on a tree starting with `N` nodes takes at most `O(M log N + N log N)` time. This means the **amortized** time complexity per operation is O(log N).

| Operation | Amortized Worst Case | Single Op Worst Case | Space (Worst) |
| :-------- | :------------------- | :------------------- | :------------ |
| Search    | O(log N)             | O(N)                 | O(N)*         |
| Insert    | O(log N)             | O(N)                 | O(N)*         |
| Delete    | O(log N)             | O(N)                 | O(N)*         |

\* O(1) space if implemented iteratively, excluding the tree structure itself.

## Use Cases & Trade-offs

*   **Advantages:**
    *   Good performance in practice due to locality of reference (recently accessed items are faster to access again).
    *   No need to store extra balance information (like height or color) per node, saving space.
    *   Relatively simpler implementation compared to AVL/RBT once the splay logic is understood.
    *   Excellent amortized guarantees.
*   **Disadvantages:**
    *   Worst-case time for a *single* operation can be O(N), which may be unsuitable for real-time applications.
    *   Frequent restructuring can make concurrent access difficult to implement efficiently.
    *   The height of the tree can become linear temporarily.
*   **Common Uses:** Caches, memory allocators, network routing, situations where temporal locality is high.

## Related Concepts

*   [[binary_search_tree.md]]
*   [[avl_tree.md]]
*   [[red_black_tree.md]]
*   [[../techniques/tree/tree_rotations.md]]
*   Amortized Analysis (concept) 