import unittest
from .solution import Solution  # Relative import


class TestPalindromeNumber(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solution = Solution()

    def test_example1(self):
        """Test the first example: 121"""
        self.assertTrue(self.solution.isPalindrome(121), "Failed on x = 121")

    def test_example2(self):
        """Test the second example: -121"""
        self.assertFalse(self.solution.isPalindrome(-121),
                         "Failed on x = -121")

    def test_example3(self):
        """Test the third example: 10"""
        self.assertFalse(self.solution.isPalindrome(10), "Failed on x = 10")

    def test_zero(self):
        """Test edge case: 0"""
        self.assertTrue(self.solution.isPalindrome(0), "Failed on x = 0")

    def test_single_digit(self):
        """Test edge case: single digit positive number"""
        self.assertTrue(self.solution.isPalindrome(7), "Failed on x = 7")

    def test_negative_number(self):
        """Test another negative number"""
        self.assertFalse(self.solution.isPalindrome(-101),
                         "Failed on x = -101")

    def test_number_ending_in_zero(self):
        """Test a non-zero number ending in 0"""
        self.assertFalse(self.solution.isPalindrome(120), "Failed on x = 120")

    def test_even_digits_palindrome(self):
        """Test a palindrome with an even number of digits"""
        self.assertTrue(self.solution.isPalindrome(1221), "Failed on x = 1221")

    def test_large_palindrome(self):
        """Test a larger palindrome"""
        self.assertTrue(self.solution.isPalindrome(
            123454321), "Failed on x = 123454321")

    def test_large_non_palindrome(self):
        """Test a larger non-palindrome"""
        self.assertFalse(self.solution.isPalindrome(
            123456789), "Failed on x = 123456789")

    def test_max_int(self):
        """Test the maximum 32-bit signed integer constraint"""
        self.assertFalse(self.solution.isPalindrome(2**31 - 1),
                         "Failed on x = 2^31 - 1")  # 2147483647

    def test_min_int(self):
        """Test the minimum 32-bit signed integer constraint"""
        self.assertFalse(self.solution.isPalindrome(-2**31),
                         "Failed on x = -2^31")


if __name__ == '__main__':
    unittest.main()
