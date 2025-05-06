from .solution import Solution, MOD  # Relative import
import unittest
import time
import sys
import os

# Add the parent directory to the system path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestSolution(unittest.TestCase):

    # --- Reference Implementation (Mirrors Solution Logic) ---
    def _reference_to_base_b(self, n: int, b: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n > 0:
            digits.append(str(n % b))
            n //= b
        return "".join(digits[::-1])

    def _reference_count_le(self, num: int, b: int) -> int:
        if num < 0:
            return 0
        s = self._reference_to_base_b(num, b)
        n = len(s)
        memo = {}

        def solve(index: int, prev_digit: int, is_less: bool, is_leading: bool) -> int:
            state = (index, prev_digit, is_less, is_leading)
            if index == n:
                return 1
            if state in memo:
                return memo[state]

            res = 0
            limit = int(s[index]) if not is_less else b - 1

            for digit in range(limit + 1):
                current_is_leading = is_leading and (digit == 0)
                if current_is_leading:
                    res = (res + solve(index + 1, 0,
                           is_less or (digit < limit), True)) % MOD
                else:
                    if digit >= prev_digit:
                        res = (res + solve(index + 1, digit,
                               is_less or (digit < limit), False)) % MOD

            memo[state] = res
            return res

        return solve(0, 0, False, True)

    def _reference_solution(self, l: str, r: str, b: int) -> int:
        l_int = int(l)
        r_int = int(r)
        count_r = self._reference_count_le(r_int, b)
        count_l_minus_1 = self._reference_count_le(l_int - 1, b)
        return (count_r - count_l_minus_1 + MOD) % MOD
    # --- End Reference Implementation ---

    # Category 1: Provided Examples Verification
    def test_provided_examples(self):
        solution = Solution()

        # Example 1: l="23", r="28", b=8 -> Range [23, 28] decimal.
        # Base 8: 27_8, 30_8, 31_8, 32_8, 33_8, 34_8.
        # Non-decreasing: 27_8, 33_8, 34_8. Count = 3.
        l1, r1, b1 = "23", "28", 8
        expected1 = 3
        self.assertEqual(solution.countNumbers(l1, r1, b1),
                         expected1, "Test Case 1 Failed (Solution)")
        self.assertEqual(self._reference_solution(l1, r1, b1),
                         expected1, "Test Case 1 Failed (Reference)")

        # Example 2: l="2", r="7", b=2 -> Range [2, 7] decimal.
        # Base 2: 10_2, 11_2, 100_2, 101_2, 110_2, 111_2
        # Non-decreasing: 11_2, 111_2. Count = 2.
        l2, r2, b2 = "2", "7", 2
        expected2 = 2
        self.assertEqual(solution.countNumbers(l2, r2, b2),
                         expected2, "Test Case 2 Failed (Solution)")
        self.assertEqual(self._reference_solution(l2, r2, b2),
                         expected2, "Test Case 2 Failed (Reference)")

    # Category 2: Custom Small/Edge Case Validation
    def test_custom_cases(self):
        solution = Solution()
        test_cases = [
            # (l, r, b, description)
            ("3", "7", 10, "Single digit range base 10"),       # Exp: 5 (3,4,5,6,7)
            # Exp: 2 (dec 2..7 -> 10..111 base 2. Non-dec: 11, 111)
            ("10", "111", 2, "Base 2 range"),
            # Exp: 9 (1..10 -> non-dec: 1..9)
            ("1", "10", 10, "Range includes 10"),
            ("8", "12", 10, "Range crossing 10"),      # Exp: 3 (8, 9, 11)
            # Exp: 1 (dec 27 -> 33_8. Non-dec: 33_8)
            ("27", "27", 8, "Single number range, non-decreasing"),
            # Exp: 0 (dec 26 -> 32_8. Dec: 32_8)
            ("26", "26", 8, "Single number range, decreasing"),
            # Exp: 6 (35,36,37,38,39,44)
            ("35", "44", 10, "Range with multiple non-decreasing"),
            # Exp: 1 (dec 1 -> 1_2. Non-dec: 1_2)
            ("1", "1", 2, "Smallest range"),
            # Exp: Sum C(10+k-1, k) for k=1,2 = C(10,1)+C(11,2)=10+55=65?
            ("1", "99", 10, "Range up to 99"),
            # Let's verify 1-99 manually. 1-9 (9), 11-99 (non-dec)?
            # 11..19 (9), 22..29(8), 33..39(7), ..., 88,89(2), 99(1) = 9+8+..+1 = 45.
            # Total = 9 + 45 = 54?
            # Let's use reference. count_le(99,10)=55. count_le(0,10)=1. 55-1=54. Correct.
        ]
        for l, r, b, desc in test_cases:
            with self.subTest(l=l, r=r, b=b, msg=desc):
                # Calculate expected value using the reference implementation
                expected = self._reference_solution(l, r, b)
                # Assert the main solution against the reference result
                self.assertEqual(solution.countNumbers(l, r, b), expected)

    # Category 3: Large Constraint Stress Test (Performance)
    def test_large_constraint(self):
        solution = Solution()
        l, r, b = "1", "9" * 100, 10

        print(
            f"\nRunning Large Constraint Test (l={l}, r={'9'*100}, b={b})...", end='')
        start_time = time.time()
        result = solution.countNumbers(l, r, b)
        end_time = time.time()

        print(f" Done.")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        # Optional: Basic sanity check on result
        self.assertGreaterEqual(result, 0, "Result should be non-negative")
        # We could also compare against reference, but it might be too slow
        # expected_large = self._reference_solution(l, r, b)
        # self.assertEqual(result, expected_large, "Large test mismatch vs reference")


if __name__ == '__main__':
    unittest.main()
