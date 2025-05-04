# Pattern: Digit DP with Carry and Multiple Counts

## Description

This pattern applies to problems where we need to sum a value over sequences/assignments `seq = (idx_0, ..., idx_{M-1})` (length `M`, choosing indices from `0..N-1`) satisfying:

1.  A primary constraint limits the total number of items chosen: `Sum_{k=0}^{N-1} count(k) = M`, where `count(k)` is the number of times index `k` appears in `seq`.
2.  A target property (e.g., number of set bits `K`) depends on a value `S` derived from the counts using positional significance: `S = Sum_{k=0}^{N-1} count(k) * Base^k` (commonly `Base=2`). The calculation of `S` involves carry propagation between positions `k`.
3.  The value summed involves terms related to the sequence choices, often `Value(seq) = Product_{k=0}^{N-1} base_value[k]^{count(k)}` combined with combinatorial factors (implicitly handled by the DP).

This pattern uses Digit DP, processing the calculation of `S` **position by position (e.g., bit by bit if Base=2)**, while simultaneously tracking the primary count constraint (`M`) and the evolving target property (`K`).

## DP State (Iterating by Position `j`)

The state typically captures the progress after considering the first `j` positions (e.g., bits 0 to `j-1`):

`dp[j][m][carry][prop]` or `dp_j = {(m, carry, prop): value}`

*   `j`: The current position (e.g., bit index) being processed (from 0 upwards).
*   `m`: The total number of sequence elements assigned to positions less than `j` (`Sum_{k<j} c_k`, where `c_k` is count assigned to position `k`).
*   `carry`: The carry propagated *into* position `j` from the sum calculated using positions less than `j`.
*   `prop`: The value of the target property accumulated so far based on positions `0` to `j-1` of `S` (e.g., number of set bits `k`).
*   `value`: The aggregated sum of terms (e.g., using Formulation 1 or 2) corresponding to all valid partial assignments leading to this state.

**Implementation Note:** Use dictionaries for sparse states.

## DP Transition (Iterating by Position `j`)

To calculate states for `j+1` from `dp_j`:
Iterate through state `(m, carry, prop)` with `current_value` in `dp_j`.
Iterate through `c_j` (count assigned to position `j`), `0 <= c_j <= M - m`.

1.  **Calculate Next State:** `m_next = m + c_j`, `value_at_j = carry + c_j`, `prop_next`, `carry_next`.
2.  **Check Constraints:** `m_next <= M`, `prop_next <= K`.
3.  **Calculate Multiplier:** Based on Formulation 1 (`nCr * pow`) or 2 (`inv_fact * pow`).
4.  **Update `dp_{j+1}`:** `dp_{j+1}[m_next][carry_next][prop_next] += current_value * multiplier`.

## Base Case

Typically `dp_0 = {(0, 0, initial_prop): 1}`, representing the state before processing any bits (0 items used, 0 carry, initial property value), with a base value of 1.

## Final Answer

After processing all necessary bits `j` (up to `max_bits`, often `N + log_Base(M)`), the answer is found in the final DP state `dp_{max_bits}`. It's usually the value associated with the state where the primary constraint is met (`m=M`), the carry is resolved (`carry=0`), and the target property matches the requirement (`prop=K`): `dp_{max_bits}[(M, 0, K)]`.

## Complexity

*   **Time:** `O(max_bits * StateSize * TransitionCost)`.
    *   `StateSize` is roughly `M * MaxCarry * MaxProp` (e.g., `M * M * K`).
    *   `TransitionCost` involves iterating `c_j` (up to `M`) and doing calculations (often O(1) with precomputation).
    *   Total: `O(max_bits * M * MaxCarry * MaxProp * M)`. E.g., `O((N + log M) * M^3 * K)`.
*   **Space:** `O(StateSize)` if only storing the previous state, e.g., `O(M * MaxCarry * MaxProp)`.

## Required Precomputation

*   Combinations (`nCr`) modulo `MOD`.
*   Powers (`pow(base, exp, MOD)`), potentially precomputed for all bases and exponents up to `M`.

## Related Concepts

*   [[../dynamic_programming/dynamic_programming.md]]
*   [[./digit_dp.md]] (Standard Digit DP - this pattern is a variant)
*   [[../../techniques/combinatorics/iterative_nCr_modulo.md]]
*   Exponential Generating Functions (EGFs) - The combinatorial term `value * C(m_next, c_j) * base_value[j]^c_j` is related to the coefficients when multiplying EGFs, although the carry propagation makes it non-standard. 

## Implementation Variants

### Formulation 1: Using Combinations (`nCr`) in Transition

*   **DP Value Meaning:** Stores `Sum [ (m! / Prod_{i<j} c_i!) * Prod_{i<j} base_value[i]^{c_i} ]`.
*   **Transition:** Updates `dp_next` by adding `current_value * C(m_next, c_j) * pow(base_value[j], c_j, MOD)`. Requires precomputed combinations (`nCr`).
*   **Final Answer:** The value in the target final state `dp[max_bits][M][0][K]` is the answer.
*   *This is the formulation described in the main DP State/Transition sections above and implemented in the first analyzed Python solution.* 

### Formulation 2: Using Inverse Factorials (`1/c!`) in Transition

*   **Mathematical Basis:** Relies on `Sum[P(seq)] = M! * Sum [ Product( (nums[i]^ci) / ci! ) ]`.
*   **DP Value Meaning:** Stores `Sum [ Product_{j<i} (base_value[j]^cj / cj!) ]`.
*   **Transition:** Updates `dp_next` by adding `current_value * inverse_factorial[c_j] * pow(base_value[j], c_j, MOD)`. Requires precomputed inverse factorials.
*   **Final Aggregation:** After iterating through all bits `j` up to `max_bits`, iterate through final states `(final_carry, M, final_prop_accumulated)`.
    *   Calculate the total property value: `total_prop = final_prop_accumulated + final_carry.bit_count()` (if property is bit count).
    *   If `total_prop == TargetProp`, add the `dp_value` of this state to a running sum `ans`.
    *   The final answer is `ans * factorial[M] % MOD`.
*   **Key Point:** Explicitly handling the bits in the `final_carry` during aggregation is crucial.
*   *This formulation is used in the second analyzed iterative solution.*
*   **Iterative Implementation Detail:**
    *   Precompute `w[j][c] = (pow(base_value[j], c, MOD) * inverse_factorial[c]) % MOD`.
    *   Outer loop iterates `j` (bit position / index).
    *   Inner loop iterates through `(carry, m, prop), current_value` in `dp_prev`.
    *   Innermost loop iterates `c_j` from `0` to `M - m`.
    *   Calculate next state `(carry_next, m_next, prop_next)`.
    *   Update `dp_next[(carry_next, m_next, prop_next)] += current_value * w[j][c_j]`.
    *   After loops, perform final aggregation as described above.

### Bottom-Up (Iterative by Position `j`)

*   Uses nested loops to iterate through bit positions `j`, and then through existing states `(m, carry, prop)` from the previous bit `j-1`.
*   Explicitly manages the DP table (often using dictionaries for sparse states) for the current and next bit positions.
*   State variables typically track counts/properties *used so far*.
*   Can use either Formulation 1 or 2 for the transition calculation.

### Top-Down (Recursive by Position `j`)

*   Uses a recursive function, typically memoized using `@lru_cache` in Python.
*   **State:** The function signature often represents the state, e.g., `dp(remaining_m, remaining_prop, current_bit_j, carry_value)`.
    *   State variables track counts/properties *still remaining*.
    *   The `carry_value` represents the accumulated numerical value carried *from* previous bits, not just the single bit carry *into* the current position.
*   **Transitions:** The function iterates through choices `c_j` for the `current_bit_j`, calculates the contribution factor (typically using Formulation 1 with `C(remaining_m, c_j)`), and calls itself recursively with updated state parameters (`remaining_m - c_j`, `remaining_prop - current_bit`, `current_bit_j + 1`, `new_carry_value`).
*   **Base Cases:** Handle termination conditions (e.g., `remaining_m == 0`, `current_bit_j` exceeds limits) and pruning for impossible states. When `remaining_m == 0`, must check if `remaining_prop == carry_value.bit_count()`.
*   **Memoization:** Crucial for performance. `@lru_cache` handles storing and retrieving results for computed states.
*   **Pruning:** Can incorporate checks like `remaining_m + carry_value.bit_count() < remaining_prop` to cut off branches early.
*   **Conciseness:** Often results in shorter code compared to the iterative version.
*   **Comparison:** See [[../../optimizations/dynamic_programming/digit_dp_carry_counts_topdown_vs_bottomup.md]] for a detailed comparison.

## Alternative Approach & Comparison

*   **Item-Based DP:** An alternative is the [[./dp_on_items_bitwise_sum_constraint.md]] pattern. Instead of iterating through the positions `j` of the sum `S`, it iterates through the input items/indices `i = 0..N-1` used to *form* the sequence. Its state typically tracks `(elements_chosen_so_far, carry_into_item_i_pos, prop_accumulated)`. See the pattern document for details.
*   **When to Use Which:**
    *   **Bit-Level DP (This Pattern):** May feel more natural if the constraints are strongly tied to the properties of the sum `S` itself (like standard Digit DP). Might be necessary if `N` is very large but the number of relevant positions (`max_bits`) is smaller.
    *   **Item-Level DP:** Can be significantly faster in practice (as seen in LC3539) if iterating through `N` items leads to better state pruning or structure, especially when combined with Formulation 2. Often preferred if `N` is reasonably small (e.g., N<=60).

For problems fitting this structure, also consider the [[./dp_on_items_bitwise_sum_constraint.md]] pattern, which iterates through items `0..N-1` instead of abstract bit positions and can be significantly faster in practice. 