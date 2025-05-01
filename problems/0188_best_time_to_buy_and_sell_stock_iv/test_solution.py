import unittest
from typing import List
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test method."""
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Test the first example provided by LeetCode."""
        k = 2
        prices = [2, 4, 1]
        expected = 2
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_leetcode_example_2(self):
        """Test the second example provided by LeetCode."""
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        expected = 7
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_zero_transactions(self):
        """Test the case where k = 0."""
        k = 0
        prices = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_empty_prices(self):
        """Test the case with an empty prices list (should return 0)."""
        k = 3
        prices: List[int] = []
        expected = 0
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_single_price(self):
        """Test the case with only one price (should return 0)."""
        k = 1
        prices = [5]
        expected = 0
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_one_transaction(self):
        """Test the case where only one transaction is allowed."""
        k = 1
        prices = [3, 2, 6, 5, 0, 3]
        expected = 4  # Buy at 2, sell at 6
        self.assertEqual(self.solution.maxProfit(k, prices), expected)
        k = 1
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5  # Buy at 1, sell at 6
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_decreasing_prices(self):
        """Test the case where prices are strictly decreasing."""
        k = 3
        prices = [5, 4, 3, 2, 1]
        expected = 0
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_increasing_prices(self):
        """Test the case where prices are strictly increasing."""
        k = 2
        prices = [1, 2, 3, 4, 5]
        expected = 4  # Buy at 1, sell at 5 (only 1 transaction needed)
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_constant_prices(self):
        """Test the case where all prices are the same."""
        k = 5
        prices = [7, 7, 7, 7, 7]
        expected = 0
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_large_k_optimization(self):
        """Test the optimization where k >= n / 2."""
        k = 10  # k > len(prices) / 2 = 3
        prices = [3, 2, 6, 5, 0, 3]
        # Same as infinite transactions: (6-2) + (3-0) = 4 + 3 = 7
        expected = 7
        self.assertEqual(self.solution.maxProfit(k, prices), expected)
        k = 2  # k == len(prices) / 2 = 2
        prices = [1, 2, 3, 4]
        expected = 3  # (2-1) + (4-3) = 1 + 1 = 2, or (4-1) = 3. Max is 3.
        self.assertEqual(self.solution.maxProfit(k, prices), expected)
        k = 100  # Large k
        prices = [1, 3, 2, 8, 4, 9]
        # Infinite tx profit: (3-1) + (8-2) + (9-4) = 2 + 6 + 5 = 13
        expected = 13
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_fewer_transactions_optimal(self):
        """Test cases where the optimal profit uses fewer than k transactions."""
        k = 3
        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        # Profits: (4-1)=3, (7-2)=5, (9-2)=7. Total = 15
        # With k=3, can do all: (4-1) + (7-2) + (9-2) = 3+5+7=15
        expected = 15
        self.assertEqual(self.solution.maxProfit(k, prices), expected)
        k = 1  # Only one transaction allowed
        expected = 8  # Buy at 1, sell at 9
        self.assertEqual(self.solution.maxProfit(k, prices), expected)

    def test_complex_case(self):
        """A more complex test case requiring careful transaction management."""
        k = 3
        prices = [2, 6, 8, 7, 8, 9, 4, 5]
        # Possible tx: (6-2)=4, (8-6)=2 -> combined (8-2)=6
        # Possible tx: (8-7)=1, (9-8)=1 -> combined (9-7)=2
        # Possible tx: (5-4)=1
        # With k=3: Buy 2 Sell 8 (Profit 6), Buy 7 Sell 9 (Profit 2), Buy 4 Sell 5 (Profit 1) -> Total = 9
        # Or: Buy 2 Sell 9 (Profit 7), Buy 4 Sell 5 (Profit 1) -> Total = 8 (Incorrect, must sell before buy)
        # Correct with k=3: Buy 2 Sell 8 (6), Buy 7 Sell 9 (2), Buy 4 Sell 5 (1). Total 9.
        expected = 9
        self.assertEqual(self.solution.maxProfit(k, prices), expected)


if __name__ == '__main__':
    unittest.main()
