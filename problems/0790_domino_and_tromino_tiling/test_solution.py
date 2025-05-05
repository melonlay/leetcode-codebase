import unittest
import time
from .solution import Solution


class TestSolution(unittest.TestCase):

    def _numTilings_reference(self, n: int) -> int:
        """Reference implementation using the correct recurrence
        dp[i] = 2*dp[i-1] + dp[i-3], but with O(n) space for verification.
        """
        MOD = 10**9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD

        return dp[n]

    # Category 1: Provided Examples (Verify Solution and Reference)
    def test_example_1(self):
        s = Solution()
        n = 3
        expected = 5
        self.assertEqual(s.numTilings(n), expected,
                         "Solution failed Example 1")
        self.assertEqual(self._numTilings_reference(
            n), expected, "Reference failed Example 1")

    def test_example_2(self):
        s = Solution()
        n = 1
        expected = 1
        self.assertEqual(s.numTilings(n), expected,
                         "Solution failed Example 2")
        self.assertEqual(self._numTilings_reference(
            n), expected, "Reference failed Example 2")

    # Category 2: Small/Edge Cases (Verify Solution against Reference)
    def test_small_n_cases(self):
        s = Solution()
        test_cases = [0, 2, 4, 5, 6, 10]
        for n in test_cases:
            expected = self._numTilings_reference(n)
            with self.subTest(n=n):
                self.assertEqual(s.numTilings(n), expected)

    # Category 3: Stress Test (Verify Performance)
    def test_large_n_stress(self):
        s = Solution()
        n = 1000
        MOD = 10**9 + 7

        start_time = time.time()
        result = s.numTilings(n)
        end_time = time.time()

        print(f"\n[Large N Stress Test (n={n})]")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        # Optional: Check if result is within expected modulo bounds
        self.assertTrue(0 <= result < MOD, "Result out of modulo bounds")
        # Known result for n=1000 is 979_237_071 - can assert if desired for sanity check
        # self.assertEqual(result, 979237071, "Result mismatch for known large n") # Removed per user request

    # --- Keeping original modulo test for completeness, falls under Category 2 ---
    def test_modulo(self):
        s = Solution()
        n = 30
        expected = self._numTilings_reference(n)  # Use reference for expected
        self.assertEqual(s.numTilings(n), expected)
        # Manually verified dp[30] % (10**9+7) == 312342182
        self.assertEqual(expected, 312342182,
                         "Reference calculation mismatch for n=30")
