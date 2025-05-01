import unittest
from .solution import Solution
import copy  # To avoid modifying the original test case board


class TestSudokuSolver(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def is_valid_sudoku(self, board):
        """Checks if a completed Sudoku board is valid."""
        n = 9
        # Check rows
        for r in range(n):
            row_nums = {board[r][c] for c in range(n) if board[r][c] != '.'}
            if len(row_nums) != n:
                return False  # Should have 9 unique numbers
            if not all('1' <= num <= '9' for num in row_nums):
                return False  # Check range

        # Check columns
        for c in range(n):
            col_nums = {board[r][c] for r in range(n) if board[r][c] != '.'}
            if len(col_nums) != n:
                return False
            if not all('1' <= num <= '9' for num in col_nums):
                return False

        # Check 3x3 boxes
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                box_nums = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != '.':
                            box_nums.add(board[r][c])
                if len(box_nums) != n:
                    return False
                if not all('1' <= num <= '9' for num in box_nums):
                    return False

        return True

    def assertBoardEqual(self, board1, board2):
        """Helper method to compare two boards."""
        self.assertEqual(len(board1), len(board2),
                         "Boards have different numbers of rows.")
        for i in range(len(board1)):
            self.assertListEqual(board1[i], board2[i], f"Row {i} differs.")

    def test_example_1(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        # Create a deep copy to pass to the function, as it modifies in-place
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        self.assertBoardEqual(board_copy, expected)

    def test_already_solved(self):
        board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                 ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                 ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                 ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                 ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                 ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                 ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                 ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        expected = copy.deepcopy(board)  # Expected is the same as input
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        self.assertBoardEqual(board_copy, expected)

    def test_sparse_board_validity(self):
        # A board with only a few clues. May have multiple solutions.
        # We will verify if the solver returns *a* valid solution.
        board = [[".", ".", ".", "7", ".", ".", ".", ".", "."],
                 ["1", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", "2", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", "5", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "7", "3"],
                 [".", ".", "2", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", "8", ".", "."]]
        # No expected board needed, we just check validity
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        # Assert that the returned board is a valid Sudoku solution
        self.assertTrue(self.is_valid_sudoku(board_copy),
                        "The returned board is not a valid Sudoku solution.")

    def test_empty_board(self):
        """Test the solver with a completely empty board."""
        board = [["." for _ in range(9)] for _ in range(9)]
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        # Assert that the returned board is a valid Sudoku solution
        self.assertTrue(self.is_valid_sudoku(board_copy),
                        "Solver failed to produce a valid solution for an empty board.")

    def test_minimal_sudoku_unique(self):
        """Test with a known minimal Sudoku puzzle (17 clues) with a unique solution."""
        # Example: Arto Inkala's "World's Hardest Sudoku" (often cited)
        board = [['8', '.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
                 ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
                 ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
                 ['.', '.', '.', '.', '4', '5', '7', '.', '.'],
                 ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
                 ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
                 ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
                 ['.', '9', '.', '.', '.', '.', '4', '.', '.']]

        expected = [['8', '1', '2', '7', '5', '3', '6', '4', '9'],
                    ['9', '4', '3', '6', '8', '2', '1', '7', '5'],
                    ['6', '7', '5', '4', '9', '1', '2', '8', '3'],
                    ['1', '5', '4', '2', '3', '7', '8', '9', '6'],
                    ['3', '6', '9', '8', '4', '5', '7', '2', '1'],
                    ['2', '8', '7', '1', '6', '9', '5', '3', '4'],
                    ['5', '2', '1', '9', '7', '4', '3', '6', '8'],
                    ['4', '3', '8', '5', '2', '6', '9', '1', '7'],
                    ['7', '9', '6', '3', '1', '8', '4', '5', '2']]
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        self.assertBoardEqual(board_copy, expected)

    def test_almost_full_board(self):
        """Test a board that is almost complete, needing only one cell filled."""
        board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                 ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                 ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                 ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                 ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                 ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                 ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                 ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                 ["3", "4", "5", "2", "8", "6", "1", "7", "."]]  # Last cell empty
        expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]  # Expected filled cell
        board_copy = copy.deepcopy(board)
        self.solution.solveSudoku(board_copy)
        self.assertBoardEqual(board_copy, expected)


if __name__ == '__main__':
    unittest.main()
