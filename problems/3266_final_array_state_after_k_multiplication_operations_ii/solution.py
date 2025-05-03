import heapq
from typing import List

# === END SELF-REFLECTION ===

# Import necessary functions directly for conciseness like user example
from heapq import heapify, heappushpop, heappop


class Solution:
    """
    Solves LeetCode 3266: Final Array State After K Multiplication Operations II.
    Implementation based on the user's concise and correct final logic.
    """

    def getFinalState(self, nums: List[int], k: int,
                      multiplier: int, mod=1_000_000_007) -> List[int]:

        # Handle multiplier = 1 edge case first
        if multiplier == 1:
            # Per user's code, return original nums directly.
            # If LeetCode requires mod even for mult=1, change to: return [num % mod for num in nums]
            return nums

        n = len(nums)
        # unseen tracks indices NOT yet operated on at least once
        unseen = set(range(n))
        ans = [0] * n  # Pre-allocate result array

        # Initialize heap with (value, index) tuples using assignment expression
        heapify(heap := list(zip(nums, range(n))))

        # Phase 1: Simulate until k runs out OR all elements have been operated on once
        while k > 0 and unseen:
            # Peek the current minimum value and its index
            num, idx = heap[0]
            # Efficiently push the new value and pop the overall smallest
            heappushpop(heap, (num * multiplier, idx))
            k -= 1  # Decrement remaining operations
            unseen.discard(idx)  # Mark this index as seen/operated on

        # Phase 2: Calculate final values based on heap state after Phase 1
        # The heap now contains the values after Phase 1 simulation.
        # The remaining 'k' dictates the Phase 2 operations (cycles + remainder).
        # The order elements are popped *now* determines who gets the remainder ops.
        for i in range(n):
            # Pop the next smallest element according to the state *after* Phase 1
            num_at_p1_end, idx = heappop(heap)

            # Calculate the exponent for Phase 2 operations:
            # k // n : number of full cycles applied to every element in Phase 2
            # (i < k % n): adds 1 to the exponent for the first k % n elements popped,
            #              representing those hit by the final remainder operations.
            exponent_p2 = k // n + (i < k % n)

            # Calculate the final value:
            # Base is num_at_p1_end (value after Phase 1)
            # Power is exponent_p2 (operations during Phase 2)
            ans[idx] = (num_at_p1_end *
                        pow(multiplier, exponent_p2, mod)) % mod

        return ans
