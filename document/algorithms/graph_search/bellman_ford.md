# Bellman-Ford Algorithm

**Category:** Algorithm (`algorithms/graph_search/`)

## Description

The Bellman-Ford algorithm computes shortest paths from a single source vertex to all other vertices in a weighted graph. Unlike Dijkstra's algorithm ([`dijkstra.md`](./dijkstra.md)), it can handle graphs with **negative edge weights**.

It can also detect negative cycles reachable from the source node.

## How it Works

1.  **Initialization:**
    *   Initialize distances from the source to all vertices as infinity, except the source itself, which is 0.
    *   `distance[source] = 0`
    *   `distance[v] = infinity` for all other vertices `v`.

2.  **Relaxation Rounds:**
    *   Repeat `|V| - 1` times (where `|V|` is the number of vertices):
        *   For each edge `(u, v)` with weight `w` in the graph:
            *   Perform **edge relaxation** (see [[../../techniques/graph_traversal/edge_relaxation.md]]): If `distance[u] + w < distance[v]`, then update `distance[v] = distance[u] + w`.

3.  **Negative Cycle Detection:**
    *   After `|V| - 1` rounds, perform one *additional* round of relaxation for all edges `(u, v)`:
        *   If any `distance[v]` can still be decreased (i.e., if `distance[u] + w < distance[v]` for any edge), it means there is a negative cycle reachable from the source. The shortest path is undefined in this case (or can be considered negative infinity for nodes affected by the cycle).

## Why |V| - 1 Rounds?

*   The shortest path in a graph with no negative cycles can have at most `|V| - 1` edges.
*   In each round `k`, Bellman-Ford finds the shortest paths that use at most `k` edges.
*   Therefore, after `|V| - 1` rounds, it guarantees finding the shortest paths if no negative cycles exist.

## Complexity

*   **Time Complexity:** O(V * E), where `V` is the number of vertices and `E` is the number of edges. This is because it iterates through all edges `V` times (V-1 rounds + 1 check round).
*   **Space Complexity:** O(V) to store the distances.

## Use Cases

*   Finding shortest paths in graphs with negative edge weights (but no negative cycles reachable from the source if a finite shortest path is desired).
*   Detecting negative cycles reachable from a source node.
*   Routing protocols (like RIP - Routing Information Protocol).

## Comparison

*   **vs. Dijkstra:** Bellman-Ford is slower (O(V*E) vs O(E log V)) but handles negative edges. Dijkstra cannot.
*   **vs. SPFA ([`spfa.md`](./spfa.md)):** SPFA is often faster in practice on many graphs (average case closer to O(E)), but its worst-case complexity is also O(V*E). SPFA is generally an optimization of Bellman-Ford.
*   **vs. Floyd-Warshall:** Floyd-Warshall finds all-pairs shortest paths in O(V^3) and handles negative edges (detects negative cycles anywhere). Bellman-Ford is single-source.

## Implementation Notes

```python
def bellman_ford(graph, num_vertices, source):
    # graph should be a list of edges: [(u, v, weight), ...]
    distances = {i: float('inf') for i in range(num_vertices)}
    distances[source] = 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        # Optimization: If no distances updated in a round, can stop early
        if not updated:
            break

    # Step 3: Check for negative cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative cycle reachable from the source")
            # Optionally, mark affected nodes or return an indicator
            # To find nodes affected by cycle, can run further relaxation or DFS/BFS
            return None # Indicate cycle

    return distances

# Example Usage:
# num_vertices = 5
# graph_edges = [
#     (0, 1, -1),
#     (0, 2, 4),
#     (1, 2, 3),
#     (1, 3, 2),
#     (1, 4, 2),
#     (3, 2, 5),
#     (3, 1, 1),
#     (4, 3, -3)
# ]
# source_node = 0
# shortest_paths = bellman_ford(graph_edges, num_vertices, source_node)
# print(shortest_paths) # Output: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
``` 