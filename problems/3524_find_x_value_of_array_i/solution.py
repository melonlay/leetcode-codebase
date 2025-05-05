from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        Calculates the X-value of the array nums modulo k.

        The X-value is an array of size k where result[x] is the number
        of ways to remove a non-overlapping prefix and suffix (possibly empty)
        such that the product of the remaining non-empty subarray elements
        is congruent to x modulo k.

        Args:
            nums: A list of positive integers.
            k: A positive integer.

        Returns:
            A list of size k representing the X-value.

        Approach:
        Uses dynamic programming. Iterates through the array nums.
        Keeps track of the counts of product remainders for all subarrays
        ending at the current index j.
        dp[r] = count of subarrays ending at j with product % k == r.
        The final result is the sum of dp states across all j.

        Complexity:
        Time: O(n * k), where n is the length of nums.
        Space: O(k) for the dp array and result array.
        """
        n = len(nums)
        if n == 0:
            return [0] * k

        result = [0] * k
        # dp[r] stores the count of subarrays ending at the *current* index j
        # whose product modulo k equals r.
        dp = [0] * k

        for j in range(n):
            v = nums[j] % k
            # Create the dp state for subarrays ending at index j
            new_dp = [0] * k

            # Consider extending previous subarrays ending at j-1
            # If dp[r_prev] > 0, it means there were dp[r_prev] subarrays
            # ending at j-1 with product r_prev mod k.
            # Appending nums[j] results in subarrays ending at j with
            # product (r_prev * v) % k.
            for r_prev in range(k):
                if dp[r_prev] > 0:
                    new_r = (r_prev * v) % k
                    new_dp[new_r] += dp[r_prev]

            # Add the single-element subarray nums[j]
            new_dp[v] += 1

            # Add the counts from subarrays ending at j to the total result
            for r in range(k):
                result[r] += new_dp[r]

            # Update dp for the next iteration (j+1)
            dp = new_dp

        return result
