# Solution Explanation: 3515. Shortest Path in a Weighted Tree

## 1. Problem Summary

The problem asks us to find shortest path distances from a fixed root (node 1) to various nodes in a weighted tree. Additionally, edge weights in the tree can be updated. We need to process a series of these update and path query operations.

## 2. Approach

The core idea is to use a Depth-First Search (DFS) to flatten the tree structure and then use a Fenwick Tree (Binary Indexed Tree - BIT) to efficiently handle subtree distance updates and point distance queries.

### a. Initial Tree Processing (DFS)

A DFS traversal is performed starting from the root (node 1, internally 0-indexed) to gather essential information:

1.  **`adj` (Adjacency List):** Standard representation of the tree, storing initial edge weights.
2.  **`depth[i]`**: Stores the depth of node `i`.
3.  **`parent[i]`**: Stores the parent of node `i` in the DFS tree.
4.  **`tin[i]` and `tout[i]` (DFS Times):** 
    *   `tin[i]` is the "entry time" of node `i` in the DFS traversal.
    *   `tout[i]` is the "exit time" after visiting all nodes in the subtree of `i`.
    *   The contiguous range of time values `[tin[i], tout[i]]` corresponds to all nodes in the subtree rooted at `i` (when considering the `tin` values as indices).
5.  **`initial_distances_at_tin[t]`**: An array where `initial_distances_at_tin[t]` stores the initial shortest path weight from the root (node 0) to the node whose `tin` value is `t`.
6.  **`edge_map`**: A dictionary to store information about each edge (keyed by sorted 0-indexed node pairs):
    *   `'current_w'`: The current weight of this edge.
    *   `'child_node_for_update'`: The 0-indexed node that is the child of the other in the DFS tree. Updates to this edge's weight affect distances in this child's subtree.

### b. Fenwick Tree (BIT) for Distance Updates and Queries

A Fenwick Tree is used to efficiently manage changes to distances and query current distances. This approach is for "range add, point query" functionality.

1.  **`initial_distances_at_tin` Array**: This array (size `n`), populated during DFS, stores the baseline distances. `initial_distances_at_tin[t]` is the initial distance to the node whose `tin` is `t`.
2.  **`fenwick_tree_deltas` (BIT)**: A Fenwick tree of size `n` (to operate on `tin` values `0` to `n-1`), initialized to all zeros. This BIT stores the cumulative *deltas* (changes) that need to be applied to the initial distances.

3.  **Operations**:
    *   **Range Add on Deltas (`update(idx, val)` and `update(idx, -val)` on BIT):** 
        When the weight of an edge `(p, c)` (where `c` is child of `p`) changes, causing distances in `c`'s subtree to change by `delta_w`, this translates to adding `delta_w` to distances for nodes whose `tin` values are in the range `[L_tin, R_tin] = [tin[c], tout[c]]`.
        This is achieved on `fenwick_tree_deltas` by:
        1.  `fenwick_tree_deltas.update(L_tin, delta_w)`: Adds `delta_w` to the prefix sums from `L_tin` onwards.
        2.  `fenwick_tree_deltas.update(R_tin + 1, -delta_w)`: Cancels out the `delta_w` for prefix sums from `R_tin + 1` onwards. (Care is taken if `R_tin + 1 == n`).
        Each BIT `update` is O(log N).
    *   **Point Query for Current Distance (`query_prefix_sum(idx)` on BIT):**
        To find the current shortest distance from the root to a node `x_orig` (0-indexed `x0`): 
        Let `target_t = tin[x0]`.
        The current distance is `initial_distances_at_tin[target_t] + fenwick_tree_deltas.query_prefix_sum(target_t)`.
        The `query_prefix_sum` on BIT is O(log N).

### c. Processing Queries

1.  **Type 1 Query (Update `[1, u, v, new_w']`)**:
    1.  Convert 1-indexed `u, v` to 0-indexed `u0, v0`.
    2.  Look up the edge `(u0, v0)` in `edge_map` to get `old_w` and `child_node_for_update` (let this be `c`).
    3.  Calculate `delta = new_w - old_w`.
    4.  Update `edge_map` with `new_w`.
    5.  If `delta != 0`:
        *   `L_tin = tin[c]`, `R_tin = tout[c]`.
        *   `fenwick_tree_deltas.update(L_tin, delta)`.
        *   If `R_tin + 1 < n`, `fenwick_tree_deltas.update(R_tin + 1, -delta)`.

2.  **Type 2 Query (Path Query `[2, x]`)**:
    1.  Convert 1-indexed `x` to 0-indexed `x0`.
    2.  `target_t = tin[x0]`.
    3.  Result is `initial_distances_at_tin[target_t] + fenwick_tree_deltas.query_prefix_sum(target_t)`.

## 3. Complexity Analysis

*   **Time Complexity**:
    *   DFS: `O(N)`.
    *   Fenwick Tree Initialization: `O(N)` for `initial_distances_at_tin`, BIT is `O(N)` to init array, effectively O(1) content-wise as it starts at zeros.
    *   Each query (Type 1 or Type 2): Two BIT updates or one BIT query, so `O(log N)`.
    *   Total for `Q` queries: `O(Q log N)`.
    *   Overall: `O(N + Q log N)`. (The Fenwick Tree approach aims for better constant factors compared to a Segment Tree with lazy propagation).

*   **Space Complexity**:
    *   Adjacency list, DFS arrays: `O(N)`.
    *   `edge_map`: `O(N)`.
    *   `initial_distances_at_tin`: `O(N)`.
    *   Fenwick Tree (`bit_array`): `O(N)`.
    *   Overall: `O(N)`.

## 4. Knowledge Base References

*   The general graph traversal is based on Depth-First Search: [[document/algorithms/graph_search/dfs.md]]
*   The data structure for managing dynamic updates and queries is the Fenwick Tree (BIT), using the technique for range updates and point queries: [[document/data_structures/fenwick_tree_bit.md]] 