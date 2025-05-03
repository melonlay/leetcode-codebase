import unittest
from .solution import Solution


class TestSkyline(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        buildings = [[2, 9, 10], [3, 7, 15], [
            5, 12, 12], [15, 20, 10], [19, 24, 8]]
        expected = [[2, 10], [3, 15], [7, 12], [
            12, 0], [15, 10], [20, 8], [24, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_example2(self):
        buildings = [[0, 2, 3], [2, 5, 3]]
        expected = [[0, 3], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_single_building(self):
        buildings = [[1, 5, 10]]
        expected = [[1, 10], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_no_buildings(self):
        buildings = []
        expected = []
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_adjacent_different_heights(self):
        buildings = [[1, 3, 5], [3, 5, 10]]
        expected = [[1, 5], [3, 10], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_overlapping_buildings(self):
        buildings = [[1, 5, 5], [2, 4, 10]]
        expected = [[1, 5], [2, 10], [4, 5], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_contained_building(self):
        buildings = [[1, 10, 5], [3, 7, 10]]
        expected = [[1, 5], [3, 10], [7, 5], [10, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_identical_buildings(self):
        buildings = [[1, 5, 10], [1, 5, 10]]
        expected = [[1, 10], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_touching_buildings_complex(self):
        buildings = [[1, 2, 1], [2, 3, 2], [3, 4, 3]]
        expected = [[1, 1], [2, 2], [3, 3], [4, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_complex_overlap_and_adjacent(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],
                     [12, 15, 10], [15, 20, 10], [19, 24, 8]]
        expected = [[2, 10], [3, 15], [7, 12], [12, 10], [20, 8], [24, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_multiple_buildings_ending_at_same_x(self):
        buildings = [[1, 5, 10], [2, 5, 12]]
        expected = [[1, 10], [2, 12], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_multiple_buildings_starting_at_same_x(self):
        buildings = [[1, 5, 10], [1, 4, 12]]
        expected = [[1, 12], [4, 10], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_zero_height_implicit(self):
        # Although constraints say height >= 1, testing the drop to zero
        buildings = [[1, 2, 1], [3, 4, 1]]
        expected = [[1, 1], [2, 0], [3, 1], [4, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)


if __name__ == '__main__':
    unittest.main()
