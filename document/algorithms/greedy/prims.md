# Prim's Algorithm

**Category:** Algorithm (`algorithms/greedy/`)

## Description

Prim's algorithm is a **greedy algorithm** used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, and weighted graph. Like Kruskal's algorithm ([`kruskal.md`](./kruskal.md)), it finds a subgraph that connects all vertices with the minimum possible total edge weight without forming cycles.

See also: [[../../patterns/graph/minimum_spanning_tree.md]]

## How it Works

Prim's algorithm grows the MST incrementally, starting from an arbitrary vertex. It maintains two sets of vertices: those already included in the MST and those not yet included.

1.  **Initialization:**
    *   Choose an arbitrary starting vertex `s`.
    *   Initialize the MST weight to 0 and the MST edge list to empty.
    *   Maintain a way to track the minimum edge weight connecting each vertex *outside* the MST to a vertex *inside* the MST. A common approach uses a min-priority queue (min-heap).
    *   Use a set or boolean array `in_mst` to track vertices currently in the MST.
    *   Initialize a min-heap storing `(weight, vertex)` or `(weight, u, v)` representing potential edges to add. Add `(0, s)` or equivalent information for the starting node to the heap.
    *   Alternatively, maintain an array `min_weight[v]` storing the minimum weight edge connecting `v` (outside MST) to the current MST, initialized to infinity (except for the start node).

2.  **Main Loop (Iterate V times):**
    *   While the heap is not empty (or until `V` vertices are in the MST):
        *   Extract the vertex `u` (or edge `(u, v)`) with the minimum weight from the priority queue that connects to a vertex not yet in the MST.
        *   If `u` is already in the MST, continue (this handles stale entries in some heap implementations).
        *   Add `u` to the MST (`in_mst[u] = True`).
        *   Add the corresponding edge weight to the total MST weight.
        *   For each neighbor `v` of `u`:
            *   If `v` is not in the MST (`!in_mst[v]`) and the edge `(u, v)` with weight `w` is cheaper than the current best known edge connecting `v` to the MST:
                *   Update the minimum weight for `v`.
                *   Add `(w, v)` or `(w, u, v)` to the priority queue. (This might add duplicate entries for `v` with different weights; the heap ensures the minimum is processed first. Some implementations update existing entries if the heap supports it).

3.  **Termination:**
    *   The loop terminates when `V` vertices have been added to the MST.

## Data Structures

*   **Graph Representation:** Adjacency list is common.
*   **Priority Queue (Min-Heap):** Essential for efficiently selecting the minimum weight edge connecting a vertex outside the MST to one inside. See [[../../data_structures/heap_priority_queue.md]]. Python's `heapq` is often used.
*   **Visited Set/Array (`in_mst`):** To track which vertices are already part of the growing MST.
*   **(Alternative Implementation):** Instead of a heap storing all potential edges, one can use an array `min_weight[v]` and update it, then linearly scan for the minimum in each step (O(V^2) total), or use a heap storing just `(min_weight[v], v)` pairs.

## Complexity

Let `V` be the number of vertices and `E` be the number of edges.

*   **Using Binary Heap (like `heapq`):**
    *   **Time Complexity:** O(E log V). Extracting min takes O(log V), and potentially E edge weight updates (decreases) take O(log V) each.
    *   **Space Complexity:** O(V + E) for graph, heap, visited array.
*   **Using Fibonacci Heap:**
    *   **Time Complexity:** O(E + V log V). `decrease_key` operation is O(1) amortized.
    *   **Space Complexity:** O(V + E).
*   **Using Adjacency Matrix and Array Scan (Dense Graphs):**
    *   **Time Complexity:** O(V^2).
    *   **Space Complexity:** O(V^2) for matrix.

## Use Cases

*   Finding the Minimum Spanning Tree.
*   Often preferred over Kruskal's for *dense* graphs where `E` is close to `V^2` (especially the O(V^2) or O(E + V log V) versions).

## Comparison with Kruskal's Algorithm ([`kruskal.md`](./kruskal.md))

*   **Approach:** Prim's grows one tree from a start node; Kruskal's merges components by adding the globally cheapest safe edge.
*   **Graph Density:** Prim's (with heap) is often better for dense graphs; Kruskal's is often better for sparse graphs.
*   **Disconnected Graphs:** Kruskal's naturally finds MSF; Prim's needs restarting for each component.

## Implementation Notes (Python using `heapq`)

```python
import heapq

def prim(num_vertices, graph, start_node=0):
    # graph: Adjacency list {u: [(weight, v), ...], ...}
    if not graph or num_vertices == 0:
        return 0, []

    mst_weight = 0
    mst_edges_list = []
    in_mst = {i: False for i in range(num_vertices)}
    # Heap stores (weight, u, v) - edge connecting v to MST via u
    min_heap = [(0, start_node, start_node)] # (weight_to_connect, vertex, connected_from_vertex)
    edges_count = 0

    while min_heap and edges_count < num_vertices:
        weight, u, connected_from = heapq.heappop(min_heap)

        if in_mst[u]:
            continue

        # Add vertex u to MST
        in_mst[u] = True
        mst_weight += weight
        if u != connected_from: # Avoid adding edge from start node to itself
             mst_edges_list.append((connected_from, u, weight))
        edges_count += 1

        # Explore neighbors
        if u in graph:
            for edge_weight, v in graph[u]:
                if not in_mst[v]:
                    heapq.heappush(min_heap, (edge_weight, v, u))

    # Check if MST is complete (all vertices included)
    if edges_count == num_vertices:
        return mst_weight, mst_edges_list
    else:
        # Graph was likely disconnected
        return mst_weight, mst_edges_list # Return MSF info for the reached component

# Example Usage:
# num_vertices = 4
# adj_list = {
#     0: [(10, 1), (6, 2), (5, 3)],
#     1: [(10, 0), (15, 3)],
#     2: [(6, 0), (4, 3)],
#     3: [(5, 0), (15, 1), (4, 2)]
# }
# mst_w, mst_e = prim(num_vertices, adj_list, 0)
# print(f"MST Weight: {mst_w}") # Output: MST Weight: 19
# print(f"MST Edges: {mst_e}") # Edges like [(0, 3, 5), (3, 2, 4), (0, 1, 10)] or similar depending on tie-breaking
``` 