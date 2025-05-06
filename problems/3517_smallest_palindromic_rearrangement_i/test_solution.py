import unittest
import time
import collections
from .solution import Solution


class TestSmallestPalindrome(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def _reference_solution(self, s: str) -> str:
        """Reference implementation (same logic, for validation)."""
        counts = collections.Counter(s)
        first_half = []
        middle_char = ""
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if counts[char] > 0:
                first_half.extend([char] * (counts[char] // 2))
                if counts[char] % 2 == 1:
                    middle_char = char
        first_half_str = "".join(first_half)
        second_half_str = "".join(first_half[::-1])
        return first_half_str + middle_char + second_half_str

    # Category 1: Provided Examples Verification
    def test_provided_examples(self):
        """Test the examples provided in the problem description."""
        examples = [
            ("z", "z"),
            ("babab", "abbba"),
            ("daccad", "acddca"),
        ]
        for i, (s_input, expected_output) in enumerate(examples):
            with self.subTest(msg=f"Provided Example {i+1}", s=s_input):
                # Verify both main solution and reference against expected output
                self.assertEqual(self.solution.smallestPalindrome(
                    s_input), expected_output)
                self.assertEqual(self._reference_solution(
                    s_input), expected_output)

    # Category 2: Custom Small/Edge Case Validation
    def test_custom_edge_cases(self):
        """Test custom small inputs and edge cases."""
        test_cases = [
            "a",          # Single char
            "aa",         # Even length, one char type
            "aba",        # Odd length, simple
            "aaaa",       # Longer even length, one char type
            "aabb",       # Even length, two char types
            "racecar",    # Common palindrome example
            "topspot",    # Another odd length palindrome
            "level",
            "madamimadam",  # Longer complex odd
            "aabbaa",      # Longer complex even
        ]
        for s_input in test_cases:
            with self.subTest(msg=f"Custom Case", s=s_input):
                # Verify main solution against reference solution
                expected = self._reference_solution(s_input)
                self.assertEqual(
                    self.solution.smallestPalindrome(s_input), expected)

    # Category 3: Large Constraint Stress Test (Performance)
    def test_large_input_performance(self):
        """Test performance with maximum constraints."""
        # Test Case 1: Max length, single character
        s_large_single = 'a' * (10**5)
        # Test Case 2: Max length, mixed characters (odd length)
        n_large_odd = 10**5 - 1  # Ensure odd length
        s_large_mixed_odd = ('a' * (n_large_odd // 2)) + \
            'b' + ('a' * (n_large_odd // 2))
        # Test Case 3: Max length, mixed characters (even length)
        n_large_even = 10**5
        s_large_mixed_even = ('a' * (n_large_even // 4)) + \
            ('b' * (n_large_even // 2)) + ('a' * (n_large_even // 4))

        large_inputs = {
            "large_single": s_large_single,
            "large_mixed_odd": s_large_mixed_odd,
            "large_mixed_even": s_large_mixed_even
        }

        for name, s_input in large_inputs.items():
            with self.subTest(msg=f"Performance Test: {name}", size=len(s_input)):
                start_time = time.time()
                result = self.solution.smallestPalindrome(s_input)
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"\n[{name}] Execution Time: {execution_time:.6f} seconds")
                # Basic validity check (optional)
                self.assertEqual(len(result), len(s_input))
                self.assertTrue(
                    result == result[::-1], "Result should be a palindrome")
                # Cannot assert against reference for large inputs due to time


if __name__ == '__main__':
    unittest.main()
