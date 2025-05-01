import unittest
from .solution import Solution  # Relative import


class TestZigzagConversion(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_example2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_example3_numRows1(self):
        s = "A"
        numRows = 1
        expected = "A"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_numRows1_general(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numRows = 1
        expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_single_char(self):
        s = "B"
        numRows = 5
        expected = "B"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_numRows_equals_length(self):
        s = "ABCDE"
        numRows = 5
        expected = "ABCDE"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_numRows_greater_than_length(self):
        s = "ABCDE"
        numRows = 10
        expected = "ABCDE"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_numRows2(self):
        s = "ABCDE"
        numRows = 2
        expected = "ACEBD"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_with_symbols(self):
        s = "A,B.C"
        numRows = 2
        expected = "ABC,."
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_longer_string_numRows3(self):
        s = "THISISAZIGZAGTEST"
        numRows = 3
        # T   S   Z   G   T
        # H I I A I Z A T S
        # S   S   G   E
        expected = "TIIGTHSSZGATSIAZE"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")

    def test_longer_string_numRows5(self):
        s = "PYTHONISVERYUSEFUL"
        numRows = 5
        # P       N       Y
        # Y     S V     S F
        # T   I   E   U   U
        # H O     R Y     L
        # N       U
        expected = "PVUYSEFLTIREHNYSOU"
        self.assertEqual(self.solution.convert(s, numRows),
                         expected, f"Failed on s = {s}, numRows = {numRows}")


if __name__ == '__main__':
    unittest.main()
