# Dijkstra's Algorithm

**Category:** Algorithm (`algorithms/graph_search/`)

## Description

Dijkstra's algorithm finds the shortest paths from a single source node to all other nodes in a graph with **non-negative** edge weights. It is a greedy algorithm that maintains a set of nodes for which the shortest path from the source is known and iteratively expands this set.

## How it Works

1.  **Initialization:**
    *   Initialize distances to all nodes as infinity, except for the source node, which has a distance of 0.
    *   Use a priority queue (min-heap) to store `(distance, node)` pairs, initially containing `(0, source_node)`. The priority queue orders nodes by their current known shortest distance from the source.
    *   Optionally, maintain a set or boolean array to track visited nodes (nodes for which the final shortest path has been determined).

2.  **Main Loop:**
    *   While the priority queue is not empty:
        *   Extract the node `u` with the smallest distance from the priority queue.
        *   If `u` has already been visited (its shortest path is finalized), continue.
        *   Mark `u` as visited.
        *   For each neighbor `v` of `u`:
            *   Calculate the tentative distance from the source to `v` through `u`: `distance[u] + weight(u, v)`.
            *   **Relaxation:** If this tentative distance is shorter than the current `distance[v]`:
                *   Update `distance[v]` to the new shorter distance.
                *   Add `(distance[v], v)` to the priority queue. (Note: The priority queue might now contain multiple entries for `v` with different distances; the algorithm correctly handles this by always processing the entry with the minimum distance first).

3.  **Termination:** The loop terminates when the priority queue is empty, meaning all reachable nodes have been visited. The `distance` array now holds the shortest path distances from the source node.

## Data Structures

*   **Graph Representation:** Typically an adjacency list (`Dict[Node, List[Tuple[Node, Weight]]]`) is efficient.
*   **Priority Queue (Min-Heap):** Essential for efficiently selecting the node with the minimum current distance. Python's `heapq` module is commonly used. See [[../../data_structures/heap_priority_queue.md]].
*   **Distance Array/Dictionary:** To store the shortest distance found so far from the source to each node (`Dict[Node, float]`). Initialized to infinity.
*   **(Optional) Visited Set/Array:** To avoid reprocessing nodes whose shortest path is already finalized. Can sometimes be omitted if checks are done when extracting from the heap (i.e., if extracted distance > stored final distance, skip).

## Complexity

*   **Time Complexity:** `O(E log V)` using a binary heap (like Python's `heapq`), where `E` is the number of edges and `V` is the number of vertices. This is because each edge relaxation might involve a `log V` heap operation. If using a Fibonacci heap, it can be `O(E + V log V)`, which is better for dense graphs.
*   **Space Complexity:** `O(V + E)` to store the graph, distances, and the priority queue.

## Use Cases

*   Finding the shortest path in road networks, network routing protocols (like OSPF).
*   Any problem reducible to finding the shortest path on a non-negatively weighted graph.

## Limitations

*   **Negative Edge Weights:** Dijkstra's algorithm **does not work correctly** if the graph contains negative edge weights. The greedy approach fails because a shorter path might be found later via a negative edge. For graphs with negative edges (but no negative cycles), use the Bellman-Ford algorithm or SPFA.
*   **Unweighted Graphs:** While Dijkstra works for unweighted graphs (treating edge weights as 1), Breadth-First Search ([[../bfs.md]]) is more efficient (`O(V + E)`).

## Implementation Notes (Python `heapq`)

```python
import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)] # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Optimization: If we find a shorter path already, skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items(): # Assuming graph[node] = {neighbor: weight, ...}
            distance = current_distance + weight

            # Relaxation
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example Graph Representation (Adjacency List using Dict)
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
# shortest_paths = dijkstra(graph, 'A')
# print(shortest_paths) # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
``` 