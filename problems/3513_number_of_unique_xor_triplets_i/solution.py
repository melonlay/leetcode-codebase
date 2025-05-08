from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else: # n >= 3
            # For n >= 3, the numbers 1, 2, ..., n are available.
            # Let k = n.bit_length(). This means 2^(k-1) <= n < 2^k.
            # The basis elements 1, 2, 4, ..., 2^(k-1) are all <= n and thus available.
            # It's a known result that if these basis elements are available,
            # any integer X from 0 to (2^k - 1) can be formed as v1 ^ v2 ^ v3,
            # where v1, v2, v3 are from the set {1, ..., n}.
            # Also, any v1^v2^v3 will be < 2^k since each element is < 2^k.
            # Thus, for n >= 3, the number of unique XOR values is 2^k.
            return 1 << n.bit_length()
        # Constraints state: 1 <= n == nums.length <= 10^5, so n=0 handled for robustness.
