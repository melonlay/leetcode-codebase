import math
from typing import List


class Solution:
    """
    Solves the Best Meeting Point problem.

    The key insight is that the Manhattan distance allows separating the row and column
    components. The total distance is sum(|r_i - meeting_r|) + sum(|c_i - meeting_c|).
    To minimize this sum, we need to minimize each component independently.

    The value that minimizes the sum of absolute differences to a set of points
    in 1D is the median of those points.

    Therefore, the optimal meeting point (meeting_r, meeting_c) corresponds to the
    median of the row coordinates and the median of the column coordinates of all
    the houses (1s).

    We don't need to find the median point explicitly. The minimum sum of distances
    can be calculated directly from the sorted coordinates.
    """

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum total Manhattan distance.

        Args:
            grid: The m x n binary grid where 1 represents a house.

        Returns:
            The minimum total travel distance.
        """
        rows = []
        cols = []
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Collect row and column coordinates of houses
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        # Rows are collected in sorted order because we iterate row by row.
        # Columns need to be sorted.
        cols.sort()

        # Calculate the minimum 1D distance for rows and columns
        row_distance = self._calculate_min_distance_1d(rows)
        col_distance = self._calculate_min_distance_1d(cols)

        return row_distance + col_distance

    def _calculate_min_distance_1d(self, sorted_coords: List[int]) -> int:
        """
        Calculates the minimum sum of distances to the median in 1D.
        Assumes the input list `sorted_coords` is already sorted.

        This leverages the property that the sum of distances is minimized
        at the median. The sum can be calculated efficiently by pairing
        the smallest and largest elements, the second smallest and second
        largest, and so on.

        Args:
            sorted_coords: A sorted list of 1D coordinates.

        Returns:
            The minimum sum of absolute differences from the median.
        """
        total_distance = 0
        low, high = 0, len(sorted_coords) - 1
        while low < high:
            total_distance += sorted_coords[high] - sorted_coords[low]
            low += 1
            high -= 1
        return total_distance
