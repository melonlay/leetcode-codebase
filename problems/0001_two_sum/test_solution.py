import unittest
from .solution import Solution  # Relative import from the same directory


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        """
        Set up the Solution instance before each test.
        """
        self.solver = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solver.twoSum(nums, target)
        # Sort because the order doesn't matter
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_min_size(self):
        nums = [1, 2]
        target = 3
        expected = [0, 1]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_negative_numbers(self):
        nums = [-1, -3, 5, 10]
        target = -4
        expected = [0, 1]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_zero_involved(self):
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_large_numbers(self):
        nums = [10**9, -10**9, 5, 2]
        target = 7
        expected = [2, 3]
        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_large_array(self):
        # Stress test with array size close to 10^4
        # Ensure the target pair is unique and placed towards the end
        n = 10000
        # Initialize with numbers unlikely to sum to the target accidentally
        # Start range high, e.g., [10000, 10001, ...]
        nums = [i + n for i in range(n)]

        # Define the unique pair and target
        val1 = 15000
        val2 = 25000
        idx1 = n // 2       # Place somewhere in the middle/end
        idx2 = n - 1
        nums[idx1] = val1
        nums[idx2] = val2
        target = val1 + val2
        expected = [idx1, idx2]

        result = self.solver.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
