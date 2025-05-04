# Pattern: DP on Items with Bitwise Sum Constraint

## Description

This pattern solves problems where we need to sum a value (like a product `P`) over all sequences `seq = (idx_0, ..., idx_{M-1})` satisfying:
1.  Length of `seq` is `M`.
2.  Each `0 <= idx_k < N` (indices chosen from `0` to `N-1`, corresponding to `base_value[idx_k]` from `nums`).
3.  A constraint based on the bitwise representation of a weighted sum involving the *counts* of each index `k` used in the sequence: `S = Sum_{k=0}^{N-1} count(k) * Base^k`. Typically `Base=2`. Example constraint: `popcount(S) == K`.
4.  The value summed usually involves terms like `P = Product_{k=0}^{N-1} base_value[k]^{count(k)}` combined with combinatorial factors (for permutations).

This approach iterates through the **items/indices `i = 0..N-1`** and builds a DP state that tracks the number of elements chosen so far (`j`) and the state of the bitwise sum constraint (`carry`, `prop`).

## DP State (Iterating by Item `i`)

A common state representation is a DP table (often nested dictionaries for sparsity) indexed by `(j, carry)`:
`dp[j][carry] = map {prop: value}`

*   The DP state `dp[j][carry]` stores results *after* processing items `0` to `i-1`.
*   `j`: The total number of sequence elements chosen using items `0` to `i-1` (`Sum_{k=0}^{i-1} count(k)`).
*   `carry`: The carry value generated *into* position `i` when calculating the sum `S` based on counts from items `0` to `i-1`.
*   `prop`: The accumulated value of the target property (e.g., set bits) derived from the sum `S` considering bits `0` to `i-1`.
*   `value`: The aggregated sum of terms for all ways to reach this state `(j, carry, prop)`. If using Formulation 2 (Inverse Factorials), `value = Sum [ Product_{k=0}^{i-1} (base_value[k]^{count_k} / count_k!) ]`.

## DP Transition (Iterating `i` from `0` to `N-1`)

To compute `dp_next` (state after considering item `i` with value `base_value[i]`) from `dp_prev` (state after item `i-1`):

1.  Iterate through previous states `(j_prev, carry_prev, {prop_prev: value_prev})` in `dp_prev`.
2.  Iterate through `count_i` (number of times item `i` is chosen), from `0` to `M - j_prev`.
3.  **Calculate Next State Variables:**
    *   `j = j_prev + count_i` (Total elements chosen up to item `i`).
    *   `current_sum = count_i + carry_prev` (Value contributed at position `i` of the sum `S`, assuming `Base=2`).
    *   `bit_value = current_sum % Base` (The `i`-th bit of `S`).
    *   `new_carry = current_sum // Base` (Carry into position `i+1`).
    *   `prop = update_property(prop_prev, bit_value)` (e.g., `prop_prev + bit_value`).
4.  **Check Constraints:** Ensure `prop <= K` (or other property constraints).
5.  **Calculate Term Multiplier:** Based on the formulation:
    *   **Formulation 2 (Faster):** `factor = (pow(base_value[i], count_i, MOD) * inverse_factorial[count_i]) % MOD`.
6.  **Update `dp_next`:**
    *   `target_map = dp_next[j][new_carry]`
    *   `target_map[prop] = (target_map.get(prop, 0) + value_prev * factor) % MOD`

## Final Aggregation

After iterating `i` through `N-1`:
1.  Iterate through the final DP states `(M, final_carry, {prop_at_n: value})` (where `j=M`).
2.  Calculate the property contribution from the `final_carry` (bits `N` and higher), e.g., `prop_carry = popcount(final_carry)`.
3.  `total_prop = prop_at_n + prop_carry`.
4.  If `total_prop == TargetProp` (e.g., `K`):
    *   **Formulation 2:** Add `value * factorial[M]` to the final result (modulo `MOD`).

## Complexity

*   **Time:** `O(N * StateSize * TransitionCost)`
    *   `StateSize`: Number of reachable states `(j, carry, prop)`. Roughly `M * MaxCarry * MaxProp`. `MaxCarry` can be up to `M`.
    *   `TransitionCost`: Dominated by the loop for `count_i` (up to `M`).
    *   Total: `O(N * M * M * MaxProp * M) = O(N * M^3 * MaxProp)`. E.g., `O(N * M^3 * K)` if property is bit count `K`.
*   **Space:** `O(StateSize)` = `O(M * M * K)`.
*   **Note:** While the theoretical complexity seems high, this approach can be practically faster than bit-level DP if the reachable state space is smaller or due to implementation details.

## Comparison to Bit-Level Digit DP

This pattern iterates through **items `0..N-1`** instead of abstract bit positions `0..max_bits` used in [[./digit_dp_carry_counts.md]]. It simulates the bitwise sum calculation within the state transitions. This can be more efficient for certain problem structures (e.g., smaller `N`, larger `M`) or constraints, as seen in LC3539 where it was significantly faster.
Compare with [[./digit_dp_carry_counts.md]].

## Optimization: M == K Case

If the target property `K` (e.g., bit count) is equal to the number of items `M`, the problem often reduces to selecting `M` *distinct* indices.
The sum of products can then be calculated efficiently using the M-th Elementary Symmetric Polynomial (ESP) of `nums[0...N-1]`, multiplied by `M!`.
See [[../../techniques/polynomial/elementary_symmetric_polynomial_dp.md]]. This optimization has complexity `O(N * M)`. Implement this as a separate check before the main DP.

## Required Precomputation

*   Factorials (`fact`) modulo `MOD`.
*   Inverse Factorials (`inv_fact`) modulo `MOD`.
*   Powers (`pow(num, exp, MOD)`) potentially precomputed per item `i`.

## Foundational Concepts
*   [[../dynamic_programming/dynamic_programming.md]]
*   [[../../techniques/combinatorics/iterative_nCr_modulo.md]] (Implicitly used via factorials/inverse factorials)
*   Popcount (Bit Manipulation)
*   Formulation 2 from [[./digit_dp_carry_counts.md]] 