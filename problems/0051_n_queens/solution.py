from typing import List, Set


class Solution:
    """Solves the N-Queens problem using backtracking."""

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Finds all distinct solutions to the N-Queens puzzle.

        Args:
            n: The size of the chessboard (n x n) and the number of queens.

        Returns:
            A list of all distinct board configurations representing solutions.
        """
        solutions: List[List[str]] = []
        # Store the column index of the queen for each row
        queen_cols: List[int] = [-1] * n

        # Sets to track occupied columns and diagonals
        occupied_cols: Set[int] = set()
        occupied_pos_diagonals: Set[int] = set()  # row + col
        occupied_neg_diagonals: Set[int] = set()  # row - col

        def _build_board() -> List[str]:
            """Constructs the board representation from queen_cols."""
            board = []
            for r in range(n):
                col = queen_cols[r]
                board.append("." * col + "Q" + "." * (n - 1 - col))
            return board

        def _backtrack(row: int):
            """Recursive helper function to place queens row by row."""
            if row == n:
                # Found a valid solution
                solutions.append(_build_board())
                return

            for col in range(n):
                pos_diag = row + col
                neg_diag = row - col

                # Check if the current position is under attack
                if (col in occupied_cols or
                    pos_diag in occupied_pos_diagonals or
                        neg_diag in occupied_neg_diagonals):
                    continue  # Skip this column

                # Place the queen
                queen_cols[row] = col
                occupied_cols.add(col)
                occupied_pos_diagonals.add(pos_diag)
                occupied_neg_diagonals.add(neg_diag)

                # Recurse to the next row
                _backtrack(row + 1)

                # Backtrack: Remove the queen and its influence
                occupied_cols.remove(col)
                occupied_pos_diagonals.remove(pos_diag)
                occupied_neg_diagonals.remove(neg_diag)
                # No need to reset queen_cols[row] as it will be overwritten

        _backtrack(0)  # Start placing from row 0
        return solutions
