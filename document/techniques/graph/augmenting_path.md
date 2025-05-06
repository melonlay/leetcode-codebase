# Augmenting Path

**Category:** Techniques
**Sub-Category:** Graph (Max Flow)

## Description

An Augmenting Path, in the context of maximum flow algorithms, is a path from the source `s` to the sink `t` in the [[residual_graph.md]] (`Gf`) consisting entirely of edges with positive residual capacity (`cf(u, v) > 0`).

The existence of an augmenting path indicates that the current flow `f` in the original network `G` is not maximal, and more flow can be pushed from `s` to `t`.

## Properties

*   **Path in Residual Graph:** An augmenting path exists in `Gf`, not necessarily in the original graph `G`.
*   **Positive Capacity:** Every edge along the path must have `cf(u, v) > 0`.
*   **Flow Increase:** Finding an augmenting path allows the total flow value from `s` to `t` to be increased.
*   **Composition:** The path can consist of both forward edges (representing unused capacity in `G`) and backward edges (representing flow that can be pushed back in `G`).

## Role in Max Flow Algorithms

*   **Ford-Fulkerson Method:** This general method iteratively finds *any* augmenting path in the residual graph, calculates its bottleneck capacity (the minimum residual capacity along the path), and increases the flow along this path by the bottleneck amount. The process repeats until no more augmenting paths can be found.
*   **Edmonds-Karp Algorithm:** A specific implementation of Ford-Fulkerson that uses [[../../algorithms/graph_search/bfs.md]] (Breadth-First Search) to find the *shortest* augmenting path (in terms of number of edges) in each iteration. This strategy is crucial for its polynomial time complexity proof.
*   **Dinic's Algorithm:** Uses BFS to build a layered network based on shortest path distances and then finds multiple augmenting paths within this layered network using DFS in each phase.

## Max-Flow Min-Cut Theorem Connection

The Ford-Fulkerson method terminates when no more augmenting paths can be found from `s` to `t` in the residual graph. According to the Max-Flow Min-Cut theorem, the maximum flow value in a network is equal to the minimum capacity of an s-t cut. The absence of an augmenting path implies that the current flow achieves this maximum value and corresponds to a minimum cut.

## Related Concepts

*   [[residual_graph.md]]
*   [[../../algorithms/graph/max_flow_ford_fulkerson.md]]
*   [[../../algorithms/graph/max_flow_edmonds_karp.md]]
*   [[../../algorithms/graph/max_flow_dinic.md]]
*   [[../../algorithms/graph_search/bfs.md]]
*   [[../../algorithms/graph_search/dfs.md]]
*   Max-Flow Min-Cut Theorem (Concept) 