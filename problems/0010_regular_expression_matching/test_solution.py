import unittest
# Use relative import for the solution
from .solution import Solution


class TestRegularExpressionMatching(unittest.TestCase):

    def setUp(self):
        """Set up the Solution object for each test."""
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.isMatch("aa", "a"))

    def test_example_2(self):
        self.assertTrue(self.solution.isMatch("aa", "a*"))

    def test_example_3(self):
        self.assertTrue(self.solution.isMatch("ab", ".*"))

    def test_dot_matches_single_char(self):
        self.assertTrue(self.solution.isMatch("a", "."))
        self.assertFalse(self.solution.isMatch("aa", "."))
        self.assertTrue(self.solution.isMatch("ab", ".."))
        self.assertFalse(self.solution.isMatch("a", ".."))

    def test_star_matches_zero(self):
        self.assertTrue(self.solution.isMatch("aab", "c*a*b"))
        # Empty string, pattern can match zero
        self.assertTrue(self.solution.isMatch("", "a*"))
        # Empty string, pattern can match zero
        self.assertTrue(self.solution.isMatch("", ".*"))
        self.assertTrue(self.solution.isMatch("", "a*b*c*"))

    def test_star_matches_one(self):
        self.assertTrue(self.solution.isMatch("a", "a*"))
        self.assertTrue(self.solution.isMatch("abc", "a*b*c*"))

    def test_star_matches_multiple(self):
        self.assertTrue(self.solution.isMatch("aaa", "a*"))
        self.assertTrue(self.solution.isMatch("aaaa", "a*a"))
        self.assertTrue(self.solution.isMatch("aaaa", "a*aa*"))
        self.assertTrue(self.solution.isMatch("aaaa", "a*aaa"))
        self.assertTrue(self.solution.isMatch("mississippi", "mis*is*ip*."))

    def test_dot_star_combinations(self):
        self.assertTrue(self.solution.isMatch("abc", ".*c"))
        self.assertTrue(self.solution.isMatch("abcd", ".*d"))
        self.assertFalse(self.solution.isMatch("abc", ".*d"))
        self.assertTrue(self.solution.isMatch("a", ".*"))
        self.assertTrue(self.solution.isMatch("aaaaaaaaaaaaab",
                        "a*a*a*a*a*a*a*a*a*a*a*a*b"))  # Long match

    def test_complex_patterns(self):
        # Doesn't match p*. requires one more char
        self.assertFalse(self.solution.isMatch("mississippi", "mis*is*p*."))
        self.assertFalse(self.solution.isMatch(
            "ab", ".*c"))  # Does not end with c
        self.assertTrue(self.solution.isMatch(
            "a", "ab*"))  # b* matches zero b's
        # Matches a, (b* zero), (a* two), (c* zero), a
        self.assertTrue(self.solution.isMatch("aaa", "ab*a*c*a"))
        # .* eats bbbb, a* eats zero, a matches a
        self.assertTrue(self.solution.isMatch("bbbba", ".*a*a"))

    def test_constraints_edge_cases(self):
        # Existing short cases
        s_short = "a"
        p_short = "a"
        self.assertTrue(self.solution.isMatch(s_short, p_short))
        p_short_star = "a*"
        self.assertTrue(self.solution.isMatch(s_short, p_short_star))
        p_short_dot = "."
        self.assertTrue(self.solution.isMatch(s_short, p_short_dot))

        # Max lengths (20) stress tests
        s_max_a = "a" * 20
        p_max_a_star = "a*" * 10  # 10 * 'a*' = length 20
        self.assertTrue(self.solution.isMatch(s_max_a, p_max_a_star))

        p_max_dot_star = ".*" * 10  # 10 * '.*' = length 20
        self.assertTrue(self.solution.isMatch(s_max_a, p_max_dot_star))

        s_max_ab = "ab" * 10  # length 20
        # len 20 -> This is not valid regex syntax for this problem. Let's use simpler patterns.
        p_max_ab_pattern = "(ab)*" * 5
        p_max_ab_match = ".*"  # Simple match
        self.assertTrue(self.solution.isMatch(s_max_ab, p_max_ab_match))
        p_max_ab_match_specific = ".*ab.*ab.*ab.*ab.*ab"  # length 20
        self.assertTrue(self.solution.isMatch(
            s_max_ab, p_max_ab_match_specific))
        p_max_ab_fail = ".*ac.*ab.*ab.*ab.*ab"  # length 20
        self.assertFalse(self.solution.isMatch(s_max_ab, p_max_ab_fail))

        s_max_mix = "a" * 19 + "b"
        p_max_mix_match = "a*a*a*a*a*a*a*a*a*b"  # len 19
        self.assertTrue(self.solution.isMatch(s_max_mix, p_max_mix_match))
        p_max_mix_fail = "a*a*a*a*a*a*a*a*a*c"  # len 19
        self.assertFalse(self.solution.isMatch(s_max_mix, p_max_mix_fail))
        p_max_mix_fail_star = "a*a*a*a*a*a*a*a*a*a*"  # len 20
        self.assertFalse(self.solution.isMatch(s_max_mix, p_max_mix_fail_star))

        s_max_unique = "abcdefghijklmnopqrst"
        self.assertTrue(self.solution.isMatch(s_max_unique, ".*"))  # len 2
        p_max_unique_dots = ".*" * 10  # len 20
        self.assertTrue(self.solution.isMatch(s_max_unique, p_max_unique_dots))
        p_max_unique_dots_star = "..*..*..*..*..*..*..*"  # len 20
        self.assertTrue(self.solution.isMatch(
            s_max_unique, p_max_unique_dots_star))
        p_max_unique_fail = "..*..*..*..*..*..*..u"  # len 20
        self.assertFalse(self.solution.isMatch(
            s_max_unique, p_max_unique_fail))

        s_long_prefix_suffix = "b" + "a" * 18 + "b"  # len 20
        p_long_match = "b.*b"  # len 4
        self.assertTrue(self.solution.isMatch(
            s_long_prefix_suffix, p_long_match))
        p_long_fail = "b.*c"  # len 4
        self.assertFalse(self.solution.isMatch(
            s_long_prefix_suffix, p_long_fail))


if __name__ == '__main__':
    unittest.main()
