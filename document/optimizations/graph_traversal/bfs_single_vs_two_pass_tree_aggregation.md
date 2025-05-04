# Optimization: BFS Single-Pass vs. Two-Pass for Tree Path Aggregation

**Related Concepts:**
*   Graph Traversal: [[../../algorithms/graph_search/bfs.md]]
*   Tree Data Structure
*   Path Aggregation (e.g., sum, product)

## Context

When solving problems involving aggregating values (like products or sums) along paths in a tree rooted at a specific node (e.g., node 0), Breadth-First Search (BFS) is a common approach.

Consider a scenario where the tree edges and their associated values (e.g., conversion factors, edge weights) are provided as a list of connections, but the explicit parent->child direction might not be immediately clear from the *order* of the list, although the problem guarantees a tree structure rooted at a specific node (e.g., node 0) and that connections implicitly flow away from the root.

Example Problem: LeetCode 3528 - Unit Conversion I. Input `conversions = [[u, v, factor]]` guarantees a tree rooted at 0, and `u` is always the parent of `v` relative to the root.

## Approaches Compared

### 1. Two-Pass BFS (Safe but Potentially Less Efficient)

*   **Pass 1: Build Explicit Directed Tree:**
    1.  Create a temporary *undirected* adjacency list from the input connections.
    2.  Perform an initial BFS starting from the root (node 0).
    3.  As this BFS explores, build a *new, directed* adjacency list, only adding edges `(parent, child)` in the direction they are discovered away from the root.
*   **Pass 2: Aggregate Values:**
    1.  Perform a second BFS on the *directed* tree built in Pass 1.
    2.  During this traversal, calculate the cumulative path aggregate (e.g., product modulo MOD) for each node based on its parent's aggregate and the connecting edge value.
*   **Pros:** Robust to the order of input connections. Guarantees correct edge direction before calculation.
*   **Cons:** Requires two full graph traversals. Uses extra space for the temporary undirected graph, the visited set for the first BFS, the first BFS queue, and the final directed graph.

### 2. Single-Pass BFS (Efficient When Guarantees Hold)

*   **Assumption/Requirement:** This approach relies **critically** on a guarantee that the input format *directly* represents the directed edges away from the specified root. For example, if the input is `[u, v, value]`, it's guaranteed that `u` is the parent and `v` is the child in the tree relative to the root.
*   **Pass 1: Build Directed Graph & Aggregate Values Simultaneously:**
    1.  Build a *directed* adjacency list directly from the input connections, trusting the implied direction (`adj[u].append((v, value))`).
    2.  Initialize the result array/map (e.g., `values[root] = identity_element`).
    3.  Perform a single BFS starting from the root.
    4.  When traversing from node `u` to an *unvisited* neighbor `v` using the edge `(u, v, value)`:
        *   Calculate `values[v]` based on `values[u]` and `value`.
        *   Mark `v` as visited (implicitly by setting its value).
        *   Enqueue `v`.
*   **Pros:** Requires only one graph traversal. Uses less memory by avoiding the intermediate structures of the two-pass approach.
*   **Cons:** **Incorrect if the input format guarantee doesn't hold.** If `[u, v, value]` could sometimes mean `v` is the parent of `u`, this approach would fail.

## Conclusion

When the problem statement provides a strong guarantee about the input connections defining a directed tree rooted at a specific node, the **Single-Pass BFS** approach is significantly more efficient in terms of both time (constant factors) and space compared to the safer but slower **Two-Pass BFS**.

Always verify the problem constraints and guarantees before choosing the single-pass method. If directionality is uncertain, the two-pass approach is more robust. 