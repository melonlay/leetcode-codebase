# Blocking Flow (in Dinic's Algorithm)

**Category:** Techniques
**Sub-Category:** Graph (Max Flow)

## Description

A Blocking Flow is a flow `f` in a flow network (specifically, within the [[level_graph.md]] used in a phase of [[../../algorithms/graph/max_flow_dinic.md]]) such that every path from the source `s` to the sink `t` contains at least one *saturated* edge (an edge `(u, v)` where the flow `f(u, v)` equals its capacity `c(u, v)`).

In the context of Dinic's algorithm, finding a blocking flow refers to the process within a single phase where [[../../algorithms/graph_search/dfs.md]] is used repeatedly on the [[level_graph.md]] to find and augment flow along `s-t` paths until no more such paths exist *in that level graph*.

## Process in Dinic's Algorithm

After constructing the [[level_graph.md]] `LG` for a phase:

1.  Initialize a DFS search from source `s`.
2.  The DFS explores paths in `LG`, only moving from `u` to `v` if `level(v) = level(u) + 1`.
3.  When the DFS reaches the sink `t`, an augmenting path has been found.
4.  Calculate the bottleneck capacity of this path within `LG`.
5.  Augment flow along the path by the bottleneck capacity, updating residual capacities in `LG` (and implicitly in `Gf`). Crucially, saturated edges effectively become unusable for subsequent DFS searches *within the same phase* because their residual capacity in `LG` drops to 0.
6.  Use techniques like pointer-based DFS (where each node maintains a pointer to the next edge to explore) to avoid re-exploring edges that led to dead ends or were part of paths whose bottleneck occurred further downstream.
7.  Repeat the DFS search from `s` (potentially resuming from partially explored paths thanks to pointers) until DFS can no longer find any path from `s` to `t` in the *current state* of `LG`.
8.  The total flow pushed during this DFS process constitutes the blocking flow for that phase.

## Significance

*   **Efficiency:** Finding a blocking flow ensures that significant progress is made in each phase of Dinic's algorithm. By saturating at least one edge on every possible `s-t` path within the level graph, it guarantees that the shortest path distance `d(s, t)` will increase in the next phase.
*   **Complexity:** The process of finding a blocking flow using DFS with appropriate pointer management can be shown to take `O(V * E)` time within a single phase.

## Related Concepts

*   [[../../algorithms/graph/max_flow_dinic.md]]
*   [[level_graph.md]]
*   [[residual_graph.md]]
*   [[augmenting_path.md]]
*   [[../../algorithms/graph_search/dfs.md]] 