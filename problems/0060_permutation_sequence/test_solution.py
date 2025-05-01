import unittest
import math
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example: n=3, k=3 -> "213"."""
        self.assertEqual(self.solution.getPermutation(3, 3), "213")

    def test_example_2(self):
        """Test the second example: n=4, k=9 -> "2314"."""
        self.assertEqual(self.solution.getPermutation(4, 9), "2314")

    def test_example_3(self):
        """Test the third example: n=3, k=1 -> "123"."""
        self.assertEqual(self.solution.getPermutation(3, 1), "123")

    def test_n1_k1(self):
        """Test constraint: n=1, k=1 -> "1"."""
        self.assertEqual(self.solution.getPermutation(1, 1), "1")

    def test_n2_k1(self):
        """Test edge case: n=2, k=1 -> "12"."""
        self.assertEqual(self.solution.getPermutation(2, 1), "12")

    def test_n2_k2(self):
        """Test edge case: n=2, k=2 -> "21"."""
        self.assertEqual(self.solution.getPermutation(2, 2), "21")

    def test_n3_k2(self):
        """Test edge case: n=3, k=2 -> "132"."""
        self.assertEqual(self.solution.getPermutation(3, 2), "132")

    def test_n3_k4(self):
        """Test edge case: n=3, k=4 -> "231"."""
        self.assertEqual(self.solution.getPermutation(3, 4), "231")

    def test_n3_k5(self):
        """Test edge case: n=3, k=5 -> "312"."""
        self.assertEqual(self.solution.getPermutation(3, 5), "312")

    def test_n3_k6(self):
        """Test last permutation: n=3, k=6 -> "321"."""
        self.assertEqual(self.solution.getPermutation(3, 6), "321")

    def test_max_n_first_k(self):
        """Test max constraint n=9, k=1 -> "123456789"."""
        self.assertEqual(self.solution.getPermutation(9, 1), "123456789")

    def test_max_n_last_k(self):
        """Test max constraint n=9, k=9! -> "987654321"."""
        n = 9
        k = math.factorial(n)
        self.assertEqual(self.solution.getPermutation(n, k), "987654321")

    def test_max_n_mid_k(self):
        """Test max constraint n=9, k=100000 -> "378419265"."""
        # Manually calculated or derived for verification
        # For n=9, 8! = 40320
        # k=100000 -> k-1 = 99999
        # index = 99999 // 40320 = 2. Digit = 3. Remaining k = 99999 % 40320 = 19359. Digits = [1,2,4,5,6,7,8,9]
        # index = 19359 // 7! (5040) = 3. Digit = 7. Remaining k = 19359 % 5040 = 4239. Digits = [1,2,4,5,6,8,9]
        # index = 4239 // 6! (720) = 5. Digit = 8. Remaining k = 4239 % 720 = 639. Digits = [1,2,4,5,6,9]
        # index = 639 // 5! (120) = 5. Digit = 9. Remaining k = 639 % 120 = 39. Digits = [1,2,4,5,6]
        # index = 39 // 4! (24) = 1. Digit = 2. Remaining k = 39 % 24 = 15. Digits = [1,4,5,6]
        # index = 15 // 3! (6) = 2. Digit = 5. Remaining k = 15 % 6 = 3. Digits = [1,4,6]
        # index = 3 // 2! (2) = 1. Digit = 4. Remaining k = 3 % 2 = 1. Digits = [1,6]
        # index = 1 // 1! (1) = 1. Digit = 6. Remaining k = 1 % 1 = 0. Digits = [1]
        # index = 0 // 0! (1) = 0. Digit = 1. Remaining k = 0 % 1 = 0. Digits = []
        # Result: 378925461 - Rerun calculation needed.

        # Re-calculating for k=100000, n=9
        # k=99999 (0-based)
        # Digits: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # i=9, fact=8!=40320. index=99999//40320=2. Pick digits[2]='3'. result='3'. k=99999%40320=19359. digits=[1,2,4,5,6,7,8,9]
        # i=8, fact=7!=5040. index=19359//5040=3. Pick digits[3]='5'. result='35'. k=19359%5040=4239. digits=[1,2,4,6,7,8,9]
        # i=7, fact=6!=720. index=4239//720=5. Pick digits[5]='8'. result='358'. k=4239%720=639. digits=[1,2,4,6,7,9]
        # i=6, fact=5!=120. index=639//120=5. Pick digits[5]='9'. result='3589'. k=639%120=39. digits=[1,2,4,6,7]
        # i=5, fact=4!=24. index=39//24=1. Pick digits[1]='2'. result='35892'. k=39%24=15. digits=[1,4,6,7]
        # i=4, fact=3!=6. index=15//6=2. Pick digits[2]='6'. result='358926'. k=15%6=3. digits=[1,4,7]
        # i=3, fact=2!=2. index=3//2=1. Pick digits[1]='4'. result='3589264'. k=3%2=1. digits=[1,7]
        # i=2, fact=1!=1. index=1//1=1. Pick digits[1]='7'. result='35892647'. k=1%1=0. digits=[1]
        # i=1, fact=0!=1. index=0//1=0. Pick digits[0]='1'. result='358926471'. k=0%1=0. digits=[]
        # Expected: 358926471
        self.assertEqual(self.solution.getPermutation(9, 100000), "358926471")


if __name__ == '__main__':
    unittest.main()
