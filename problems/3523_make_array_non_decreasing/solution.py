from typing import List

# Faster Solution based on counting descents


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        """Calculates the maximum possible size of a non-decreasing array
        obtainable by merging subarrays into their maximum value.

        Uses the optimal Greedy Scan approach:
        Iterate through nums, maintaining the maximum value of the last
        element (`lastMax`) in the conceptual final non-decreasing sequence.
        If the current number `n` is >= `lastMax`, it can form the next
        element, so increment the count (`ans`) and update `lastMax`.
        Otherwise, `n` gets merged into the previous segment and doesn't
        increase the count.

        Args:
            nums: The input list of integers.

        Returns:
            The maximum possible size of the resulting non-decreasing array.
        """
        ans = 0
        # Initialize lastMax to a value smaller than any possible nums[i]
        # or handle the first element separately.
        # Since nums[i] >= 1, 0 is a safe initialization.
        lastMax = 0
        for n in nums:
            if n >= lastMax:
                ans += 1
                lastMax = n
            # Implicit else: if n < lastMax, n is merged into the previous
            # segment, the effective maximum remains lastMax, and ans
            # does not increase.
        return ans
