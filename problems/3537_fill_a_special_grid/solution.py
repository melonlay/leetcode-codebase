from typing import List


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        memo = {}

        def _fill(n: int, offset: int) -> List[List[int]]:
            # Check memoization table
            if (n, offset) in memo:
                return memo[(n, offset)]

            # Base case: N=0 -> 1x1 grid
            if n == 0:
                return [[offset]]

            size = 1 << n  # 2^n
            sub_size = 1 << (n - 1)  # 2^(n-1)
            quadrant_count = 1 << (2 * n - 2)  # 4^(n-1) or (2^n * 2^n) // 4

            # Recursively fill the four quadrants with appropriate offsets
            tr = _fill(n - 1, offset)
            br = _fill(n - 1, offset + quadrant_count)
            bl = _fill(n - 1, offset + 2 * quadrant_count)
            tl = _fill(n - 1, offset + 3 * quadrant_count)

            # Create the grid for the current level
            grid = [[0] * size for _ in range(size)]

            # Combine the results from the recursive calls into the grid
            for r in range(sub_size):
                for c in range(sub_size):
                    # Top-Left quadrant of result grid
                    grid[r][c] = tl[r][c]
                    # Top-Right quadrant of result grid
                    grid[r][c + sub_size] = tr[r][c]
                    # Bottom-Left quadrant of result grid
                    grid[r + sub_size][c] = bl[r][c]
                    # Bottom-Right quadrant of result grid
                    grid[r + sub_size][c + sub_size] = br[r][c]

            # Store result in memoization table before returning
            memo[(n, offset)] = grid
            return grid

        # Initial call to the recursive helper function
        return _fill(N, 0)
