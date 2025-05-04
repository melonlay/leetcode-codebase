import unittest
from collections import defaultdict, deque
from typing import List
from .solution import Solution

# Helper function for brute-force calculation


def _calculate_profit(order: List[int], score: List[int]) -> int:
    profit = 0
    for i, node in enumerate(order):
        profit += score[node] * (i + 1)  # 1-based position
    return profit


def _brute_force_max_profit(n: int, edges: List[List[int]], score: List[int]) -> int:
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    max_profit = 0

    # Backtracking function to find all topological sorts
    def backtrack(current_order: List[int], current_in_degree: List[int]):
        nonlocal max_profit

        if len(current_order) == n:
            profit = _calculate_profit(current_order, score)
            max_profit = max(max_profit, profit)
            return

        possible_next_nodes = []
        for i in range(n):
            # Check if node i is not already in the order and has in-degree 0
            if current_in_degree[i] == 0 and i not in current_order:
                possible_next_nodes.append(i)

        # Crucial for correctness: Sort possible nodes by score descending
        # This doesn't guarantee optimality overall but is needed if we want
        # to prune based on greedy choices within the brute force (which we won't do here).
        # For pure brute force, order doesn't strictly matter, but let's process them.
        # Sorting isn't actually needed for pure brute-force, but doesn't hurt.

        for node in possible_next_nodes:
            # Choose
            current_order.append(node)
            # Temporarily decrement in-degrees of neighbors
            new_in_degree = list(current_in_degree)  # Make a copy
            new_in_degree[node] = -1  # Mark as visited/processed
            for neighbor in adj[node]:
                new_in_degree[neighbor] -= 1

            # Explore
            backtrack(current_order, new_in_degree)

            # Unchoose (Backtrack)
            current_order.pop()  # Remove last node
            # No need to restore in_degree explicitly as we passed a copy

    # Initial call with empty order and original in-degrees
    # Find initial nodes with in-degree 0
    initial_nodes = [i for i, degree in enumerate(in_degree) if degree == 0]

    # Need to start the backtrack from an empty state correctly
    # The backtrack function assumes nodes with 0 in_degree can be added.
    backtrack([], list(in_degree))  # Pass a copy of initial in_degree

    return max_profit


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 2
        edges = [[0, 1]]
        score = [2, 3]
        expected = 8
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)
        # Verify brute force matches example
        self.assertEqual(_brute_force_max_profit(n, edges, score), expected)

    def test_example_2(self):
        n = 3
        edges = [[0, 1], [0, 2]]
        score = [1, 6, 3]
        expected = 25
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)
        # Verify brute force matches example
        self.assertEqual(_brute_force_max_profit(n, edges, score), expected)

    def test_no_edges(self):
        n = 3
        edges = []
        score = [10, 1, 100]
        # Optimal order: [1, 0, 2] -> 1*1 + 10*2 + 100*3 = 1 + 20 + 300 = 321
        expected = _brute_force_max_profit(n, edges, score)  # Use brute force
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)

    def test_single_node(self):
        n = 1
        edges = []
        score = [5]
        expected = 5  # 5 * 1
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)
        self.assertEqual(_brute_force_max_profit(n, edges, score), expected)

    def test_chain(self):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3]]
        score = [1, 1, 10, 100]
        # Only order [0, 1, 2, 3] -> 1*1 + 1*2 + 10*3 + 100*4 = 1 + 2 + 30 + 400 = 433
        expected = 433
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)
        self.assertEqual(_brute_force_max_profit(n, edges, score), expected)

    def test_multiple_components(self):
        n = 4
        edges = [[0, 1]]
        score = [10, 1, 100, 5]
        # Let brute force calculate
        expected = _brute_force_max_profit(n, edges, score)  # Use brute force
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)

    def test_complex_dependencies(self):
        n = 5
        edges = [[0, 2], [1, 2], [2, 3], [2, 4]]
        score = [10, 20, 5, 50, 60]  # Nodes 0, 1 before 2. Nodes 3, 4 after 2.
        # Let brute force calculate
        expected = _brute_force_max_profit(n, edges, score)  # Use brute force
        self.assertEqual(self.solution.maxProfit(n, edges, score), expected)


if __name__ == '__main__':
    unittest.main()
