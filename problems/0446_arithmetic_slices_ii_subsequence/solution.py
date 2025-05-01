from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Counts the number of arithmetic subsequences in the given list using optimized DP.

        An arithmetic subsequence must have at least three elements.
        This approach uses a DP state dp[(j, i)] representing the count of
        arithmetic subsequences of length >= 3 ending with the pair (nums[j], nums[i]).
        It uses a helper map `seen` to quickly find potential third elements.

        Time Complexity: O(n^3) worst-case (all elements equal), O(n^2) average.
        Space Complexity: O(n^2) for dp map and seen map.

        Args:
            nums: The input list of integers.

        Returns:
            The total number of arithmetic subsequences.
        """
        n = len(nums)
        if n < 3:
            return 0

        ans = 0
        # dp[(j, i)] stores the count of arithmetic subsequences (length >= 3)
        # ending specifically with the pair of indices (j, i).
        dp = defaultdict(int)
        # seen[value] stores list of indices where 'value' appears.
        seen = defaultdict(list)

        for i in range(n):
            # Add current index to seen map *before* inner loop
            seen[nums[i]].append(i)
            for j in range(i):
                target_val = 2 * nums[j] - nums[i]
                if target_val in seen:
                    # Iterate through all k where nums[k] == target_val and k < j
                    for k in seen[target_val]:
                        if k < j:
                            # Count of sequences ending at (k, j)
                            count_ending_at_kj = dp[(k, j)]  # Uses defaultdict
                            # New sequences ending at (j, i) formed by extending from (k, j)
                            # = 1 (for the sequence k, j, i) + count_ending_at_kj (for longer ones)
                            newly_formed_count = 1 + count_ending_at_kj
                            # Add to total answer
                            ans += newly_formed_count
                            # Add the newly formed count to the count for sequences ending at (j, i)
                            dp[(j, i)] += newly_formed_count

        return ans
