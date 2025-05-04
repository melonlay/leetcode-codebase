# Technique: DFS on Derived Tree for Path Queries

## 1. Description

This technique tackles path query problems (e.g., shortest path, distance) on certain types of implicit graphs, particularly those where nodes correspond to elements in a **sorted sequence**, and connectivity is defined by proximity or relative constraints.

Instead of building the full potentially dense implicit graph and running standard algorithms like BFS (which can be too slow), this approach transforms the problem by constructing an explicit **derived tree or forest structure**. Queries are then answered efficiently by performing a Depth-First Search (DFS) on this derived structure.

See also: [[../../patterns/graph/implicit_graph_to_tree_transformation.md]]

## 2. Core Idea

1.  **Sort Data:** The underlying data (nodes) must typically be processable in sorted order.
2.  **Define Parent/Child Relationship:** Based on the problem's connectivity rules, define a directed edge relationship for each node `i` pointing *from* a specific "parent" `p` *to* `i`. This parent `p` is often chosen based on a rule related to the sorted sequence (e.g., the leftmost/rightmost node satisfying a constraint, the nearest neighbor meeting a condition).
3.  **Build Derived Tree/Forest:** Construct the explicit adjacency list (`conn`) representing these directed parent-to-child edges. This often forms a forest (a collection of trees).
4.  **Offline Query Processing:** Group queries `(u, v)` by one of their endpoints (e.g., group by `v`).
5.  **DFS Traversal:** Perform a DFS traversal on the derived forest.
6.  **Maintain Path History:** During DFS, maintain the current path from the root of the tree being traversed (e.g., in a list `path`).
7.  **Answer Queries:** When the DFS visits a node `v`, process all queries `(u, v)` grouped with `v`. Use the `path` history (often with binary search like `bisect`) to efficiently find the distance or relationship between `u` and `v` *within the derived tree*. Check if `u` is actually part of the same tree/component traversed so far.

## 3. Generic Algorithm Steps

1.  **Sort & Index:** Sort original data, map original indices to sorted indices (`pos`). Update queries to use sorted indices.
2.  **Calculate "Parent" Pointers:** For each node `i` (in sorted order), calculate the index `p` of its designated "parent" based on the specific problem's rule (e.g., using two pointers, binary search). Store this in an array `parent_ptr`.
    *   Example (Leftmost Pointer): See [[../sequence/find_boundary_pointer_sorted_constraint.md]].
3.  **Build Connectivity Forest `conn`:** Create adjacency lists `conn` where `conn[p].append(i)` if `parent_ptr[i] == p`.
4.  **Group Queries (`qMap`):** Group queries `(u, v, query_idx)` by endpoint `v` -> `qMap[v] = [(u, query_idx), ...]`. Use sorted indices.
5.  **DFS Traversal & Query Answering:**
    *   Initialize `ans`, `path`.
    *   Find roots of the forest (nodes `r` where `parent_ptr[r]` points to itself or satisfies a root condition).
    *   For each root `r`, call `dfs(r)`.
    *   **`dfs(node)` function:**
        *   Add `node` to `path`.
        *   For each query `(u, query_idx)` in `qMap[node]`:
            *   Check if `u` is an ancestor in the current `path` (e.g., `u >= path[0]` if roots are minimal indices).
            *   If connected, calculate distance using `path` and `bisect` (e.g., `len(path) - bisect.bisect_right(path, u)`).
            *   Store result in `ans[query_idx]`.
        *   Recursively call `dfs` for children `c` in `conn[node]`.
        *   Remove `node` from `path` (backtrack).
6.  **Return `ans`.**

## 4. Correctness Assumption

The crucial assumption is that paths (and therefore distances) in the *derived tree structure* accurately reflect the desired paths (e.g., shortest paths) in the *original implicit graph* for the specific problem type. This often holds for graphs derived from sorted data with proximity constraints but needs careful justification for each specific problem.
*   See: [[../../common_mistakes/graph/incorrect_shortest_path_assumption_on_derived_tree.md]]

## 5. Complexity

Depends on the parent pointer calculation and query processing:
*   **Time:** Often O(N log N + P + Q log N), where N is number of nodes, P is parent calculation time (e.g., O(N) or O(N log N)), Q is number of queries. Sorting is O(N log N), DFS is O(N+Edges)=O(N) (since it's a tree/forest), query processing is O(Q log N).
*   **Space:** O(N + Q) for storing pointers, connections, query map, DFS path/stack, and answers.

## 6. Related Concepts

*   [[../../patterns/graph/implicit_graph_to_tree_transformation.md]] (Overall pattern)
*   [[../../algorithms/graph_search/dfs.md]] (Core traversal algorithm)
*   [[../../algorithms/searching/binary_search.md]] (`bisect` module for path querying)
*   Techniques for parent calculation (e.g., [[../sequence/find_boundary_pointer_sorted_constraint.md]], [[../sequence/find_reach_bounds_sorted_constraint.md]])
*   Offline Query Processing
*   Implicit Graphs
*   [[../binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]] (Alternative approach for some similar problems)
*   [[../../optimizations/graph_shortest_path/path_query_sorted_value_diff_graph.md]] (Comparison of approaches for LC3534) 