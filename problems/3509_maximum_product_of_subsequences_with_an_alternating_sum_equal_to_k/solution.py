# Implementing EXACTLY based on user-provided correct code structure - Final Attempt
import collections
from typing import List, Set, DefaultDict


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # Optional pre-check from reference
        n = len(nums)
        # Assuming max_val = 12 based on typical constraints, adjust if needed
        max_val = 12
        odd_inds = n >> 1
        even_inds = n - odd_inds
        # Bound check exactly as provided in reference
        # Using max_val derived from constraints
        if not (-max_val * odd_inds <= k <= max_val * even_inds):
            return -1

        # State dictionaries as in the reference
        # Key: sum, Value: {products} for odd length
        odd_sums = collections.defaultdict(set)
        # Key: sum, Value: {products} for even length
        even_sums = collections.defaultdict(set)

        for val in nums:
            # Temporary dictionaries exactly as in reference
            new_odd_sums = collections.defaultdict(set)
            new_even_sums = collections.defaultdict(set)

            # --- Transitions exactly as in reference code logic ---

            # Extend EVEN length subsequences (from even_sums) -> ODD length (new_odd_sums)
            for curr in even_sums:  # Use 'curr' as key variable name like reference
                # Calculate products using set comprehension exactly as reference
                # Ensure 0 check in comprehension condition
                new_odd_sums[curr + val] = {i *
                                            val for i in even_sums[curr] if 0 <= i * val <= limit}
                # Explicitly add 0 if the current value is 0, using reference key logic
                if val == 0:
                    new_odd_sums[curr + val].add(0)

            # Extend ODD length subsequences (from odd_sums) -> EVEN length (new_even_sums)
            for curr in odd_sums:  # Use 'curr' as key variable name like reference
                # Calculate products using set comprehension exactly as reference
                # Ensure 0 check in comprehension condition
                new_even_sums[curr - val] = {i *
                                             val for i in odd_sums[curr] if 0 <= i * val <= limit}
                # Explicitly add 0 if the current value is 0, using reference key logic
                if val == 0:
                    # USING THE EXACT KEY FROM REFERENCE CODE: curr + val
                    new_even_sums[curr + val].add(0)

            # --- Merge new states into main state dictionaries ---
            # Iterating through keys exactly as in reference
            for i in new_odd_sums:  # Use 'i' as iteration variable like reference
                odd_sums[i].update(new_odd_sums[i])
            for i in new_even_sums:  # Use 'i' as iteration variable like reference
                even_sums[i].update(new_even_sums[i])

            # --- Add base case: subsequence [val] (length 1 -> odd length) ---
            # Placed at the end of the loop, exactly as in reference
            # Ensure 0 check consistent with set comprehension condition
            if 0 <= val <= limit:
                odd_sums[val].add(val)

        # --- Final Result Calculation ---
        ans = -1
        # Check odd length results for sum k, exactly as in reference
        # Check existence and non-empty set exactly as reference
        if k in odd_sums and len(odd_sums[k]):
            ans = max(ans, max(odd_sums[k]))
        # Check even length results for sum k, exactly as in reference
        # Check existence and non-empty set exactly as reference
        if k in even_sums and len(even_sums[k]):
            ans = max(ans, max(even_sums[k]))

        return ans
