import heapq
from typing import List

# === SELF-REFLECTION ON FAILED ATTEMPTS (FOR FUTURE REFERENCE) ===
# 1. Logarithm-Based Approaches:
#    - MISTAKE: Used math.log to avoid large integers for comparisons and batching.
#    - WHY FAILED (WA): Floating-point precision errors. abs(log1 - log2) < EPSILON
#      is unreliable for exact ordering and tie-breaking, especially with error accumulation.
# 2. Pure Integer + Binary Search Batching:
#    - MISTAKE: Calculated batch size p via binary search using pow(multiplier, p).
#    - WHY FAILED (TLE): pow(multiplier, large_p) is computationally too expensive,
#      even with Python's large integers, when p can be up to k=10^9, especially inside loops.
# 3. Overly Complex State Tracking (op_counts/stale checks in user's final approach):
#    - MISTAKE: Insisted on using op_counts and complex stale checks even within the
#      user's two-phase round-robin detection approach, failing to grasp that Phase 1's
#      main goal was establishing final *relative order*, not exact intermediate counts.
#    - WHY UNNECESSARY: The user's final correct logic cleverly bypasses the need for
#      explicit intermediate counts and staleness checks *after* Phase 1.
#      Phase 1 simulation (until all elements seen) correctly establishes the *relative order*
#      of elements. Phase 2 calculation uses this final order and the remaining k
#      to directly calculate the final exponent (`k//n + (i < k%n)`) which is applied
#      to the value *at the end of Phase 1*. Explicit counts/staleness become redundant.
# === USER'S CORRECT AND CONCISE APPROACH (IMPLEMENTED BELOW) ===
#    - INSIGHT: Realized the process likely stabilizes into a round-robin pattern after
#      an initial phase (Phase 1) where all elements are touched. The exact values
#      during phase 1 matter less than the final *relative order* established.
#    - STRATEGY:
#      a) Simulate Phase 1 step-by-step using heap `(value, index)`. Use `heappushpop`
#         for efficiency and track `unseen` indices. Stop when k=0 or `unseen` is empty.
#         This establishes the crucial relative order in the heap.
#      b) Calculate remaining ops `k` and determine Phase 2 full cycles (`k // n`) and
#         remainder ops (`k % n`).
#      c) Iterate through the heap *as it exists after Phase 1*. For the i-th element popped
#         (representing the i-th smallest at the end of Phase 1):
#         i. Determine its final exponent: `exponent = k // n + (i < k % n)`.
#            The `(i < k % n)` adds 1 for the elements that get hit by remainder ops.
#         ii.Calculate final value: `final_val = (val_at_end_of_p1 * pow(multiplier, exponent, mod)) % mod`.
#            Use the value popped from the heap (`val_at_end_of_p1`) as the base.
#    - WHY IT WORKS: Avoids float precision. Avoids expensive pow() in loops.
#      Correctly separates initial phase (for ordering) from bulk calculation (using final order).
#      The `k // n + (i < k % n)` exponent elegantly combines cycle and remainder effects.
#      The base value `val_at_end_of_p1` implicitly includes all Phase 1 multiplications.
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
