import unittest
from .solution import Solution


class TestLongestPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "babad"
        # Both "bab" and "aba" are valid answers
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"], f"Failed on s = {s}")

    def test_example2(self):
        s = "cbbd"
        expected = "bb"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_single_char(self):
        s = "a"
        expected = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_all_same_chars(self):
        s = "aaaaa"
        expected = "aaaaa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_no_palindrome_longer_than_one(self):
        s = "abcde"
        # Any single character is a valid palindrome of length 1
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1, f"Failed on s = {s}")
        self.assertIn(result, list(s), f"Failed on s = {s}")

    def test_even_length_palindrome(self):
        s = "abba"
        expected = "abba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_long_string_mixed(self):
        s = "forgeeksskeegfor"
        expected = "geeksskeeg"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_palindrome_at_beginning(self):
        s = "racecarabc"
        expected = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_palindrome_at_end(self):
        s = "abcracecar"
        expected = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    # --- Stress Tests and Edge Cases ---
    def test_max_length_all_same(self):
        """Tests near max length with all same chars (worst-case time)"""
        s = 'a' * 1000
        expected = s
        # This test might take slightly longer due to O(n^2) nature
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected,
                         f"Failed on s = {s[:10]}... (len {len(s)})")

    def test_max_length_no_long_palindrome(self):
        """Tests near max length with no long palindrome expected"""
        # Construct a string likely to not have long palindromes
        pattern = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = (pattern * (1000 // len(pattern) + 1))[:1000]
        result = self.solution.longestPalindrome(s)
        # Expect a very short palindrome (likely length 1, possibly 2 if adjacent same chars)
        self.assertLessEqual(
            len(result), 2, f"Failed on s = {s[:10]}... (len {len(s)})")

    def test_max_length_long_palindrome_middle(self):
        """Tests near max length with the longest palindrome in the middle."""
        prefix = "xyz" * 100  # 300 chars
        palindrome = "level" * 100  # 500 chars
        suffix = "123" * 67  # 201 chars -> total 1001, trim one
        s = prefix + palindrome + suffix[:-1]  # Total 1000
        expected = palindrome
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected,
                         f"Failed on s = ...long string... (len {len(s)})")

    def test_mixed_chars_digits_palindrome(self):
        """Tests string with mixed letters/digits forming the longest palindrome."""
        s = "a1b2c3c2b1a"
        expected = "a1b2c3c2b1a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

        s = "find12321needle"
        expected = "12321"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_mixed_chars_digits_short_palindrome(self):
        """Tests string with mixed letters/digits forming only short palindromes."""
        s = "a1b2c1d2e"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1, f"Failed on s = {s}")
        self.assertIn(result, list(s), f"Failed on s = {s}")

    def test_near_palindrome(self):
        """Tests a string that is almost a palindrome but fails by one char."""
        s = "racecax"
        expected = "aceca"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

        s = "topcooder"
        expected = "oo"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    # --- More Critical/Edge Cases ---
    def test_length_two_palindrome(self):
        s = "aa"
        expected = "aa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_length_two_no_palindrome(self):
        s = "ab"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1, f"Failed on s = {s}")
        self.assertIn(result, ['a', 'b'], f"Failed on s = {s}")

    def test_overlapping_palindromes(self):
        s = "bananas"
        expected = "anana"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_interleaved_palindromes(self):
        """Checks if the longest is chosen among multiple."""
        s = "abaxyzzyxfabcba"  # xyzzyx (6) vs abcba (5)
        expected = "xyzzyx"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_case_sensitive(self):
        """Tests case sensitivity."""
        s = "Racecar"
        expected = "aceca"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

        s = "aBcDcBa"
        # This string is itself a palindrome
        expected = "aBcDcBa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_mixed_complex_palindrome(self):
        s = "1a2b3c3b2a1"
        expected = "1a2b3c3b2a1"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_max_length_full_palindrome(self):
        """Tests max length string that is itself a palindrome."""
        s = "a" + ("b" * 998) + "a"
        expected = s
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected,
                         f"Failed on s = a...a (len {len(s)})")

    def test_max_length_palindrome_at_start(self):
        """Tests max length with longest palindrome at the beginning."""
        s = ("a" * 500) + ("b" * 500)
        expected = "a" * 500
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected,
                         f"Failed on s = a...b... (len {len(s)})")

    def test_max_length_palindrome_at_end(self):
        """Tests max length with longest palindrome at the end."""
        s = ("b" * 500) + ("a" * 500)
        expected_len = 500
        possible_results = ["b" * 500, "a" * 500]
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), expected_len,
                         f"Failed on s = b...a... (len {len(s)}) - Incorrect Length")
        self.assertIn(result, possible_results,
                      f"Failed on s = b...a... (len {len(s)}) - Incorrect String")


if __name__ == '__main__':
    unittest.main()
