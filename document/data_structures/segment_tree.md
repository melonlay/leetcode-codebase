# Data Structure: Segment Tree

## 1. Description

A Segment Tree is a versatile tree-based data structure primarily used for efficiently querying aggregate values over intervals (ranges) of an array and supporting updates to individual elements or ranges.

It's particularly useful when dealing with problems requiring frequent range queries (like sum, minimum, maximum, GCD) and point/range updates on a static or dynamic array.

## 2. Core Concepts

*   **Tree Structure:** It's a binary tree where each node represents an interval (segment) of the original array.
    *   The **root** represents the entire array interval (e.g., `[0, n-1]`).
    *   Each **internal node** represents the union of its children's intervals. If a node represents `[L, R]`, its left child typically represents `[L, mid]` and its right child `[mid+1, R]`, where `mid = (L+R)//2`.
    *   **Leaf nodes** represent individual elements of the array (intervals of length 1, e.g., `[i, i]`).
*   **Node Value:** Each node stores an aggregate value (e.g., sum, max) computed from the interval it represents. This value is derived from its children's values.
*   **Height:** A segment tree built on an array of size `n` has a height of O(log n).
*   **Size:** Requires approximately `4n` space in common array-based implementations to avoid index calculation complexities.

## 3. Common Operations

Let `n` be the size of the original array.

*   **Build:** Constructs the segment tree from the initial array.
    *   Complexity: O(n)
    *   Recursively builds the tree bottom-up from the leaves.
*   **Point Update:** Updates the value of a single element in the array and propagates the change up the tree to affected ancestor nodes.
    *   Complexity: O(log n)
    *   Recursively finds the leaf node corresponding to the element and updates values along the path back to the root.
*   **Range Query:** Queries an aggregate value over a specified range `[queryL, queryR]`.
    *   Complexity: O(log n)
    *   Recursively traverses the tree. If a node's interval is fully contained within the query range, its precomputed value is used. If it partially overlaps, the query continues recursively into the relevant children. If it doesn't overlap, it contributes a neutral value (e.g., 0 for sum, infinity for min).
*   **Range Update (with Lazy Propagation):** Updates all elements within a specified range `[updateL, updateR]` with a certain value or operation (e.g., add `x` to all elements, set all elements to `x`).
    *   Complexity: O(log n)
    *   Uses **Lazy Propagation:** Instead of updating all `k` elements in the range individually (which would be O(k log n) or worse), updates are applied to higher-level nodes covering the range. A `lazy` array stores pending updates. These updates are only propagated down to children nodes when those children are explicitly visited during subsequent queries or updates.

## 4. Implementation Notes (Array-Based)

*   Often implemented using an array `tree` of size ~`4n`.
*   Root is at index 1 (or 0, adjust formulas).
*   If node is at index `idx`:
    *   Left child: `2 * idx`
    *   Right child: `2 * idx + 1`
*   Helper functions (`build`, `query`, `update`) are typically recursive.
*   Lazy propagation requires an additional `lazy` array of the same size as `tree`.

## 5. Use Cases

*   Range Sum Queries (RSQ)
*   Range Minimum/Maximum Queries (RMQ)
*   Range Frequency Queries
*   Problems involving dynamic intervals where updates and range aggregates are needed.
*   Geometry problems (often after Coordinate Compression).
*   Finding the maximum height profile (Skyline problem - used in one optimized approach).

## 6. Complexity Summary

*   **Build:** O(n)
*   **Point Update:** O(log n)
*   **Range Query:** O(log n)
*   **Range Update (Lazy):** O(log n)
*   **Space:** O(n)

## 7. Lazy Propagation Details

*   When performing a range update `[L, R]`:
    *   If the current node's range is fully contained within `[L, R]`, apply the update to this node and mark it as `lazy` (store the pending update value).
    *   If partially overlapping, first **push down** any existing lazy updates from the current node to its children, then recurse into relevant children.
*   When querying or traversing through a node:
    *   Always **push down** any lazy update from the current node to its children *before* processing the children or returning the node's value.
*   Pushing down involves applying the parent's lazy update to the children's values and marking the children as lazy.

## 8. Related Concepts

*   Binary Indexed Tree (Fenwick Tree): More space-efficient (O(n)) but less versatile (primarily for point updates and prefix queries).
*   [[../../techniques/coordinate_compression.md]]
*   Divide and Conquer
*   Recursion 