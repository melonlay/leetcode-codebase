# Technique: Edge Relaxation

**Category:** Technique (`techniques/graph_traversal/`)

## Description

Edge relaxation is the fundamental operation used in many shortest path algorithms, such as Dijkstra's, Bellman-Ford, and SPFA.

It aims to improve the estimated shortest distance to a vertex `v` by considering a path through another vertex `u`.

## Core Concept

Given:
*   An edge from vertex `u` to vertex `v` with weight `w` (denoted `(u, v)` with `weight(u, v) = w`).
*   The current shortest distance estimate from the source node `s` to `u`, denoted `distance[u]`.
*   The current shortest distance estimate from the source node `s` to `v`, denoted `distance[v]`.

The relaxation step for edge `(u, v)` performs the following check and update:

```
if distance[u] + weight(u, v) < distance[v]:
    distance[v] = distance[u] + weight(u, v)
    # Optionally, update predecessor information: predecessor[v] = u
```

**In words:** If the path from the source `s` to `v` *through* `u` (`distance[u] + weight(u, v)`) is shorter than the currently known shortest path from `s` to `v` (`distance[v]`), then update `distance[v]` with this shorter path distance.

## Role in Algorithms

*   **Initialization:** Typically, `distance[source]` is initialized to 0 and all other `distance[v]` to infinity.
*   **Iteration:** Shortest path algorithms repeatedly apply the relaxation step to edges in the graph according to their specific logic (e.g., based on priority queue order in Dijkstra, or iterating through all edges in Bellman-Ford) until the shortest path estimates converge to the true shortest path distances (or a negative cycle is detected).

## Connection to Algorithms

*   **Dijkstra's Algorithm ([`../../algorithms/graph_search/dijkstra.md`](../../algorithms/graph_search/dijkstra.md)):** Relaxes outgoing edges of the vertex with the smallest current distance estimate extracted from a priority queue.
*   **Bellman-Ford Algorithm ([`../../algorithms/graph_search/bellman_ford.md`](../../algorithms/graph_search/bellman_ford.md)):** Relaxes *all* edges in the graph repeatedly (`|V|-1` times, plus one check round).
*   **SPFA ([`../../algorithms/graph_search/spfa.md`](../../algorithms/graph_search/spfa.md)):** Relaxes outgoing edges of vertices whose distances have recently been updated (managed via a queue). 