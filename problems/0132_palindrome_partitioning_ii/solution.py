import sys
from typing import List


class Solution:
    """
    Solves LeetCode Problem 132: Palindrome Partitioning II using dynamic programming.

    The goal is to find the minimum number of cuts needed to partition a string
    such that every substring in the partition is a palindrome.

    This optimized solution uses O(N) space and O(N^2) time.
    It combines the minimum cuts DP calculation with palindrome checking
    using the "Expand from Center" technique.
    """

    def minCut(self, s: str) -> int:
        """
        Calculates the minimum cuts needed for a palindrome partitioning.

        Args:
            s: The input string.

        Returns:
            The minimum number of cuts.
        """
        n = len(s)
        if n <= 1:
            return 0

        # dp[i] stores the minimum cuts needed for the prefix s[0...i-1]
        # Initialize with worst-case cuts (i-1 cuts for length i)
        dp = [i - 1 for i in range(n + 1)]
        # Base case dp[0] = -1 is helpful conceptually (0 cuts for empty string means dp[0]+1=0)

        for i in range(n):
            # Expand for odd length palindromes centered at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                # s[l...r] is a palindrome
                # Cost to partition s[0...r] is 1 (cut after r) + cost for s[0...l-1] (dp[l])
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

            # Expand for even length palindromes centered at i, i+1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                # s[l...r] is a palindrome
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

        return dp[n]
