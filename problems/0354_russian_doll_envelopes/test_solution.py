import unittest
from .solution import Solution  # Relative import


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 3, "Example 1 Failed")

    def test_example_2(self):
        envelopes = [[1, 1], [1, 1], [1, 1], [1, 1]]
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 1, "Example 2 Failed")

    def test_empty_input(self):
        envelopes = []
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 0, "Empty Input Failed")

    def test_single_envelope(self):
        envelopes = [[1, 1]]
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 1, "Single Envelope Failed")

    def test_no_nesting_possible(self):
        envelopes = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]
        self.assertEqual(self.solver.maxEnvelopes(envelopes),
                         1, "No Nesting Possible Failed")

    def test_all_can_nest(self):
        envelopes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 5, "All Can Nest Failed")

    def test_complex_case_with_ties(self):
        envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
        # Sorted: [[1,1], [2,3], [4,6], [4,5], [6,7]]
        # Heights: [1, 3, 6, 5, 7]
        # LIS: [1, 3, 5, 7] -> length 4
        self.assertEqual(self.solver.maxEnvelopes(envelopes),
                         4, "Complex Case with Ties Failed")

    def test_decreasing_heights(self):
        envelopes = [[1, 5], [2, 4], [3, 3]]
        # Sorted: [[1,5], [2,4], [3,3]]
        # Heights: [5, 4, 3]
        # LIS: [5] or [4] or [3] -> length 1
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 1, "Decreasing Heights Failed")

    def test_large_input_perf_hint(self):
        # Not a real perf test, but checks a larger sequence structure
        envelopes = [[i, 100000 - i] for i in range(1, 100)] + [[100, 1]]
        # Mostly increasing widths, decreasing heights, then one small height
        # Sorted: [[1, 99999], [2, 99998], ..., [99, 99901], [100, 1]]
        # Heights: [99999, 99998, ..., 99901, 1]
        # LIS: [99999] or [99998] ... or [99901] or [1] -> length 1
        self.assertEqual(self.solver.maxEnvelopes(
            envelopes), 1, "Large Input Hint 1 Failed")

        envelopes = [[i, i] for i in range(1, 100)]
        self.assertEqual(self.solver.maxEnvelopes(envelopes),
                         99, "Large Input Hint 2 Failed")


if __name__ == '__main__':
    unittest.main()
