import unittest
import time
from .solution import Solution  # Using relative import
from typing import List


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def _brute_force_countCells(self, grid: List[List[str]], pattern: str) -> int:
        """Slow but simple implementation for verification."""
        m = len(grid)
        n = len(grid[0])
        L = len(pattern)

        if L == 0:
            return 0
        if m * n < L:
            return 0

        text_h = "".join("".join(row) for row in grid)
        text_v = "".join(grid[r][c] for c in range(n) for r in range(m))

        bf_is_horizontal = [[False] * n for _ in range(m)]
        bf_is_vertical = [[False] * n for _ in range(m)]

        # Horizontal brute-force search
        for k in range(len(text_h) - L + 1):
            if text_h[k:k+L] == pattern:
                for i in range(L):
                    idx = k + i
                    r, c = divmod(idx, n)
                    if 0 <= r < m and 0 <= c < n:
                        bf_is_horizontal[r][c] = True

        # Vertical brute-force search
        for k in range(len(text_v) - L + 1):
            if text_v[k:k+L] == pattern:
                for i in range(L):
                    idx = k + i
                    r, c = idx % m, idx // m
                    if 0 <= r < m and 0 <= c < n:
                        bf_is_vertical[r][c] = True

        # Count overlaps
        count = 0
        for r in range(m):
            for c in range(n):
                if bf_is_horizontal[r][c] and bf_is_vertical[r][c]:
                    count += 1
        return count

    def test_example_1(self):
        grid = [["a", "a", "c", "c"], ["b", "b", "b", "c"], [
            "a", "a", "b", "a"], ["c", "a", "a", "c"], ["a", "a", "b", "a"]]
        pattern = "abaca"
        self.assertEqual(self.solution.countCells(grid, pattern), 1)

    def test_example_2(self):
        grid = [["c", "a", "a", "a"], ["a", "a", "b", "a"],
                ["b", "b", "a", "a"], ["a", "a", "b", "a"]]
        pattern = "aba"
        self.assertEqual(self.solution.countCells(grid, pattern), 4)

    def test_example_3(self):
        grid = [["a"]]
        pattern = "a"
        self.assertEqual(self.solution.countCells(grid, pattern), 1)

    def test_no_matches(self):
        grid = [["a", "b"], ["c", "d"]]
        pattern = "xyz"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_horizontal_only(self):
        grid = [["a", "b", "a"], ["c", "d", "c"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_vertical_only(self):
        grid = [["a", "c"], ["b", "d"], ["a", "c"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_multiple_overlaps(self):
        grid = [["a", "b", "a"], ["b", "a", "b"], ["a", "b", "a"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_full_match_horizontal(self):
        grid = [["a", "b", "c"], ["d", "e", "f"]]
        pattern = "abcdef"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_full_match_vertical(self):
        grid = [["a", "d"], ["b", "e"], ["c", "f"]]
        pattern = "abcdef"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_full_grid_match(self):
        grid = [["a", "b"], ["c", "d"]]
        pattern = "abcd"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_empty_pattern(self):
        grid = [["a"]]
        pattern = ""
        self.assertEqual(self.solution.countCells(grid, pattern), 0)

    def test_pattern_longer_than_grid(self):
        grid = [["a", "b"], ["c", "d"]]
        pattern = "abcde"
        self.assertEqual(self.solution.countCells(grid, pattern), 0)

    def test_complex_pattern(self):
        grid = [["a", "a", "a", "a"], [
            "a", "a", "a", "a"], ["a", "a", "a", "a"]]
        pattern = "aaaa"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_overlapping_kmp(self):
        grid = [["a", "b", "a", "b", "a"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_single_column(self):
        grid = [["a"], ["b"], ["a"], ["c"], ["a"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_single_row(self):
        grid = [["a", "b", "a", "c", "a"]]
        pattern = "aba"
        expected = self._brute_force_countCells(grid, pattern)
        self.assertEqual(self.solution.countCells(grid, pattern), expected)

    def test_large_grid_performance(self):
        m, n = 500, 500  # m*n = 250,000
        # Simple grid, pattern unlikely to cause excessive matches
        grid = [['a'] * n for _ in range(m)]
        pattern = "b" * 10

        start_time = time.time()
        result = self.solution.countCells(grid, pattern)
        end_time = time.time()
        duration = end_time - start_time
        print(
            f"\nLarge Grid Performance Test ({m}x{n}): Time = {duration:.4f}s")

        # Basic assertion - mainly care about completion time
        self.assertGreaterEqual(result, 0)
        # Optional: Add a time limit assertion if needed
        # self.assertLess(duration, 2.0) # Example: Assert runs under 2 seconds


if __name__ == '__main__':
    unittest.main()
