import unittest
# Use relative import for standard test discovery
from .solution import Solution


class TestMyAtoi(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()
        self.INT_MAX = 2**31 - 1
        self.INT_MIN = -2**31

    def test_examples(self):
        """Test the examples provided in the problem description."""
        self.assertEqual(self.solution.myAtoi("42"), 42, "Example 1 Failed")
        self.assertEqual(self.solution.myAtoi(
            "   -42"), -42, "Example 2 Failed")
        self.assertEqual(self.solution.myAtoi(
            "1337c0d3"), 1337, "Example 3 Failed")
        self.assertEqual(self.solution.myAtoi("0-1"), 0, "Example 4 Failed")
        self.assertEqual(self.solution.myAtoi(
            "words and 987"), 0, "Example 5 Failed")

    def test_leading_whitespace(self):
        """Test strings with various leading whitespace."""
        self.assertEqual(self.solution.myAtoi("   123"), 123)
        self.assertEqual(self.solution.myAtoi("  -123 abc"), -123)

    def test_signs(self):
        """Test strings with signs."""
        self.assertEqual(self.solution.myAtoi("+1"), 1)
        self.assertEqual(self.solution.myAtoi("-1"), -1)
        self.assertEqual(self.solution.myAtoi(
            " +-12"), 0)  # Invalid: whitespace between sign and number
        self.assertEqual(self.solution.myAtoi(
            "+-12"), 0)  # Invalid sign sequence
        self.assertEqual(self.solution.myAtoi(
            "-+12"), 0)  # Invalid sign sequence
        # Sign followed by non-digit
        self.assertEqual(self.solution.myAtoi("  + "), 0)

    def test_leading_zeros(self):
        """Test numbers with leading zeros."""
        self.assertEqual(self.solution.myAtoi("0000042"), 42)
        self.assertEqual(self.solution.myAtoi("-0000012a42"), -12)
        self.assertEqual(self.solution.myAtoi(
            "  0000000000012345678"), 12345678)
        # Zero followed by non-digit (space)
        self.assertEqual(self.solution.myAtoi("   +0 123"), 0)

    def test_no_digits(self):
        """Test cases where no valid digits are found after optional sign/whitespace."""
        self.assertEqual(self.solution.myAtoi(""), 0)
        self.assertEqual(self.solution.myAtoi("   "), 0)
        self.assertEqual(self.solution.myAtoi("+"), 0)
        self.assertEqual(self.solution.myAtoi("-"), 0)
        self.assertEqual(self.solution.myAtoi("abc"), 0)
        self.assertEqual(self.solution.myAtoi("+abc"), 0)
        self.assertEqual(self.solution.myAtoi("  - word"), 0)
        self.assertEqual(self.solution.myAtoi("."), 0)
        self.assertEqual(self.solution.myAtoi("-."), 0)
        self.assertEqual(self.solution.myAtoi("+."), 0)

    def test_integer_limits(self):
        """Test values at and beyond the 32-bit integer limits."""
        self.assertEqual(self.solution.myAtoi(str(self.INT_MAX)), self.INT_MAX)
        self.assertEqual(self.solution.myAtoi(str(self.INT_MIN)), self.INT_MIN)
        self.assertEqual(self.solution.myAtoi("2147483646"), self.INT_MAX - 1)
        self.assertEqual(self.solution.myAtoi("-2147483647"), self.INT_MIN + 1)

        # Positive overflow
        self.assertEqual(self.solution.myAtoi("2147483648"),
                         self.INT_MAX)  # INT_MAX + 1
        self.assertEqual(self.solution.myAtoi("91283472332"),
                         self.INT_MAX)  # Much larger than INT_MAX
        # Causes overflow during multiplication
        self.assertEqual(self.solution.myAtoi("21474836470"), self.INT_MAX)

        # Negative overflow
        self.assertEqual(self.solution.myAtoi("-2147483649"),
                         self.INT_MIN)  # INT_MIN - 1
        self.assertEqual(self.solution.myAtoi("-91283472332"),
                         self.INT_MIN)  # Much smaller than INT_MIN
        # Causes overflow during multiplication
        self.assertEqual(self.solution.myAtoi("-21474836480"), self.INT_MIN)

    def test_mixed_characters(self):
        """Test strings with digits followed by non-digits."""
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.solution.myAtoi("-5-"), -5)
        self.assertEqual(self.solution.myAtoi("  -0012a42"), -12)
        self.assertEqual(self.solution.myAtoi("1.6"), 1)  # '.' is not a digit
        self.assertEqual(self.solution.myAtoi("123 456"), 123)

    def test_stress_and_coverage(self):
        """Test cases targeting constraints and specific edge conditions."""
        # Max length considerations (200 chars)
        max_len_positive = "1" * 199
        max_len_negative = "-1" + "1" * 198
        self.assertEqual(self.solution.myAtoi(max_len_positive), self.INT_MAX)
        self.assertEqual(self.solution.myAtoi(max_len_negative), self.INT_MIN)

        long_string_overflow = "9" * 200
        self.assertEqual(self.solution.myAtoi(
            long_string_overflow), self.INT_MAX)
        long_string_underflow = "-" + "9" * 199
        self.assertEqual(self.solution.myAtoi(
            long_string_underflow), self.INT_MIN)

        spaces_then_num = (" " * 190) + "12345"
        self.assertEqual(self.solution.myAtoi(spaces_then_num), 12345)

        spaces_sign_num = (" " * 190) + "-12345"
        self.assertEqual(self.solution.myAtoi(spaces_sign_num), -12345)

        spaces_sign_spaces = (" " * 198) + "- "
        self.assertEqual(self.solution.myAtoi(spaces_sign_spaces), 0)

        all_spaces = " " * 200
        self.assertEqual(self.solution.myAtoi(all_spaces), 0)

        all_letters = "a" * 200
        self.assertEqual(self.solution.myAtoi(all_letters), 0)

        num_then_letters = "12345" + ("a" * 195)
        self.assertEqual(self.solution.myAtoi(num_then_letters), 12345)

        # Specific overflow trigger points
        # Positive: 214748364 -> add 7 (ok), add 8 (overflow)
        self.assertEqual(self.solution.myAtoi("2147483647"), self.INT_MAX)
        self.assertEqual(self.solution.myAtoi("2147483648"), self.INT_MAX)
        # Just before overflow check limit
        self.assertEqual(self.solution.myAtoi("214748364"), 214748364)

        # Negative: -214748364 -> add 8 (ok), add 9 (overflow)
        self.assertEqual(self.solution.myAtoi("-2147483648"), self.INT_MIN)
        self.assertEqual(self.solution.myAtoi("-2147483649"), self.INT_MIN)
        # Just before overflow check limit
        self.assertEqual(self.solution.myAtoi("-214748364"), -214748364)

        # Other mixed cases
        self.assertEqual(self.solution.myAtoi("  -0 "), 0)  # Sign, zero, space
        self.assertEqual(self.solution.myAtoi("0.1"), 0)  # Zero, dot
        # Whitespace between sign and digit
        self.assertEqual(self.solution.myAtoi(" + 1"), 0)
        self.assertEqual(self.solution.myAtoi(
            "123   "), 123)  # Trailing whitespace
        self.assertEqual(self.solution.myAtoi("123e4"), 123)  # Non-digit 'e'
        # More whitespace between sign and digit
        self.assertEqual(self.solution.myAtoi("  - 1"), 0)


if __name__ == '__main__':
    unittest.main()
