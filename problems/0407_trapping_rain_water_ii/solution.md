# LeetCode 407: Trapping Rain Water II - Solution Explanation

## Problem Summary

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

## Algorithmic Approach: Min-Heap + DFS from Boundary

This problem extends the 1D "Trapping Rain Water" concept to 2D. Simple linear scan approaches fail due to the complex 2D boundary interactions.

The core idea is to simulate water filling from the outside inwards. Water is held back by the outer grid boundary and internal high points. The water level in any pool is limited by the lowest point on its surrounding effective wall.

We use a Min-Heap to manage the boundary wall segments, always processing the lowest segment first. From that segment, we use Depth-First Search (DFS) to efficiently explore the connected area that can be reached without exceeding the height of that segment.

This approach is detailed in the Knowledge Base:
*   **Reference:** `[[../document/algorithms/graph_search/heap_dfs_boundary_fill.md]]`

## Logic Explanation

1.  **Initialization:**
    *   Handle edge cases (grid too small to trap water: `m <= 2` or `n <= 2`).
    *   Create a min-heap `heap` to store `(height, row, col)` tuples.
    *   Use in-place modification of `heightMap` to track visited cells (set to `-1`).
    *   Initialize `total_water = 0`.
2.  **Add Initial Boundaries:** Add all cells on the outer border of the `heightMap` to the `heap` and mark them as visited (`-1`) in the `heightMap`.
3.  **Process Heap:** While the `heap` is not empty:
    *   **Extract Lowest Boundary:** Pop the cell `(level, r, c)` with the minimum height `level` from the `heap`. This `level` is the lowest known boundary height for the region we are about to explore.
    *   **Start DFS:** Use a stack `dfs_stack` initialized with `(r, c)` to explore reachable cells from this boundary point.
    *   **Explore Neighbors:** While `dfs_stack` is not empty, pop `(curr_r, curr_c)` and check its 4-directional neighbors `(nr, nc)`.
    *   For each valid (in bounds) and unvisited (`heightMap[nr][nc] != -1`) neighbor:
        *   Let `neighbor_height = heightMap[nr][nc]`.
        *   Mark the neighbor as visited (`heightMap[nr][nc] = -1`).
        *   **If `neighbor_height <= level`:** The neighbor is inside the current water level determined by `level`. Calculate trapped water `total_water += level - neighbor_height`. Add the neighbor `(nr, nc)` to the `dfs_stack` to continue exploring at this level.
        *   **If `neighbor_height > level`:** The neighbor is higher than the current boundary `level`. It forms a new, higher boundary segment. Add it to the `heap`: `heappush(heap, (neighbor_height, nr, nc))`.
4.  **Return `total_water`.**

## Knowledge Base References

*   **Core Algorithm:** [[../document/algorithms/graph_search/heap_dfs_boundary_fill.md]] (Details the specific Heap + DFS boundary approach).
*   **General Pattern:** [[../document/patterns/array/find_capacity_between_boundaries.md]] (Discusses the general capacity problem and the 2D heap approach).
*   **Optimization:** [[../document/optimizations/grid_traversal/heap_dfs_vs_bfs_boundary_fill.md]] (Compares Heap+DFS vs Heap+BFS).
*   **Data Structures:** [[../document/data_structures/heap_priority_queue.md]]

## Complexity Analysis

Let R = rows, C = cols, N = R * C.
*   **Time Complexity:** O(R * C * log(R * C)). Each cell is visited once. In the worst case, most cells could be pushed onto the heap, leading to O(N log N) complexity dominated by heap operations.
*   **Space Complexity:** O(R * C). The heap and the DFS stack can potentially store up to O(N) elements in the worst case. Using in-place marking avoids extra space for a visited matrix. 