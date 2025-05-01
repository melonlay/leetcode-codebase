import unittest
from .solution import Solution


class TestMaxSumSubmatrix(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[1, 0, 1], [0, -2, 3]]
        k = 2
        self.assertEqual(self.solution.maxSumSubmatrix(
            matrix, k), 2, "Example 1 Failed")

    def test_example2(self):
        matrix = [[2, 2, -1]]
        k = 3
        self.assertEqual(self.solution.maxSumSubmatrix(
            matrix, k), 3, "Example 2 Failed")

    def test_single_element_le_k(self):
        matrix = [[5]]
        k = 10
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), 5)

    def test_single_element_gt_k(self):
        # Problem guarantees a solution exists <= k, but let's test edge cases
        # If the single element is > k, and it's the only element,
        # the guarantee implies k >= element? Let's assume guarantee holds.
        # If matrix was [[10]] and k=5, the guarantee is violated.
        # Test case based on guarantee: result must be <= k
        matrix = [[-1]]
        k = 0
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), -1)
        matrix = [[-5]]
        k = -2
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), -5)
        matrix = [[5]]
        k = 5
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), 5)

    def test_all_negative(self):
        matrix = [[-1, -2], [-3, -4]]
        k = -1
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), -1)
        k = -5
        # Subarray [-3,-4] sum = -7, [-1,-2] = -3, [-1,-3]=-4, [-2,-4]=-6. Max <= -5 is -6
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), -6)

    def test_k_zero(self):
        matrix = [[2, 2, -1]]
        k = 0
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), -1)
        matrix = [[1, -1], [-1, 1]]
        k = 0
        # Sums: 1,-1,-1,1. Rects: [1]=1, [-1]=-1, [-1]=-1, [1]=1, [1,-1]=0, [-1,1]=0, [1,-1,-1,1]=0. Max <=0 is 0
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), 0)

    def test_large_k(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        k = 100
        self.assertEqual(self.solution.maxSumSubmatrix(
            matrix, k), 21)  # Sum of all elements

    def test_complex_case1(self):
        matrix = [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]]
        k = 8
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), 8)  # Example: [[4,5],[5,-4]] sum = 10. [[-3,4],[4,5]] sum = 10. [[4],[5],[-4]] sum=5. [[4,5],[1,5]] sum=15. [[5,1,5]] sum=11. [[-4,4,5],[1,5,-4]] sum=7. [[-3,4],[4,5],[5,-4]] sum=11. [[4,5]] sum=9. [[5,-4]] sum=1. [[-4,-3,4],[-4,4,5],[1,5,-4]] sum=4. [[-3,4],[4,5]] sum=10. [[4],[5]] sum=9. [[5],[5]] sum=10. [[4,5],[5,-4]] sum=10. [[-4,-3],[-3,-4],[5,1]] sum=-3. [[-3,4],[4,5]] sum=10. [[4,5],[5,-4]] sum=10. [[4],[5]] sum=9. [[5]] sum=5. [[5,1,5]] sum=11. Need rectangle sum <=8. Single 5 works. [[-4,4], [1,5]] sum=6. [[-3,4],[4,5]] sum=10. [[4],[5],[-4]] sum=5. [[-4,4],[1,5]] sum=6. [[5,1],[5,-4]] sum = 7. [[4,4,5]] sum=13. [[5,-4,-3,4],[-3,-4,4,5]] sum=4. [[-3,-4,4,5],[5,1,5,-4]] sum=9. The rectangle [[-3,4],[4,5],[5,-4]] has cols 1,2 and rows 1,2,3 -> sum=11. Rectangle cols 2,3 rows 1,2: [[-3,4],[4,5]] sum=10. Rectangle cols 3 rows 1,2: [[4],[5]] sum=9. Rectangle cols 0,1 rows 0,1,2: [[5,-4],[-3,-4],[5,1]] sum=-1. Rectangle cols 2,3 rows 1,2: [[4,4],[5,-4]] sum = 9 ? no. cols 2,3 rows 1,2 is [[4, 5], [5, -4]]. Sum 10. Rectangle cols 2 row 1,2 [[4],[4],[5]] sum = 13. Rectangle cols 0, 1, 2 rows 1, 2 [[-3,-4,4], [5,1,5]] sum = 8.

    def test_transpose_needed(self):
        # Test case where rows > cols
        matrix = [[1, 0], [0, -2], [1, 3]]  # 3 rows, 2 cols
        k = 2
        # Expected is 2 (rectangle [[0], [-2]] sum -2; [[1],[3]] sum 4; [[0,-2],[1,3]] sum 2)
        self.assertEqual(self.solution.maxSumSubmatrix(matrix, k), 2)


if __name__ == '__main__':
    unittest.main()
