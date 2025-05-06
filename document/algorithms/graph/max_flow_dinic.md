# Dinic's Algorithm for Maximum Flow

**Category:** Algorithms
**Sub-Category:** Graph (Max Flow)

## Description

Dinic's algorithm is an efficient algorithm for computing the maximum flow in a flow network. It improves upon [[max_flow_edmonds_karp.md]] by finding multiple augmenting paths in each "phase." It achieves this by constructing a [[../techniques/graph/level_graph.md]] using [[../graph_search/bfs.md]] and then finding a [[../techniques/graph/blocking_flow.md]] within that level graph using [[../graph_search/dfs.md]].

## Algorithm Steps

1.  Initialize flow `f(u, v) = 0` for all edges.
2.  **While** a path from `s` to `t` exists in the current [[../techniques/graph/residual_graph.md]] `Gf`:
    a.  **Build Level Graph:** Construct the [[../techniques/graph/level_graph.md]] `LG` from `Gf` using BFS starting at `s`. If `t` is not reachable from `s` in `Gf` (i.e., `level(t)` is infinite), terminate the algorithm.
    b.  **Find Blocking Flow:** While an augmenting path from `s` to `t` can be found in the *current level graph* `LG` using DFS:
        i.  Perform DFS from `s` following edges `(u, v)` only if `level(v) = level(u) + 1`.
        ii. When a path to `t` is found, calculate its bottleneck capacity `cf(p)` in `LG`.
        iii. Augment flow by `cf(p)` along this path (updating `f` in the original network and residual capacities in `Gf` and `LG`).
        iv. Prune saturated edges or edges leading to dead ends from the DFS search within this phase (often using edge pointers).
    c.  (End of Phase: No more `s-t` paths exist in the current `LG`). Go back to step 2a to rebuild the level graph based on the updated `Gf`.
3.  Return the total computed flow.

## Complexity

*   **Time Complexity:** `O(V^2 * E)` in general graphs.
    *   Building the level graph (BFS): `O(E)` per phase.
    *   Finding the blocking flow (DFS with pruning): `O(V * E)` per phase.
    *   Number of phases: At most `V - 1`, because the shortest path distance `d(s, t)` strictly increases after each phase (see [[../../optimizations/graph/max_flow_dinic_complexity_proof.md]]).
    *   Total: `O(V) * (O(E) + O(VE)) = O(V^2 * E)`.
*   **Unit Capacity Networks:** The complexity improves to `O(min(V^(2/3), E^(1/2)) * E)`. For simple graphs (like bipartite matching), it becomes `O(E * sqrt(V))`.
*   **Space Complexity:** `O(V + E)` for graph representation, BFS/DFS data structures.

## Properties

*   **Efficient:** Significantly faster than Edmonds-Karp for many graphs.
*   **Phased Approach:** Groups augmentations based on shortest path lengths.
*   **Implementation:** More complex than Edmonds-Karp due to level graph construction and the pointer-based DFS for blocking flow.

## Related Concepts

*   [[max_flow_ford_fulkerson.md]]
*   [[max_flow_edmonds_karp.md]]
*   [[../techniques/graph/residual_graph.md]]
*   [[../techniques/graph/augmenting_path.md]]
*   [[../techniques/graph/level_graph.md]]
*   [[../techniques/graph/blocking_flow.md]]
*   [[../graph_search/bfs.md]]
*   [[../graph_search/dfs.md]]
*   [[../../optimizations/graph/max_flow_dinic_complexity_proof.md]]
*   Unit Capacity Graphs (Concept) 