# Optimization Comparison: Path Query Strategies for Sorted Value Difference Graphs

## Problem Context

This comparison addresses problems like LeetCode 3534 ("Path Existence Queries in a Graph II"), where we need to answer shortest path (in terms of edges) queries `(u, v)` on an implicit graph.

The graph's nodes correspond to elements in an array `nums`. An edge exists between nodes `i` and `j` if `|nums[i] - nums[j]| <= maxDiff`.

Direct BFS is often too slow due to the potentially dense nature of the implicit graph.

## Strategies Compared

1.  **Binary Lifting on Precomputed Ranges:**
    *   **Technique:** [[../techniques/binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]]
    *   **Core Idea:** Sort `nums`. Precompute the farthest right (`fr`) and farthest left (`fl`) reachable index for each node `i` in a single step (using [[../techniques/sequence/find_reach_bounds_sorted_constraint.md]]). Build binary lifting tables (`nxt`, `prv`) based on `fr`/`fl`. Query the minimum steps between `s` and `t` using these tables.
    *   **Time:** O(N log N + Q log N) (O(N log N) for sorting and table build, O(log N) per query).
    *   **Space:** O(N log N) for the `nxt` and `prv` tables.

2.  **DFS on Derived Leftmost-Pointer Tree:**
    *   **Technique:** [[../techniques/graph_traversal/dfs_derived_tree_path_query.md]]
    *   **Core Idea:** Sort `nums`. Compute the *leftmost* reachable index `prv[i]` for each `i` (using [[../techniques/sequence/find_boundary_pointer_sorted_constraint.md]]). Build a directed forest based on reversed `prv` pointers (`p -> i`). Perform DFS on this forest, answering queries offline using `bisect` on the DFS path.
    *   **Time:** O(N log N + Q log N) (O(N log N) for sorting, O(N) for `prv` and forest build, O(N + Q log N) for DFS + queries).
    *   **Space:** O(N + Q) for storing sorted data map, `prv`, connectivity, query map, DFS stack/path, and answers.

## Trade-offs & Recommendation

| Feature         | Binary Lifting                                   | DFS on Derived Tree                               |
| :-------------- | :----------------------------------------------- | :------------------------------------------------ |
| **Time**        | O(N log N + Q log N)                             | O(N log N + Q log N)                              |
| **Space**       | **O(N log N)**                                   | **O(N + Q)**                                      |
| Implementation  | Table building and query logic can be complex.   | Requires multiple steps (sort, prv, conn, DFS).   |
| Correctness     | Relies on binary lifting logic.                  | Relies on assumption that derived tree path = shortest path. See [[../common_mistakes/graph/incorrect_shortest_path_assumption_on_derived_tree.md]]. |
| Online Queries  | Supports online queries.                         | Requires offline query processing (grouping).     |

**Recommendation:**

*   For competitive programming scenarios where space is often constrained, the **DFS on Derived Tree** approach is generally preferred due to its significantly better **O(N + Q)** space complexity compared to O(N log N) for Binary Lifting.
*   If online query processing is strictly required, Binary Lifting might be necessary despite its higher space usage.

Both approaches offer the same optimal time complexity for this specific problem type.

## Related Concepts

*   [[../patterns/graph/implicit_graph_to_tree_transformation.md]]
*   [[../algorithms/graph_search/dfs.md]]
*   [[../techniques/binary_lifting/binary_lifting.md]]
*   [[../algorithms/searching/binary_search.md]] (`bisect`)
*   Sorting
*   Offline Query Processing 