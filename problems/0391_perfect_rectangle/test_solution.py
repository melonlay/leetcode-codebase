import unittest
from .solution import Solution  # Use relative import


class TestPerfectRectangle(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from LeetCode."""
        rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [
            1, 3, 2, 4], [3, 2, 4, 4], [2, 3, 4, 4]]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_example_2_gap(self):
        """Test the second example from LeetCode (gap)."""
        rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_example_3_overlap(self):
        """Test the third example from LeetCode (overlap)."""
        rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_single_rectangle(self):
        """Test with a single rectangle."""
        rectangles = [[0, 0, 1, 1]]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_two_rectangles_perfect(self):
        """Test with two rectangles forming a perfect cover."""
        rectangles = [[0, 0, 1, 1], [1, 0, 2, 1]]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_two_rectangles_overlap(self):
        """Test with two overlapping rectangles."""
        rectangles = [[0, 0, 2, 2], [1, 1, 3, 3]]
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_complex_perfect_cover(self):
        """Test a more complex perfect cover scenario."""
        rectangles = [
            [0, 0, 1, 1], [1, 0, 2, 1],
            [0, 1, 1, 2], [1, 1, 2, 2]
        ]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_internal_hole(self):
        """Test a scenario where rectangles surround an empty space."""
        rectangles = [
            [0, 0, 3, 1], [0, 1, 1, 2], [2, 1, 3, 2], [0, 2, 3, 3]
        ]
        # Bounding box is (0,0) to (3,3). Area sum matches.
        # Corners: (0,0)x1, (3,0)x1, (0,3)x1, (3,3)x1 -> these are ok
        # (0,1)x1, (3,1)x1 -> should be even
        # (1,1)x0 -> missing corners
        # (1,2)x1, (2,2)x1 -> should be even
        # (0,2)x1, (3,2)x1 -> should be even
        # The corner check should fail.
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_complex_overlap(self):
        """Test a complex scenario with overlap."""
        rectangles = [
            [0, 0, 2, 2], [1, 1, 3, 3], [0, 2, 2, 4], [2, 0, 4, 2]
        ]
        # Overlap around (1,1) to (2,2)
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_large_coordinates(self):
        """Test with large coordinate values."""
        offset = 10**5 - 5
        rectangles = [
            [offset+0, offset+0, offset+1, offset+1],
            [offset+1, offset+0, offset+2, offset+1]
        ]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_negative_coordinates(self):
        """Test with negative coordinate values."""
        rectangles = [
            [-2, -1, -1, 0], [-1, -1, 0, 0],
            [-2, 0, -1, 1], [-1, 0, 0, 1]
        ]
        self.assertTrue(self.solution.isRectangleCover(rectangles))


if __name__ == '__main__':
    unittest.main()
