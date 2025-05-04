import unittest
from .solution import Solution


class TestUnitConversion(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        conversions = [[0, 1, 2], [1, 2, 3]]
        expected = [1, 2, 6]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_example_2(self):
        conversions = [[0, 1, 2], [0, 2, 3], [1, 3, 4],
                       [1, 4, 5], [2, 5, 2], [4, 6, 3], [5, 7, 4]]
        expected = [1, 2, 3, 8, 10, 6, 30, 24]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_minimum_n(self):
        conversions = [[0, 1, 100]]
        expected = [1, 100]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_large_factors_modulo(self):
        factor1 = 10**9
        factor2 = 10**9
        conversions = [[0, 1, factor1], [1, 2, factor2]]
        expected = [1, factor1 % (10**9 + 7), 49]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_linear_graph(self):
        conversions = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
        expected = [1, 2, 6, 24, 120]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_star_graph(self):
        conversions = [[0, 1, 10], [0, 2, 20], [0, 3, 30]]
        expected = [1, 10, 20, 30]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)

    def test_shuffled_conversions(self):
        conversions = [[1, 3, 5], [0, 1, 2], [0, 2, 3]]  # Shuffled order
        expected = [1, 2, 3, 10]
        self.assertEqual(
            self.solver.baseUnitConversions(conversions), expected)


if __name__ == '__main__':
    unittest.main()
