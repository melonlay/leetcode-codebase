# Shortest Path Faster Algorithm (SPFA)

**Category:** Algorithm (`algorithms/graph_search/`)

## Description

The Shortest Path Faster Algorithm (SPFA) is generally considered an improvement over the Bellman-Ford algorithm ([`bellman_ford.md`](./bellman_ford.md)) for finding the single-source shortest paths in a weighted directed graph. Like Bellman-Ford, it can handle **negative edge weights** and detect **negative cycles**.

It is essentially a queue-based optimization of Bellman-Ford. Instead of relaxing all edges in each iteration, SPFA maintains a queue of vertices whose distances have recently decreased and only relaxes the outgoing edges of those vertices.

## How it Works

1.  **Initialization:**
    *   Initialize distances from the source to all vertices as infinity, except the source itself (0).
    *   Create a queue (typically FIFO, like `collections.deque`) and add the source node to it.
    *   Maintain a way to track if a node is currently in the queue (e.g., a boolean array `in_queue`). Mark the source as being in the queue.
    *   (Optional but recommended for negative cycle detection): Maintain a count of how many times each node has been enqueued/relaxed (`relax_count`).

2.  **Relaxation Loop:**
    *   While the queue is not empty:
        *   Dequeue a vertex `u`.
        *   Mark `u` as *not* being in the queue (`in_queue[u] = False`).
        *   For each outgoing edge `(u, v)` with weight `w`:
            *   Perform **edge relaxation** (see [[../../techniques/graph_traversal/edge_relaxation.md]]): If `distance[u] + w < distance[v]`:
                *   Update `distance[v] = distance[u] + w`.
                *   If `v` is not currently in the queue (`!in_queue[v]`):
                    *   Enqueue `v`.
                    *   Mark `v` as being in the queue (`in_queue[v] = True`).
                    *   Increment `relax_count[v]`.
                    *   **Negative Cycle Check:** If `relax_count[v]` exceeds `|V|`, a negative cycle involving `v` has been detected. Terminate or handle as needed.

## Complexity

*   **Time Complexity:**
    *   **Average Case:** Often performs much better than Bellman-Ford, close to O(E) on random graphs and many typical inputs.
    *   **Worst Case:** O(V * E), same as Bellman-Ford. The worst case can be constructed, particularly on graphs designed to exploit the queue mechanism.
*   **Space Complexity:** O(V) for distances, queue, `in_queue` status, and relaxation counts.

## Use Cases

*   Finding single-source shortest paths in graphs with negative edge weights.
*   Faster alternative to Bellman-Ford when the graph structure is suitable (though beware the worst case).
*   Detecting negative cycles.

## Comparison

*   **vs. Bellman-Ford ([`bellman_ford.md`](./bellman_ford.md)):** Same worst-case time complexity (O(V*E)), but SPFA is often much faster in practice by avoiding redundant relaxations.
*   **vs. Dijkstra ([`dijkstra.md`](./dijkstra.md)):** Dijkstra (with binary heap O(E log V)) is generally faster on graphs with non-negative weights. SPFA handles negative weights, which Dijkstra cannot.

## Implementation Variations

*   **Queue vs. Stack (LIFO):** Using a stack instead of a queue (making it more like a DFS-based relaxation) is sometimes referred to as LIFO SPFA. This can change performance characteristics but doesn't alter the worst-case complexity.
*   **SLF (Small Label First) Optimization:** Use a deque. When enqueueing node `v`, if `distance[v]` is less than `distance[front_of_deque]`, push `v` to the front; otherwise, push to the back. This heuristic can sometimes improve performance further but also has potential worst-case scenarios.
*   **LLL (Large Label Last) Optimization:** Another heuristic involving comparing the new distance to the average distance in the queue.

*Caution:* While often fast, SPFA's O(V*E) worst case makes it unsuitable for problems where Bellman-Ford would time out and where Dijkstra isn't applicable (due to negative edges).

```python
from collections import deque

def spfa(graph, num_vertices, source):
    # graph = adjacency list {u: {v: weight, ...}, ...}
    distances = {i: float('inf') for i in range(num_vertices)}
    relax_count = {i: 0 for i in range(num_vertices)}
    in_queue = {i: False for i in range(num_vertices)}
    queue = deque()

    distances[source] = 0
    queue.append(source)
    in_queue[source] = True
    relax_count[source] = 1

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        if u not in graph: # Node might have no outgoing edges
            continue

        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    relax_count[v] += 1
                    if relax_count[v] > num_vertices:
                        print("Negative cycle detected")
                        return None # Indicate cycle

    return distances

# Example Usage (needs Adjacency List format):
# num_vertices = 5
# adj_list = {
#     0: {1: -1, 2: 4},
#     1: {2: 3, 3: 2, 4: 2},
#     # 2 has no outgoing edges
#     3: {2: 5, 1: 1},
#     4: {3: -3}
# }
# source_node = 0
# shortest_paths = spfa(adj_list, num_vertices, source_node)
# print(shortest_paths) # Output: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
``` 