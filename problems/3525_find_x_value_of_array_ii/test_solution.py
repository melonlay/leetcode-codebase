import unittest
import time
from typing import List

# Ensure the solution class is imported correctly based on the file structure
# Assuming test_solution.py is in the same directory as solution.py
# Adjust the import path if the structure is different (e.g., using packages)
try:
    from .solution import Solution
except ImportError:
    # Fallback for running the test file directly
    from solution import Solution


class TestSolution(unittest.TestCase):

    def _reference_solution(self, initial_nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        """Reference implementation using naive O(n) calculation per query."""
        if k == 0:
            return [0] * len(queries)

        nums = initial_nums[:]
        n = len(nums)
        results = []

        for index, value, start, x_target in queries:
            # 1. Update (persistently for this simulation)
            nums[index] = value

            # 2. Calculate x-value for the query
            count = 0
            if start < n:
                current_product = 1
                # Iterate through prefixes of nums[start:]
                for j in range(start, n):
                    # Important: calculate product modulo k at each step to avoid large numbers
                    current_product = (current_product * nums[j]) % k
                    if current_product == x_target:
                        count += 1
            results.append(count)

        return results

    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        queries = [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]
        expected = [2, 2, 2]
        solution_output = Solution().resultArray(nums[:], k, queries)
        reference_output = self._reference_solution(nums[:], k, queries)
        self.assertEqual(reference_output, expected,
                         "Reference implementation failed Example 1")
        self.assertEqual(solution_output, expected,
                         "Solution implementation failed Example 1")

    def test_example_2(self):
        nums = [1, 2, 4, 8, 16, 32]
        k = 4
        queries = [[0, 2, 0, 2], [0, 2, 0, 1]]
        # Query 1: nums=[2,2,4,8,16,32], start=0, x=2
        # Pfx [2]: 2%4=2. (c=1)
        # Pfx [2,2]: 4%4=0.
        # Pfx [2,2,4]: 16%4=0.
        # Pfx [2,2,4,8]: 128%4=0.
        # Pfx [2,2,4,8,16]: ...0
        # Pfx [2,2,4,8,16,32]: ...0.  Result = 1
        # Query 2: nums=[2,2,4,8,16,32], start=0, x=1. Result = 0
        expected = [1, 0]
        solution_output = Solution().resultArray(nums[:], k, queries)
        reference_output = self._reference_solution(nums[:], k, queries)
        self.assertEqual(reference_output, expected,
                         "Reference implementation failed Example 2")
        self.assertEqual(solution_output, expected,
                         "Solution implementation failed Example 2")

    def test_example_3(self):
        nums = [1, 1, 2, 1, 1]
        k = 2
        queries = [[2, 1, 0, 1]]
        # nums=[1,1,1,1,1], start=0, x=1
        # Pfx [1]: 1%2=1 (c=1)
        # Pfx [1,1]: 1%2=1 (c=2)
        # Pfx [1,1,1]: 1%2=1 (c=3)
        # Pfx [1,1,1,1]: 1%2=1 (c=4)
        # Pfx [1,1,1,1,1]: 1%2=1 (c=5)
        expected = [5]
        solution_output = Solution().resultArray(nums[:], k, queries)
        reference_output = self._reference_solution(nums[:], k, queries)
        self.assertEqual(reference_output, expected,
                         "Reference implementation failed Example 3")
        self.assertEqual(solution_output, expected,
                         "Solution implementation failed Example 3")

    def test_custom_edge_cases(self):
        # Test k=1
        nums1 = [10, 20, 30]
        k1 = 1
        queries1 = [[0, 5, 0, 0]]  # All products are 0 mod 1
        # nums=[5,20,30], start=0, x=0
        # Pfx [5]: 5%1=0 (c=1)
        # Pfx [5,20]: 100%1=0 (c=2)
        # Pfx [5,20,30]: 3000%1=0 (c=3)
        expected1 = [3]
        self.assertEqual(Solution().resultArray(
            nums1[:], k1, queries1), expected1)
        self.assertEqual(self._reference_solution(
            nums1[:], k1, queries1), expected1)

        # Test start = n-1
        nums2 = [2, 3, 4]
        k2 = 5
        queries2 = [[1, 6, 2, 4]]  # Update to [2,6,4], start=2, x=4
        # Pfx [4]: 4%5=4 (c=1)
        expected2 = [1]
        self.assertEqual(Solution().resultArray(
            nums2[:], k2, queries2), expected2)
        self.assertEqual(self._reference_solution(
            nums2[:], k2, queries2), expected2)

        # Test start = 0, empty prefix removal
        nums3 = [7]
        k3 = 3
        queries3 = [[0, 5, 0, 2]]  # Update to [5], start=0, x=2
        # Pfx [5]: 5%3=2 (c=1)
        expected3 = [1]
        self.assertEqual(Solution().resultArray(
            nums3[:], k3, queries3), expected3)
        self.assertEqual(self._reference_solution(
            nums3[:], k3, queries3), expected3)

        # Test query range becomes empty
        nums4 = [1, 2, 3]
        k4 = 4
        queries4 = [[0, 1, 3, 1]]  # start=3 >= n=3. Empty range.
        expected4 = [0]
        self.assertEqual(Solution().resultArray(
            nums4[:], k4, queries4), expected4)
        self.assertEqual(self._reference_solution(
            nums4[:], k4, queries4), expected4)

        # Test multiple queries with updates
        nums5 = [1, 2, 3]
        k5 = 4
        queries5 = [
            # nums=[5,2,3], s=0, x=1. Pfx[5]=5%4=1(c=1). Pfx[5,2]=10%4=2. Pfx[5,2,3]=30%4=2. -> [1]
            [0, 5, 0, 1],
            # nums=[5,6,3], s=1, x=2. Pfx[6]=6%4=2(c=1). Pfx[6,3]=18%4=2(c=2). -> [2]
            [1, 6, 1, 2]
        ]
        expected5 = [1, 2]
        self.assertEqual(Solution().resultArray(
            nums5[:], k5, queries5), expected5)
        self.assertEqual(self._reference_solution(
            nums5[:], k5, queries5), expected5)

    # @unittest.skip("Skipping performance test for CI/local speed")
    def test_large_constraints(self):
        n = 10**5  # Max n
        q = 2 * 10**4  # Max q
        k = 5  # Max k
        nums = [i % 100 + 1 for i in range(n)]  # Sample large array
        queries = [[i % n, (i * 3) % 100 + 1, min(i, n-1), i % k]
                   for i in range(q)]

        start_time = time.time()
        result = Solution().resultArray(nums, k, queries)
        end_time = time.time()

        print(
            f"\nExecution Time (Large Constraints n={n}, q={q}): {end_time - start_time:.6f} seconds")
        # No assertion against reference here, just check it runs without crashing and time
        self.assertEqual(len(result), q)


if __name__ == '__main__':
    unittest.main()
