import unittest
# Use relative import for the Solution class
from .solution import Solution


class TestReverseInteger(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example: 123 -> 321"""
        self.assertEqual(self.solution.reverse(123), 321, "Failed on x = 123")

    def test_example_2(self):
        """Test the second example: -123 -> -321"""
        self.assertEqual(self.solution.reverse(-123), -
                         321, "Failed on x = -123")

    def test_example_3(self):
        """Test the third example: 120 -> 21"""
        self.assertEqual(self.solution.reverse(120), 21, "Failed on x = 120")

    def test_zero(self):
        """Test input 0"""
        self.assertEqual(self.solution.reverse(0), 0, "Failed on x = 0")

    def test_single_digit_positive(self):
        """Test a single positive digit"""
        self.assertEqual(self.solution.reverse(5), 5, "Failed on x = 5")

    def test_single_digit_negative(self):
        """Test a single negative digit"""
        self.assertEqual(self.solution.reverse(-8), -8, "Failed on x = -8")

    def test_positive_overflow(self):
        """Test a positive number that overflows upon reversal"""
        # 2^31 - 1 = 2147483647
        # Reversing 1534236469 gives 9646324351, which is > 2^31 - 1
        self.assertEqual(self.solution.reverse(1534236469), 0,
                         "Failed on positive overflow x = 1534236469")
        # Reversing 1563847412 gives 2147483651, which is > 2^31 - 1
        self.assertEqual(self.solution.reverse(1563847412), 0,
                         "Failed on positive overflow x = 1563847412")

    def test_negative_overflow(self):
        """Test a negative number that overflows upon reversal"""
        # -2^31 = -2147483648
        # Reversing -1534236469 gives -9646324351, which is < -2^31
        self.assertEqual(self.solution.reverse(-1534236469), 0,
                         "Failed on negative overflow x = -1534236469")
        # Reversing -2147483648 gives -8463847412 (effectively), which is < -2^31
        self.assertEqual(self.solution.reverse(-2147483648), 0,
                         "Failed on negative overflow x = -2147483648")
        # Reversing -1563847412 gives -2147483651, which is < -2^31
        self.assertEqual(self.solution.reverse(-1563847412), 0,
                         "Failed on negative overflow x = -1563847412")

    def test_max_int(self):
        """Test the maximum 32-bit signed integer (reverses to non-overflow)"""
        # 2147483647 -> 7463847412 (overflows)
        self.assertEqual(self.solution.reverse(
            2147483647), 0, "Failed on x = MAX_INT")

    def test_just_below_overflow_positive(self):
        """Test a positive number whose reversal just fits"""
        self.assertEqual(self.solution.reverse(1463847412),
                         2147483641, "Failed on positive just below overflow")

    def test_just_below_overflow_negative(self):
        """Test a negative number whose reversal just fits"""
        # Reversing -1463847412 gives -2147483641 which fits
        self.assertEqual(self.solution.reverse(-1463847412), -
                         2147483641, "Failed on negative just below overflow")

    def test_large_number_ending_zero(self):
        """Test large positive number ending in zero"""
        # 1000000003 reverses to 3000000001 which > 2^31 - 1
        self.assertEqual(self.solution.reverse(
            1000000003), 0, "Failed on large positive ending zero - overflow expected")
        self.assertEqual(self.solution.reverse(
            1000000000), 1, "Failed on 1000000000")
        self.assertEqual(self.solution.reverse(2147483640), 463847412,
                         "Failed on large positive ending zero near max")

    def test_large_negative_number_ending_zero(self):
        """Test large negative number ending in zero"""
        self.assertEqual(self.solution.reverse(-1000000000), -
                         1, "Failed on -1000000000")
        self.assertEqual(self.solution.reverse(-2147483640), -
                         463847412, "Failed on large negative ending zero near min")

    def test_number_reversing_to_max_div_10(self):
        """Test number whose reversal is INT_MAX // 10"""
        # INT_MAX // 10 = 214748364
        self.assertEqual(self.solution.reverse(463847412),
                         214748364, "Failed on reversing to INT_MAX // 10")

    def test_number_reversing_to_near_max(self):
        """Test number whose reversal is close to INT_MAX"""
        self.assertEqual(self.solution.reverse(1147483641),
                         1463847411, "Failed on 1147483641")

    def test_number_reversing_to_near_min(self):
        """Test number whose reversal is close to INT_MIN"""
        self.assertEqual(self.solution.reverse(-1147483641), -
                         1463847411, "Failed on -1147483641")
        # Reversing -8463847412 (hypothetical) gives -2147483648 (MIN_INT)
        # The input -8463847412 is out of bounds. Check input near it.
        self.assertEqual(self.solution.reverse(-1463847412), -2147483641,
                         "Failed on -1463847412")  # Already present, good check

    def test_near_max_int_overflow(self):
        """Test INT_MAX - 1 which overflows on reverse"""
        self.assertEqual(self.solution.reverse(
            2147483646), 0, "Failed on INT_MAX - 1")

    def test_near_min_int_overflow(self):
        """Test INT_MIN + 1 which overflows on reverse"""
        self.assertEqual(self.solution.reverse(-2147483647),
                         0, "Failed on INT_MIN + 1")

    def test_positive_palindrome(self):
        """Test a positive palindromic number"""
        self.assertEqual(self.solution.reverse(123454321),
                         123454321, "Failed on positive palindrome")

    def test_negative_palindrome(self):
        """Test a negative palindromic number"""
        self.assertEqual(self.solution.reverse(-123454321), -
                         123454321, "Failed on negative palindrome")

    def test_large_non_overflowing_positive(self):
        """Test a large positive number that doesn't overflow"""
        self.assertEqual(self.solution.reverse(1000000001),
                         1000000001, "Failed on 1000000001")

    def test_large_non_overflowing_negative(self):
        """Test a large negative number that doesn't overflow"""
        self.assertEqual(self.solution.reverse(-1000000001), -
                         1000000001, "Failed on -1000000001")


if __name__ == '__main__':
    unittest.main()
