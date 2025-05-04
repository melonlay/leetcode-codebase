# Common Mistake: Incorrect Shortest Path Assumption on Derived Tree

## The Mistake

A common error when dealing with implicitly defined graphs (especially those based on geometric proximity or value differences) is to construct a simpler derived tree structure (like a Minimum Spanning Tree (MST), a Disjoint Set Union (DSU) forest, or a tree based on some greedy connection rule) and then incorrectly assume that the path distance between two nodes *within that derived tree* is equal to the shortest path distance between the same two nodes in the *original implicit graph*.

## Why It's Wrong

The original implicit graph might contain "shortcut" edges that are not part of the derived tree structure. The derived tree typically captures connectivity or some optimal property (like minimum total edge weight for MST), but it doesn't necessarily preserve all shortest paths.

*   **Example:** Consider nodes A, B, C with values 1, 5, 6 and `maxDiff = 5`. Edges are (A, B) because |1-5|<=5 and (B, C) because |5-6|<=5, and (A, C) because |1-6|<=5. The graph is a triangle. A simple derived tree might only include edges (A, B) and (B, C). The distance A-C in this tree is 2. However, the shortest path distance in the original implicit graph is 1, using the direct edge (A, C).
*   **DSU Forests:** DSU only tracks connectivity (which component a node belongs to). It doesn't store path information. Using a DSU forest directly for shortest paths is fundamentally incorrect.

## How to Avoid

1.  **Identify Goal:** Clarify if the goal is connectivity, MST, or *shortest paths*.
2.  **Use Correct Algorithm:** For unweighted shortest paths, use Breadth-First Search (BFS) on the relevant graph representation. For weighted shortest paths, use Dijkstra's or Bellman-Ford.
3.  **Validate Derived Structures:** If using a derived structure (like the Leftmost-Pointer Tree in [[../techniques/graph_traversal/dfs_leftmost_pointer_tree_path_query.md]]), ensure there's a specific proof or property demonstrating that paths in this structure *do* correspond to shortest paths in the original implicit graph for the specific problem type.
4.  **Consider Explicit Graph (If Feasible):** If N is small enough, building the explicit adjacency list for the implicit graph and running standard BFS might be viable.
5.  **Specialized Techniques:** If standard BFS is too slow due to the number of implicit edges, look for specialized techniques like the Binary Lifting on ranges or the DFS on Leftmost-Pointer Tree, but understand *why* they work for the specific graph structure.

## Related Concepts

*   Breadth-First Search (BFS)
*   Dijkstra's Algorithm
*   Minimum Spanning Tree (MST)
*   Disjoint Set Union (DSU)
*   Implicit Graphs
*   [[../techniques/graph_traversal/dfs_leftmost_pointer_tree_path_query.md]]
*   [[../techniques/binary_lifting/binary_lifting_min_steps_on_ranges.md]] 