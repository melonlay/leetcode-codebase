# 3528. Unit Conversion I - Solution Explanation

## Problem Summary

Given `n` unit types (0 to n-1) and `n-1` conversions `[source, target, factor]`, we need to find the conversion factor from unit 0 to every other unit `i`. The conversions form a directed tree structure rooted at 0, meaning there's a unique path from 0 to any other unit following the conversion directions. Results should be modulo `10^9 + 7`.

## Approach: Single Pass Breadth-First Search (BFS)

The problem structure guarantees a directed tree rooted at node 0. We want to find the product of conversion factors along the unique path from the root (node 0) to every other node `i`.

This is a classic graph traversal problem solvable efficiently with BFS.

1.  **Graph Representation:** We can represent the conversions as a directed adjacency list `adj`. Since the problem guarantees the input `[u, v, factor]` represents a conversion *away* from the root 0 (meaning `u` is the parent of `v`), we can directly build this directed graph. `adj[u]` will store a list of tuples `(v, factor)`, indicating a direct conversion from `u` to `v` with the given factor.

2.  **Initialization:**
    *   Create an array `baseUnitConversion` of size `n`, initialized with `-1` to mark nodes as unvisited/uncalculated.
    *   Set `baseUnitConversion[0] = 1`, as 1 unit of type 0 is equivalent to 1 unit of type 0.
    *   Initialize a queue `q` for BFS and add the starting node `0`.

3.  **BFS Traversal and Calculation:**
    *   While the queue is not empty:
        *   Dequeue the current node `u`.
        *   Retrieve the already calculated conversion factor for `u`: `factor_u = baseUnitConversion[u]`.
        *   Iterate through all neighbors `(v, factor_uv)` of `u` in the adjacency list `adj[u]`.
        *   For each neighbor `v`:
            *   Check if `v` has already been visited/calculated (`baseUnitConversion[v] != -1`). If it has, we skip it (due to the tree structure, we only care about the first time we reach a node via the unique path from the root).
            *   If `baseUnitConversion[v] == -1`:
                *   Calculate the conversion factor for `v`: `factor_v = (factor_u * factor_uv) % MOD`.
                *   Store this factor: `baseUnitConversion[v] = factor_v`.
                *   Enqueue `v` to process its neighbors later.

4.  **Result:** After the BFS completes, the `baseUnitConversion` array will contain the required conversion factors for all units from 0 to `n-1`.

## Complexity Analysis

*   **Time Complexity:** `O(N + E)`, where `N` is the number of units (`n`) and `E` is the number of conversions (`n-1`). Building the adjacency list takes `O(E) = O(n)`. The BFS visits each node and edge exactly once, taking `O(N + E) = O(n)`. Therefore, the total time complexity is **O(n)**.
*   **Space Complexity:** `O(N + E) = O(n)`. We store the adjacency list `adj` which takes `O(E) = O(n)` space. The `baseUnitConversion` array takes `O(N)` space. The queue `q` can hold up to `O(N)` nodes in the worst case (for a wide tree). Therefore, the total space complexity is **O(n)**.

## Foundational Concepts

*   Graph Traversal: [[../../document/algorithms/graph_search/bfs.md]]
*   Adjacency List
*   Modulo Arithmetic
