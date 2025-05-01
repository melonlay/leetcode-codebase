import sys
from typing import List


class Solution:
    """
    Solves LeetCode Problem 132: Palindrome Partitioning II using dynamic programming.

    Finds the minimum number of cuts needed to partition a string such that
    all resulting substrings are palindromes.
    """

    def minCut(self, s: str) -> int:
        """
        Calculates the minimum cuts for palindrome partitioning.

        Args:
            s: The input string.

        Returns:
            The minimum number of cuts required.
        """
        n = len(s)
        if n <= 1:
            return 0

        # is_pal[j][i] is True if s[j...i] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        # Precompute all palindromic substrings
        # O(n^2) time and space
        for length in range(1, n + 1):
            for j in range(n - length + 1):
                i = j + length - 1
                if length == 1:
                    is_pal[j][i] = True
                elif length == 2:
                    is_pal[j][i] = (s[j] == s[i])
                else:
                    is_pal[j][i] = (s[j] == s[i]) and is_pal[j + 1][i - 1]

        # cuts[i] = minimum cuts needed for prefix s[0...i-1]
        # Size n + 1, cuts[0] = -1 (for base case)
        # Initialize cuts[i] = i - 1 (worst case: cut after each char)
        cuts = list(range(-1, n))  # cuts = [-1, 0, 1, ..., n-1]

        # O(n^2) time
        for i in range(1, n + 1):
            for j in range(i):  # Check substrings s[j...i-1]
                if is_pal[j][i - 1]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)

        return cuts[n]
