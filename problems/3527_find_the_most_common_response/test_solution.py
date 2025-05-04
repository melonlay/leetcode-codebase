import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        responses = [["good", "ok", "good"], ["ok", "ok",
                                              "bad", "good", "ok", "ok"], ["good"], ["bad"]]
        self.assertEqual(self.solution.findCommonResponse(responses), "good")

    def test_example_2(self):
        responses = [["good", "ok", "good"], ["ok", "bad"],
                     ["bad", "notsure"], ["great", "good"]]
        self.assertEqual(self.solution.findCommonResponse(responses), "bad")

    def test_single_day(self):
        responses = [["apple", "banana", "apple", "orange"]]
        self.assertEqual(self.solution.findCommonResponse(responses), "apple")

    def test_tie_lexicographical(self):
        responses = [["a", "b"], ["b", "c"], ["c", "a"]]
        # Frequencies: a: 2, b: 2, c: 2. Smallest is 'a'
        self.assertEqual(self.solution.findCommonResponse(responses), "a")

    def test_all_duplicates_within_day(self):
        responses = [["x", "x", "x"], ["y", "y"]]
        # Frequencies: x: 1, y: 1. Smallest is 'x'
        self.assertEqual(self.solution.findCommonResponse(responses), "x")

    def test_all_unique_overall(self):
        responses = [["one"], ["two"], ["three"]]
        # Frequencies: one: 1, two: 1, three: 1. Smallest is 'one'
        self.assertEqual(self.solution.findCommonResponse(responses), "one")

    def test_empty_inner_list_not_possible_by_constraints(self):
        # Constraint: 1 <= responses[i].length <= 1000
        pass

    def test_single_response(self):
        responses = [["hello"]]
        self.assertEqual(self.solution.findCommonResponse(responses), "hello")

    def test_mixed_case_not_possible_by_constraints(self):
        # Constraint: responses[i][j] consists of only lowercase English letters
        pass


if __name__ == '__main__':
    unittest.main()
