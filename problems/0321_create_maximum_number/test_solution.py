import unittest
from typing import List

# Use relative import as test and solution are in the same directory
from .solution import Solution


class TestCreateMaximumNumber(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        expected = [9, 8, 6, 5, 3]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_example_2(self):
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 5
        expected = [6, 7, 6, 0, 4]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_example_3(self):
        nums1 = [3, 9]
        nums2 = [8, 9]
        k = 3
        expected = [9, 8, 9]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_edge_k_equals_m_plus_n(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        k = 4
        expected = [3, 4, 1, 2]  # Merge [1,2] and [3,4]
        # i=0: sub1=[], sub2=[3,4]. Merge=[3,4] (incorrect length)
        # i=1: sub1=[2], sub2=[3,4]. Merge=[3,4,2]
        # i=2: sub1=[1,2], sub2=[3,4]. Merge=[3,4,1,2]
        # Check merge logic: [1,2] vs [3,4] -> 3 > 1, take 3. [1,2] vs [4] -> 4 > 1, take 4. [1,2] vs [] -> take 1, take 2. -> [3,4,1,2]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_edge_k_equals_1(self):
        nums1 = [2, 5, 1]
        nums2 = [8, 3]
        k = 1
        expected = [8]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_edge_k_equals_0(self):
        # Although constraints say k >= 1, good to test boundary
        nums1 = [1]
        nums2 = [2]
        k = 0
        expected = []
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_one_array_empty(self):
        nums1 = [2, 5, 6, 4, 4, 0]
        nums2 = []
        k = 3
        # Corrected: Max subsequence of nums1 is [6, 4, 4], not [5, 6, 4]
        expected = [6, 4, 4]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_other_array_empty(self):
        nums1 = []
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 4
        expected = [9, 5, 8, 3]  # Max subsequence of nums2
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_identical_digits_merge_lookahead(self):
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 3  # Requires picking between [6,7] and [6,0] or [6,4]
        # i=0: sub1=[], sub2=[6,0,4] -> Merge=[6,0,4]
        # i=1: sub1=[7], sub2=[6,4] -> Merge=[7,6,4]
        # i=2: sub1=[6,7], sub2=[4] -> Merge=[6,7,4]
        expected = [7, 6, 4]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_identical_digits_merge_lookahead_2(self):
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        # i=0: sub1=[], sub2=[9,5,8,3] -> [9,5,8,3]
        # i=1: sub1=[6], sub2=[9,5,8,3] -> [9,6,5,8,3]? No, merge [6] and [9,5,8,3] -> [9,6,5,8,3]
        # i=2: sub1=[6,5], sub2=[9,8,3] -> merge([6,5], [9,8,3]) -> [9,8,6,5,3]
        # i=3: sub1=[4,6,5], sub2=[9,8] -> merge([4,6,5],[9,8]) -> [9,8,4,6,5]
        # i=4: sub1=[3,4,6,5], sub2=[9] -> merge([3,4,6,5],[9]) -> [9,3,4,6,5]
        expected = [9, 8, 6, 5, 3]  # From i=2
        self.assertEqual(self.solver.maxNumber(
            nums1, nums2, k), expected)  # Same as example 1

    def test_zeros(self):
        nums1 = [0, 0, 1]
        nums2 = [0, 0, 2]
        k = 3
        # i=0: sub1=[], sub2=[0,0,2] -> [0,0,2]
        # i=1: sub1=[1], sub2=[0,2] -> merge([1], [0,2]) -> [1,0,2]
        # i=2: sub1=[0,1], sub2=[2] -> merge([0,1], [2]) -> [2,0,1]
        # i=3: sub1=[0,0,1], sub2=[] -> [0,0,1]
        expected = [2, 0, 1]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_large_case(self):
        nums1 = [8, 6, 9]
        nums2 = [1, 7, 5]
        k = 3
        # i=0: sub1=[], sub2=[7,5] -> no, sub2=[1,7,5] -> [1,7,5]
        # i=1: sub1=[9], sub2=[7,5] -> merge [9], [7,5] -> [9,7,5]
        # i=2: sub1=[8,9], sub2=[7] -> merge [8,9], [7] -> [8,9,7]
        # i=3: sub1=[8,6,9], sub2=[] -> [8,6,9]
        expected = [9, 7, 5]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)

    def test_failing_case_1(self):
        nums1 = [3, 4, 8, 9, 3, 0]
        nums2 = [6, 1, 9, 1, 1, 2]
        k = 6
        expected = [9, 9, 3, 1, 2, 0]
        self.assertEqual(self.solver.maxNumber(nums1, nums2, k), expected)


if __name__ == '__main__':
    unittest.main()
