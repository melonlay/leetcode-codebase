from typing import List


class Solution:
    def _compute_lps(self, pattern: str) -> List[int]:
        """Computes the Longest Proper Prefix which is also Suffix (LPS) array."""
        m = len(pattern)
        lps = [0] * m
        length = 0  # Length of the previous longest prefix suffix
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def _kmp_search(self, text: str, pattern: str) -> List[int]:
        """Performs KMP search to find all occurrences of pattern in text."""
        n = len(text)
        m = len(pattern)
        if m == 0 or n == 0 or m > n:
            return []

        lps = self._compute_lps(pattern)
        indices = []
        i = 0  # index for text
        j = 0  # index for pattern
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return indices

    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        """Counts cells using KMP and Difference Arrays for efficiency."""
        m = len(grid)
        n = len(grid[0])
        L = len(pattern)
        total_cells = m * n

        if L == 0 or total_cells < L:
            return 0

        # Flatten grid horizontally
        text_h = "".join("".join(row) for row in grid)

        # Flatten grid vertically (column-major)
        text_v = "".join(grid[r][c] for c in range(n) for r in range(m))

        # Find pattern matches
        indices_h = self._kmp_search(text_h, pattern)
        indices_v = self._kmp_search(text_v, pattern)

        # --- Calculate Coverage using Difference Arrays ---

        # Horizontal Coverage
        coverage_h = [False] * total_cells
        if indices_h:
            diff_h = [0] * (total_cells + 1)
            for k in indices_h:
                diff_h[k] += 1
                if k + L < total_cells:  # Use < total_cells for index k+L
                    diff_h[k + L] -= 1

            current_coverage = 0
            for idx in range(total_cells):
                current_coverage += diff_h[idx]
                if current_coverage > 0:
                    coverage_h[idx] = True

        # Vertical Coverage
        coverage_v = [False] * total_cells
        if indices_v:
            diff_v = [0] * (total_cells + 1)
            for k in indices_v:
                diff_v[k] += 1
                if k + L < total_cells:  # Use < total_cells for index k+L
                    diff_v[k + L] -= 1

            current_coverage = 0
            for idx in range(total_cells):
                current_coverage += diff_v[idx]
                if current_coverage > 0:
                    coverage_v[idx] = True

        # --- Count overlapping cells ---
        count = 0
        for r in range(m):
            for c in range(n):
                idx_h = r * n + c
                idx_v = c * m + r  # Vertical index is column-major

                if coverage_h[idx_h] and coverage_v[idx_v]:
                    count += 1

        return count
