import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_length = m + n
        if total_length == 0:
            raise ValueError(
                "Input arrays cannot both be empty (violates m+n >= 1 constraint)")

        # Ensure nums1 is the shorter array
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # total_length = m + n # Already calculated
        # Number of elements in the left partition
        half_len = (total_length + 1) // 2

        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2  # Partition index for nums1
            partition2 = half_len - partition1  # Corresponding partition index for nums2

            # Get elements around the partition points, handle edge cases
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else -math.inf
            min_right1 = nums1[partition1] if partition1 < m else math.inf

            max_left2 = nums2[partition2 - 1] if partition2 > 0 else -math.inf
            min_right2 = nums2[partition2] if partition2 < n else math.inf

            # Check if partitions are correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                max_left = max(max_left1, max_left2)

                if total_length % 2 == 1:
                    # Odd total length, median is the max of the left partition
                    return float(max_left)
                else:
                    # Even total length, median is avg of max_left and min_right
                    min_right = min(min_right1, min_right2)
                    return (max_left + min_right) / 2.0
            elif max_left1 > min_right2:
                # partition1 is too large, need to decrease it
                high = partition1 - 1
            else:  # max_left2 > min_right1
                # partition1 is too small, need to increase it
                low = partition1 + 1

        # Should not be reached if inputs are valid sorted arrays
        raise ValueError("Input arrays are not sorted or other error occurred")
