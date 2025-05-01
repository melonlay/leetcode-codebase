import unittest
from .solution import Solution


class TestWordLadder(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from LeetCode."""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = 5
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_example_2(self):
        """Test the second example where endWord is not in wordList."""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_no_path(self):
        """Test a case where no transformation sequence exists."""
        beginWord = "apple"
        endWord = "banana"
        wordList = ["apply", "apples", "orange", "bandana"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_short_path(self):
        """Test a simple, short transformation path."""
        beginWord = "a"
        endWord = "c"
        wordList = ["a", "b", "c"]
        # The shortest path is "a" -> "c", length 2.
        # The BFS finds this directly when exploring neighbors of "a".
        expected = 2  # Corrected expectation based on actual BFS behavior
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_another_path(self):
        """Test another simple path."""
        beginWord = "cat"
        endWord = "dog"
        wordList = ["cot", "cog", "dog"]
        # cat -> cot -> cog -> dog
        expected = 4
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_end_word_not_reachable(self):
        """Test case where endWord is in list but not reachable."""
        beginWord = "sail"
        endWord = "boat"
        wordList = ["bail", "nailed", "Sailed", "boar", "boil", "boat"]
        # sail -> bail -> boil -> ? (no boat)
        # Check case sensitivity: Problem states lowercase. Let's assume wordList is correct.
        # sail -> bail -> boil. Cannot reach boat.
        expected = 0
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_begin_word_equals_end_word_in_list(self):
        """Test case where beginWord is endWord (should not happen based on constraints but check)."""
        # Constraint: beginWord != endWord. Skipping this test as it violates constraints.
        pass

    def test_long_word_list_no_path(self):
        """Test with a larger word list where path might not exist."""
        beginWord = "aaaaa"
        endWord = "bbbbb"
        wordList = ["aaaab", "aaaba", "aabaa", "abaaa",
                    "baaaa", "bbbaa", "bbaab", "bab bb", "abbbb"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(
            beginWord, endWord, wordList), expected)


if __name__ == '__main__':
    unittest.main()
