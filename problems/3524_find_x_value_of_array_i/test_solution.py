import unittest
import time
from typing import List
from .solution import Solution


class TestSolution(unittest.TestCase):

    def _reference_solution(self, nums: List[int], k: int) -> List[int]:
        """
        O(n^2) reference solution. Iterates through all subarrays.
        """
        n = len(nums)
        if n == 0:
            return [0] * k

        result = [0] * k
        for i in range(n):
            current_prod = 1
            for j in range(i, n):
                # Calculate product incrementally to avoid large numbers
                current_prod = (current_prod * nums[j]) % k
                result[current_prod] += 1
        return result

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = [9, 2, 4]
        ref_expected = self._reference_solution(nums, k)
        self.assertEqual(ref_expected, expected, "Reference failed Example 1")
        self.assertEqual(sol.resultArray(nums, k), expected,
                         "Solution failed Example 1")

    def test_example_2(self):
        sol = Solution()
        nums = [1, 2, 4, 8, 16, 32]
        k = 4
        expected = [18, 1, 2, 0]
        ref_expected = self._reference_solution(nums, k)
        self.assertEqual(ref_expected, expected, "Reference failed Example 2")
        self.assertEqual(sol.resultArray(nums, k), expected,
                         "Solution failed Example 2")

    def test_example_3(self):
        sol = Solution()
        nums = [1, 1, 2, 1, 1]
        k = 2
        expected = [9, 6]
        ref_expected = self._reference_solution(nums, k)
        self.assertEqual(ref_expected, expected, "Reference failed Example 3")
        self.assertEqual(sol.resultArray(nums, k), expected,
                         "Solution failed Example 3")

    # Category 2: Custom Small/Edge Case Validation
    def test_custom_cases(self):
        sol = Solution()
        # Define only inputs for Category 2 tests
        test_inputs = [
            ([1], 1),
            ([5], 3),
            ([2, 4], 4),
            ([3, 3], 3),
            ([1, 2, 3], 5),
            ([7, 7, 7], 4),
            # Add more edge cases if needed
            ([10**9, 10**9 - 1], 2),  # Test large numbers
            ([1, 1, 1, 1, 1], 1),    # Test k=1
        ]
        for i, (nums, k) in enumerate(test_inputs):
            with self.subTest(case=i, nums=nums, k=k):
                # Generate expected output using the reference solution
                expected_output = self._reference_solution(nums, k)
                # Assert the main solution against the reference solution's output
                self.assertEqual(sol.resultArray(nums, k), expected_output,
                                 f"Solution failed custom case {i} compared to reference")

    # Category 3: Large Constraint Stress Test (Performance)
    def test_large_constraints(self):
        sol = Solution()
        n = 100000  # Max n
        k = 5       # Max k
        # Create a large array, e.g., alternating 1s and 2s
        nums = [(i % 2) + 1 for i in range(n)]

        start_time = time.time()
        result = sol.resultArray(nums, k)
        end_time = time.time()

        print(
            f"\nExecution Time (n={n}, k={k}): {end_time - start_time:.6f} seconds")
        # Basic sanity check on result format
        self.assertEqual(len(result), k)
        self.assertTrue(all(count >= 0 for count in result))
        # Total number of subarrays is n*(n+1)/2
        total_subarrays = n * (n + 1) // 2
        self.assertEqual(sum(result), total_subarrays)


if __name__ == '__main__':
    unittest.main()
