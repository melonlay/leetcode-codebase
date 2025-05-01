from typing import List


class Solution:
    """Solves the Trapping Rain Water problem using the Two Pointers approach."""

    def trap(self, height: List[int]) -> int:
        """Calculates the total trapped water.

        Uses two pointers, one starting from the left end and one from the right
        end of the height map. It maintains the maximum height encountered so far
        from the left (left_max) and from the right (right_max).

        The amount of water trapped at any position is limited by the minimum of
        the maximum heights on its left and right. The algorithm iteratively
        processes the shorter bar between the left and right pointers, calculates
        the trapped water based on the corresponding max height (left_max or right_max),
        and moves the pointer inward.

        Args:
            height: A list of non-negative integers representing the elevation map.

        Returns:
            The total amount of trapped rain water.
        """
        if not height:
            return 0

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            # Process the side with the lower bar, as the water level is
            # limited by the shorter surrounding wall.
            if height[left] < height[right]:
                # If the current left bar is higher than the left_max seen so far,
                # it becomes the new boundary and cannot trap water relative to left_max.
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Otherwise, the water trapped above the current bar is
                    # determined by the left_max (since we know height[right]
                    # is even higher, guaranteeing a right wall).
                    total_water += left_max - height[left]
                left += 1
            else:
                # Symmetric logic for the right pointer.
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water
