from typing import List


class Solution:
    """Solves LeetCode problem 41: First Missing Positive."""

    def firstMissingPositive(self, nums: List[int]) -> int:
        """Finds the smallest missing positive integer in an unsorted array.

        Uses an in-place cyclic sort approach to achieve O(n) time and
        O(1) auxiliary space complexity.

        Args:
            nums: The input list of integers.

        Returns:
            The smallest positive integer not present in nums.
        """
        n = len(nums)

        # Place each positive number k in its correct position nums[k-1]
        # Ignore numbers <= 0 or > n
        for i in range(n):
            # Use a while loop to handle cases where the swapped element
            # also needs to be moved.
            # Condition: nums[i] should be in the range [1, n]
            # Condition: nums[i] is not already in its correct place (nums[nums[i] - 1] != nums[i])
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Target index for the current number nums[i]
                target_index = nums[i] - 1

                # Swap nums[i] with the element at its target index
                # This avoids infinite loops if duplicates exist (e.g., [1, 1])
                # because if nums[target_index] == nums[i], the loop condition
                # nums[nums[i] - 1] != nums[i] will become false.
                nums[i], nums[target_index] = nums[target_index], nums[i]

        # Find the first index where the number doesn't match the expected value (i+1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers from 1 to n are present, the missing one is n+1
        return n + 1
