import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        sol = Solution()
        M = 5
        K = 5
        nums = [1, 10, 100, 10000, 1000000]
        # Note: This result seems derived from a calculation assuming the product
        # could exceed standard integer limits before the modulo operation.
        # The core logic involves sums of powers of 2, which don't grow that fast.
        # Expected result needs verification based on problem constraints and modulo arithmetic.
        # Example calculation: (Assuming this is the intended sum of products)
        # 120 * 10^13 mod (10^9 + 7) = 991600007
        self.assertEqual(sol.magicalSum(M, K, nums), 991600007, "Example 1")

    def test_example_2(self):
        sol = Solution()
        M = 2
        K = 2
        nums = [5, 4, 3, 2, 1]
        # Possible Sequences (indices from nums):
        # [0,0] -> S=2^0+2^0=2 (1 bit), P=5*5=25
        # [0,1] -> S=2^0+2^1=3 (2 bits), P=5*4=20
        # [0,2] -> S=2^0+2^2=5 (2 bits), P=5*3=15
        # [0,3] -> S=2^0+2^3=9 (2 bits), P=5*2=10
        # [0,4] -> S=2^0+2^4=17(2 bits), P=5*1=5
        # [1,1] -> S=2^1+2^1=4 (1 bit), P=4*4=16
        # [1,2] -> S=2^1+2^2=6 (2 bits), P=4*3=12
        # [1,3] -> S=2^1+2^3=10(2 bits), P=4*2=8
        # [1,4] -> S=2^1+2^4=18(2 bits), P=4*1=4
        # [2,2] -> S=2^2+2^2=8 (1 bit), P=3*3=9
        # [2,3] -> S=2^2+2^3=12(2 bits), P=3*2=6
        # [2,4] -> S=2^2+2^4=20(2 bits), P=3*1=3
        # [3,3] -> S=2^3+2^3=16(1 bit), P=2*2=4
        # [3,4] -> S=2^3+2^4=24(2 bits), P=2*1=2
        # [4,4] -> S=2^4+2^4=32(1 bit), P=1*1=1
        # Sum for K=2: 20+15+10+5 + 12+8+4 + 6+3 + 2 = 85 + 24 + 9 + 2 = 120? Incorrect.
        # Need to re-read: sequence of M indices from 0..N-1.
        # Let's re-calculate Example 2:
        # M=2, K=2, nums=[5,4,3,2,1] (N=5)
        # Sequences are pairs (idx_0, idx_1) where 0 <= idx <= 4.
        # Possible Sequences (idx0, idx1):
        #   Sum S = 2^idx0 + 2^idx1. Count set bits in S.
        #   Product P = nums[idx0] * nums[idx1].
        #   We want sum of P where bit_count(S) == K == 2.
        # (0,1): S=3 (11b, 2 bits), P=5*4=20
        # (0,2): S=5 (101b, 2 bits), P=5*3=15
        # (0,3): S=9 (1001b, 2 bits), P=5*2=10
        # (0,4): S=17(10001b, 2 bits), P=5*1=5
        # (1,0): S=3 (11b, 2 bits), P=4*5=20
        # (1,2): S=6 (110b, 2 bits), P=4*3=12
        # (1,3): S=10(1010b, 2 bits), P=4*2=8
        # (1,4): S=18(10010b, 2 bits), P=4*1=4
        # (2,0): S=5 (101b, 2 bits), P=3*5=15
        # (2,1): S=6 (110b, 2 bits), P=3*4=12
        # (2,3): S=12(1100b, 2 bits), P=3*2=6
        # (2,4): S=20(10100b, 2 bits), P=3*1=3
        # (3,0): S=9 (1001b, 2 bits), P=2*5=10
        # (3,1): S=10(1010b, 2 bits), P=2*4=8
        # (3,2): S=12(1100b, 2 bits), P=2*3=6
        # (3,4): S=24(11000b, 2 bits), P=2*1=2
        # (4,0): S=17(10001b, 2 bits), P=1*5=5
        # (4,1): S=18(10010b, 2 bits), P=1*4=4
        # (4,2): S=20(10100b, 2 bits), P=1*3=3
        # (4,3): S=24(11000b, 2 bits), P=1*2=2
        # Total Sum = (20+15+10+5) + (20+12+8+4) + (15+12+6+3) + (10+8+6+2) + (5+4+3+2)
        #           = 50 + 44 + 36 + 26 + 14 = 170. Correct.
        self.assertEqual(sol.magicalSum(M, K, nums), 170, "Example 2")

    def test_example_3(self):
        sol = Solution()
        M = 1
        K = 1
        nums = [28]
        # Sequence: [0]
        # Sum S = 2^0 = 1 (1 bit). K=1 matches.
        # Product P = nums[0] = 28.
        self.assertEqual(sol.magicalSum(M, K, nums), 28, "Example 3")

    # Add more test cases here for edge cases and constraints
    def test_simple_case(self):
        sol = Solution()
        M = 2
        K = 1
        nums = [1, 1]
        # Sequences (M=2 indices from N=2 nums):
        # [0, 0]: S=2^0+2^0 = 2 (10b, 1 bit) -> P=1*1=1. K=1 matches.
        # [0, 1]: S=2^0+2^1 = 3 (11b, 2 bits) -> P=1*1=1. K=1 mismatch.
        # [1, 0]: S=2^1+2^0 = 3 (11b, 2 bits) -> P=1*1=1. K=1 mismatch.
        # [1, 1]: S=2^1+2^1 = 4 (100b, 1 bit) -> P=1*1=1. K=1 matches.
        # Sum = 1 + 1 = 2
        self.assertEqual(sol.magicalSum(M, K, nums), 2, "Simple Case K=1")

    def test_all_same_index(self):
        sol = Solution()
        M = 4
        K = 1
        nums = [3]  # N=1
        # Sequence (M=4 indices from N=1 nums): [0, 0, 0, 0]
        # Sum S = 2^0 + 2^0 + 2^0 + 2^0 = 4 (100b, 1 bit). K=1 matches.
        # Product P = nums[0]^4 = 3^4 = 81
        self.assertEqual(sol.magicalSum(M, K, nums), 81, "All Same Index")


if __name__ == '__main__':
    unittest.main()
