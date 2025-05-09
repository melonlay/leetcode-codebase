import collections
import functools
import math

class Solution:
    def countBalancedPermutations(self, num_str: str) -> int:
        MOD = 1_000_000_007
        n = len(num_str)

        counts = collections.Counter(int(d) for d in num_str)
        current_sum = sum(int(d) for d in num_str)

        if current_sum % 2 != 0:
            return 0

        # Python 3.8+ has math.comb, for older versions, a manual comb function would be needed.
        # Assuming LeetCode environment supports math.comb (Python 3.8+).
        # If not, this would need a helper for combinations.
        # comb = math.comb 

        @functools.lru_cache(None)
        def dfs(digit_val: int, odd_slots_to_fill: int, even_slots_to_fill: int, odd_sum_balance_needed: int) -> int:
            """
            digit_val: Current digit we are trying to place (e.g., from 9 down to 0).
            odd_slots_to_fill: Number of odd-indexed slots remaining to be filled.
            even_slots_to_fill: Number of even-indexed slots remaining to be filled.
            odd_sum_balance_needed: The sum that digits placed into ODD slots must still achieve.
            """
            if odd_sum_balance_needed < 0:
                return 0
            
            if digit_val < 0: # All digits (9 through 0) have been processed
                if odd_slots_to_fill == 0 and even_slots_to_fill == 0 and odd_sum_balance_needed == 0:
                    return 1 # All conditions met
                else:
                    return 0 # Conditions not met

            # If no slots left but balance not zero (or vice versa), or slots left but no digits.
            # This is implicitly handled by the digit_val < 0 check and the conditions there.
            # Also, if odd_slots_to_fill < 0 or even_slots_to_fill < 0, this is an invalid path, which
            # can be pruned by checks before recursive calls or handled if math.comb allows k > n (returns 0).
            # For safety, let's add explicit checks, though math.comb(n, k) returns 0 if k > n or k < 0.
            if odd_slots_to_fill < 0 or even_slots_to_fill < 0:
                return 0

            ans_for_current_digit_val = 0
            num_occurrences_of_digit = counts[digit_val]

            # Iterate over how many of the current digit (digit_val) are placed in odd slots
            for count_for_odd_slots in range(num_occurrences_of_digit + 1):
                count_for_even_slots = num_occurrences_of_digit - count_for_odd_slots

                if count_for_odd_slots > odd_slots_to_fill or count_for_even_slots > even_slots_to_fill:
                    continue # Not enough slots for this distribution

                ways_to_choose_slots = (math.comb(odd_slots_to_fill, count_for_odd_slots) *
                                        math.comb(even_slots_to_fill, count_for_even_slots)) % MOD
                
                term_result = dfs(digit_val - 1, 
                                  odd_slots_to_fill - count_for_odd_slots, 
                                  even_slots_to_fill - count_for_even_slots, 
                                  odd_sum_balance_needed - digit_val * count_for_odd_slots)
                
                ans_for_current_digit_val = (ans_for_current_digit_val + ways_to_choose_slots * term_result) % MOD
            
            return ans_for_current_digit_val

        initial_odd_slots = n // 2
        initial_even_slots = (n + 1) // 2
        target_odd_half_sum = current_sum // 2
        
        # Start DFS from digit 9 down to 0
        result = dfs(9, initial_odd_slots, initial_even_slots, target_odd_half_sum)
        
        dfs.cache_clear() # Clear cache for lru_cache
        return result 