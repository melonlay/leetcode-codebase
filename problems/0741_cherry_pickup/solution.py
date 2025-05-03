from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Top-down DP with memoization (@cache)
        # State: dp(i1, j1, i2) -> max cherries when path 1 is at (i1, j1)
        #                           and path 2 is at row i2.
        # The column for path 2 (j2) is implicitly determined by the total steps:
        # total_steps = i1 + j1 = i2 + j2  =>  j2 = i1 + j1 - i2
        @cache
        def dp(i1, j1, i2):
            j2 = i1 + j1 - i2  # Calculate second path's column

            # Symmetry Optimization: Ensure i1 <= i2
            # If i1 > i2, swap the roles of path 1 and path 2 to compute
            # the canonical state dp(i2, j2, i1). This halves the state space.
            if i1 > i2:
                return dp(i2, j2, i1)

            # Base Case 1: Out of bounds or hit a thorn
            # Check if either path has gone out of the grid or hit a thorn.
            if i1 == n or j1 == n or i2 == n or j2 == n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
                # Use -1 to represent an impossible/invalid path, distinct from 0 cherries.
                return -1

            # Base Case 2: Both paths reached the destination
            # This is the target state for the recursion.
            if i1 == n - 1 and j1 == n - 1:
                # Since i1=n-1, j1=n-1, and i1<=i2, we must have i2=n-1.
                # Then j2 = (n-1)+(n-1)-(n-1) = n-1. Both are at the end.
                return grid[n - 1][n - 1]

            # Recursive Step: Calculate the max cherries obtainable from the *next* step.
            # Explore the 4 possible combined moves for the two paths:
            # dd: Path1 Down, Path2 Down -> (i1+1, j1), (i2+1, j2)
            # dr: Path1 Down, Path2 Right -> (i1+1, j1), (i2, j2+1) => state dp(i1+1, j1, i2)
            # rd: Path1 Right, Path2 Down -> (i1, j1+1), (i2+1, j2) => state dp(i1, j1+1, i2+1)
            # rr: Path1 Right, Path2 Right -> (i1, j1+1), (i2, j2+1) => state dp(i1, j1+1, i2)
            dd = dp(i1 + 1, j1, i2 + 1)
            dr = dp(i1 + 1, j1, i2)
            rd = dp(i1, j1 + 1, i2 + 1)
            rr = dp(i1, j1 + 1, i2)

            best_future = max(dd, dr, rd, rr)

            # If all future paths from the next step are invalid
            if best_future == -1:
                return -1

            # Calculate cherries collected at the *current* step (i1, j1, i2, j2)
            current_cherries = 0
            if i1 == i2:
                # Both paths are on the same cell (i1, j1) == (i2, j2)
                # Collect the cherry only once.
                current_cherries = grid[i1][j1]
            else:
                # Paths are on different cells. Collect cherries from both.
                current_cherries = grid[i1][j1] + grid[i2][j2]

            # Total cherries = cherries from current step + max cherries from future steps
            return best_future + current_cherries

        # Initial call: Start both paths at (0, 0)
        result = dp(0, 0, 0)

        # If dp(0, 0, 0) returned -1, it means the destination is unreachable.
        return max(result, 0)
