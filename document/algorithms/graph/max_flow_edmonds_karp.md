# Edmonds-Karp Algorithm for Maximum Flow

**Category:** Algorithms
**Sub-Category:** Graph (Max Flow)

## Description

The Edmonds-Karp algorithm is a specific implementation of the [[max_flow_ford_fulkerson.md]] method for finding the maximum flow in a network. Its key characteristic is that it uses [[../graph_search/bfs.md]] (Breadth-First Search) to find the [[../techniques/graph/augmenting_path.md]] with the *fewest number of edges* (shortest path) in the [[../techniques/graph/residual_graph.md]] (`Gf`) during each iteration.

This specific choice of using BFS guarantees a polynomial time complexity, unlike the general Ford-Fulkerson method which can be exponential or non-terminating depending on path selection.

## Algorithm Steps

The steps are identical to Ford-Fulkerson, with the crucial difference in Step 2:

1.  Initialize flow `f(u, v) = 0` for all edges `(u, v)`.
2.  **While** there exists an augmenting path `p` from `s` to `t` in the residual graph `Gf` **found using BFS (shortest path in terms of number of edges)**:
    a.  Calculate the bottleneck capacity `cf(p) = min{cf(u, v) | (u, v) is in p}`.
    b.  Augment flow along `p` by `cf(p)` (update `f` for original edges corresponding to `p`'s forward and backward edges).
    c.  Update the residual graph `Gf` based on the new flow `f`.
3.  Return the total flow.

## Complexity

*   **Time Complexity:** `O(V * E^2)`
    *   Finding the shortest augmenting path using BFS takes `O(E)` time (since the residual graph has O(E) edges).
    *   The number of augmentations is proven to be at most `O(V * E)`. The core idea of the proof (detailed in [[../../optimizations/graph/max_flow_ek_complexity_proof.md]]) relies on showing that the shortest path distance from `s` to any node `v`, `d(s, v)`, is non-decreasing, and each time an edge `(u, v)` becomes saturated, `d(s, u)` must increase by at least 2 before `(u, v)` can be saturated again. Since distances are bounded by `V`, each edge is saturated O(V) times, leading to O(V*E) total saturations/augmentations.
    *   Total Time = `O(V * E)` augmentations * `O(E)` time/augmentation = `O(V * E^2)`.
*   **Space Complexity:** `O(V + E)` for graph representation (adjacency list) and BFS queue/visited arrays.

## Properties

*   **Polynomial Time:** Guarantees termination in polynomial time.
*   **Simplicity:** Relatively simple to implement compared to more advanced max-flow algorithms like Dinic's.
*   **Not the Fastest:** While polynomial, `O(V * E^2)` is often too slow for large graphs compared to algorithms like [[max_flow_dinic.md]] (`O(V^2 * E)` or better).

## Related Concepts

*   [[max_flow_ford_fulkerson.md]]
*   [[../techniques/graph/residual_graph.md]]
*   [[../techniques/graph/augmenting_path.md]]
*   [[../graph_search/bfs.md]]
*   [[max_flow_dinic.md]]
*   [[../../optimizations/graph/max_flow_ek_complexity_proof.md]] 