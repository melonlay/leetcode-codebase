class Solution:
    """Solves the N-Queens II problem using optimized backtracking with bitmasks."""

    def totalNQueens(self, n: int) -> int:
        """
        Calculates the total number of distinct solutions using bit manipulation.

        Args:
            n: The size of the chessboard (n x n).

        Returns:
            The total number of distinct solutions.
        """
        self.count = 0
        # Mask for all columns (e.g., n=4 -> 1111)
        self.all_cols_mask = (1 << n) - 1

        def _backtrack(row: int, cols_mask: int, neg_diag_mask: int, pos_diag_mask: int):
            """Recursive helper using bitmasks.

            Args:
                row: Current row index.
                cols_mask: Bitmask of occupied columns.
                neg_diag_mask: Bitmask of occupied negative diagonals (shifted).
                pos_diag_mask: Bitmask of occupied positive diagonals (shifted).
            """
            if row == n:
                self.count += 1
                return

            # Calculate all occupied positions for the current row
            # Combine column, negative diagonal (shifted left for current row view),
            # and positive diagonal (shifted right for current row view)
            # Note: The way diagonals are stored requires shifting them
            # appropriately when considering the *current* row.
            # It's often easier to think about the masks representing the *next* row's state.
            # Let's adjust the recursive call instead.

            # Optimized approach: Calculate available positions directly for the current row
            occupied_mask = cols_mask | neg_diag_mask | pos_diag_mask
            available_pos_mask = self.all_cols_mask & (~occupied_mask)

            # Iterate through each available position (column) for the current row
            while available_pos_mask:
                # Get the least significant bit (LSB) which represents the column to place the queen
                pos = available_pos_mask & (-available_pos_mask)

                # Remove this position from the available mask for the next iteration
                available_pos_mask -= pos

                # Recurse to the next row with updated masks
                # cols_mask | pos: Marks the current column as occupied.
                # (neg_diag_mask | pos) >> 1: Marks the negative diagonal and shifts right for the next row.
                # (pos_diag_mask | pos) << 1: Marks the positive diagonal and shifts left for the next row.
                _backtrack(row + 1,
                           cols_mask | pos,
                           (neg_diag_mask | pos) >> 1,
                           (pos_diag_mask | pos) << 1)

        # Initial call: Start at row 0 with all masks empty (0)
        _backtrack(0, 0, 0, 0)
        return self.count
