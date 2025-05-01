import bisect
from bisect import bisect_left  # Specific import
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Calculates the maximum number of envelopes that can be Russian dolled.

        Sorts envelopes first by height descending, then stably by width ascending.
        Then finds the Longest Increasing Subsequence (LIS) of the heights
        using an optimized approach with bisect_left.

        Args:
            envelopes: A list of lists, where each inner list is [width, height].

        Returns:
            The maximum number of nested envelopes.
        """
        if not envelopes:
            return 0

        # Sort by height descending first
        envelopes = sorted(envelopes, key=lambda x: x[1], reverse=True)
        # Then sort by width ascending (stable sort preserves height order for ties)
        envelopes = sorted(envelopes, key=lambda x: x[0])

        # Find LIS of heights using binary search (Patience Sorting variant)
        # Initialize dp (tails) with the height of the first envelope
        dp = [envelopes[0][1]]

        # Iterate from the second envelope
        for _, h in envelopes[1:]:
            # If current height extends the LIS, append directly
            if dp[-1] < h:
                dp.append(h)
            else:
                # Otherwise, find the position to replace an existing tail
                # This keeps the smallest tail for a given LIS length.
                i = bisect_left(dp, h)
                dp[i] = h

        # The length of the LIS is the length of the dp array
        return len(dp)
