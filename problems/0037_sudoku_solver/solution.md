## Problem Summary

Write a program to solve a Sudoku puzzle by filling the empty cells. A Sudoku solution must satisfy all of the following rules:
1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.
The `.` character indicates empty cells.

## Algorithmic Approach

The solution uses an optimized **backtracking algorithm**. Key optimizations include:
1.  **Bitmask State Tracking:** Integers are used as bitmasks to efficiently track which numbers (1-9) are already present in each row, column, and 3x3 box. The `k`-th bit (0-indexed) represents the number `k+1`.
2.  **Minimum Remaining Values (MRV) Heuristic:** Instead of processing empty cells in a fixed order, the algorithm selects the empty cell with the *fewest* possible valid numbers to try next. This often prunes the search space more effectively.

## Logic Explanation

1.  **Initialization:**
    *   Create bitmask arrays (`rows`, `cols`, `boxes`) initialized to 0.
    *   Create a list `empty_cells` to store the coordinates `(r, c)` of all empty cells (`.`).
    *   Iterate through the initial board:
        *   If a cell `(r, c)` contains a number `d`, update the corresponding `rows[r]`, `cols[c]`, and `boxes[box_idx]` bitmasks by setting the `(d-1)`-th bit using bitwise OR (`|= 1 << (d - 1)`).
        *   If a cell is empty, add its `(r, c)` coordinates to `empty_cells`.

2.  **Helper Functions:**
    *   `count_set_bits(num)`: Counts the number of set bits in a mask (used by MRV).
    *   `get_possible_values(r, c)`: Calculates a bitmask representing the possible numbers (1-9) that can be placed at `(r, c)`. It does this by OR-ing the masks for the row, column, and box, inverting the result (`~`), and masking with `0x1FF` (binary `111111111`) to keep only bits 0-8.
    *   `find_best_empty_cell()`: Implements the MRV heuristic. It iterates through `empty_cells`, calculates the number of possible values for each using `get_possible_values` and `count_set_bits`, and returns the cell info (`r`, `c`, `index_in_list`) with the minimum number of possibilities. Returns `None` if any cell has 0 possibilities (immediate failure).

3.  **Backtracking Function (`backtrack()`):**
    *   **Base Case:** If `empty_cells` is empty, the board is solved. Return `True`.
    *   **Select Cell (MRV):** Call `find_best_empty_cell()` to get the next cell `(r, c)` to process and its index `idx` in the `empty_cells` list.
    *   **Check for Failure:** If `find_best_empty_cell` returned `None` (indicating a conflict), return `False`.
    *   **Remove Cell:** Temporarily remove the selected cell from `empty_cells` (using `pop(idx)`). This ensures it's not reconsidered in recursive calls until backtracking restores it.
    *   **Try Numbers:** Get the `possible_mask` for the selected cell `(r, c)`. Iterate through digits `d` from 1 to 9.
        *   Check if `d` is possible: `if possible_mask & (1 << (d - 1))`.
        *   If `d` is possible:
            *   **Place:** Put `str(d)` on the board. Update `rows`, `cols`, and `boxes` masks by setting the `(d-1)`-th bit.
            *   **Recurse:** Call `backtrack()`.
            *   **Check Result:** If the recursive call returns `True`, a solution is found. **Crucially, re-insert the processed cell** into `empty_cells` at its original `idx` before returning `True` up the call stack.
            *   **Backtrack (Undo):** If the recursive call returns `False`, remove the placed digit (`board[r][c] = '.'`) and clear the corresponding bit in the `rows`, `cols`, and `boxes` masks using bitwise AND with the inverted bit (`&= ~(1 << (d - 1))`).
    *   **Restore Cell & Return False:** If the loop finishes without finding a valid number for the current cell, **re-insert the processed cell** into `empty_cells` at its original `idx` and return `False`.

4.  **Initial Call:** Start the process by calling `backtrack()`.

## Knowledge Base References

*   **Algorithm:** `document/algorithms/recursion/backtracking.md`
*   **Optimization Technique:** `document/techniques/bitmask_state_tracking.md` (used for tracking used numbers in rows, columns, boxes).
*   **Heuristic:** `document/patterns/mrv_heuristic.md` (used to select the next cell to fill).

## Complexity Analysis

*   **Time Complexity:** Hard to determine precisely due to the heuristic pruning, but in the worst case, it's roughly O(9^(N*N)), where N=9. For each empty cell, we might try up to 9 possibilities. However, the constraints and MRV make it much faster in practice for typical Sudoku puzzles.
*   **Space Complexity:** O(N*N) or O(81) for the board itself. O(N) or O(9) for the bitmask arrays. O(E) for `empty_cells` list (where E <= 81). The recursion depth can go up to E in the worst case. So, roughly O(N*N) or O(81) dominated by the board and recursion stack. 