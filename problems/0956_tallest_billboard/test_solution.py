import unittest
from .solution import Solution  # Use relative import


class TestTallestBillboard(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from LeetCode."""
        rods = [1, 2, 3, 6]
        expected = 6
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_example_2(self):
        """Test the second example from LeetCode."""
        rods = [1, 2, 3, 4, 5, 6]
        expected = 10
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_example_3(self):
        """Test the third example from LeetCode (no solution)."""
        rods = [1, 2]
        expected = 0
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_edge_single_rod(self):
        """Test with a single rod."""
        rods = [1]
        expected = 0
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_edge_two_equal_rods(self):
        """Test with two equal rods."""
        rods = [1, 1]
        expected = 1
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_all_same_rods(self):
        """Test with multiple identical rods."""
        rods = [5, 5, 5, 5]
        expected = 10  # Subsets {5, 5} and {5, 5}
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_no_solution_possible(self):
        """Test a case where no two disjoint subsets can sum to the same value."""
        rods = [7, 11, 13]
        expected = 0
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_large_values(self):
        """Test with large rod values."""
        rods = [1000, 1000]
        expected = 1000
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_larger_set(self):
        """Test with a larger set of rods."""
        rods = [61, 45, 43, 54, 40, 50, 48, 49, 42,
                55]  # Example sums: {61,40} = 101, {48,50} = 98? No.. {55,45}=100 {40,61}=101? {54,48}=102 {43,61}=104 {54,50}=104
        # Try to find a solution manually or use a known result if available.
        # Let's manually try: {61, 50} = 111, {55, 54} = 109.. No.
        # {61, 49} = 110, {55, 45} = 100.. No.
        # {61, 43} = 104, {54, 50} = 104. Remaining: [45, 40, 48, 49, 42, 55]
        # Correction: {61, 54, 45, 42} = 202 and {55, 50, 49, 48} = 202
        expected = 202
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_full_constraints(self):
        """Test near max constraints (n=20). Exact result not pre-calculated."""
        rods = list(range(1, 21))  # Sum = 210
        # Expected needs calculation, let's find it.
        # Try to split 210/2 = 105
        # {20, 19, 18, 17, 16, 15} = 105
        # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14} = 105
        # These are disjoint, so 105 is possible.
        expected = 105
        self.assertEqual(self.solution.tallestBillboard(rods), expected)

    def test_empty_input(self):
        """Test with an empty list of rods."""
        rods = []
        expected = 0
        self.assertEqual(self.solution.tallestBillboard(rods), expected)


if __name__ == '__main__':
    unittest.main()
