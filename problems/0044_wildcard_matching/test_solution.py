import unittest
import os  # For skipping slow tests
from .solution import Solution

# Flag to run slow stress tests (e.g., set environment variable RUN_SLOW_TESTS=1)
RUN_SLOW_TESTS = os.environ.get('RUN_SLOW_TESTS') == '1'


class TestWildcardMatch(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def test_example_cases(self):
        """Test the examples provided by LeetCode."""
        self.assertFalse(self.solution.isMatch("aa", "a"), "Example 1")
        self.assertTrue(self.solution.isMatch("aa", "*"), "Example 2")
        self.assertFalse(self.solution.isMatch("cb", "?a"), "Example 3")
        self.assertTrue(self.solution.isMatch(
            "adceb", "*a*b"), "Example 4 (Common)")
        self.assertFalse(self.solution.isMatch(
            "acdcb", "a*c?b"), "Example 5 (Common)")

    def test_empty_string_and_pattern(self):
        """Test cases involving empty strings and patterns."""
        self.assertTrue(self.solution.isMatch("", ""),
                        "Empty string, empty pattern")
        self.assertTrue(self.solution.isMatch("", "*"),
                        "Empty string, star pattern")
        self.assertTrue(self.solution.isMatch("", "*****"),
                        "Empty string, multiple stars")
        self.assertFalse(self.solution.isMatch("", "?"),
                         "Empty string, question mark")
        self.assertFalse(self.solution.isMatch("", "a"),
                         "Empty string, char pattern")
        self.assertFalse(self.solution.isMatch("a", ""),
                         "Non-empty string, empty pattern")
        self.assertFalse(self.solution.isMatch("abc", ""),
                         "Longer string, empty pattern")

    def test_star_behavior(self):
        """Test various behaviors of the '*' wildcard."""
        self.assertTrue(self.solution.isMatch(
            "abc", "*c"), "Star matches prefix")
        self.assertTrue(self.solution.isMatch(
            "abc", "a*c"), "Star matches middle")
        self.assertTrue(self.solution.isMatch(
            "abc", "a*"), "Star matches suffix")
        self.assertTrue(self.solution.isMatch(
            "abc", "*abc*"), "Stars at both ends")
        self.assertTrue(self.solution.isMatch(
            "abc", "***a***b***c***"), "Multiple stars")
        self.assertTrue(self.solution.isMatch(
            "abc", "a*b*c"), "Stars separating chars")
        self.assertFalse(self.solution.isMatch("abc", "a*d"),
                         "Star cannot make char match fail")
        self.assertTrue(self.solution.isMatch(
            "mississippi", "m*iss*"), "Star matching sequences")
        self.assertFalse(self.solution.isMatch(
            "mississippi", "m*iss*p*a"), "Star cannot invent chars")
        # Pattern "*a*" cannot match empty string because 'a' requires a character.
        self.assertFalse(self.solution.isMatch(
            "", "*a*"), "Star matching empty between chars - Expected False")
        self.assertTrue(self.solution.isMatch("a", "*a*"),
                        "Star matching empty around char")

    def test_question_mark_behavior(self):
        """Test various behaviors of the '?' wildcard."""
        self.assertTrue(self.solution.isMatch(
            "a", "?"), "Single char matches ?")
        self.assertTrue(self.solution.isMatch("abc", "???"), "Multiple ?")
        self.assertTrue(self.solution.isMatch("abc", "a?c"), "? in middle")
        self.assertFalse(self.solution.isMatch("ab", "a?c"),
                         "? doesn't match missing char")
        self.assertFalse(self.solution.isMatch(
            "ac", "a?c"), "? requires a char")

    def test_combined_wildcards(self):
        """Test combinations of '?' and '*'."""
        self.assertTrue(self.solution.isMatch(
            "abcdef", "a*c?e*f"), "Complex combination 1")
        self.assertTrue(self.solution.isMatch(
            "xaylmz", "x?y*z"), "Complex combination 2")
        self.assertFalse(self.solution.isMatch(
            "mississippi", "m??*ss*?i*pi"), "Complex combination 3 (False)")
        self.assertTrue(self.solution.isMatch(
            "abcabczzzde", "*abc???de*"), "Complex combination 4 (True)")

    def test_additional_coverage(self):
        """More cases for edge conditions and coverage."""
        self.assertTrue(self.solution.isMatch(
            "abefcdgiescdfimde", "ab*cd?i*de"), "Coverage 1")
        self.assertFalse(self.solution.isMatch("a", "a*a"),
                         "Coverage 2: * cannot backtrack past required char")
        self.assertTrue(self.solution.isMatch("aa", "*a"),
                        "Coverage 3: Star at start matching one char")
        self.assertTrue(self.solution.isMatch("a", "*a"),
                        "Coverage 4: Star at start matching zero chars")
        self.assertTrue(self.solution.isMatch("ab", "?*"),
                        "Coverage 5: ? followed by *")
        self.assertTrue(self.solution.isMatch(
            "aasdfkasdf", "*f"), "Coverage 6")
        # The pattern *?*?* requires at least two characters for the two '?'
        self.assertFalse(self.solution.isMatch("b", "*?*?*"),
                         "Coverage 7: Expected False")
        self.assertFalse(self.solution.isMatch("b", "*?*?"),
                         "Coverage 8: Requires two chars")
        # This string ends with 'a', so pattern ending in 'b' cannot match
        self.assertFalse(self.solution.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba",
                         "a*******b"), "Coverage 9: Expected False (string ends in 'a')")
        self.assertFalse(self.solution.isMatch(
            "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******c"), "Coverage 10: Many stars non-match")
        self.assertTrue(self.solution.isMatch(
            "ab", "*?*"), "Coverage 11: True")
        # Pattern starts with 'c', string starts with 'a'. Cannot match.
        self.assertFalse(self.solution.isMatch(
            "aab", "c*a*b"), "Coverage 12: Expected False")

    @unittest.skipUnless(RUN_SLOW_TESTS, "Skipping slow stress tests")
    def test_stress_tests_slow(self):
        """Performance tests with large inputs (potentially slow)."""
        print("\nRunning SLOW stress tests...")  # Indicate slow tests are running

        s_long = "a" * 1998 + "b"
        p_long_match = "a*" * 999 + "b"
        p_long_nomatch = "a*" * 999 + "c"
        self.assertTrue(self.solution.isMatch(
            s_long, p_long_match), "Stress 1 (Long, Match)")
        self.assertFalse(self.solution.isMatch(
            s_long, p_long_nomatch), "Stress 2 (Long, No Match)")

        s = 'a' * 1000 + 'b' * 1000
        p = '*' * 1000 + 'a' * 500 + 'b' * 1000
        self.assertFalse(self.solution.isMatch(
            s, p), "Stress 3 (Very Long, No Match)")

        s = 'a' * 2000
        p = '*' * 1000 + 'a' * 1000
        self.assertTrue(self.solution.isMatch(s, p),
                        "Stress 4 (Max Length Match)")

        # This is likely the absolute worst case: ~2000 * ~2000 DP table
        s = 'a' * 1999
        p = 'a*' * 999 + 'a'
        self.assertTrue(self.solution.isMatch(s, p),
                        "Stress 5 (Near Max, Complex Pattern Match)")

    def test_stress_tests_fast(self):
        """Performance tests expected to be relatively fast despite large N."""
        s_long = "a" * 2000
        self.assertTrue(self.solution.isMatch(s_long, "*"),
                        "Stress Fast 1 (Long s, simple p)")
        self.assertTrue(self.solution.isMatch(s_long, "*"*2000),
                        "Stress Fast 2 (Long s, long p simple)")
        self.assertTrue(self.solution.isMatch(s_long, "?"*2000),
                        "Stress Fast 3 (Long s, long p simple)")
        self.assertTrue(self.solution.isMatch(s_long, "a"*2000),
                        "Stress Fast 4 (Long s, long p simple)")
        self.assertFalse(self.solution.isMatch(s_long, "a*b"),
                         "Stress Fast 5 (Long s, simple p no match)")
        self.assertTrue(self.solution.isMatch("a", "*"*2000),
                        "Stress Fast 6 (Short s, long p)")
        self.assertTrue(self.solution.isMatch("a", "*"*1999 + "a"),
                        "Stress Fast 7 (Short s, long p match)")
        self.assertFalse(self.solution.isMatch("a", "*"*1999 + "b"),
                         "Stress Fast 8 (Short s, long p no match)")


if __name__ == '__main__':
    unittest.main()
