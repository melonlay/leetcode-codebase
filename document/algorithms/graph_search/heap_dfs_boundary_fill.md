# Algorithm: Heap + DFS for Boundary-Limited Grid Fill

## Description

This algorithm solves grid/matrix problems where the goal is to calculate a quantity (like trapped water volume) based on exploring regions limited by boundary heights, starting from the grid edges.

It combines a Min-Heap (Priority Queue) to manage processing order based on boundary height with Depth-First Search (DFS) to efficiently explore connected regions below a given boundary height.

## Core Idea

1.  **Min-Heap for Boundaries:** Use a min-heap to store `(height, row, col)` tuples representing cells on the current boundary between visited and unvisited regions. Initially, populate it with the grid's outer border cells.
2.  **Extract Lowest Boundary:** Repeatedly extract the cell `(level, r, c)` with the minimum height (`level`) from the heap. This `level` is the lowest point on the current known boundary.
3.  **DFS for Internal Pool:** Initiate a DFS (using an explicit stack) starting from the extracted cell `(r, c)`. The DFS explores all reachable, unvisited neighbors.
4.  **Conditional Processing during DFS:**
    *   **Neighbor Below/At Level (`neighbor_height <= level`):** This cell is part of the internal pool defined by the current `level`. Process it (e.g., calculate trapped water `level - neighbor_height`), mark it visited, and add it to the DFS stack to continue exploring the pool.
    *   **Neighbor Above Level (`neighbor_height > level`):** This cell is a new, higher boundary segment. Mark it visited, but instead of adding it to the DFS stack, add it to the **Min-Heap** `(neighbor_height, nr, nc)`. This ensures higher boundary segments are processed later.
5.  **Visited Tracking:** Mark cells as visited as they are encountered during the DFS/heap processing. Can use a separate boolean matrix or modify the input grid in-place (e.g., setting cell value to -1) if allowed.

## Use Cases

*   Calculating trapped rainwater in 2D elevation maps ([Problem 407](../../../problems/0407_trapping_rain_water_ii/solution.md)).
*   Other grid problems involving flood-fill or region exploration limited by boundary values where processing from lowest boundaries first is advantageous.

## Complexity

*   **Time:** O(M * N * log(M * N)) - Each cell visited once. Heap operations dominate in the worst case.
*   **Space:** O(M * N) - For the heap, DFS stack, and potentially a visited matrix.

## Implementation Notes

*   Careful handling of boundary conditions and visited state is crucial.
*   The choice of visited tracking (in-place vs. separate matrix) depends on problem constraints.

## Optimization Considerations

*   This approach is generally considered an optimization over a pure Heap+BFS approach for this problem type, as it reduces the number of potentially expensive heap operations. See [Optimization: Heap+DFS vs Heap+BFS for Boundary Fill](../../optimizations/grid_traversal/heap_dfs_vs_bfs_boundary_fill.md) (*Link assumed*).

## Related Concepts

*   [Data Structure: Heap (Priority Queue)](../../data_structures/heap_priority_queue.md)
*   Algorithm: Depth-First Search (DFS)
*   Algorithm: Breadth-First Search (BFS) (Alternative base)
*   Algorithm: Dijkstra's Algorithm (Conceptual similarity)
*   [Pattern: Find Capacity Between Boundaries](../../patterns/array/find_capacity_between_boundaries.md) 