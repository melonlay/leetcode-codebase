import unittest
from .solution import Solution


class TestMaxProduct(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        k = 2
        limit = 10
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 6)

    def test_example_2(self):
        nums = [0, 2, 3]
        k = -5
        limit = 12
        self.assertEqual(self.solver.maxProduct(nums, k, limit), -1)

    def test_example_3(self):
        nums = [2, 2, 3, 3]
        k = 0
        limit = 9
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 9)

    def test_no_solution(self):
        nums = [1]
        k = 0
        limit = 10
        self.assertEqual(self.solver.maxProduct(nums, k, limit), -1)

    def test_single_element_solution(self):
        nums = [5]
        k = 5
        limit = 10
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 5)

    def test_single_element_at_limit(self):
        nums = [10]
        k = 10
        limit = 10
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 10)

    def test_single_element_exceeds_limit(self):
        nums = [11]
        k = 11
        limit = 10
        self.assertEqual(self.solver.maxProduct(nums, k, limit), -1)

    def test_zero_handling_1(self):
        nums = [1, 0, 2]
        k = -1
        limit = 10
        # Subsequence [1, 2] has sum 1-2 = -1, product 1*2 = 2
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 2)

    def test_zero_handling_2(self):
        nums = [1, 0, 1]
        k = 0
        limit = 10
        # Subsequence [1, 1] has sum 1-1=0, product 1*1=1
        # Subsequence [0] has sum 0, product 0
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 1)

    def test_product_limit_hit(self):
        nums = [10, 1, 10]
        k = 10
        limit = 50
        # Subsequence [10] has sum 10, product 10.
        # Subsequence [10, 1, 10] has sum 19, product 100 (exceeds limit).
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 10)

    def test_negative_k(self):
        nums = [1, 5, 2]
        k = -4
        limit = 20
        # Subsequence [1, 5] has sum 1-5=-4, product 1*5=5.
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 5)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        k = 0
        limit = 10
        # Subsequence [0] has sum 0, product 0.
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 0)

    def test_large_limit_no_exceed(self):
        nums = [3, 4, 2]
        k = 1  # 3 - 4 + 2 = 1
        limit = 100
        # Subsequence [3, 4, 2] has sum 1, product 24
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 24)

    def test_product_becomes_zero(self):
        nums = [5, 0, 6]
        k = -1  # 5-0+6 = 11, 5-0=5, 0-6=-6, 5-6 = -1
        limit = 10
        # Subsequence [5, 6] has sum 5-6=-1, product 30 (exceeds limit)
        # Subsequence [5, 0, 6] has sum 11, product 0
        # Subsequence [0, 6] has sum -6, product 0
        # There is no subsequence with sum -1 and product <= 10 other than those involving 0
        # The only way to get sum -1 is [5, 6], product 30 > 10. So -1.
        # Let's rethink: The code calculates new_prod = min(p * num, limit + 1) if p > 0 else 0.
        # For [5, 0]: p=5, num=0 -> new_prod = 0. State added: dp_odd[5-0=5] = max(dp_odd[5], 0) = 0
        # For [5, 0, 6]: from dp_odd[5]=0 -> new_sum = 5+6=11, new_prod = min(0*6, 11)=0. State added: dp_even[11]=max(dp_even[11],0)=0
        # For [5, 6]: from dp_even[5]=5 -> new_sum = 5-6=-1, new_prod = min(5*6, 11)=min(30,11)=11.
        # State update check: if new_prod <= limit: next_dp_odd[new_sum] = max(...) -> if 11 <= 10 -> false.
        # So the state dp_odd[-1] never gets updated with 11. max_prod_at_k remains -1.
        self.assertEqual(self.solver.maxProduct(nums, k, limit), -1)

    def test_product_becomes_zero_after_exceeding_limit(self):
        nums = [10, 10, 9, 0]
        k = 1
        limit = 20
        # Subsequence [10, 9] -> sum 1, prod 90 (>limit)
        # Subsequence [10, 9, 0] -> sum 1, prod 0 (<=limit)
        # Expected: 0
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 0)

    def test_zero_product_for_k_gh_issue(self):
        nums = [6, 9, 0, 3, 11]
        k = 17
        limit = 50
        # Subsequence [6, 0, 11] -> sum 6 - 0 + 11 = 17. Product = 0.
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 0)

    def test_zero_product_from_zero_start(self):
        nums = [0, 8]
        k = -8
        limit = 20
        # Subsequence [0, 8] -> sum 0 - 8 = -8. Product = 0.
        self.assertEqual(self.solver.maxProduct(nums, k, limit), 0)


if __name__ == '__main__':
    unittest.main()
