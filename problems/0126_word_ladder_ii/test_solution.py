import unittest
from typing import List, Set

# Assuming solution.py is in the same directory or accessible via PYTHONPATH
from .solution import Solution

# Helper function to sort lists of lists for comparison


def sort_lists(list_of_lists: List[List[str]]) -> List[List[str]]:
    return sorted([sorted(inner_list) for inner_list in list_of_lists])

# Helper function to sort lists of lists based on the full list content


def sort_paths(list_of_lists: List[List[str]]) -> List[List[str]]:
    # Sort each inner list first to handle cases where order within path matters for uniqueness
    # Then sort the outer list based on the tuple representation of inner lists
    # Example: ["a", "b"] comes before ["a", "c"]
    return sorted(list_of_lists)


class TestWordLadderII(unittest.TestCase):

    def setUp(self):
        """Set up the test case.
        Instantiates the Solution class before each test method.
        """
        self.solution = Solution()

    def assertListOfListsEqual(self, list1: List[List[str]], list2: List[List[str]], msg: str = None):
        """Asserts that two lists of lists contain the same paths, ignoring order.

        Sorts both lists of lists before comparison to ensure order doesn't matter.
        Each inner list represents a path.
        """
        self.assertCountEqual(list1, list2, msg)
        # Additionally check if the sorted versions are equal to be more robust
        self.assertEqual(sort_paths(list1), sort_paths(list2), msg)

    def test_example_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = [["hit", "hot", "dot", "dog", "cog"],
                    ["hit", "hot", "lot", "log", "cog"]]
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_example_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = []
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_no_path(self):
        beginWord = "a"
        endWord = "c"
        # wordList = ["a", "b", "c"] # Original test line comment
        # This path is not valid as 'b' must be used if it exists. # Original comment
        # expected = [["a","c"]] # Original expected
        # Corrected expectation: BFS finds distance 1 (a->c) path is shortest.
        expected_correct = [["a", "c"]]
        wordList_correct = ["b", "c"]  # 'a' is beginWord
        result = self.solution.findLadders(
            beginWord, endWord, wordList_correct)
        self.assertListOfListsEqual(expected_correct, result)

    def test_endWord_not_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]  # cog is missing
        expected = []
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_beginWord_equals_endWord_constraint(self):
        # Constraint states beginWord != endWord, so this case shouldn't occur per problem def.
        # If it could, the result should likely be [[beginWord]].
        pass  # Skipping test based on constraint

    def test_empty_wordList(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = []
        expected = []
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_longer_path(self):
        beginWord = "cat"
        endWord = "dog"
        wordList = ["cot", "cog", "cag", "dag", "dog"]
        # cat -> cot -> cog -> dog (len 4)
        # cat -> cag -> dag -> dog (len 4)
        # cat -> cag -> cog -> dog (len 4) # Added path
        expected = [["cat", "cot", "cog", "dog"], [
            "cat", "cag", "dag", "dog"], ["cat", "cag", "cog", "dog"]]
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_multiple_paths_complex(self):
        beginWord = "red"
        endWord = "tax"
        wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
        # red -> ted -> tex -> tax (4)
        # red -> rex -> tex -> tax (4)
        # red -> ted -> tad -> tax (4) # Added path
        expected = [["red", "ted", "tex", "tax"], [
            "red", "rex", "tex", "tax"], ["red", "ted", "tad", "tax"]]
        result = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertListOfListsEqual(expected, result)

    def test_short_words(self):
        beginWord = "a"
        endWord = "c"
        # wordList = ["a", "b", "c"]  # Original comment
        # Corrected expectation: path a->c is shortest
        expected = [["a", "c"]]
        # Need to adjust wordList based on rules: intermediate words in list
        wordList_adjusted = ["b", "c"]
        result = self.solution.findLadders(
            beginWord, endWord, wordList_adjusted)
        self.assertListOfListsEqual(expected, result)

    def test_no_intermediate_word(self):
        beginWord = "hot"
        endWord = "dog"
        wordList = ["hot", "dog"]  # Only start/end present, cannot transform
        # Corrected wordList based on rules: intermediate words
        wordList_adjusted = ["dog"]  # endWord must be in list
        # BFS: q=[hot], dist={hot:0}
        # Neighbors of hot? None in wordSet={dog}.
        # Result should be []
        expected = []
        result = self.solution.findLadders(
            beginWord, endWord, wordList_adjusted)
        self.assertListOfListsEqual(expected, result)

        # Case: Direct transformation possible
        beginWord2 = "hot"
        endWord2 = "dot"
        wordList2 = ["dot"]  # endWord must be in list
        expected2 = [["hot", "dot"]]
        result2 = self.solution.findLadders(beginWord2, endWord2, wordList2)
        self.assertListOfListsEqual(expected2, result2)

    # Consider adding a stress test if performance is a concern
    # @unittest.skip("Stress test - potentially slow")
    # def test_stress_max_constraints(self):
    #     # Requires generating a large word list (500 words, length 5)
    #     # that potentially has many short paths. This is hard to craft.
    #     # Example: A -> B -> ... -> Z structure
    #     # For now, rely on LeetCode's test cases for large inputs.
    #     pass


if __name__ == '__main__':
    unittest.main()
