# Level Graph (for Dinic's Algorithm)

**Category:** Techniques
**Sub-Category:** Graph (Max Flow)

## Description

The Level Graph (`LG`) is a key component of [[../../algorithms/graph/max_flow_dinic.md]] (Dinic's algorithm). It is a directed acyclic graph (DAG) constructed during each phase of the algorithm based on the shortest path distances from the source `s` in the current [[residual_graph.md]] (`Gf`).

## Construction

Given a residual graph `Gf`:

1.  **Calculate Levels:** Perform a [[../../algorithms/graph_search/bfs.md]] starting from the source `s` in `Gf` to compute the shortest path distance (in terms of number of edges) `level(v)` for all reachable vertices `v`.
2.  **Filter Edges:** The Level Graph `LG` contains only the vertices reachable from `s` in `Gf`. An edge `(u, v)` from `Gf` is included in `LG` **if and only if** `level(v) == level(u) + 1`.

## Properties

*   **Subset of Residual Graph:** `LG` is a subgraph of `Gf`.
*   **DAG:** The level graph is always a Directed Acyclic Graph.
*   **Shortest Path Edges:** It only contains edges that could potentially belong to a shortest augmenting path from `s` to `t` in the current `Gf`.
*   **Phase Specific:** A new level graph is constructed at the beginning of each phase of Dinic's algorithm.

## Role in Dinic's Algorithm

The level graph serves to restrict the search space for augmenting paths within a phase:

1.  **Directed Search:** The [[../../algorithms/graph_search/dfs.md]] used in Dinic's algorithm to find augmenting paths operates *only* on the level graph `LG`.
2.  **Efficiency:** By only considering edges that advance towards the sink `t` along shortest paths (`level(v) == level(u) + 1`), the DFS avoids exploring unproductive paths, contributing to the algorithm's efficiency.
3.  **Blocking Flow:** The DFS finds a [[blocking_flow.md]] within this level graph, meaning it augments flow along paths until no more `s-t` paths exist *within that specific LG*.

## Related Concepts

*   [[../../algorithms/graph/max_flow_dinic.md]]
*   [[residual_graph.md]]
*   [[blocking_flow.md]]
*   [[../../algorithms/graph_search/bfs.md]]
*   [[../../algorithms/graph_search/dfs.md]] 