# Kruskal's Algorithm

**Category:** Algorithm (`algorithms/greedy/`)

## Description

Kruskal's algorithm is a **greedy algorithm** used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, and weighted graph. An MST is a subgraph that connects all vertices together, without any cycles, and with the minimum possible total edge weight.

If the graph is not connected, Kruskal's algorithm finds a Minimum Spanning Forest (a collection of MSTs for each connected component).

## How it Works

1.  **Initialization:**
    *   Create a forest where each vertex is in its own tree (a disjoint set for each vertex). Use the [Disjoint Set Union (DSU) data structure](../../data_structures/disjoint_set_union.md) for this.
    *   Create a list of all edges in the graph.
    *   Initialize an empty list `mst_edges` to store the edges belonging to the MST.
    *   Initialize a variable `mst_weight` to 0.

2.  **Sort Edges:**
    *   Sort all edges in the graph in non-decreasing order of their weights. See [[../sorting/builtin_sort.md]].

3.  **Iterate and Union:**
    *   Iterate through the sorted edges `(u, v)` with weight `w`:
        *   Check if vertices `u` and `v` belong to different sets using the DSU's `find` operation (`find(u) != find(v)`).
        *   If they belong to different sets (i.e., adding this edge **does not** form a cycle):
            *   Add the edge `(u, v)` to `mst_edges`.
            *   Add its weight `w` to `mst_weight`.
            *   Merge the sets containing `u` and `v` using the DSU's `union` operation (`union(u, v)`).

4.  **Termination:**
    *   The algorithm terminates when `|V| - 1` edges have been added to `mst_edges` (for a connected graph) or when all edges have been considered.
    *   The `mst_edges` list contains the MST, and `mst_weight` holds its total weight.

## Data Structures

*   **List of Edges:** To store all graph edges, typically as tuples `(weight, u, v)` for easy sorting.
*   **Disjoint Set Union (DSU):** Crucial for efficiently checking if adding an edge creates a cycle. See [[../../data_structures/disjoint_set_union.md]].

## Complexity

Let `V` be the number of vertices and `E` be the number of edges.

*   **Time Complexity:** O(E log E) or O(E log V).
    *   Sorting the edges takes O(E log E).
    *   The DSU operations (find and union) take nearly constant amortized time O(α(V)) each. Over E edges, this is O(E α(V)).
    *   The dominant factor is usually the sorting step. If E is close to V^2, log E is similar to log V, making O(E log E) ≈ O(E log V).
*   **Space Complexity:** O(V + E) to store the graph edges, the DSU structure, and the resulting MST edges.

## Use Cases

*   Finding the Minimum Spanning Tree of a graph.
*   Network design (e.g., laying cables with minimum cost).
*   Approximation algorithms for other problems (like the Traveling Salesperson Problem).
*   Cluster analysis.

## Comparison with Prim's Algorithm

*   Prim's algorithm also finds the MST but grows the tree starting from a single vertex, adding the cheapest edge connecting a vertex in the tree to one outside the tree.
*   Prim's is often more efficient for *dense* graphs (using adjacency matrix and Fibonacci heap: O(E + V log V)) while Kruskal's is often better for *sparse* graphs (where O(E log E) or O(E log V) is faster).
*   Kruskal's can easily find Minimum Spanning Forests in disconnected graphs; Prim's needs to be run separately for each component.
*   See [[./prims.md](./prims.md)] for details on Prim's algorithm.

## Implementation Notes (Python)

```python
# Assumes DSU class is defined as in ../../data_structures/disjoint_set_union.md
class DSU:
    # ... (DSU implementation from disjoint_set_union.md)
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal(num_vertices, edges):
    # edges: list of tuples [(weight, u, v), ...]
    
    # 1. Sort edges by weight
    edges.sort() 
    
    # 2. Initialize DSU and MST variables
    dsu = DSU(num_vertices)
    mst_weight = 0
    mst_edges_count = 0
    mst_edges_list = []

    # 3. Iterate through sorted edges
    for weight, u, v in edges:
        # If adding edge (u, v) doesn't form a cycle
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges_count += 1
            mst_edges_list.append((u, v, weight))
            # Optional: Stop early if MST is complete
            if mst_edges_count == num_vertices - 1:
                break
                
    # Check if MST was formed (for connected graphs)
    if mst_edges_count == num_vertices - 1:
        return mst_weight, mst_edges_list
    else:
        # Graph might be disconnected, return Minimum Spanning Forest info
        return mst_weight, mst_edges_list # Or indicate failure for connected expectation

# Example Usage:
# num_vertices = 4
# graph_edges = [
#     (10, 0, 1),
#     (6, 0, 2),
#     (5, 0, 3),
#     (15, 1, 3),
#     (4, 2, 3)
# ]
# mst_w, mst_e = kruskal(num_vertices, graph_edges)
# print(f"MST Weight: {mst_w}") # Output: MST Weight: 19 (Edges: (4, 2, 3), (5, 0, 3), (10, 0, 1))
# print(f"MST Edges: {mst_e}")
``` 