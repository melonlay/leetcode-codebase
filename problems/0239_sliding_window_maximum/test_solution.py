import unittest
import random
from typing import List
from .solution import Solution

# Helper function (if needed, maybe not for this one)


class TestSlidingWindowMaximum(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_example_2(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_k_equals_n(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 8
        expected = [7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_k_equals_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 1
        expected = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_all_same_elements(self):
        nums = [5, 5, 5, 5, 5]
        k = 3
        expected = [5, 5, 5]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_decreasing_elements(self):
        nums = [9, 8, 7, 6, 5, 4, 3]
        k = 3
        expected = [9, 8, 7, 6, 5]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_increasing_elements(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 4
        expected = [4, 5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_mixed_elements_negative(self):
        nums = [-7, -8, 7, 5, 7, 1, 6, 0]
        k = 4
        expected = [7, 7, 7, 7, 6]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_empty_input(self):
        nums = []
        k = 3
        expected = []
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_k_zero(self):
        nums = [1, 2, 3]
        k = 0
        expected = []
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    # @unittest.skip("Stress test: large input, potentially slow")
    def test_stress_large_input(self):
        n = 10**5
        k = n // 2
        # Create a somewhat varied large input
        nums = [random.randint(-10**4, 10**4) if i % 10 != 0 else 10**4 + i
                for i in range(n)]

        # Manually calculate expected result for large input is infeasible.
        # Instead, we can implement a simpler O(n*k) solution and compare
        # or trust the logic for smaller cases and verify length.
        # Here, we'll just run it and check the length.
        # A more robust test would involve a verified naive solution comparison.

        result = self.solution.maxSlidingWindow(nums, k)

        # Expected number of windows is n - k + 1
        expected_len = n - k + 1
        self.assertEqual(len(result), expected_len)

        # Optional: Verify some properties if possible, e.g., first/last element
        # if calculation is feasible for those.


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
