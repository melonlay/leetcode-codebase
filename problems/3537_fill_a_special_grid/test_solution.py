import unittest
# Use relative import for testing within the package structure
from .solution import Solution


class TestSpecialGrid(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solver = Solution()

    def test_n_0(self):
        """Test the base case N=0."""
        self.assertEqual(self.solver.specialGrid(0), [[0]])

    def test_n_1(self):
        """Test the case N=1."""
        expected = [[3, 0], [2, 1]]
        self.assertEqual(self.solver.specialGrid(1), expected)

    def test_n_2(self):
        """Test the case N=2."""
        expected = [
            [15, 12, 3, 0],
            [14, 13, 2, 1],
            [11, 8, 7, 4],
            [10, 9, 6, 5]
        ]
        self.assertEqual(self.solver.specialGrid(2), expected)


if __name__ == '__main__':
    unittest.main()
