# Ford-Fulkerson Method for Maximum Flow

**Category:** Algorithms
**Sub-Category:** Graph (Max Flow)

## Description

The Ford-Fulkerson method is a general greedy approach for computing the maximum flow in a flow network `G = (V, E)` from a source `s` to a sink `t`. It works by iteratively finding an [[../techniques/graph/augmenting_path.md]] (a path from `s` to `t` with available capacity) in the [[../techniques/graph/residual_graph.md]] (`Gf`) and increasing the flow along that path.

The method continues until no more augmenting paths can be found in the residual graph.

## Algorithm Steps

1.  Initialize the flow `f(u, v) = 0` for all edges `(u, v)` in `E`.
2.  While there exists an augmenting path `p` from `s` to `t` in the residual graph `Gf`:
    a.  Calculate the bottleneck capacity `cf(p)` of the path `p`: `cf(p) = min{cf(u, v) | (u, v) is in p}`.
    b.  For each edge `(u, v)` in the augmenting path `p`:
        i.  **If `(u, v)` is a forward edge in `Gf` (corresponding to `(u, v)` in `G`):** Increase the flow in the original edge: `f(u, v) = f(u, v) + cf(p)`.
        ii. **If `(u, v)` is a backward edge in `Gf` (corresponding to `(v, u)` in `G`):** Decrease the flow in the original edge: `f(v, u) = f(v, u) - cf(p)`.
    c.  Update the residual graph `Gf` based on the new flow `f`.
3.  Return the total flow (calculated as the net flow out of the source `s` or into the sink `t`).

## Properties

*   **Greedy:** At each step, it increases the flow along *some* available path.
*   **Correctness:** Guaranteed to terminate with the maximum flow value due to the Max-Flow Min-Cut Theorem. When no augmenting path exists, the current flow represents a maximum flow, and a corresponding minimum cut can be identified.
*   **Integer Capacities:** If all edge capacities are integers, the algorithm terminates, and the resulting maximum flow value will also be an integer.

## Complexity

*   **Time Complexity:** The time complexity depends heavily on *how* the augmenting path is chosen in step 2.
    *   If paths are chosen arbitrarily (e.g., using DFS), the complexity can be poor, potentially `O(F * E)` where `F` is the maximum flow value. If `F` is very large, this can be pseudo-polynomial or even non-terminating for irrational capacities.
    *   [[max_flow_edmonds_karp.md]] (using BFS to find the shortest path) guarantees `O(V * E^2)`.
    *   [[max_flow_dinic.md]] (using blocking flows) achieves `O(V^2 * E)` or better for unit capacity graphs.
*   **Space Complexity:** Depends on the graph representation and path-finding algorithm. Typically O(V + E) for adjacency lists and BFS/DFS.

## Implementations / Variants

The Ford-Fulkerson *method* is a template. Specific *algorithms* arise from different ways of finding the augmenting path:

*   [[max_flow_edmonds_karp.md]]: Uses BFS.
*   [[max_flow_dinic.md]]: Uses BFS + DFS on a layered graph.
*   Capacity Scaling: Chooses paths based on capacity constraints.

## Related Concepts

*   [[../techniques/graph/residual_graph.md]]
*   [[../techniques/graph/augmenting_path.md]]
*   Max-Flow Min-Cut Theorem (Concept)
*   Flow Network (Concept)
*   [[max_flow_edmonds_karp.md]]
*   [[max_flow_dinic.md]]
*   [[../graph_search/bfs.md]]
*   [[../graph_search/dfs.md]] 