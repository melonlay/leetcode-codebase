# LeetCode 407: Trapping Rain Water II

## Problem Summary

Given a 2D `m x n` matrix representing an elevation map, calculate the total volume of rainwater that can be trapped within the map after raining.

## Solution Approach: Min-Heap (Priority Queue) + DFS

This problem extends the 1D "Trapping Rain Water" concept to 2D. Simple linear scan approaches fail due to the complex 2D boundary.

The core idea is to simulate water filling from the outside inwards. Water is held back by the outer grid boundary and internal high points. The water level in any pool is limited by the lowest point on its surrounding effective wall.

We use a Min-Heap to manage the boundary wall segments, always processing the lowest segment first. From that segment, we use Depth-First Search (DFS) to explore the connected area that can be reached without exceeding the height of that segment.

**Algorithm:**

1.  **Initialization:**
    *   Check for trivial cases: If `m` or `n` is less than or equal to 2, return 0.
    *   Create a min-heap to store boundary cells as `(height, row, col)`.
    *   Initialize `total_water = 0`.
    *   **Visited Tracking:** Modify the input `heightMap` in-place. Mark visited cells with `-1` to save space compared to a separate boolean matrix.

2.  **Add Initial Boundaries to Heap:**
    *   Iterate through all cells on the border (first/last row, first/last column).
    *   If a border cell hasn't been marked visited yet (important for corners/small maps), push `(heightMap[r][c], r, c)` onto the heap and mark it as visited (`heightMap[r][c] = -1`).

3.  **Process Boundaries and Explore Pools (Heap + DFS):**
    *   Use a `while heap:` loop (continues as long as there are boundary segments to process).
    *   **Extract Lowest Boundary:** Pop the cell `(level, r_min, c_min)` with the minimum height (`level`) from the heap. This `level` represents the lowest known point on the current boundary surrounding unexplored areas.
    *   **Start DFS:** Initialize a DFS `stack` with the popped cell `(r_min, c_min)`.
    *   **DFS Loop:** Use a `while stack:` loop:
        *   Pop a cell `(r, c)` from the DFS stack.
        *   **Explore Neighbors:** For each 4-directional neighbor `(nr, nc)`:
            *   Check if the neighbor is within grid bounds (`0 <= nr < m`, `0 <= nc < n`).
            *   Check if the neighbor is **unvisited** (`heightMap[nr][nc] != -1`).
            *   Let `neighbor_height = heightMap[nr][nc]`.
            *   **Case 1: Neighbor Below/At Boundary (`neighbor_height <= level`)**
                *   This neighbor is inside the potential pool defined by the current boundary `level`.
                *   Water trapped at this cell: `total_water += level - neighbor_height`.
                *   Continue exploring this pool: Add `(nr, nc)` to the DFS `stack`.
            *   **Case 2: Neighbor Above Boundary (`neighbor_height > level`)**
                *   This neighbor is part of a *higher* wall segment bounding a potentially deeper pool.
                *   Add this new boundary segment to the min-heap: `heappush(heap, (neighbor_height, nr, nc))`.
            *   **Mark Visited:** Set `heightMap[nr][nc] = -1`.

4.  **Termination:**
    *   The outer `while heap:` loop finishes when all reachable cells have been visited (either via DFS or by being pushed onto the heap as boundaries).
    *   Return `total_water`.

## Why it Works

The min-heap ensures we always process the lowest point (`level`) on the current boundary wall. The DFS efficiently explores all connected cells that are definitely below or at this `level`. Any trapped water found during DFS is added based on this confirmed `level`. Cells higher than `level` encountered during DFS become new boundary candidates, added to the heap to define the walls for potentially deeper pools processed later.

The in-place marking (`-1`) efficiently tracks visited cells, saving space.

## Complexity Analysis

*   **Time Complexity:** O(m * n * log(m * n)) (or potentially faster in practice)
    *   Adding initial borders: O(m + n).
    *   Each cell is visited at most once (marked -1). When visited, it's either processed in DFS (O(1) stack operations) or pushed onto the heap (O(log K) where K is heap size, max O(m*n)).
    *   In the worst case, most cells might get pushed onto the heap, leading to O(m*n log(m*n)). However, the DFS optimization often reduces the number of heap operations significantly compared to a pure heap-based BFS.
*   **Space Complexity:** O(m * n)
    *   For the min-heap, which can store up to O(m * n) boundary cells.
    *   For the DFS stack, which in the worst case (e.g., a long snake path) could also approach O(m * n).
    *   The in-place modification avoids O(m*n) for a separate visited matrix.

## Knowledge Base Connections

*   **Algorithm:** Combines Priority-Queue based exploration (like Dijkstra/BFS) with Depth-First Search (DFS) for optimization.
*   **Data Structure:** Uses a [Min-Heap (Priority Queue)](../../document/data_structures/heap_priority_queue.md).
*   **Pattern:** An optimized approach for the 2D version of the [Find Capacity Between Boundaries](../../document/patterns/array/find_capacity_between_boundaries.md) pattern.
*   **Technique:** Employs in-place modification of the input array for visited tracking, saving space. 