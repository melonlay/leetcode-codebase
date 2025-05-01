import unittest
from typing import List
from .solution import Solution


def sort_solutions(solutions: List[List[str]]) -> List[List[str]]:
    """Sorts the list of board solutions for consistent comparison."""
    # Sort each board representation internally (optional, but good practice if needed)
    # Then sort the list of boards based on their string representation
    return sorted(solutions, key=lambda board: "\n".join(board))


class TestSolution(unittest.TestCase):
    """Tests the Solution class for N-Queens."""

    def setUp(self):
        """Set up the test environment."""
        self.solution = Solution()

    def assertCountEqualBoards(self, actual: List[List[str]], expected: List[List[str]]):
        """Asserts that two lists of board solutions are equal, ignoring order."""
        self.assertCountEqual(sort_solutions(actual), sort_solutions(expected))

    def test_example_1(self):
        """Tests the first example case (n=4)."""
        n = 4
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        result = self.solution.solveNQueens(n)
        self.assertCountEqualBoards(result, expected)

    def test_example_2(self):
        """Tests the second example case (n=1)."""
        n = 1
        expected = [["Q"]]
        result = self.solution.solveNQueens(n)
        self.assertCountEqualBoards(result, expected)

    def test_no_solution_n2(self):
        """Tests the case where n=2 (no solution)."""
        n = 2
        expected: List[List[str]] = []
        result = self.solution.solveNQueens(n)
        self.assertCountEqualBoards(result, expected)

    def test_no_solution_n3(self):
        """Tests the case where n=3 (no solution)."""
        n = 3
        expected: List[List[str]] = []
        result = self.solution.solveNQueens(n)
        self.assertCountEqualBoards(result, expected)

    def test_n5(self):
        """Tests a slightly larger case (n=5)."""
        n = 5
        # Manually verified or generated expected solutions for n=5
        expected = [
            ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
            ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
            [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
            [".Q...", "....Q", "..Q..", "Q....", "...Q."],
            ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
            ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
            ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
            ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
            ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
            ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]
        ]
        result = self.solution.solveNQueens(n)
        self.assertCountEqualBoards(result, expected)

    # @unittest.skip("Skipping n=9 test due to potentially long runtime")
    def test_max_constraint_n9(self):
        """Tests the maximum constraint (n=9). Checks only the count."""
        n = 9
        # Expected number of solutions for n=9 is 352
        expected_count = 352
        result = self.solution.solveNQueens(n)
        self.assertEqual(len(result), expected_count,
                         f"Expected {expected_count} solutions for n=9, but got {len(result)}")


if __name__ == '__main__':
    unittest.main()
