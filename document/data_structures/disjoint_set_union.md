# Data Structure: Disjoint Set Union (DSU) / Union-Find

**Category:** Data Structure (`data_structures/`)

## Description

A Disjoint Set Union (DSU), also known as the Union-Find data structure, is used to efficiently track a partition of a set of elements into a number of disjoint (non-overlapping) subsets.

It provides two primary operations:

1.  **`find(i)`:** Determine which subset element `i` belongs to. It returns a canonical representative (often called the "root" or "parent") of that subset. If two elements have the same representative, they are in the same subset.
2.  **`union(i, j)`:** Merge the subsets containing elements `i` and `j` into a single subset.

## Implementation

Typically implemented using an array (or dictionary) `parent`, where `parent[i]` stores the parent of element `i`. The representative of a set is an element `r` such that `parent[r] == r`.

## Optimizations

To achieve near-constant amortized time complexity for operations, two key optimizations are crucial:

1.  **Path Compression (during `find`):** When finding the representative of an element `i`, make all nodes on the path from `i` to the root point directly to the root. This flattens the structure for future `find` operations.
2.  **Union by Rank / Union by Size (during `union`):** When merging two sets, make the root of the smaller tree (based on rank/height or number of nodes/size) point to the root of the larger tree. This helps keep the trees relatively shallow.

## Key Operations & Complexity (with optimizations)

Let `N` be the number of elements and `M` be the number of operations.

*   **`make_set(i)`:** Initialize a new set containing only element `i`. O(1).
*   **`find(i)`:** Find the representative of `i`'s set (with path compression). Amortized time is nearly constant, often denoted as O(α(N)), where α is the extremely slow-growing inverse Ackermann function (practically <= 4 for any conceivable input size).
*   **`union(i, j)`:** Merge the sets containing `i` and `j` (using union by rank/size). Amortized time O(α(N)).

Without optimizations, `find` can degrade to O(N) in the worst case (skewed tree).

## Use Cases

*   **Kruskal's Algorithm for Minimum Spanning Tree ([`../algorithms/greedy/kruskal.md`](../algorithms/greedy/kruskal.md)):** Used to efficiently detect if adding an edge would form a cycle by checking if the endpoints are already in the same set.
*   **Detecting Cycles in Undirected Graphs:** Iterate through edges `(u, v)`. If `find(u) == find(v)`, a cycle exists. Otherwise, perform `union(u, v)`.
*   **Finding Connected Components in Graphs:** Process all nodes and edges. The number of distinct sets remaining corresponds to the number of connected components.
*   **Network Connectivity Problems:** Determining if nodes in a network are connected.
*   **Least Common Ancestor (LCA) Offline Algorithm (Tarjan's):** Uses DSU as part of the process.

## Implementation Notes (Python)

```python
class DSU:
    def __init__(self, n):
        # Initialize parent array: each element is its own parent initially
        self.parent = list(range(n)) 
        # Optional: Initialize rank/size for union optimization
        self.rank = [0] * n # Or self.size = [1] * n

    def find(self, i):
        # Find representative with path compression
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i, j):
        # Union by rank (or size)
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Indicates a successful union (sets were different)
        return False # Indicates i and j were already in the same set

# Example Usage
# dsu = DSU(5)
# dsu.union(0, 1)
# dsu.union(1, 2)
# print(dsu.find(0) == dsu.find(2)) # Output: True
# print(dsu.find(0) == dsu.find(3)) # Output: False
# print(dsu.union(0, 3))
# print(dsu.find(0) == dsu.find(3)) # Output: True
``` 