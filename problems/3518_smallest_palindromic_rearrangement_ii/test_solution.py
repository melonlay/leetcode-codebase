import unittest
import time
from collections import Counter
from itertools import permutations
import string

from .solution import Solution


class TestSmallestPalindrome(unittest.TestCase):

    def _reference_solution(self, s: str, k: int) -> str:
        """Generates all palindromic rearrangements and finds the k-th.
           Only feasible for small N.
        """
        n = len(s)
        counts = Counter(s)
        half_chars = []
        middle_char = ""
        for char, count in counts.items():
            if count % 2 == 1:
                middle_char = char
            half_chars.extend([char] * (count // 2))

        if not half_chars and middle_char:
            # Special case like s="a"
            return middle_char if k == 1 else ""
        if not half_chars and not middle_char:
            # Empty string input? Return empty.
            return ""

        # Generate permutations of the first half
        unique_half_perms = set()
        for p in permutations(half_chars):
            unique_half_perms.add("".join(p))

        sorted_half_perms = sorted(list(unique_half_perms))

        if k < 1 or k > len(sorted_half_perms):
            return ""

        # Get the (k-1)th half permutation
        kth_half = sorted_half_perms[k-1]

        # Construct the full palindrome
        return kth_half + middle_char + kth_half[::-1]

    def setUp(self):
        self.solution = Solution()

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        s = "abba"
        k = 2
        expected = "baab"
        # Verify both main and reference against ground truth
        self.assertEqual(self.solution.smallestPalindrome(s, k), expected)
        self.assertEqual(self._reference_solution(s, k), expected)

    def test_example_2(self):
        s = "aa"
        k = 2
        expected = ""
        # Verify both main and reference against ground truth
        self.assertEqual(self.solution.smallestPalindrome(s, k), expected)
        self.assertEqual(self._reference_solution(s, k), expected)

    def test_example_2_k1(self):
        s = "aa"
        k = 1
        expected = "aa"
        # Verify both main and reference against ground truth
        self.assertEqual(self.solution.smallestPalindrome(s, k), expected)
        self.assertEqual(self._reference_solution(s, k), expected)

    def test_example_3(self):
        s = "bacab"
        k = 1
        expected = "abcba"
        # Verify both main and reference against ground truth
        self.assertEqual(self.solution.smallestPalindrome(s, k), expected)
        self.assertEqual(self._reference_solution(s, k), expected)

    def test_example_3_k2(self):
        s = "bacab"
        k = 2
        expected = "bacab"
        # Verify both main and reference against ground truth
        self.assertEqual(self.solution.smallestPalindrome(s, k), expected)
        self.assertEqual(self._reference_solution(s, k), expected)

    # Category 2: Custom Small/Edge Case Validation
    # Verify main solution against reference solution
    def test_all_same_char(self):
        s = "aaaaa"
        for k in [1, 2]:
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    def test_simple_even(self):
        s = "aabb"
        for k in [1, 2, 3]:
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    def test_simple_odd(self):
        s = "aabbc"
        for k in [1, 2, 3]:
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    def test_single_char(self):
        s = "a"
        for k in [1, 2]:
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    def test_no_rearrangement_possible(self):
        s = "aba"
        for k in [1, 2]:
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    def test_slightly_larger_k(self):
        s = "aabbcc"
        # Half: abc -> Perms: abc, acb, bac, bca, cab, cba (6 total)
        for k in range(1, 8):
            with self.subTest(s=s, k=k):
                expected = self._reference_solution(s, k)
                self.assertEqual(
                    self.solution.smallestPalindrome(s, k), expected)

    # Category 3: Large Constraint Stress Test (Performance)
    # Reference solution is NOT used here due to performance limitations
    def test_large_n_simple(self):
        s = "a" * 5000 + "b" * 5000
        k = 1
        start_time = time.time()
        result = self.solution.smallestPalindrome(s, k)
        end_time = time.time()
        print(
            f"\nLarge N Simple (N=10000, k=1) Time: {end_time - start_time:.6f} seconds")
        # Expected: a...ab...ba...a
        self.assertTrue(result.startswith("a"*2500 + "b"))
        self.assertTrue(result.endswith("b" + "a"*2500))
        self.assertEqual(len(result), 10000)

    def test_large_n_all_same(self):
        s = "z" * 10000
        k = 1
        start_time = time.time()
        result = self.solution.smallestPalindrome(s, k)
        end_time = time.time()
        print(
            f"Large N All Same (N=10000, k=1) Time: {end_time - start_time:.6f} seconds")
        self.assertEqual(result, s)

        k = 2
        start_time = time.time()
        result = self.solution.smallestPalindrome(s, k)
        end_time = time.time()
        print(
            f"Large N All Same (N=10000, k=2) Time: {end_time - start_time:.6f} seconds")
        self.assertEqual(result, "")

    # It's hard to know the expected result for large k without running the code,
    # so this test mainly checks if it computes within time limits for large k.
    def test_large_k_and_n(self):
        half = ('a'*20 + 'b'*20 + 'c'*20 + 'd'*20 + 'e'*20) * \
            50  # 5 * 20 * 50 = 5000 -> N=10000
        s = half + half[::-1]
        k = 10**6  # Large k
        start_time = time.time()
        result = self.solution.smallestPalindrome(s, k)
        end_time = time.time()
        print(
            f"Large N and K (N=10000, k=1M) Time: {end_time - start_time:.6f} seconds")
        self.assertEqual(len(result), 10000)  # Check length
        # Verify it's a palindrome
        self.assertEqual(result, result[::-1])
        # Could add a check that the character counts match s, but less critical for perf test
        # from collections import Counter
        # self.assertEqual(Counter(result), Counter(s))


if __name__ == '__main__':
    unittest.main()
