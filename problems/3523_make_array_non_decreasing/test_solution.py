import unittest
import time
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        nums = [4, 2, 5, 3, 5]
        expected = 3
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed Example 1")

    def test_example_2(self):
        nums = [1, 2, 3]
        expected = 3
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed Example 2")

    # Category 2: Custom Small/Edge Case Validation
    # Note: No reference implementation, relying on manual verification of expected results.
    def test_single_element(self):
        nums = [1]
        expected = 1
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed single element")

    def test_all_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected = 1
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed all decreasing")

    def test_all_equal(self):
        nums = [1, 1, 1, 1]
        expected = 4
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed all equal")

    def test_complex_merge_1(self):
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = 4
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed complex merge 1")

    def test_complex_merge_2(self):
        nums = [2, 4, 1, 3, 5]
        expected = 3
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed complex merge 2")

    def test_empty_input(self):
        nums = []
        expected = 0
        self.assertEqual(self.solution.maximumPossibleSize(
            nums.copy()), expected, "Failed empty input")

    # Category 3: Large Constraint Stress Test (Performance)

    def test_large_alternating(self):
        n = 2 * 10**5
        nums = []
        for i in range(n // 2):
            nums.append(i + 1)
            nums.append(n - i)
        if n % 2 == 1:
            nums.append(n // 2 + 1)

        print(f"\nTesting large alternating array (N={len(nums)})...")
        start_time = time.time()
        result_size = self.solution.maximumPossibleSize(nums.copy())
        end_time = time.time()
        print(
            f"Execution Time (New Algo): {end_time - start_time:.6f} seconds")
        print(f"Result Size: {result_size}")
        self.assertTrue(result_size > 0, "Result size should be positive")

    def test_large_decreasing(self):
        n = 2 * 10**5
        nums = list(range(n, 0, -1))

        print(f"\nTesting large decreasing array (N={len(nums)})...")
        start_time = time.time()
        result_size = self.solution.maximumPossibleSize(nums.copy())
        end_time = time.time()
        print(
            f"Execution Time (New Algo): {end_time - start_time:.6f} seconds")
        self.assertEqual(result_size, 1, "Failed large decreasing array")


if __name__ == '__main__':
    unittest.main()
