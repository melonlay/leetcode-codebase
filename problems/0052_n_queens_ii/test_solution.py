import unittest
from .solution import Solution  # Use relative import


class TestTotalNQueens(unittest.TestCase):
    """Test cases for LeetCode 52: N-Queens II."""

    def setUp(self):
        """Set up the Solution object for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example provided: n = 4."""
        self.assertEqual(self.solution.totalNQueens(4), 2)

    def test_example_2(self):
        """Test the second example provided: n = 1."""
        self.assertEqual(self.solution.totalNQueens(1), 1)

    def test_small_n_no_solution(self):
        """Test cases where n is small and no solution exists."""
        self.assertEqual(self.solution.totalNQueens(2), 0)
        self.assertEqual(self.solution.totalNQueens(3), 0)

    def test_medium_n(self):
        """Test cases for medium values of n."""
        self.assertEqual(self.solution.totalNQueens(5), 10)
        self.assertEqual(self.solution.totalNQueens(6), 4)
        self.assertEqual(self.solution.totalNQueens(7), 40)
        self.assertEqual(self.solution.totalNQueens(8), 92)

    def test_max_constraint(self):
        """Test the maximum constraint value: n = 9."""
        # This is the largest value allowed by constraints
        self.assertEqual(self.solution.totalNQueens(9), 352)


if __name__ == '__main__':
    unittest.main()
