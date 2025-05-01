# 407. Trapping Rain Water II (Hard)

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return *the volume of water it can trap after raining*.

## Example 1:

**Input:** `heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]`
**Output:** 4
**Explanation:** After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

**Visual Representation (Conceptual):**

Imagine a 3x6 grid of blocks with heights given by the input.

```
Row 0: [1, 4, 3, 1, 3, 2]
Row 1: [3, 2, 1, 3, 2, 4]
Row 2: [2, 3, 3, 2, 3, 1]
```

Water can be trapped in lower areas surrounded by higher walls.
- The cell at `(1, 2)` with height 1 is surrounded by higher cells (3, 2, 3, 3). It can hold water up to the lowest neighbor boundary it shares, which might be complex to visualize directly but think of the 'walls' surrounding it. The example implies 1 unit of water here.
- The cell at `(1, 4)` with height 2 is also surrounded. The example implies 3 units of water here (likely up to height 3?).

Total trapped water = 1 + 3 = 4.

## Example 2:

**Input:** `heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]`
**Output:** 10

**Visual Representation (Conceptual):**

A 5x5 grid. The outer border cells all have height 3. The inner cells form a depression.

```
[3, 3, 3, 3, 3]
[3, 2, 2, 2, 3]
[3, 2, 1, 2, 3]
[3, 2, 2, 2, 3]
[3, 3, 3, 3, 3]
```
The inner 3x3 cells are lower than the surrounding border of height 3.
- Central cell (2, 2) height 1: Traps `3 - 1 = 2` units.
- Cells with height 2 (adjacent to center): Traps `3 - 2 = 1` unit each. There are 8 such cells.
Total water = 2 + (8 * 1) = 10.

## Constraints:

*   `m == heightMap.length`
*   `n == heightMap[i].length`
*   `1 <= m, n <= 200`
*   `0 <= heightMap[i][j] <= 2 * 10^4`

## Topics

*   Array
*   Breadth-First Search (BFS)
*   Heap (Priority Queue)
*   Matrix
