from typing import List
import collections


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        Finds the largest possible height of a billboard using two disjoint subsets
        of rods with equal sums.

        The problem is equivalent to partitioning the rods into three sets:
        - Set 1: Forms the left support (sum s1)
        - Set 2: Forms the right support (sum s2)
        - Set 3: Unused rods
        We want to maximize s1 such that s1 == s2.

        This can be framed as finding two subsets with sums s1 and s2, such that
        s1 - s2 = 0, and maximizing s1.

        We use dynamic programming. Let dp[diff] be the maximum possible sum of the
        *first* support (s1) when the difference between the two supports is `diff`.
        (i.e., diff = s1 - s2).

        Initialization: dp = {0: 0} (Zero difference is achievable with height 0).

        Transition: For each rod `r`, we update the dp table. For each existing
        `diff` and corresponding `s1` in the current `dp`:
          1. Add `r` to the first support:
             - new_diff = diff + r
             - new_s1 = s1 + r
             - Update dp[new_diff] with max(dp.get(new_diff, 0), new_s1)
          2. Add `r` to the second support:
             - new_diff = diff - r
             - new_s1 = s1 (s1 doesn't change)
             - Update dp[new_diff] with max(dp.get(new_diff, 0), new_s1)
          3. Do not use `r`: This is implicitly handled by iterating over a copy.

        The final answer is dp[0], which represents the maximum s1 when s1 - s2 = 0.
        """
        # dp maps difference (s1 - s2) to the max possible s1 for that difference
        dp = {0: 0}

        for r in rods:
            # Create a copy to iterate over while modifying the original dp
            dp_next = dp.copy()
            for diff, s1 in dp.items():
                # Option 1: Add rod r to the first support (s1)
                new_diff_1 = diff + r
                new_s1_1 = s1 + r
                dp_next[new_diff_1] = max(dp_next.get(new_diff_1, 0), new_s1_1)

                # Option 2: Add rod r to the second support (s2)
                # s1 remains the same, s2 increases by r, so diff decreases by r
                new_diff_2 = diff - r
                new_s1_2 = s1  # s1 does not change in this case
                dp_next[new_diff_2] = max(dp_next.get(new_diff_2, 0), new_s1_2)

            # Update dp for the next iteration
            dp = dp_next

        # The answer is the maximum height (s1) achievable with a difference of 0
        return dp.get(0, 0)
