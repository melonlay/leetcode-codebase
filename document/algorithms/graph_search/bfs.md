# Breadth-First Search (BFS)

**Related Concepts:**
*   Graph Traversal
*   Queue Data Structure ([`collections.deque`](../../../data_structures/queue.md))
*   Shortest Path (Unweighted Graphs)
*   Level Order Traversal (Trees)

## Algorithm Description

Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes "layer by layer". It starts at a selected node (the source) and explores all of its immediate neighbors first, then explores all of *their* neighbors that haven't been visited yet, and so on.

It uses a queue data structure to keep track of the nodes to visit next.

## Core Logic

1.  **Initialization:**
    *   Choose a starting node.
    *   Create a queue and enqueue the starting node.
    *   Create a set or boolean array `visited` to keep track of visited nodes, and mark the starting node as visited.
    *   Optionally, initialize a distance map/array if tracking distances from the source.

2.  **Traversal Loop:**
    *   While the queue is not empty:
        *   Dequeue a node (`current_node`) from the front of the queue.
        *   Process `current_node` (e.g., check if it's the target node).
        *   For each `neighbor` of `current_node`:
            *   If `neighbor` has not been visited:
                *   Mark `neighbor` as visited.
                *   (Optional: Update distance for `neighbor`)
                *   Enqueue `neighbor`.

## Key Properties

*   **Finds Shortest Path:** In an *unweighted* graph, BFS is guaranteed to find the shortest path (in terms of the number of edges) between the starting node and any other reachable node.
*   **Completeness:** If there is a path from the source to a target node, BFS will find it.
*   **Level-by-Level Exploration:** Explores the graph layer by layer, ensuring nodes closer to the source are visited before nodes further away.

## Data Structures

*   **Queue:** Essential for managing the order of nodes to visit (FIFO - First-In, First-Out). Python's `collections.deque` is efficient.
*   **Set/Dictionary/Array:** To keep track of `visited` nodes efficiently (O(1) average lookup).

## Complexity

Let `V` be the number of vertices (nodes) and `E` be the number of edges in the graph.

*   **Time Complexity:** O(V + E)
    *   Each vertex is enqueued and dequeued exactly once (O(V)).
    *   Each edge is examined exactly once (or twice in an undirected graph representation) when exploring neighbors (O(E)).
*   **Space Complexity:** O(V)
    *   The `visited` set can store up to V nodes.
    *   The `queue` can store up to O(V) nodes in the worst case (e.g., a star graph or a graph where the last layer has many nodes).

## Use Cases

*   Finding the shortest path in unweighted graphs.
*   Level order traversal of trees (which are special types of graphs).
*   Web crawlers (exploring pages level by level).
*   Finding connected components in a graph.
*   Network broadcasting.
*   Solving puzzle problems like Rubik's Cubes or Word Ladders where states represent nodes and moves represent edges. 