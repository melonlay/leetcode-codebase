class Solution:
    def numTilings(self, n: int) -> int:
        """Calculates the number of tilings for a 2xn board.

        Uses the recurrence dp[i] = 2*dp[i-1] + dp[i-3] with O(1) space.
        """
        MOD = 10**9 + 7

        # Handle base cases explicitly
        if n == 0:
            return 1  # One way to tile 2x0: do nothing
        if n == 1:
            return 1  # One way: | (vertical domino)
        if n == 2:
            return 2  # Two ways: || or == (two vertical or two horizontal)

        # Initialize DP states based on dp[0], dp[1], dp[2]
        dp_i_1 = 2  # Corresponds to dp[2]
        dp_i_2 = 1  # Corresponds to dp[1]
        dp_i_3 = 1  # Corresponds to dp[0]

        # Iterate from i = 3 up to n
        for _ in range(3, n + 1):
            # Calculate dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
            dp_curr = (2 * dp_i_1 + dp_i_3) % MOD

            # Update states for the next iteration
            # The old dp_i_3 becomes the new dp_i_4 (not needed)
            # The old dp_i_2 becomes the new dp_i_3
            # The old dp_i_1 becomes the new dp_i_2
            # The new dp_curr becomes the new dp_i_1
            dp_i_3 = dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_curr

        # The final answer is the last calculated dp_i_1 (which corresponds to dp[n])
        return dp_i_1
