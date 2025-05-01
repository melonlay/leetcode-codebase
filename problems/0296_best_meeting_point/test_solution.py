import unittest
from .solution import Solution  # Relative import


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solver = Solution()

    def test_example1(self):
        """Test the first example provided in the problem description."""
        grid = [
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]
        ]
        expected = 6
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed example 1")

    def test_example2(self):
        """Test the second example provided in the problem description."""
        grid = [[1, 1]]
        # Homes at (0,0) and (0,1). Median row=0, median col=0 or 1. Meet at (0,0): dist = 0+1=1. Meet at (0,1): dist = 1+0=1.
        expected = 1
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed example 2")

    def test_single_row(self):
        """Test a grid with homes only in a single row."""
        grid = [[0, 1, 0, 1, 0, 1]]  # Homes at (0,1), (0,3), (0,5)
        # Rows = [0, 0, 0]. Median row = 0. Row dist = |0-0| + |0-0| + |0-0| = 0
        # Cols = [1, 3, 5]. Median col = 3. Col dist = |1-3| + |3-3| + |5-3| = 2 + 0 + 2 = 4
        expected = 4
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed single row test")

    def test_single_col(self):
        """Test a grid with homes only in a single column."""
        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]  # Homes at (0,1), (2,1), (3,1)
        # Rows = [0, 2, 3]. Median row = 2. Row dist = |0-2| + |2-2| + |3-2| = 2 + 0 + 1 = 3
        # Cols = [1, 1, 1]. Median col = 1. Col dist = |1-1| + |1-1| + |1-1| = 0
        expected = 3
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed single column test")

    def test_scattered(self):
        """Test a grid with scattered homes."""
        grid = [
            [1, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]  # Homes: (0,0), (0,2), (1,3), (2,1), (3,0)
        # Rows = [0, 0, 1, 2, 3]. Median row = 1. Row dist = |0-1|+|0-1|+|1-1|+|2-1|+|3-1| = 1+1+0+1+2 = 5
        # Cols = [0, 0, 1, 2, 3]. Median col = 1. Col dist = |0-1|+|0-1|+|1-1|+|2-1|+|3-1| = 1+1+0+1+2 = 5
        # Alternative calculation 1D:
        # Rows sorted: [0, 0, 1, 2, 3]. Dist = (3-0) + (2-0) = 3 + 2 = 5
        # Cols sorted: [0, 0, 1, 2, 3]. Dist = (3-0) + (2-0) = 3 + 2 = 5
        expected = 10
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed scattered test")

    def test_two_homes_diagonal(self):
        """Test with exactly two homes placed diagonally."""
        grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]  # Homes at (0,0), (2,2)
        # Rows = [0, 2]. Median can be 0, 1, or 2. Let's use calculation method.
        # Row dist = (2-0) = 2
        # Cols = [0, 2]. Col dist = (2-0) = 2
        expected = 4
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed two homes diagonal")

    def test_two_homes_same_row(self):
        """Test with exactly two homes in the same row."""
        grid = [[1, 0, 0, 1]]  # Homes at (0,0), (0,3)
        # Rows = [0, 0]. Row dist = 0
        # Cols = [0, 3]. Col dist = (3-0) = 3
        expected = 3
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed two homes same row")

    def test_two_homes_same_col(self):
        """Test with exactly two homes in the same column."""
        grid = [
            [0, 1],
            [0, 0],
            [0, 1]
        ]  # Homes at (0,1), (2,1)
        # Rows = [0, 2]. Row dist = (2-0) = 2
        # Cols = [1, 1]. Col dist = 0
        expected = 2
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed two homes same column")

    def test_all_homes(self):
        """Test a grid where every cell is a home."""
        grid = [
            [1, 1],
            [1, 1]
        ]  # Homes at (0,0), (0,1), (1,0), (1,1)
        # Rows = [0, 0, 1, 1]. Row dist = (1-0) + (1-0) = 2
        # Cols = [0, 0, 1, 1]. Col dist = (1-0) + (1-0) = 2
        expected = 4
        self.assertEqual(self.solver.minTotalDistance(
            grid), expected, "Failed all homes test")


if __name__ == '__main__':
    unittest.main()
