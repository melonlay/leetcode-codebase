import heapq
from typing import List

# Renaming heappush/heappop for clarity within the class context
from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """Calculates the volume of trapped rainwater in a 2D height map.

        Uses a min-heap combined with Depth First Search (DFS).
        1. Initialize heap with border cells.
        2. Pop the lowest boundary cell (`level`, r, c) from the heap.
        3. Perform DFS starting from (r, c) to find all connected cells reachable
           below or at this `level`.
        4. For cells found via DFS that are below `level`, calculate trapped water.
        5. Any neighbor cell encountered during DFS that is *higher* than `level`
           is a new boundary segment and is added to the heap.
        6. Mark visited cells by modifying the heightMap in-place (-1).

        Args:
            heightMap: A list of lists of integers representing the 2D elevation map.
                       This map will be modified in-place.

        Returns:
            The total volume of trapped rainwater.
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:  # Cannot trap water if less than 3x3 effectively
            return 0

        heap = []  # Min-heap storing (height, row, col)
        # visited matrix is implicitly handled by modifying heightMap to -1

        # Add border cells to the min-heap (excluding corners initially, handled later)
        # Mark borders as visited (-1) in the heightMap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    # Avoid adding corners twice if m=1 or n=1 logic was different
                    if heightMap[r][c] != -1:
                        heappush(heap, (heightMap[r][c], r, c))
                        heightMap[r][c] = -1  # Mark as visited

        total_water = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            level, r_min, c_min = heappop(heap)

            # Start DFS from the popped boundary cell
            stack = [(r_min, c_min)]

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check bounds and if the neighbor is unvisited
                    if 0 <= nr < m and 0 <= nc < n and heightMap[nr][nc] != -1:
                        neighbor_height = heightMap[nr][nc]

                        if neighbor_height <= level:
                            # Neighbor is inside or at the boundary level, potentially trapping water
                            # Water trapped is determined by the boundary `level`
                            total_water += level - neighbor_height
                            # Continue DFS from this neighbor
                            stack.append((nr, nc))
                        else:
                            # Neighbor is higher, forming a new boundary wall segment
                            # Add it to the heap to be processed later
                            heappush(heap, (neighbor_height, nr, nc))

                        # Mark neighbor as visited
                        heightMap[nr][nc] = -1

        return total_water
