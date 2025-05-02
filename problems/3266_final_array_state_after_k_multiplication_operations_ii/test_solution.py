import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums = [2, 1, 3, 5, 6]
        k = 5
        multiplier = 2
        expected = [8, 4, 6, 5, 6]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_example_2(self):
        nums = [100000, 2000]
        k = 2
        multiplier = 1000000
        expected = [999999307, 999999993]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_large_k(self):
        nums = [1, 2]
        k = 10**9
        multiplier = 2
        MOD = 10**9 + 7
        # Op 1 on idx 0: c0=1. [2, 2]. k_rem = k-1.
        # Group processing: idx 0 gets ceil(k_rem/2) ops, idx 1 gets floor(k_rem/2) ops.
        k_rem = k - 1
        ops_idx1 = k_rem // 2  # floor ops applied to value 2
        ops_idx0 = k_rem - ops_idx1  # ceil ops applied to value 2
        # Final count for original nums[0] (value 1) is 1 + ops_idx0
        # Final count for original nums[1] (value 2) is ops_idx1
        c0_final = 1 + ops_idx0
        c1_final = ops_idx1
        # (1 * pow(2, 500000001)) % MOD = 125000001
        final0 = (nums[0] * pow(multiplier, c0_final, MOD)) % MOD
        # (2 * pow(2, 499999999)) % MOD = 250000002
        final1 = (nums[1] * pow(multiplier, c1_final, MOD)) % MOD
        expected = [final0, final1]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_multiplier_one(self):
        nums = [10, 20, 5, 30]
        k = 100
        multiplier = 1
        MOD = 10**9 + 7  # Need to apply modulo even if multiplier is 1
        expected = [n % MOD for n in [10, 20, 5, 30]]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_single_element(self):
        nums = [5]
        k = 10
        multiplier = 3
        MOD = 10**9 + 7
        # Count is k
        expected_val = (nums[0] * pow(multiplier, k, MOD)) % MOD
        expected = [expected_val]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_all_same_elements(self):
        nums = [7, 7, 7]
        k = 5
        multiplier = 2
        MOD = 10**9 + 7
        # Op1 on idx 0: c0=1.
        # Op2 on idx 1: c1=1.
        # Op3 on idx 2: c2=1.
        # Op4 on idx 0: c0=2.
        # Op5 on idx 1: c1=2.
        # Final counts: c0=2, c1=2, c2=1
        final0 = (nums[0] * pow(multiplier, 2, MOD)) % MOD  # 7*4=28
        final1 = (nums[1] * pow(multiplier, 2, MOD)) % MOD  # 7*4=28
        final2 = (nums[2] * pow(multiplier, 1, MOD)) % MOD  # 7*2=14
        expected = [final0, final1, final2]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_k_zero(self):
        nums = [1, 2, 3]
        k = 0
        multiplier = 10
        MOD = 10**9 + 7
        # Apply modulo even if k=0
        expected_mod = [n % MOD for n in nums]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected_mod)

    def test_large_values_and_k(self):
        nums = [10**9, 10**9 - 1]
        k = 10**9
        multiplier = 10**6
        MOD = 10**9 + 7
        # Based on careful analysis, operations alternate after Op 1.
        # Op 1 on index 1.
        # Remaining k-1 ops alternate: index 0 gets ceil((k-1)/2), index 1 gets floor((k-1)/2).
        if abs(multiplier - 1.0) < 1e-9:
            expected = [nums[0] % MOD, nums[1] % MOD]
        else:
            k_rem = k - 1
            ops0_alt = (k_rem // 2) + (k_rem % 2)  # ceil
            ops1_alt = k_rem // 2  # floor

            c0_final = ops0_alt
            c1_final = 1 + ops1_alt

            # Correct Expected Values based on alternation:
            final_val0 = (nums[0] * pow(multiplier,
                          c0_final, MOD)) % MOD  # 857142863
            final_val1 = (nums[1] * pow(multiplier,
                          c1_final, MOD)) % MOD  # 408163268
            expected = [final_val0, final_val1]

        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected)

    def test_leetcode_fail_1(self):
        nums = [1, 3, 3, 2, 1, 3, 4, 4, 5, 2, 4, 4, 2, 5, 3, 5, 4, 5]
        k = 4
        multiplier = 2
        # Original expected: [4, 3, 3, 4, 2, 2, 3, 4, 4, 5, 2, 4, 4, 2, 5, 3, 5, 4, 5]
        # Corrected expected based on manual trace and accepted solution's output:
        expected = [4, 3, 3, 4, 2, 3, 4, 4, 5, 2, 4, 4, 2, 5, 3, 5, 4, 5]
        # Apply modulo to expected result
        MOD = 10**9 + 7
        expected_mod = [x % MOD for x in expected]
        self.assertEqual(self.solver.getFinalState(
            nums, k, multiplier), expected_mod)

    def test_leetcode_fail_2(self):
        # Test case from the image (WA)
        nums_wa = [1, 3, 3, 2, 1, 3, 4, 4, 5, 2, 4, 4, 2, 5, 3, 5, 4, 5]
        k_wa = 4
        multiplier_wa = 2
        expected_wa = [4, 3, 3, 4, 2, 3, 4, 4, 5, 2, 4, 4, 2, 5, 3, 5, 4, 5]
        self.assertEqual(self.solver.getFinalState(
            nums_wa, k_wa, multiplier_wa), expected_wa)

    def test_large_k(self):
        # Test case with a large k to check efficiency
        nums = [1, 2, 3]


if __name__ == '__main__':
    unittest.main()
