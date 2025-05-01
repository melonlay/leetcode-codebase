## Problem Summary

LeetCode 52: N-Queens II asks for the total number of distinct ways to place `n` queens on an `n x n` chessboard such that no two queens threaten each other. Unlike N-Queens I, we only need the count, not the board configurations.

## Algorithmic Approach (Optimized with Bitmasks)

The solution uses an optimized **backtracking algorithm** leveraging **bit manipulation** for efficient state tracking and conflict detection. This is significantly faster for constraints like `n <= 9` compared to using sets or lists.

See `document/algorithms/recursion/backtracking.md` for the general backtracking pattern. The use of bitmasks here is a specific optimization technique for grid-based problems, detailed in `document/techniques/bitmask_state_tracking.md`.

The core idea remains placing queens row by row, but state is managed using integers (bitmasks):

1.  **State Representation (Bitmasks):** Referencing `document/techniques/bitmask_state_tracking.md` for general bitmask operations.
    *   `cols_mask`: An integer where the `i`-th bit is set (1) if column `i` is occupied in previous rows.
    *   `neg_diag_mask`: An integer representing occupied negative diagonals (top-right to bottom-left). The bit position corresponds to `row - col + n - 1`, but the mask is dynamically shifted right (`>> 1`) in recursive calls to align with the next row.
    *   `pos_diag_mask`: An integer representing occupied positive diagonals (top-left to bottom-right). The bit position corresponds to `row + col`, but the mask is dynamically shifted left (`<< 1`) in recursive calls to align with the next row.
    *   `all_cols_mask`: A precomputed mask with the lower `n` bits set (e.g., `(1 << n) - 1`), used to filter valid column positions.
    *   `self.count`: Stores the total number of solutions found.

2.  **Recursive Helper (`_backtrack`):**
    *   **Base Case:** If `row == n`, a valid placement of `n` queens is found. Increment `self.count` and return.
    *   **Calculate Available Positions:** Determine the columns available in the current `row` using bitwise operations (see `document/techniques/bitmask_state_tracking.md`):
        *   `occupied_mask = cols_mask | neg_diag_mask | pos_diag_mask`: Combine all masks representing occupied positions projected onto the current row.
        *   `available_pos_mask = self.all_cols_mask & (~occupied_mask)`: Find bits (columns) that are *not* occupied.
    *   **Iterate Through Available Positions:**
        *   Use a `while available_pos_mask:` loop.
        *   `pos = available_pos_mask & (-available_pos_mask)`: Extract the least significant bit (LSB) using the two's complement trick. `pos` is now a bitmask with only one bit set, representing the column to place the queen.
        *   `available_pos_mask -= pos` (or `&= (available_pos_mask - 1)`): Remove the processed position (column) from the mask.
    *   **Recurse (Place Queen):** Call `_backtrack` for the next row (`row + 1`) with updated masks:
        *   New `cols_mask`: `cols_mask | pos` (mark the column as occupied).
        *   New `neg_diag_mask`: `(neg_diag_mask | pos) >> 1` (mark the diagonal and shift right for the next row's perspective).
        *   New `pos_diag_mask`: `(pos_diag_mask | pos) << 1` (mark the diagonal and shift left for the next row's perspective).
    *   **Backtracking:** Backtracking is implicit. Because we pass updated masks to the recursive call without modifying the *current* function's mask variables, when the recursion returns, the masks revert to their state before the call. The `while` loop then continues to the next available position in the current row.

3.  **Initialization:** Start the process by calling `_backtrack(0, 0, 0, 0)` (row 0, all masks empty).

4.  **Result:** Return `self.count`.

## Complexity Analysis (Bitmask Version)

*   **Time Complexity:** O(N!). The fundamental number of states explored remains factorial, but the work done per state is reduced to efficient bitwise operations, leading to significant constant factor improvements over set/list-based approaches for small N.
*   **Space Complexity:** O(N). Primarily due to the recursion depth. The space used for masks is constant (O(1) integers).

---

*(Previous approach used sets for tracking conflicts, which is conceptually simpler but slower due to object overhead compared to bitwise operations)* 