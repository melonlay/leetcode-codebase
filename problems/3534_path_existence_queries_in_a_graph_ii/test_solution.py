import unittest
from .solution import Solution


class TestPathExistenceQueries(unittest.TestCase):

    def test_example_1(self):
        n = 5
        nums = [1, 8, 3, 4, 2]
        maxDiff = 3
        queries = [[0, 3], [2, 4]]
        expected = [1, 1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_example_2(self):
        n = 5
        nums = [5, 3, 1, 9, 10]
        maxDiff = 2
        queries = [[0, 1], [0, 2], [2, 3], [4, 3]]
        expected = [1, 2, -1, 1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_example_3(self):
        n = 3
        nums = [3, 6, 1]
        maxDiff = 1
        queries = [[0, 0], [0, 1], [1, 2]]
        expected = [0, -1, -1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_no_edges(self):
        n = 4
        nums = [10, 20, 30, 40]
        maxDiff = 5
        queries = [[0, 1], [1, 2], [0, 3]]
        expected = [-1, -1, -1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_full_graph(self):
        n = 4
        nums = [1, 2, 3, 4]
        maxDiff = 10
        queries = [[0, 3], [1, 2]]
        expected = [1, 1]  # All nodes connected
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_multiple_components(self):
        n = 6
        nums = [1, 2, 10, 11, 20, 21]
        maxDiff = 1
        queries = [[0, 1], [2, 3], [4, 5], [0, 2], [1, 4]]
        expected = [1, 1, 1, -1, -1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_same_node_query(self):
        n = 2
        nums = [5, 10]
        maxDiff = 1
        queries = [[0, 0], [1, 1]]
        expected = [0, 0]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)

    def test_large_diff_path(self):
        n = 5
        nums = [0, 10, 20, 30, 40]
        maxDiff = 10
        queries = [[0, 4], [0, 1]]
        expected = [4, 1]
        sol = Solution()
        self.assertEqual(sol.pathExistenceQueries(
            n, nums, maxDiff, queries), expected)


if __name__ == '__main__':
    unittest.main()
