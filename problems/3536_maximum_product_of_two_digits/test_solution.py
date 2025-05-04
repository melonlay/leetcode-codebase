import unittest
from .solution import Solution


class TestMaximumProduct(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumProduct(31),
                         3, "Example 1 Failed")

    def test_example_2(self):
        self.assertEqual(self.solution.maximumProduct(22),
                         4, "Example 2 Failed")

    def test_example_3(self):
        self.assertEqual(self.solution.maximumProduct(124),
                         8, "Example 3 Failed")

    def test_two_digits_descending(self):
        self.assertEqual(self.solution.maximumProduct(54), 20, "Test Case: 54")

    def test_multiple_digits(self):
        self.assertEqual(self.solution.maximumProduct(
            54321), 20, "Test Case: 54321")

    def test_duplicate_largest(self):
        self.assertEqual(self.solution.maximumProduct(989),
                         81, "Test Case: 989")

    def test_all_same_digits(self):
        self.assertEqual(self.solution.maximumProduct(777),
                         49, "Test Case: 777")

    def test_minimum_constraint(self):
        self.assertEqual(self.solution.maximumProduct(10), 0, "Test Case: 10")

    def test_maximum_constraint_example(self):
        # n = 10^9 is 1000000000, digits [1, 0, 0, ...], product 0
        self.assertEqual(self.solution.maximumProduct(
            1000000000), 0, "Test Case: 10^9")
        # n close to 10^9, e.g., 999,999,999
        self.assertEqual(self.solution.maximumProduct(
            999999999), 81, "Test Case: 999999999")

    def test_contains_zero(self):
        self.assertEqual(self.solution.maximumProduct(504),
                         20, "Test Case: 504")


if __name__ == '__main__':
    unittest.main()
