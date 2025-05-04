# LeetCode 51: N-Queens - Solution Explanation

## Problem Summary

The N-Queens puzzle involves placing `n` non-attacking queens on an `n x n` chessboard. The goal is to find all distinct configurations where no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).

## Algorithmic Approach: Backtracking

This problem is a classic example solved using the **Backtracking** algorithm.

We attempt to place queens row by row, from row 0 to `n-1`. For each row, we try placing a queen in each column. If placing a queen in column `c` of the current row `r` violates the constraints (attacks another queen), we abandon that choice and try the next column. If a placement is valid, we mark the position as occupied and recursively attempt to place a queen in the next row (`r+1`). If the recursive call returns (meaning it either found solutions or exhausted possibilities), we "backtrack" by removing the queen from `(r, c)` and unmarking its occupied status, allowing us to explore other possibilities for row `r`.

## Logic Explanation

1.  **State Tracking:**
    *   We need to efficiently check if placing a queen at `(r, c)` is valid.
    *   Rows are handled implicitly by the recursion (`_backtrack(row)`).
    *   `occupied_cols`: A set stores columns already occupied by queens in previous rows.
    *   `occupied_pos_diagonals`: A set stores occupied positive diagonals. All cells `(r, c)` on the same positive diagonal have a constant `r + c`.
    *   `occupied_neg_diagonals`: A set stores occupied negative diagonals. All cells `(r, c)` on the same negative diagonal have a constant `r - c`.
    *   `queen_cols`: A list of size `n` where `queen_cols[r]` stores the column index of the queen placed in row `r`. Used to build the final board representation.
2.  **`_backtrack(row)` Function:**
    *   **Base Case:** If `row == n`, all `n` queens have been placed successfully. Construct the board using `_build_board()` from `queen_cols` and add it to the `solutions` list.
    *   **Recursive Step:** Iterate through columns `col` from 0 to `n-1` for the current `row`:
        *   Calculate `pos_diag = row + col` and `neg_diag = row - col`.
        *   **Check Constraints:** If `col` is in `occupied_cols` OR `pos_diag` is in `occupied_pos_diagonals` OR `neg_diag` is in `occupied_neg_diagonals`, then placing a queen at `(row, col)` is invalid. `continue` to the next column.
        *   **Place Queen:** If valid, mark the position as occupied:
            *   `queen_cols[row] = col`
            *   Add `col` to `occupied_cols`.
            *   Add `pos_diag` to `occupied_pos_diagonals`.
            *   Add `neg_diag` to `occupied_neg_diagonals`.
        *   **Recurse:** Call `_backtrack(row + 1)`.
        *   **Backtrack (Undo):** After the recursive call returns, unmark the position:
            *   Remove `col` from `occupied_cols`.
            *   Remove `pos_diag` from `occupied_pos_diagonals`.
            *   Remove `neg_diag` from `occupied_neg_diagonals`.
3.  **Initialization:** Call `_backtrack(0)` to start the process.

## Knowledge Base References

*   **Core Algorithm:** [[../document/algorithms/recursion/backtracking.md]] (Explains the backtracking template and includes N-Queens as an example, highlighting the O(1) constraint checks using sets).
*   **Data Structures:** [[../document/data_structures/hash_set.md]] (Used for efficient O(1) lookups of occupied columns/diagonals).

## Complexity Analysis

*   **Time Complexity:** Difficult to state precisely, but bounded by O(N!). The algorithm explores a permutation-like state space but prunes branches significantly using the constraints. Each step within the backtracking takes O(1) time due to the use of sets for constraint checking.
*   **Space Complexity:** O(N) to store the `queen_cols` list, the occupied sets, and the recursion call stack depth. 