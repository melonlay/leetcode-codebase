import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
    Solves the Skyline Problem using a sweep-line algorithm with a max-heap.
    """

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Computes the skyline contour from a list of buildings.

        Args:
            buildings: A list of buildings, where each building is represented
                       as [left, right, height].

        Returns:
            A list of key points [[x1, y1], [x2, y2], ...] representing the
            skyline contour, sorted by x-coordinate.
        """
        # Create events: (x, -height) for start, (x, height) for end
        # Sorting by x, then by height ensures starts are processed before ends
        # at the same x, and taller events are processed first.
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))

        # Sort events by x-coordinate, then by height (start events first)
        events.sort()

        skyline = []
        # Max-heap storing active heights (using negative values for max-heap simulation)
        live_heights = [0]  # Initialize with ground level
        # Dictionary to track counts of active heights
        height_counts = defaultdict(int)
        height_counts[0] = 1

        prev_max_h = 0

        for x, h_event in events:
            is_start = h_event < 0
            height = abs(h_event)

            if is_start:
                # Start event: add height to counts and heap
                if height_counts[height] == 0:
                    # Push negative for max-heap
                    heapq.heappush(live_heights, -height)
                height_counts[height] += 1
            else:
                # End event: decrement height count
                height_counts[height] -= 1

            # Clean the heap: remove heights whose counts are zero
            # These are heights of buildings that have ended but might still be at the heap top
            while height_counts[-live_heights[0]] == 0:
                heapq.heappop(live_heights)

            # Current maximum height is the top of the cleaned heap
            current_max_h = -live_heights[0]

            # If the maximum height changes, add a key point to the skyline
            if current_max_h != prev_max_h:
                skyline.append([x, current_max_h])
                prev_max_h = current_max_h

        return skyline
