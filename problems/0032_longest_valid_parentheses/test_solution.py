import unittest
from .solution import Solution


class TestLongestValidParentheses(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Input from LeetCode Example 1
        self.assertEqual(self.solution.longestValidParentheses(
            "(()"), 2, "Example 1 failed")

    def test_example2(self):
        self.assertEqual(self.solution.longestValidParentheses(
            ")()())"), 4, "Example 2 failed")

    def test_example3(self):
        self.assertEqual(self.solution.longestValidParentheses(
            ""), 0, "Example 3 (Empty string) failed")

    def test_no_valid(self):
        self.assertEqual(self.solution.longestValidParentheses(
            ")(("), 0, "Test No Valid failed")

    def test_all_opening(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "((("), 0, "Test All Opening failed")

    def test_all_closing(self):
        self.assertEqual(self.solution.longestValidParentheses(
            ")))"), 0, "Test All Closing failed")

    def test_simple_valid(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "()()"), 4, "Test Simple Valid failed")

    def test_nested_valid(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "(())("), 4, "Test Nested Valid failed")

    def test_complex1(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "()(()"), 2, "Test Complex 1 failed")

    def test_complex2(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "(()())"), 6, "Test Complex 2 failed")

    def test_invalid_start(self):
        self.assertEqual(self.solution.longestValidParentheses(
            ")(("), 0, "Test Invalid Start failed")

    def test_invalid_end(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "()("), 2, "Test Invalid End failed")

    def test_long_alternating(self):
        s = "()" * 1000
        self.assertEqual(self.solution.longestValidParentheses(
            s), 2000, "Test Long Alternating failed")

    def test_long_nested(self):
        s = "(" * 1000 + ")" * 1000
        self.assertEqual(self.solution.longestValidParentheses(
            s), 2000, "Test Long Nested failed")

    def test_mixed_long(self):
        s = "())((())())((" * 100
        # Longest within one unit is "((())())" -> 8
        # But across units, e.g., "... (( )) (( ...", the connection allows for longer:
        # unit1 = ")..)((())())(( "
        # unit2 = ")..)((())())(( "
        #         ^ ^
        # The '))' at the start of unit 2 close the '((' at the end of unit 1,
        # extending the valid sequence "((())())" from unit 1.
        # The sequence across the boundary becomes: "((())()))))" which has length 12.
        self.assertEqual(self.solution.longestValidParentheses(
            s), 12, "Test Mixed Long failed")

    def test_leading_closing(self):
        self.assertEqual(self.solution.longestValidParentheses(
            "))(())"), 4, "Test Leading Closing failed")


if __name__ == '__main__':
    unittest.main()
