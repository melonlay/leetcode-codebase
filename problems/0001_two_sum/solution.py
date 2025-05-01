from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list such that they add up to the target.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list containing the indices of the two numbers.
        """
        num_map = {}  # Hash map to store number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # Found the complement in the map
                return [num_map[complement], i]
            # Add the current number and its index to the map
            num_map[num] = i

        # Should not be reached given the constraint that exactly one solution exists
        return []
