import unittest
from typing import List

from .solution import Solution


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 0]
        expected = 3
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_example2(self):
        nums = [3, 4, -1, 1]
        expected = 2
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_example3(self):
        nums = [7, 8, 9, 11, 12]
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_all_positives_present(self):
        nums = [1, 2, 3, 4, 5]
        expected = 6
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_all_negatives_or_zero(self):
        nums = [-1, -2, -3, 0]
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_empty_list_constraint(self):
        # Constraint is 1 <= nums.length <= 10^5
        # Testing the smallest valid size
        nums = [1]
        expected = 2
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")
        nums = [2]
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")
        nums = [0]
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")
        nums = [-5]
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_duplicates(self):
        nums = [1, 1, 2, 2]
        expected = 3
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")
        nums = [1, 1]
        expected = 2
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_large_numbers_out_of_range(self):
        nums = [1, 2, 100, 200, 3]
        expected = 4
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_mixed_order(self):
        nums = [2, 1]
        expected = 3
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_complex_case(self):
        nums = [2, 3, -7, 6, 8, 1, 10, 9, 4, 5]
        expected = 7  # After placing 1-6 and 8-10, index 6 should be where 7 is missing
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on nums = {nums}")

    def test_stress_size(self):
        # Stress test with max size (consider skipping if too slow)
        # Creates [1, 2, ..., 100000]
        n = 10**5
        nums = list(range(1, n + 1))
        expected = n + 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on large consecutive list")

        # Creates [2, 3, ..., 100001], missing 1
        nums = list(range(2, n + 2))
        expected = 1
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, expected, f"Failed on large list missing 1")


if __name__ == '__main__':
    unittest.main()
