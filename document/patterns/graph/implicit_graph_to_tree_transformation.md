# Pattern: Implicit Graph to Tree/Forest Transformation

## 1. Description

This pattern applies to problems involving pathfinding, connectivity, or distance queries on **implicit graphs**, especially those where nodes correspond to elements in a **sorted sequence** and edges are defined by proximity or relative value constraints (e.g., `|value[i] - value[j]| <= k`, `value[j]` is the smallest value greater than `value[i]`).

Directly applying standard graph algorithms (like BFS) can be too slow if the implicit graph is dense (many edges).

The core idea is to **transform** the implicit graph problem into one defined on an **explicit tree or forest structure**. This is achieved by defining a specific, deterministic parent-child relationship based on the connectivity rules of the implicit graph.

## 2. General Strategy

1.  **Identify Implicit Graph:** Recognize that the problem can be modeled as a graph where nodes are sequence elements and edges exist based on certain conditions, but the graph isn't given explicitly.
2.  **Sort Data (if necessary):** Many problems using this pattern involve sorted sequences, as sorting often simplifies defining the parent/child relationship.
3.  **Define Parent/Child Rule:** Establish a rule to assign a unique "parent" (or sometimes a specific "child") for each node based on the implicit graph's connectivity. This rule should aim to capture the essential structure needed to answer the original problem's queries.
    *   *Example Rules:*
        *   Parent `p` of `i` is the *leftmost* index `p < i` such that `node i` and `node p` are connected in the implicit graph.
        *   Parent `p` of `i` is the *nearest* node `p` satisfying the connection criteria.
        *   Child `c` of `i` is the *next* node `c > i` reachable according to some rule.
4.  **Construct Derived Tree/Forest:** Build the explicit graph (adjacency list) representing the chosen parent-child relationships. This structure will often be a tree or a forest (collection of trees).
5.  **Solve Problem on Derived Structure:** Apply an appropriate algorithm (often DFS, sometimes combined with other techniques like binary search or offline query processing) to the derived tree/forest to answer the original queries about the implicit graph.
    *   *Example:* Use [[../techniques/graph_traversal/dfs_derived_tree_path_query.md]] to answer distance queries.

## 3. Why it Works (Heuristically)

By carefully choosing the parent/child rule, the derived tree often preserves the essential path or connectivity information from the implicit graph needed for the specific problem. For instance, connecting to the *leftmost* reachable node in a sorted sequence might correspond to the shortest path in terms of number of edges in the implicit graph defined by proximity.

**Caution:** The validity of this transformation (i.e., whether solving the problem on the derived tree gives the correct answer for the original implicit graph) must be justified for each specific problem. See [[../common_mistakes/graph/incorrect_shortest_path_assumption_on_derived_tree.md]].

## 4. When to Consider This Pattern

*   Pathfinding/distance queries on graphs defined implicitly on sorted sequences.
*   Connectivity constraints based on value differences (`|val[i] - val[j]| <= k`).
*   Standard BFS/Dijkstra seems too slow due to potentially dense implicit edges.
*   Problems where defining a specific neighbor (e.g., leftmost, rightmost, nearest satisfying a condition) seems possible and useful.

## 5. Implementation Techniques

*   Calculating Parent Pointers:
    *   [[../techniques/sequence/find_boundary_pointer_sorted_constraint.md]] (Two Pointers)
    *   [[../techniques/sequence/find_reach_bounds_sorted_constraint.md]] (Binary Search)
*   Solving on Derived Tree:
    *   [[../techniques/graph_traversal/dfs_derived_tree_path_query.md]] (DFS + Offline Queries + Bisect)
    *   Standard [[../algorithms/graph_search/dfs.md]] or [[../algorithms/graph_search/bfs.md]] if the query is simpler (e.g., reachability).

## 6. Related Concepts

*   Implicit Graphs
*   Graph Traversal ([[../algorithms/graph_search/dfs.md]], [[../algorithms/graph_search/bfs.md]])
*   Tree Algorithms
*   Sorting 