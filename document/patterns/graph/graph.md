# Pattern: Graphs - Overview

**Category:** Pattern (`patterns/graph/`)

## 1. General Concept

Graphs are fundamental structures used to model relationships between objects (vertices or nodes) through connections (edges). Many LeetCode problems can be modeled as graph problems, even if not explicitly stated.

Understanding graph representations, traversal algorithms, and common graph patterns is crucial for solving a wide range of problems.

## 2. Core Concepts & Representations

*   **Vertices (Nodes):** Represent entities.
*   **Edges:** Represent connections or relationships between vertices. Edges can be:
    *   **Undirected:** Connection goes both ways (e.g., friendship).
    *   **Directed:** Connection has a direction (e.g., dependency, hyperlink).
    *   **Weighted:** Edges have associated costs or values.
    *   **Unweighted:** Edges have uniform cost (often considered 1).
*   **Representations:**
    *   **Adjacency List:** Preferred for sparse graphs. A dictionary or array mapping each vertex to a list of its neighbors (and edge weights, if applicable).
    *   **Adjacency Matrix:** Better for dense graphs. A V x V matrix where `matrix[i][j]` indicates an edge (or its weight) from `i` to `j`.
    *   **Edge List:** A simple list of all edges, often `(u, v, weight)`. Useful for algorithms like Kruskal's.

## 3. Fundamental Algorithms

These algorithms form the building blocks for solving many graph problems.

*   **Graph Traversal:** Systematically visiting nodes.
    *   **Breadth-First Search (BFS):** Explores layer by layer. Finds shortest paths in unweighted graphs. [[../../algorithms/graph_search/bfs.md]]
    *   **Depth-First Search (DFS):** Explores as deeply as possible before backtracking. Used for cycle detection, connectivity, topological sort, path finding. [[../../algorithms/graph_search/dfs.md]]
*   **Shortest Path Algorithms:** Finding the minimum cost path between nodes.
    *   **Dijkstra's Algorithm:** Single-source shortest paths in graphs with non-negative edge weights. [[../../algorithms/graph_search/dijkstra.md]]
    *   **Bellman-Ford Algorithm:** Single-source shortest paths, handles negative edge weights, detects negative cycles. [[../../algorithms/graph_search/bellman_ford.md]]
    *   **SPFA (Shortest Path Faster Algorithm):** Often faster than Bellman-Ford in practice for random graphs, also handles negative weights. [[../../algorithms/graph_search/spfa.md]]
    *   **Floyd-Warshall Algorithm:** All-pairs shortest paths.
*   **Topological Sort:** Linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge `(u, v)`, vertex `u` comes before vertex `v` in the ordering. Often implemented using Kahn's algorithm (BFS-based) or DFS.

## 4. Common Graph Patterns & Problems

*   **Minimum Spanning Tree (MST):** Finding the cheapest set of edges to connect all vertices in an undirected, weighted graph.
    *   **Pattern Overview:** [[./minimum_spanning_tree.md]]
    *   **Algorithms:** Kruskal's [[../../algorithms/greedy/kruskal.md]], Prim's [[../../algorithms/greedy/prims.md]]
*   **Connectivity:** Determining if paths exist between nodes, finding connected components.
    *   **Algorithms:** DFS, BFS, Disjoint Set Union (DSU) [[../../data_structures/disjoint_set_union.md]]
*   **Cycle Detection:** Identifying cycles in graphs.
    *   **Algorithms:** DFS (using visited states), DSU (for undirected graphs).
*   **Implicit Graphs:** Graphs where nodes and edges are defined by rules or properties rather than explicit lists (e.g., grid cells, states in a search, numbers with relationships).
    *   **Transformation Pattern:** [[./implicit_graph_to_tree_transformation.md]]
*   **Bipartite Graphs:** Checking if a graph's vertices can be divided into two disjoint sets such that no two vertices within the same set are adjacent.
    *   **Algorithm:** BFS or DFS with coloring.

## 5. Relevant Techniques & Optimizations

*   **Traversal Techniques:** [[../../techniques/graph_traversal/dfs_derived_tree_path_query.md]], [[../../techniques/graph_traversal/edge_relaxation.md]]
*   **Optimization Considerations:** [[../../optimizations/graph_shortest_path/path_query_sorted_value_diff_graph.md]]

## 6. Common Mistakes

*   Assuming shortest paths on derived trees: [[../../common_mistakes/graph/incorrect_shortest_path_assumption_on_derived_tree.md]]
*   Incorrect handling of visited states in DFS/BFS (leading to infinite loops or missed nodes).
*   Off-by-one errors in path reconstruction.
*   Choosing the wrong algorithm (e.g., Dijkstra with negative weights).

This overview serves as a starting point. Explore the linked documents for detailed explanations of specific algorithms, patterns, and techniques. 