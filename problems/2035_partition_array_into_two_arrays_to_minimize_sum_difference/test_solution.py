import unittest
from .solution import Solution


class TestMinimumDifference(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums = [3, 9, 7, 3]
        expected = 2
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_example_2(self):
        nums = [-36, 36]
        expected = 72
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_example_3(self):
        nums = [2, -1, 0, 4, -2, -9]
        expected = 0
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_all_identical(self):
        nums = [5, 5, 5, 5, 5, 5]
        expected = 0
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_simple_positive(self):
        # n=3, total=21, target=10.5 -> closest sums 10, 11
        nums = [1, 2, 3, 4, 5, 6]
        expected = 1
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_mixed_signs(self):
        # n=3, total=15, target=7.5 -> closest sums 5, 10
        nums = [10, -5, 20, -15, 0, 5]
        expected = 5
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_large_numbers_zero_diff(self):
        # n=2, total=0, target=0
        nums = [10000000, -10000000, 5000000, -5000000]
        expected = 0
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_large_numbers_non_zero_diff(self):
        # n=2, total=3M, target=1.5M
        nums = [10000000, -9000000, 8000000, -6000000]
        # Partitions:
        # [10M, -9M] = 1M, [-6M, 8M] = 2M -> diff=abs(1M-2M)=1M
        # [10M, 8M] = 18M, [-9M, -6M] = -15M -> diff=abs(18M-(-15M))=33M
        # [10M, -6M] = 4M, [-9M, 8M] = -1M -> diff=abs(4M-(-1M))=5M
        expected = 1000000
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_n_equals_1(self):
        nums = [10, -2]  # n=1
        expected = 12
        self.assertEqual(self.solver.minimumDifference(nums), expected)

    def test_another_case(self):
        nums = [76, 8, 45, 20, 74, 84, 28, 1]  # n=4, sum=336, target=168
        # Example partition: [76, 8, 28, 1] = 113; [45, 20, 74, 84] = 223 -> diff = 110
        # Another: [76, 45, 20, 1] = 142; [8, 74, 84, 28] = 194 -> diff = 52
        # Another: [76, 74, 8, 1] = 159; [45, 20, 84, 28] = 177 -> diff = 18
        # Another: [76, 84, 8, 1] = 169; [45, 20, 74, 28] = 167 -> diff = 2
        expected = 2
        self.assertEqual(self.solver.minimumDifference(nums), expected)


if __name__ == '__main__':
    unittest.main()
