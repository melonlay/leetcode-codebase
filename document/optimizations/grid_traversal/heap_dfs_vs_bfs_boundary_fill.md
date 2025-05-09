# Optimization: Heap+DFS vs. Heap+BFS for Boundary Fill

## Context

When solving grid problems involving exploring regions limited by boundary heights starting from the edges (like Trapping Rain Water II), two common approaches use a Min-Heap:

1.  **Heap + BFS:** Add initial border cells to the heap. Repeatedly extract the lowest cell `(h, r, c)`. For each unvisited neighbor `(nr, nc)`, calculate trapped water based on `h`, mark visited, and push the neighbor onto the heap with an effective height `max(h, heightMap[nr][nc])`.
2.  **Heap + DFS:** Add initial border cells to the heap. Repeatedly extract the lowest cell `(level, r, c)`. Initiate a DFS from this cell. Neighbors *below* `level` are explored via DFS (stack). Neighbors *above* `level` are pushed onto the heap.

This document discusses the trade-offs.

## Trade-offs

*   **Heap Operations:**
    *   **Heap+BFS:** Potentially pushes almost every cell onto the heap (O(M*N) pushes/pops).
    *   **Heap+DFS:** Only pushes initial border cells and internal cells that form *new, higher boundaries* onto the heap. Cells within a basin below the current boundary level are explored via DFS (O(1) stack operations). This often leads to significantly fewer heap operations (O(log K)), which can be a major performance win.
*   **Conceptual Complexity:**
    *   **Heap+BFS:** Arguably slightly simpler logic flow.
    *   **Heap+DFS:** Combines two traversal methods, potentially slightly more complex to implement correctly.
*   **Visited Tracking Space:**
    *   Both approaches require tracking visited cells.
    *   **Heap+DFS with In-Place Modification:** Can achieve O(1) *additional* space for visited tracking (beyond heap/stack) if modifying the input grid is allowed. This is a common optimization paired with Heap+DFS.
    *   **Heap+BFS:** Typically requires a separate O(M*N) visited matrix.
*   **Worst-Case Time Complexity:** Remains O(M*N log(M*N)) for both in theory (dominated by heap operations if many cells become boundary points).
*   **Practical Performance:** Heap+DFS often performs noticeably faster due to the reduction in heap operations, especially on maps with large basins.

## Recommendation

For problems like Trapping Rain Water II, the **Heap + DFS** approach, especially when combined with in-place visited marking, is generally the preferred and more optimized solution due to the significant reduction in practical overhead from fewer heap operations.

## Related Concepts

*   [Algorithm: Heap + DFS for Boundary-Limited Grid Fill](../../algorithms/graph_search/heap_dfs_boundary_fill.md)
*   [Algorithm: Breadth-First Search (BFS)](../../algorithms/graph_search/bfs.md)
*   [Algorithm: Depth-First Search (DFS)](../../algorithms/graph_search/dfs.md)
*   [Data Structure: Heap (Priority Queue)](../../data_structures/heap_priority_queue.md)
*   Time/Space Complexity Analysis 