from typing import List
from itertools import islice # Required for the optimized solution

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if not nums:
            return 0

        xorPairs = {0}      # Stores unique XOR sums of two elements (n_a ^ n_b) from processed prefix, plus 0.
                            # Initial {0} allows forming (num ^ x ^ x) and (num ^ num ^ num) effectively.
        xorTriplets = set(nums) # Stores final unique triplet XORs. 
                                # Initialized with nums to cover (x^x^x = x) and (x^y^y = x) cases from the start.

        # Determine the limit for early exit. 
        # If max(nums) is m, its bit_length is k_bl. Limit is 2^k_bl.
        # All possible XOR sums from nums will be < 2^k_bl.
        # If len(xorTriplets) reaches this, all possible values are found.
        current_max_val = 0
        for x_val in nums: # Find max in nums to determine bit_length for the limit
            if x_val > current_max_val:
                current_max_val = x_val
        
        limit = 0
        if current_max_val == 0: # handles nums = [0] or [0,0,0] (not allowed by 1 <= nums[i] but robust)
            limit = 1 # Only {0} is possible
        else:
            limit = 1 << current_max_val.bit_length()

        # Iterating through nums to build pairs and triplets
        for i, num in enumerate(nums):
            # Combine current `num` with all existing `xorPairs` to form triplets
            # xorPairs contains {0} and {nums[a]^nums[b] for a < b < i}
            # num ^ 0 -> num (covers num^x^x type cases)
            # num ^ (nums[a]^nums[b]) -> nums[a]^nums[b]^num (covers a < b < i cases)
            xorTriplets.update(map(num.__xor__, xorPairs))

            # Update xorPairs with pairs formed by `num` and all preceding elements
            # This adds {num ^ nums[j] for j < i} to xorPairs for the *next* iteration.
            xorPairs.update(map(num.__xor__, islice(nums, 0, i)))
            
            # Early exit if all possible XOR sums for the given range of numbers are found
            if len(xorTriplets) >= limit:
                return limit
        
        return len(xorTriplets) 