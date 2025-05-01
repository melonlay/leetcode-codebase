import unittest
# Assuming solution.py is in the same directory or accessible
from .solution import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 2.00000)

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 2.50000)

    def test_empty_first(self):
        nums1 = []
        nums2 = [1]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 1.00000)

    def test_empty_second(self):
        nums1 = [1]
        nums2 = []
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 1.00000)

    def test_empty_both_raises_error(self):
        # The problem constraints state 1 <= m + n <= 2000, so both can't be empty.
        # The current implementation would raise ValueError due to accessing indices
        # or potentially ZeroDivisionError if total_length was 0 (which it isn't here).
        # We expect ValueError based on the implementation's check.
        nums1 = []
        nums2 = []
        # Depending on exact implementation, the error might differ slightly, but it should fail.
        # Let's test for ValueError as raised in the current code's logic path.
        # Note: The constraints 1 <= m+n should prevent this call in LeetCode.
        # If the code didn't have the swap logic, it might hit `high = -1` and exit loop.
        # With the swap, if m=0, n=0, it proceeds. half_len = 1. low=0, high=0.
        # partition1=0, partition2=1. max_left1=-inf, min_right1=inf.
        # max_left2=-inf, min_right2=nums2[1] -> IndexError
        # Let's refine to expect IndexError based on detailed trace with m=0, n=0
        # Or potentially ValueError depending on internal logic path reached first
        # Update: Now expecting ValueError due to explicit check added in solution
        with self.assertRaises(ValueError):
            self.solver.findMedianSortedArrays(nums1, nums2)
        # However, since the function guarantees to find a median for valid inputs,
        # testing this case might be less relevant than testing boundary conditions within constraints.

    def test_even_length_separated(self):
        nums1 = [1, 2]
        nums2 = [3, 4, 5, 6]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 3.50000)

    def test_odd_length_separated(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 3.00000)

    def test_interleaved_odd(self):
        nums1 = [1, 4, 5]
        nums2 = [2, 3]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 3.00000)

    def test_interleaved_even(self):
        nums1 = [1, 5, 6]
        nums2 = [2, 3, 4]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 3.50000)

    def test_duplicates(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 1.00000)

    def test_longer_first_array_swap(self):
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = [0, 7]
        # Combined: [0, 1, 2, 3, 4, 5, 6, 7]. Median (3+4)/2 = 3.5
        self.assertAlmostEqual(
            self.solver.findMedianSortedArrays(nums1, nums2), 3.50000)


if __name__ == '__main__':
    unittest.main()
