import typing


class Solution:
    """
    Implements wildcard pattern matching using dynamic programming.

    The DP table `dp[i][j]` stores whether the first `i` characters of the string `s`
    match the first `j` characters of the pattern `p`.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        Checks if the input string `s` matches the wildcard pattern `p`.

        Args:
            s: The input string.
            p: The pattern string containing '?' and '*'.

        Returns:
            True if the pattern matches the entire string, False otherwise.
        """
        m, n = len(s), len(p)
        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: Empty string matches empty pattern
        dp[0][0] = True

        # Base case: Pattern matching empty string (s)
        # A pattern can match an empty string only if it consists of '*'.
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                # If a non-'*' character is encountered, it cannot match empty string anymore
                break  # Optimization: Subsequent dp[0][k] will also be False

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = s[i - 1]
                p_char = p[j - 1]

                if p_char == s_char or p_char == '?':
                    # Match: depends on the previous diagonal state
                    dp[i][j] = dp[i - 1][j - 1]
                elif p_char == '*':
                    # '*': can match empty sequence (dp[i][j-1])
                    #      or match the current char s_char (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # else: dp[i][j] remains False (mismatch)

        return dp[m][n]
