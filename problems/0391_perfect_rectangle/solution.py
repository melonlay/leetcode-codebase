from typing import List, Set, Tuple


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Checks if a list of rectangles forms a perfect cover using the most
        optimized approach based on area summation and corner point cancellation.

        Algorithm:
        - Iterate through rectangles, calculating the total sum of their areas.
        - Use a set and the symmetric difference operator (`^=`) to track corners.
          Points appearing an even number of times cancel out.
        - After the loop, check if exactly 4 points remain in the set.
          If not, it cannot be a perfect cover (due to overlaps or gaps
          affecting interior/boundary point counts).
        - If 4 points remain, derive the potential bounding box corners directly
          from these 4 points using min/max based on coordinate sums:
          - Bottom-left (bl): The point with the minimum coordinate sum (x + y).
          - Top-right (tr): The point with the maximum coordinate sum (x + y).
        - Calculate the area of this derived bounding box.
        - Return True if the derived bounding box area equals the total summed area.
          This combined check ensures area conservation and implicitly verifies
          that the 4 points were the correct bounding box corners for a perfect tiling.

        Args:
            rectangles: A list of rectangles [x1, y1, a1, b1].

        Returns:
            True if the rectangles form a perfect cover, False otherwise.
        """
        total_area = 0
        corners: Set[Tuple[int, int]] = set()

        for x1, y1, a1, b1 in rectangles:
            # Accumulate area
            total_area += (a1 - x1) * (b1 - y1)

            # Use symmetric difference to track corners (XOR effect)
            corners ^= {(x1, y1), (x1, b1), (a1, y1), (a1, b1)}

        # Check 1: Exactly 4 points must remain for a perfect rectangle
        # If not 4, gaps or overlaps have occurred.
        if len(corners) != 4:
            return False

        # Check 2: Derive bounding box from the 4 remaining points
        # These *must* be the bounding box corners if len(corners) == 4
        # and the area check below passes.
        bl_x, bl_y = min(corners, key=lambda p: p[0] + p[1])
        tr_a, tr_b = max(corners, key=lambda p: p[0] + p[1])

        # Check 3: Area check
        # Calculate the area of the bounding box derived from the corners
        # If this matches the sum of individual areas, AND we have exactly 4
        # corner points remaining, it guarantees a perfect cover.
        expected_area = (tr_a - bl_x) * (tr_b - bl_y)
        return total_area == expected_area
