# Data Structure: Disjoint Set Union (DSU) / Union-Find

**Related Concepts:**
*   Graph Connectivity
*   Connected Components
*   Cycle Detection (in Undirected Graphs)
*   Kruskal's Algorithm (Minimum Spanning Tree)

## Structure Description

Disjoint Set Union (DSU), also known as Union-Find, is a data structure that tracks a partition of a set of `n` elements into a number of disjoint (non-overlapping) subsets.

It provides two primary operations efficiently:

1.  **`find(i)`:** Determines which subset element `i` belongs to. It returns a canonical representative (or "root") element for that subset. If `find(i) == find(j)`, elements `i` and `j` are in the same subset.
2.  **`union(i, j)`:** Merges the two subsets containing elements `i` and `j` into a single subset. If `i` and `j` are already in the same subset, the operation does nothing.

## Implementation Details

A common way to implement DSU is using an array `parent` of size `n`.

*   `parent[i]`: Stores the parent of element `i`.
*   If `parent[i] == i`, then `i` is the representative (root) of its subset.

**Initialization:** Each element starts in its own subset: `parent[i] = i` for all `i` from `0` to `n-1`.

### `find(i)` Operation
*   Recursively traverses up the parent links from `i` until it reaches the root (where `parent[root] == root`).
*   **Path Compression (Optimization):** During the traversal up to the root, update the parent pointer of each node visited to point directly to the root. This flattens the tree structure and significantly speeds up future `find` operations for these elements.

```python
def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i]) # Path compression
    return parent[i]
```

### `union(i, j)` Operation
*   Find the representatives (roots) of the subsets containing `i` and `j`: `root_i = find(i)`, `root_j = find(j)`.
*   If `root_i != root_j`, the elements are in different subsets. Merge them by making one root the parent of the other (e.g., `parent[root_i] = root_j`).
*   **Union by Rank/Size (Optimization):** To keep the trees relatively balanced and shallow, heuristics can be used during union:
    *   **Union by Rank:** Keep track of the rank (roughly, the height) of each tree. Make the root with the smaller rank a child of the root with the larger rank. If ranks are equal, pick one root as the parent and increment its rank.
    *   **Union by Size:** Keep track of the size (number of elements) of each tree. Make the root of the smaller tree a child of the root of the larger tree.

```python
def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        # Simple union:
        parent[root_i] = root_j
        # Add rank/size logic here for optimization
        return True # Merge occurred
    return False # Already in same set
```

## Complexity

With both Path Compression and Union by Rank/Size optimizations:
*   **`find` operation:** Nearly constant time on average, amortized complexity is O(α(n)), where α is the extremely slowly growing inverse Ackermann function (α(n) < 5 for any practical value of n).
*   **`union` operation:** Also O(α(n)) amortized time.
*   **Space Complexity:** O(n) to store the `parent` array (and optional rank/size arrays).

Without optimizations, complexity can degrade towards O(n) per operation in the worst case (creating linked-list like structures).

## Use Cases
*   Finding connected components in graphs.
*   Detecting cycles in undirected graphs (if `union(u, v)` finds `u` and `v` already connected, adding edge `(u, v)` creates a cycle).
*   Kruskal's algorithm for MST.
*   Problems involving grouping elements based on equivalence relations.
*   Efficiently checking connectivity between pairs of elements as connections are added incrementally. 