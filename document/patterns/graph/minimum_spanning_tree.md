# Pattern: Minimum Spanning Tree (MST)

**Category:** Pattern (`patterns/graph/`)

## Description

A **Minimum Spanning Tree (MST)** or **Minimum Weight Spanning Tree** is a specific kind of subgraph derived from a **connected, edge-weighted, undirected graph**.

It fulfills the following properties:
1.  **Spanning:** It includes *all* the vertices from the original graph.
2.  **Tree:** It is acyclic (contains no cycles).
3.  **Minimum Weight:** The sum of the weights of all the edges in the tree is less than or equal to the sum of the weights of the edges in any other spanning tree of the graph.

In essence, it's the cheapest way to connect all vertices in the graph together.

## Key Properties

*   **Uniqueness:** If all edge weights in the graph are distinct, the MST is unique. If there are duplicate edge weights, multiple MSTs might exist, but they will all have the same minimum total weight.
*   **Number of Edges:** For a graph with `V` vertices, any spanning tree (including the MST) will have exactly `V - 1` edges.
*   **Cut Property:** For any cut (a partition of the graph's vertices into two disjoint sets), if the weight of an edge `e` crossing the cut is strictly smaller than the weights of all other edges crossing the cut, then this edge `e` belongs to all MSTs of the graph.
*   **Cycle Property:** For any cycle in the graph, if the weight of an edge `e` in the cycle is strictly greater than the weights of all other edges in the cycle, then this edge `e` cannot belong to any MST.

## Algorithms

Several greedy algorithms can find the MST:

*   **Kruskal's Algorithm ([`../../algorithms/greedy/kruskal.md`](../../algorithms/greedy/kruskal.md)):** Sorts all edges by weight and adds the next cheapest edge that doesn't form a cycle (using DSU).
*   **Prim's Algorithm ([`../../algorithms/greedy/prims.md`](../../algorithms/greedy/prims.md)):** Starts from an arbitrary vertex and grows the tree by repeatedly adding the cheapest edge that connects a vertex in the tree to a vertex outside the tree (using a priority queue).
*   **Borůvka's Algorithm:** Less commonly used in basic contexts, works by iteratively adding the cheapest edge incident to each component.

## Applications

*   Network design (connecting points with minimum cable/road length).
*   Cluster analysis.
*   Approximation algorithms for NP-hard problems (like TSP).
*   Image segmentation.
*   Circuit design.

## Minimum Spanning Forest

If the original graph is **not connected**, the concept extends to a **Minimum Spanning Forest (MSF)**. An MSF is the union of the Minimum Spanning Trees for each connected component of the graph.

*   Kruskal's algorithm naturally finds the MSF if run until all edges are considered.
*   Prim's algorithm needs to be started independently in each connected component to find the MSF. 