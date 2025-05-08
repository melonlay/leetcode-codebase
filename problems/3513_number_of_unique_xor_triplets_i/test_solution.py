import unittest
import time
from .solution import Solution

class TestSolution(unittest.TestCase):
    def _reference_solution(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        xor_values = set()
        # The problem defines triplet from nums[i], nums[j], nums[k] with i<=j<=k.
        # Since nums is a permutation, this means we pick three values from the set {1,...,n}
        # (which are the values in nums) with replacement, effectively, and then ensure the indices work.
        # A simpler interpretation matching example 1 is to iterate through indices.
        for i_idx in range(n):
            for j_idx in range(i_idx, n):
                for k_idx in range(j_idx, n):
                    xor_values.add(nums[i_idx] ^ nums[j_idx] ^ nums[k_idx])
        return len(xor_values)

    def setUp(self):
        self.solution = Solution()

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        nums = [1, 2]
        expected_output = 2 # From problem: unique {1,2}
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Example 1 Failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Example 1 Failed for reference solution")

    def test_example_2(self):
        nums = [3, 1, 2] # n = 3. Permutation of [1,2,3]
        expected_output = 4 # From problem: unique {0,1,2,3}
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Example 2 Failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Example 2 Failed for reference solution")

    # Category 2: Custom Small/Edge Case Validation (vs Reference Solution)
    def test_custom_small_cases_vs_reference(self):
        # Test up to n where reference solution is reasonably fast.
        # n.bit_length() gives k. Result is 2^k for n>=3.
        # n=1 -> 1
        # n=2 -> 2
        # n=3 -> 1<<(3).bit_length() = 1<<2 = 4
        # n=4 -> 1<<(4).bit_length() = 1<<3 = 8
        # n=5 -> 1<<(5).bit_length() = 1<<3 = 8
        # n=6 -> 1<<(6).bit_length() = 1<<3 = 8
        # n=7 -> 1<<(7).bit_length() = 1<<3 = 8
        # n=8 -> 1<<(8).bit_length() = 1<<4 = 16
        # n=9 -> 1<<(9).bit_length() = 1<<4 = 16 
        # Limit reference check to n=8 (8*8*8 = 512 loops per inner set, many sets of i,j,k, total N^3/6 triplets approx for distinct indices)
        # For i<=j<=k, roughly N*(N+1)*(N+2)/6 combinations of indices. N=8 -> 8*9*10/6 = 120. Feasible.
        # N=9 -> 9*10*11/6 = 165. Feasible.
        # N=10 -> 10*11*12/6 = 220. Feasible.
        # Let's test up to n=9 with reference.
        test_n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for n_val in test_n_values:
            # Create a simple permutation for testing (e.g., [1, 2, ..., n_val])
            # The specific permutation doesn't matter for the main solution, only its length n.
            # For the reference solution, the values do matter, so use a consistent permutation.
            nums_input = list(range(1, n_val + 1))
            with self.subTest(f"Custom case n={n_val}, nums={nums_input}"):
                expected_by_reference = self._reference_solution(nums_input)
                actual_by_solution = self.solution.uniqueXorTriplets(nums_input)
                self.assertEqual(actual_by_solution, expected_by_reference, 
                                 f"Main solution ({actual_by_solution}) != Reference ({expected_by_reference}) for n={n_val}")
    
    def test_empty_input(self):
        nums = []
        expected_output = 0 # Main solution: n=0 -> 0
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Empty input failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Empty input failed for reference solution")

    # Category 3: Large Constraint Stress Test (Performance) & Formula Check for Larger N
    def test_large_input_performance_and_formula(self):
        # Test n=10^5 (which is >= 3)
        n_large = 10**5
        nums_large = list(range(1, n_large + 1)) # Actual list not used by main solution, only length
        expected_output_large = 1 << n_large.bit_length()
        
        start_time = time.time()
        result = self.solution.uniqueXorTriplets(nums_large)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time for n={n_large}: {execution_time:.6f} seconds")
        
        self.assertLess(execution_time, 0.1, "Performance test failed: Execution too slow.")
        self.assertEqual(result, expected_output_large, f"Result for large input (n={n_large}) is incorrect based on formula 1<<n.bit_length()")

        # Test specific n values based on formula boundaries or examples
        # n=17 (user example)
        n_17 = 17
        expected_17 = 1 << n_17.bit_length() # 17 -> bit_length 5 -> 2^5 = 32
        self.assertEqual(self.solution.uniqueXorTriplets(list(range(1,n_17+1))), expected_17, "Result for n=17 is incorrect")

        # n=7 (boundary for 2^3)
        n_7 = 7
        expected_7 = 1 << n_7.bit_length() # 7 -> bit_length 3 -> 2^3 = 8
        self.assertEqual(self.solution.uniqueXorTriplets(list(range(1,n_7+1))), expected_7, "Result for n=7 is incorrect")
        
        # n=8 (boundary for 2^4)
        n_8 = 8
        expected_8 = 1 << n_8.bit_length() # 8 -> bit_length 4 -> 2^4 = 16
        self.assertEqual(self.solution.uniqueXorTriplets(list(range(1,n_8+1))), expected_8, "Result for n=8 is incorrect")

if __name__ == '__main__':
    unittest.main() 