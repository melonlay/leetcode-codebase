class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Determines if string s matches the regular expression pattern p.

        Supports '.' (matches any single character) and '*' (matches zero or
        more of the preceding element).

        Args:
            s: The input string.
            p: The regular expression pattern.

        Returns:
            True if s matches p entirely, False otherwise.
        """
        m, n = len(s), len(p)
        # dp[i][j] will be true if the first i characters of s
        # match the first j characters of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, .* that can match empty string
        # dp[0][j] depends on dp[0][j-2] if p[j-1] is '*'
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # Check the pattern two steps back
                # We need j >= 2 because '*' must follow a character
                if j >= 2:
                    dp[0][j] = dp[0][j-2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current characters being considered:
                s_char = s[i-1]
                p_char = p[j-1]

                if p_char == '.' or p_char == s_char:
                    # Match: result depends on the previous state diagonal
                    dp[i][j] = dp[i-1][j-1]
                elif p_char == '*':
                    # '*' requires looking at the preceding pattern character p[j-2]
                    # We are guaranteed j >= 2 here because the first char cannot be '*'
                    preceding_p_char = p[j-2]

                    # Option 1: '*' matches zero occurrences of preceding_p_char
                    # In this case, dp[i][j] depends on the state skipping the '*' and its preceding char
                    zero_occurrence_match = dp[i][j-2]

                    # Option 2: '*' matches one or more occurrences of preceding_p_char
                    # This is only possible if s_char matches preceding_p_char (or preceding_p_char is '.')
                    # If it matches, dp[i][j] depends on the state where the '*' consumed s_char
                    one_or_more_occurrence_match = False
                    if preceding_p_char == '.' or preceding_p_char == s_char:
                        # dp[i-1][j] means: s up to i-1 matched p up to j (where p[j-1] is '*')
                        one_or_more_occurrence_match = dp[i-1][j]

                    dp[i][j] = zero_occurrence_match or one_or_more_occurrence_match
                else:
                    # No match and p_char is not '*'
                    dp[i][j] = False

        return dp[m][n]
