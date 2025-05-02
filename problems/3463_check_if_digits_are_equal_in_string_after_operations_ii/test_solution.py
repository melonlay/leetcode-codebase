import unittest
# Use relative import for solution within the same package/directory structure
from .solution import Solution


class TestHasSameDigits(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before each test method."""
        self.solver = Solution()

    def test_example1(self):
        """Test the first example from the problem description."""
        self.assertTrue(self.solver.hasSameDigits("3902"))
        # 3902 -> 292 -> 11 -> True

    def test_example2(self):
        """Test the second example from the problem description."""
        self.assertFalse(self.solver.hasSameDigits("34789"))
        # 34789 -> 7157 -> 862 -> 48 -> False

    def test_min_length(self):
        """Test with the minimum allowed string length (3)."""
        self.assertTrue(self.solver.hasSameDigits("111"))  # 111 -> 22 -> True
        self.assertTrue(self.solver.hasSameDigits("121"))  # 121 -> 33 -> True
        self.assertFalse(self.solver.hasSameDigits("123")
                         )  # 123 -> 35 -> False

    def test_all_same_digits(self):
        """Test cases where all initial digits are the same."""
        self.assertTrue(self.solver.hasSameDigits(
            "5555"))  # 5555 -> 000 -> 00 -> True
        # 77777 -> 4444 -> 888 -> 66 -> True
        self.assertTrue(self.solver.hasSameDigits("77777"))

    def test_alternating_digits(self):
        """Test cases with alternating digits."""
        self.assertTrue(self.solver.hasSameDigits(
            "1010"))  # 1010 -> 111 -> 22 -> True
        # 10101 -> 1111 -> 222 -> 44 -> True
        self.assertTrue(self.solver.hasSameDigits("10101"))
        # 1212 -> 333 -> 66 -> True # Wait, C(2,i)=[1,2,1]. d0=(1*1+2*2+1*1)%10=6. d1=(1*2+2*1+1*2)%10=6. True.
        # 12121 -> 3333 -> 666 -> 22 -> True # Wait, C(3,i)=[1,3,3,1]. d0=(1*1+3*2+3*1+1*2)%10=(1+6+3+2)%10=2. d1=(1*2+3*1+3*2+1*1)%10=(2+3+6+1)%10=2. True.
        # Re-evaluating alternating tests. If the pattern holds, the result seems to be True.
        # Let's try a false case: 2121 -> 333 -> 66 -> True.
        # 21212 -> 3333 -> 666 -> 22 -> True.
        # It seems alternating patterns might often lead to True. Let's trust the logic.
        # Keep the original tests based on my trace
        # Should be True based on trace
        self.assertTrue(self.solver.hasSameDigits("1212"))
        # Should be True based on trace
        self.assertTrue(self.solver.hasSameDigits("12121"))

    def test_zeros(self):
        """Test cases including zeros."""
        self.assertTrue(self.solver.hasSameDigits("000"))  # 000 -> 00 -> True
        self.assertTrue(self.solver.hasSameDigits(
            "1001"))  # 1001 -> 101 -> 11 -> True
        self.assertFalse(self.solver.hasSameDigits(
            "1000"))  # 1000 -> 100 -> 10 -> False

    def test_zero_coefficients(self):
        """Test case where binomial coefficients C(k, i) % 10 become zero (k=5)."""
        self.assertFalse(self.solver.hasSameDigits("1234567"))

    def test_palindrome(self):
        """Test a palindromic input."""
        self.assertTrue(self.solver.hasSameDigits("12321"))

    def test_longer_strings(self):
        """Test with moderately longer strings."""
        # Based on the property that if all digits are the same, the result is True
        self.assertTrue(self.solver.hasSameDigits("1" * 50))
        self.assertTrue(self.solver.hasSameDigits("8" * 49))
        # A mixed longer string
        s = "12345" * 10
        n = len(s)
        k = n - 2
        digits = [int(d) for d in s]
        d0, d1 = 0, 0
        for i in range(k + 1):
            coeff = self.solver._nCr_mod10(k, i)
            if coeff == 0:
                continue
            d0 = (d0 + coeff * digits[i]) % 10
            d1 = (d1 + coeff * digits[i+1]) % 10
        self.assertEqual(self.solver.hasSameDigits(s), d0 == d1)


# This allows running the tests directly when the script is executed
if __name__ == '__main__':
    unittest.main()
