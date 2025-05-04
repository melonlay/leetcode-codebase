# Algorithm: Depth-First Search (DFS)

**Related Concepts:**
*   Graph Traversal
*   [Stack Data Structure](../../data_structures/stack.md) (often used implicitly via recursion, or explicitly)
*   [Recursion](../../algorithms/recursion/backtracking.md)
*   Tree Traversal (Pre-order, In-order, Post-order are variants)
*   Connectivity Problems
*   Cycle Detection
*   Topological Sort

## Algorithm Description

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

Starting from a selected node (or arbitrary node if exploring disconnected components), it explores along a path until it reaches a node with no unvisited neighbors, then backtracks to the previous node and explores another unvisited neighbor branch.

## Core Logic (Recursive)

1.  **Initialization:**
    *   Create a `visited` set or boolean array to track visited nodes.
    *   Choose a starting node `start_node`.
2.  **`dfs(node)` Function:**
    *   Mark `node` as visited.
    *   Process `node` (e.g., add to path, check property).
    *   For each `neighbor` of `node`:
        *   If `neighbor` has not been visited:
            *   Recursively call `dfs(neighbor)`.
3.  **Start Traversal:** Call `dfs(start_node)`.
4.  **Disconnected Graphs:** If the graph might be disconnected, loop through all nodes. If a node hasn't been visited, start a new DFS from it.

## Core Logic (Iterative with Explicit Stack)

1.  **Initialization:**
    *   Create a `visited` set or boolean array.
    *   Create an empty stack.
    *   Choose a starting node `start_node`.
    *   Push `start_node` onto the stack.
2.  **Traversal Loop:**
    *   While the stack is not empty:
        *   Pop a node `current_node` from the stack.
        *   **Check if visited (Important for iterative):** If `current_node` is already visited, `continue`.
        *   Mark `current_node` as visited.
        *   Process `current_node`.
        *   For each `neighbor` of `current_node` (often processed in reverse order to mimic recursion's order):
            *   If `neighbor` has not been visited:
                *   Push `neighbor` onto the stack.
3.  **Disconnected Graphs:** Similar to recursive, loop through all nodes and start iterative DFS if unvisited.

## Key Properties

*   **Path Finding:** Finds *a* path between two nodes (not necessarily the shortest).
*   **Connectivity:** Can determine connected components in an undirected graph.
*   **Cycle Detection:** Can detect cycles in both directed and undirected graphs (by tracking nodes currently in the recursion stack/path).
*   **Topological Sort:** Forms the basis for topological sorting in Directed Acyclic Graphs (DAGs).
*   **Exploration Order:** Explores deeply along one path before exploring alternatives.

## Data Structures

*   **Stack:** Implicitly used by recursion, or explicitly in the iterative version. Python's list can act as a stack.
*   **Set/Dictionary/Array:** To keep track of `visited` nodes efficiently.

## Complexity

Let `V` be the number of vertices (nodes) and `E` be the number of edges.

*   **Time Complexity:** O(V + E)
    *   Each vertex is visited (pushed/popped or entered recursively) at most once.
    *   Each edge is examined at most once (or twice in undirected adjacency list).
*   **Space Complexity:**
    *   O(V) for the `visited` set.
    *   O(H) for the stack, where H is the maximum depth of the traversal (height of the DFS tree). In the worst case (e.g., a path graph), H can be O(V).

## Use Cases

*   Finding connected components.
*   Detecting cycles in graphs.
*   Topological sorting.
*   Solving maze puzzles or pathfinding problems.
*   As a subroutine in other algorithms (e.g., finding articulation points/bridges).
*   Traversing derived tree/forest structures created from implicit graphs (see [[../../patterns/graph/implicit_graph_to_tree_transformation.md]]).

## Comparison with BFS ([`bfs.md`](./bfs.md))

*   **Order:** DFS explores deeply, BFS explores layer-by-layer.
*   **Shortest Path:** BFS finds shortest paths in unweighted graphs; DFS does not guarantee shortest paths.
*   **Space:** BFS space complexity depends on the maximum width of the graph (can be O(V)), DFS depends on the maximum depth (can also be O(V) worst-case, but often less on average).
*   **Data Structure:** DFS uses a stack (implicit or explicit), BFS uses a queue. 