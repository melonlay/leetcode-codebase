import unittest
import time
import random # Added for generating diverse large test cases
from .solution import Solution

class TestSolution(unittest.TestCase):
    def _reference_solution(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        xor_values = set()
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    xor_values.add(nums[i] ^ nums[j] ^ nums[k])
        return len(xor_values)

    def setUp(self):
        self.solution = Solution()

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        nums = [1, 3]
        expected_output = 2
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Example 1 Failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Example 1 Failed for reference solution")

    def test_example_2(self):
        nums = [6, 7, 8, 9]
        expected_output = 4
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Example 2 Failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Example 2 Failed for reference solution")

    # Category 2: Custom Small/Edge Case Validation (vs Reference Solution)
    def test_custom_small_cases_vs_reference(self):
        test_cases_params = [
            ([1],), 
            ([1,1,1],),
            ([1,2,3],),
            ([1,2,3,4,5],),
            ([10,20,30,10],),
            ([7,7,7,7,7,7],)
        ]
        # Max N for reference solution to run reasonably quickly (e.g., N=70 -> ~3.4e5, N=50 -> 1.25e5)
        # Let's test for N up to around 50 for reference comparison.

        for i, params in enumerate(test_cases_params):
            nums_input = params[0]
            if len(nums_input) > 50 and i > 2 : # Only run reference for smaller, varied cases unless it's one of the first few.
                 # For larger N in custom tests, we might just check if solution runs
                 # and if the output has a reasonable bound if problem had one, but here we rely on reference.
                 # So, we skip reference check for larger custom inputs to save test time.
                pass # Could add a simple check like self.assertIsInstance(self.solution.uniqueXorTriplets(nums_input), int)
            else:
                with self.subTest(f"Custom case {i+1}: nums={nums_input}"):
                    expected_by_reference = self._reference_solution(nums_input)
                    actual_by_solution = self.solution.uniqueXorTriplets(nums_input)
                    self.assertEqual(actual_by_solution, expected_by_reference, 
                                     f"Main solution ({actual_by_solution}) != Reference ({expected_by_reference}) for nums={nums_input}")
    
    def test_single_element_repeated(self):
        nums = [5] * 10 # [5,5,5,5,5,5,5,5,5,5]
        # Expected: 5^5^5 = 5. Only {5}.
        expected_output = 1
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Single element repeated failed for main solution")
        if len(nums) <= 50:
             self.assertEqual(self._reference_solution(nums), expected_output, "Single element repeated failed for reference solution")

    def test_all_same_elements(self):
        nums = [100] * 30
        expected = 1 # Only 100^100^100 = 100
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected)
        if len(nums) <= 50:
            self.assertEqual(self._reference_solution(nums), expected)

    def test_two_distinct_elements(self):
        nums = [7, 13] * 5 # [7,13,7,13,7,13,7,13,7,13]
        # Possible values: 7^7^7=7, 7^7^13=13, 7^13^13=7, 13^13^13=13. XORs: {7,13}
        expected = 2 
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected)
        if len(nums) <= 50:
             self.assertEqual(self._reference_solution(nums), expected)

    def test_empty_input(self):
        nums = []
        expected_output = 0
        self.assertEqual(self.solution.uniqueXorTriplets(nums), expected_output, "Empty input failed for main solution")
        self.assertEqual(self._reference_solution(nums), expected_output, "Empty input failed for reference solution")

    # Category 3: Large Constraint Stress Test (Performance)
    def test_large_input_performance(self):
        n_large = 1500
        max_val_in_nums = 1500
        
        test_configurations = []
        # 1. Sequential input (distinct)
        if n_large <= max_val_in_nums:
            test_configurations.append(list(range(1, n_large + 1)))
        else:
            test_configurations.append([ (i % max_val_in_nums) + 1 for i in range(n_large)]) # Patterned if n_large > max_val_in_nums

        # 2. Random distinct values (if possible)
        if n_large <= max_val_in_nums:
            population = list(range(1, max_val_in_nums + 1))
            if n_large <= len(population): # Ensure sample size isn't larger than population
                test_configurations.append(random.sample(population, n_large))
            else:
                 test_configurations.append([random.randint(1, max_val_in_nums) for _ in range(n_large)])
        else:
            test_configurations.append([random.randint(1, max_val_in_nums) for _ in range(n_large)])

        # 3. Random values with many repeats
        test_configurations.append([random.randint(1, max_val_in_nums // 10) for _ in range(n_large)])

        for i, nums_large_cfg in enumerate(test_configurations):
            # Ensure the list has the correct length if sampling logic was complex
            current_nums = list(nums_large_cfg) # Make a copy if needed or ensure it's a list
            if len(current_nums) != n_large:
                 current_nums = [random.randint(1, max_val_in_nums) for _ in range(n_large)]
            if not current_nums: # Handle case where a config might become empty
                if n_large > 0: current_nums = [1]*n_large # Default non-empty if n_large >0
                else: continue # Skip if n_large is 0 and somehow config is empty

            with self.subTest(f"Large input configuration {i+1}, size {len(current_nums)}"):
                start_time = time.time()
                result = self.solution.uniqueXorTriplets(current_nums)
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Execution Time for n={len(current_nums)} (Config {i+1}): {execution_time:.6f} seconds")
                
                # FWHT should be very fast, O(M log M) where M=2048
                self.assertLess(execution_time, 0.2, f"Performance test failed for config {i+1}: Execution too slow.") 
                self.assertIsInstance(result, int)
                if len(current_nums) > 0:
                    # The number of unique XORs for general nums can be up to 2048
                    self.assertGreaterEqual(result, 1, "Result for large input should be at least 1 if not empty")
                    self.assertLessEqual(result, 2048, "Result for large input should be at most 2048")
                else:
                    self.assertEqual(result, 0, "Result for n=0 should be 0")

    def test_max_values_input(self):
        n_max_val = 1500
        nums_max_val = [1500 - (i % 100) for i in range(n_max_val)] # numbers near max
        start_time = time.time()
        result = self.solution.uniqueXorTriplets(nums_max_val)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time for n={n_max_val} with max values: {execution_time:.6f} seconds")
        self.assertLess(execution_time, 2.0)

if __name__ == '__main__':
    unittest.main() 