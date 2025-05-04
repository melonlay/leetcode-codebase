import sys
from typing import List
from collections import defaultdict

# Setting recursion depth is not relevant for iterative DP
# sys.setrecursionlimit(2000)


class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        """
        Calculates the sum of array products for all magical sequences modulo 10^9 + 7.

        A sequence 'seq' is magical if:
        1. It has size M.
        2. 0 <= seq[i] < len(nums).
        3. The binary representation of S = 2^seq[0] + ... + 2^seq[M - 1] has K set bits.

        The array product is prod(seq) = nums[seq[0]] * ... * nums[seq[M - 1]].

        Approach: Iterative DP on Items (Formulation 2) + M==K Optimization.
        Pattern: [[document/patterns/dynamic_programming/dp_on_items_bitwise_sum_constraint.md]]

        Args:
            M: The required size of the magical sequence.
            K: The required number of set bits in the binary sum condition.
            nums: The input array of integers.

        Returns:
            The sum of array products for all magical sequences, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Helper function to count set bits (popcount)
        def popcount(num):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count

        # --- Precompute Factorials and Inverse Factorials ---
        fact = [1] * (M + 1)
        inv_fact = [1] * (M + 1)
        for i in range(1, M + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        if M >= 0:
            # Handle M=0 separately if needed, though pow(1,mod-2,mod)=1 works
            inv_fact[M] = pow(fact[M], MOD - 2, MOD)
        # else: # M < 0 not expected

        for i in range(M - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        # --- Optimization for M == K case ---
        # If K == M, only sequences with M distinct indices contribute. Sum = M! * ESP_M(nums)
        # See: [[document/techniques/polynomial/elementary_symmetric_polynomial_dp.md]]
        if M == K:
            if M > n:
                return 0

            # Calculate Sum_{combinations {i_1, ..., i_M}} (nums[i_1] * ... * nums[i_M]) using DP
            dp_poly = [0] * (M + 1)
            dp_poly[0] = 1
            for i in range(n):
                num_val = nums[i]
                for j in range(M, 0, -1):
                    dp_poly[j] = (dp_poly[j] + dp_poly[j - 1] * num_val) % MOD

            sum_of_prods_combinations = dp_poly[M]
            result = (fact[M] * sum_of_prods_combinations) % MOD
            return result

        # --- General DP (Iterative, Formulation 2: Inverse Factorials) ---
        # DP State: dp[j][carry] = map {bits: value}
        # Iterates through nums[i] (i=0..n-1)
        # j: number of elements chosen *after* considering nums[0...i-1]
        # carry: carry into bit position i for sum S = Sum(count_k * 2^k)
        # bits: popcount of S restricted to bits 0..i-1
        # value: Sum [ Product_{k=0}^{i-1} (nums[k]^count_k / count_k!) ]

        # Using list of dicts for sparse storage, indexed by [j][carry]
        dp = [[{} for _ in range(M + 1)] for _ in range(M + 1)]
        dp[0][0] = {0: 1}  # Base case: 0 elements, 0 carry, 0 bits -> value 1

        # Iterate through each number/index i (effectively bit position i)
        for i in range(n):
            num_val = nums[i] % MOD  # Ensure nums[i] is taken modulo
            next_dp = [[{} for _ in range(M + 1)] for _ in range(M + 1)]

            # Precompute powers and combined factor (num_val^p / p!) for current num_val
            # This is the 'w' array from the user's code, precomputed for this 'i'
            term_factors = [0] * (M + 1)
            current_power = 1
            for p in range(M + 1):
                term_factors[p] = (current_power * inv_fact[p]) % MOD
                if p < M:
                    current_power = (current_power * num_val) % MOD

            # Iterate through previous states (j_prev chosen, carry_prev)
            for j_prev in range(M + 1):
                for carry_prev in range(M + 1):
                    if not dp[j_prev][carry_prev]:
                        continue

                    # Iterate count_i: how many times index 'i' is chosen
                    # Max count is M - j_prev
                    for count_i in range(M - j_prev + 1):
                        j = j_prev + count_i  # New total elements chosen

                        # Simulate binary addition at bit 'i'
                        current_sum = count_i + carry_prev
                        current_bit = current_sum % 2
                        new_carry = current_sum // 2

                        # Optimization/Constraint: Carry cannot exceed M
                        if new_carry <= M:
                            # Factor for this choice: (nums[i]^count_i / count_i!)
                            factor = term_factors[count_i]

                            # Update states in next_dp based on previous bits maps
                            for bits_prev, value_prev in dp[j_prev][carry_prev].items():
                                bits = bits_prev + current_bit  # New accumulated bit count

                                # Pruning: if accumulated bits exceed K, skip
                                if bits <= K:
                                    term_val = (value_prev * factor) % MOD

                                    # Add to the target state in next_dp
                                    target_map = next_dp[j][new_carry]
                                    current_val = target_map.get(bits, 0)
                                    target_map[bits] = (
                                        current_val + term_val) % MOD

            # Move to the next state
            dp = next_dp

        # --- Final Result Calculation ---
        result = 0
        m_fact = fact[M]  # M!

        # Iterate through final states (M elements chosen, final_carry)
        for final_carry in range(M + 1):
            if not dp[M][final_carry]:
                continue

            rem_bits = popcount(final_carry)  # Bits from carry >= N

            # bits_at_n: bits accumulated from positions 0..N-1
            for bits_at_n, value in dp[M][final_carry].items():
                total_bits = bits_at_n + rem_bits

                if total_bits == K:
                    # value = Sum(Prod/Fact). Multiply by M! for final sum.
                    final_term = (value * m_fact) % MOD
                    result = (result + final_term) % MOD

        return result
