## 51. N-Queens Solution Explanation

### Problem Summary

The N-Queens puzzle asks for all distinct ways to place `n` non-attacking queens on an `n x n` chessboard. Two queens attack each other if they are in the same row, column, or diagonal.

### Algorithmic Approach

The problem is solved using a **Backtracking** algorithm, as described in `document/algorithms/recursion/backtracking.md`. The core idea is to place queens row by row, exploring possible column placements in each row.

1.  **State Representation:**
    *   We use a list `queen_cols` where `queen_cols[r]` stores the column index of the queen placed in row `r`.
    *   Three sets are used for O(1) validity checks:
        *   `occupied_cols`: Stores columns currently occupied by a queen.
        *   `occupied_pos_diagonals`: Stores diagonals with a positive slope (identified by `row + col`) that are occupied.
        *   `occupied_neg_diagonals`: Stores diagonals with a negative slope (identified by `row - col`) that are occupied.
    *   These sets allow efficient checking, similar to using hash sets/tables (`document/data_structures/hash_table_dict.md`).

2.  **Backtracking Function (`_backtrack(row)`):**
    *   **Base Case:** If `row == n`, it means we have successfully placed `n` queens (one in each row from 0 to `n-1`). A valid solution is found. We construct the board representation (a `List[str]`) using a helper function `_build_board()` based on the `queen_cols` array and add it to the `solutions` list.
    *   **Recursive Step:** For the current `row`, iterate through all possible columns (`col` from 0 to `n-1`).
        *   **Constraint Check:** Before placing a queen at `(row, col)`, check if this position is under attack by any previously placed queen. This is done efficiently by checking if `col` is in `occupied_cols`, `row + col` is in `occupied_pos_diagonals`, or `row - col` is in `occupied_neg_diagonals`.
        *   **Place Queen:** If the position is safe, place the queen:
            *   Record the placement: `queen_cols[row] = col`.
            *   Update the tracking sets: Add `col`, `row + col`, and `row - col` to their respective sets.
        *   **Recurse:** Call `_backtrack(row + 1)` to attempt placing a queen in the next row.
        *   **Backtrack (Undo Choice):** After the recursive call returns (meaning all possibilities stemming from placing the queen at `(row, col)` have been explored), remove the queen's influence to explore other possibilities for the current `row`. This involves removing `col`, `row + col`, and `row - col` from the tracking sets. The `queen_cols[row]` value doesn't strictly need to be reset as it will be overwritten by the next valid placement in the loop or ignored if the function returns.

3.  **Initialization:** Start the process by calling `_backtrack(0)`.

4.  **Result:** The function returns the `solutions` list containing all valid board configurations.

### Complexity Analysis

*   **Time Complexity:** O(N!), where N is `n`. Although the state space looks like O(N^N), the constraints (pruning invalid branches early) significantly reduce the explored states. In the worst case, the number of solutions can grow factorially.
*   **Space Complexity:** O(N^2) in the worst case. This is dominated by the space needed to store all the solutions found. Each solution requires O(N^2) space for the board representation. The recursion depth and the sets used for tracking require O(N) space.

### Knowledge Base References

*   **Algorithm:** `document/algorithms/recursion/backtracking.md`
*   **Data Structure:** Sets provide O(1) lookups, conceptually similar to hash tables (`document/data_structures/hash_table_dict.md`). 