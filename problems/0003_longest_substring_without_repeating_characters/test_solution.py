import unittest
import string  # Import string module
from .solution import Solution  # Relative import


class TestLongestSubstring(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solver = Solution()

    def test_example_1(self):
        """Test the first example: s = "abcabcbb"""
        s = "abcabcbb"
        expected = 3
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_example_2(self):
        """Test the second example: s = "bbbbb"""
        s = "bbbbb"
        expected = 1
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_example_3(self):
        """Test the third example: s = "pwwkew"""
        s = "pwwkew"
        expected = 3
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_empty_string(self):
        """Test an empty string."""
        s = ""
        expected = 0
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_no_repeating_chars(self):
        """Test a string with no repeating characters."""
        s = "abcdefg"
        expected = 7
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_one_char(self):
        """Test a string with only one character."""
        s = "a"
        expected = 1
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_with_space(self):
        """Test a string containing a space."""
        s = " a b c "
        expected = 3  # "a b", " b ", "b c", " c " -> max is 3
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_complex_case(self):
        """Test a more complex string."""
        s = "dvdf"
        expected = 3  # "vdf"
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_symbols_and_digits(self):
        """Test string with symbols and digits."""
        s = "a1b!c@d#e$"
        expected = 10
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    # --- Stress Tests and Edge Cases based on Constraints ---

    def test_long_string_all_same_char(self):
        """Stress test with a long string of the same character."""
        size = 10000  # Reduced from 5*10^4 for reasonable test time
        s = 'a' * size
        expected = 1
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected,
                         f"Failed on long string of 'a's (size {size})")

    def test_long_string_repeating_pattern(self):
        """Stress test with a long string with a repeating pattern."""
        pattern = "abcde"
        repetitions = 2000  # Total length 10000
        s = pattern * repetitions
        expected = 5  # Length of "abcde"
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(
            result, expected, f"Failed on long repeating pattern '{pattern}' (repetitions {repetitions})")

    def test_long_string_unique_prefix(self):
        """Stress test with a long unique prefix followed by repetitions."""
        # Use string.printable which includes letters, digits, punctuation, whitespace (~100 chars)
        unique_chars = string.printable
        prefix_len = 95  # Test length close to the size of unique_chars
        s = unique_chars[:prefix_len] + 'a' * 5000
        expected = prefix_len
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(
            result, expected, f"Failed on long string with unique prefix (len {prefix_len})")

    def test_long_string_unique_suffix(self):
        """Stress test with repetitions followed by a long unique suffix."""
        # Use string.printable
        unique_chars = string.printable
        suffix_len = 95
        s = 'a' * 5000 + unique_chars[:suffix_len]
        expected = suffix_len
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(
            result, expected, f"Failed on long string with unique suffix (len {suffix_len})")

    def test_max_possible_unique_chars(self):
        """Test string with ~95 unique printable ASCII characters."""
        # Generate a string with unique printable ASCII chars (approx range 32-126)
        # Should be 95 unique chars
        s = "".join([chr(i) for i in range(32, 127)])
        expected = 95
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(
            result, expected, f"Failed on string with {expected} unique ASCII chars")

        # Test with this unique block repeated
        s_repeated = s + s[:10]
        expected_repeated = 95
        result_repeated = self.solver.lengthOfLongestSubstring(s_repeated)
        self.assertEqual(result_repeated, expected_repeated,
                         f"Failed on repeated string with {expected} unique ASCII chars")

    # --- Additional Edge Cases ---
    def test_complex_shrinking(self):
        """Test case requiring multiple left shifts: tmmzuxt"""
        s = "tmmzuxt"
        expected = 5  # mzuxt
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_immediate_repetition_after_start(self):
        """Test repetition right after the start."""
        s = "aab"
        expected = 2  # ab
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_repetition_at_end_of_longest(self):
        """Test repetition immediately after the longest substring."""
        s = "abcda"
        expected = 4  # abcd
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_mixed_unique_substring(self):
        """Test substring with mixed character types."""
        s = "a 1!B c@"
        expected = 6  # Corrected expectation: "1!B c@" has length 6
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_only_spaces(self):
        """Test string consisting of only spaces."""
        s = "   "
        expected = 1  # " "
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_only_unique_symbols(self):
        """Test string with only unique symbols."""
        s = "!@#$%^"
        expected = 6
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")

    def test_only_repeating_symbols(self):
        """Test string with repeating symbols."""
        s = "!@#$!@"
        expected = 4  # @#$! or #$!@
        result = self.solver.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"Failed on s = {s}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
