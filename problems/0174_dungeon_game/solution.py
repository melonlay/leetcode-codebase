import math
from typing import List


class Solution:
    """
    Solves the Dungeon Game problem using dynamic programming.

    The problem asks for the minimum initial health a knight needs to start with
    at the top-left corner (0, 0) to reach the princess at the bottom-right
    corner (m-1, n-1) of a dungeon grid. The knight can only move right or down.
    Health must remain > 0 at all times.

    This solution uses a backward dynamic programming approach.
    dp[i][j] stores the minimum health the knight must have *upon entering*
    cell (i, j) to survive the path to the princess.
    """

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        Calculates the minimum initial health required.

        Args:
            dungeon: A list of lists of integers representing the dungeon grid.
                     Negative numbers are damage, positive numbers are health orbs.

        Returns:
            The minimum positive integer health the knight must start with.
        """
        m = len(dungeon)
        n = len(dungeon[0])

        # dp[i][j] = minimum health needed *entering* cell (i, j)
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]

        # Base cases for the target cell and adjacent virtual cells
        # The knight needs at least 1 health *after* leaving the destination cell.
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        # Fill the DP table backwards from the princess's cell
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Min health needed *after* leaving cell (i, j) is the minimum
                # required for the next step (either down or right).
                min_health_needed_after_leaving = min(
                    dp[i + 1][j], dp[i][j + 1])

                # Health needed *before* accounting for dungeon[i][j]'s effect
                health_needed_before_effect = min_health_needed_after_leaving - \
                    dungeon[i][j]

                # The health upon entering cell (i, j) must be at least 1.
                # If the calculated needed health is <= 0, it means the knight
                # has enough health from this cell onwards (or the cell gives health),
                # so they only need 1 health point upon entering.
                dp[i][j] = max(1, health_needed_before_effect)

        # The result is the minimum health needed when entering the start cell (0, 0)
        return dp[0][0]
