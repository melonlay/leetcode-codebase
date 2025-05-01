import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        # Use assertCountEqual because the order of indices doesn't matter
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_example2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_no_match(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_word_not_present(self):
        s = "foobar"
        words = ["baz", "qux"]
        expected = []
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_empty_s(self):
        s = ""
        words = ["a", "b"]
        expected = []
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_empty_words(self):
        s = "abcdef"
        words = []
        expected = []
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_s_too_short(self):
        s = "ab"
        words = ["a", "b", "c"]
        expected = []
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_duplicate_words_in_list(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "foo"]
        # Both "barfoofoo" (0) and "foofoobar" (3) match counts.
        expected = [0, 3]
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_duplicate_words_single_match(self):
        s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        words = ["fooo", "barr", "wing", "ding", "wing"]
        expected = [13]  # "foooowingdingbarrwing"
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_overlapping_matches(self):
        s = "ababaab"  # Indices 0123456 -> a b a b a a b
        words = ["ab", "ba"]
        # Strict Definition Check:
        # Target Permutations: "abba", "baab"
        # Actual Substrings:
        # s[0:4]="abab" - No
        # s[1:5]="baba" - No
        # s[2:6]="abaa" - No
        # s[3:7]="baab" - YES! Matches permutation ["ba", "ab"]
        expected = [3]
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_all_same_words(self):
        s = "aaaaaaaaaaaa"
        words = ["aa", "aa"]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_single_word(self):
        s = "word"
        words = ["word"]
        expected = [0]
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_word_len_1(self):
        s = "abcabcabc"
        words = ["a", "b", "c"]
        expected = [0, 1, 2, 3, 4, 5, 6]  # "abc", "bca", "cab", etc.
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for s='{s}', words={words}")

    def test_stress_long_s_short_words(self):
        s = "a" * 1000 + "b" * 1000
        words = ["a", "b"]
        expected = [999]  # The only "ab" is at index 999
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for long s, short words")

    def test_stress_many_words(self):
        # Check constraints: s_len <= 10000, words_len <= 5000, word_len <= 30
        # Create a case that might be slow but valid
        word_len = 2
        num_words = 4000
        s = ("ab" * num_words) + ("cd" * num_words)
        words = ["ab"] * num_words
        expected = [0]  # Only the first block matches
        # This test might take time, but should be correct
        self.assertCountEqual(self.solution.findSubstring(
            s, words), expected, f"Failed for many words stress test")


if __name__ == '__main__':
    unittest.main()
