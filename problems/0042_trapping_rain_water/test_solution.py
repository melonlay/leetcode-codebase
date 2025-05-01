import unittest
from .solution import Solution


class TestTrapRainWater(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.solution.trap(height), 6, "Failed Example 1")

    def test_example2(self):
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(self.solution.trap(height), 9, "Failed Example 2")

    def test_empty_list(self):
        height = []
        self.assertEqual(self.solution.trap(height),
                         0, "Failed empty list case")

    def test_single_element(self):
        height = [5]
        self.assertEqual(self.solution.trap(height), 0,
                         "Failed single element case")

    def test_two_elements(self):
        height = [5, 2]
        self.assertEqual(self.solution.trap(height),
                         0, "Failed two elements case")

    def test_flat_surface(self):
        height = [3, 3, 3, 3]
        self.assertEqual(self.solution.trap(height),
                         0, "Failed flat surface case")

    def test_monotonic_increasing(self):
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.trap(height), 0,
                         "Failed monotonic increasing case")

    def test_monotonic_decreasing(self):
        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.trap(height), 0,
                         "Failed monotonic decreasing case")

    def test_valley(self):
        height = [5, 1, 5]
        self.assertEqual(self.solution.trap(height), 4, "Failed valley case")

    def test_multiple_peaks_valleys(self):
        height = [2, 1, 0, 1, 2, 1, 0, 3, 1, 0, 2]
        self.assertEqual(self.solution.trap(height), 10,
                         "Failed multiple peaks/valleys case - rechecked")

    def test_tall_edges_short_middle(self):
        height = [6, 0, 0, 0, 0, 6]
        self.assertEqual(self.solution.trap(height),
                         24, "Failed tall edges case")

    def test_tall_middle_short_edges(self):
        height = [1, 0, 5, 0, 1]
        self.assertEqual(self.solution.trap(height),
                         2, "Failed tall middle case")

    def test_complex_case(self):
        height = [5, 4, 1, 2, 0, 3, 1, 2, 5, 6, 1, 4, 0, 2]
        self.assertEqual(self.solution.trap(height), 27, "Failed complex case")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
