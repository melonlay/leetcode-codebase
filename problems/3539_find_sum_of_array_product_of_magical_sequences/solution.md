# Solution Explanation for 3539: Find Sum of Array Product of Magical Sequences

## Problem Summary

Given integers `M`, `K`, and an array `nums`, we need to find the sum of products of all "magical" sequences. A sequence `seq` of length `M` is magical if `0 <= seq[i] < len(nums)` and the sum `S = 2^seq[0] + ... + 2^seq[M-1]` has exactly `K` set bits in its binary representation. The product of a sequence is `P = nums[seq[0]] * ... * nums[seq[M-1]]`. We need to compute the sum of `P` for all magical sequences, modulo `10^9 + 7`.

## Approach: Digit DP

The core idea is to count the sequences by considering the contribution of each index `j` from `0` to `N-1` (where `N = len(nums)`). Let `c_j` be the number of times index `j` is chosen in a sequence `seq`. Then:
1.  The total number of elements chosen must be `M`: `Sum(c_j for j=0..N-1) = M`.
2.  The sum of powers of 2 is `S = Sum(c_j * 2^j for j=0..N-1)`.
3.  The condition is that the population count (number of set bits) of `S` must be `K` (`popcount(S) == K`).
4.  The product for a specific combination of counts `(c_0, ..., c_{N-1})` is `Prod = Product(nums[j]^c_j for j=0..N-1)`.
5.  The number of distinct sequences `seq` corresponding to this specific count combination is given by the multinomial coefficient `M! / (c_0! * c_1! * ... * c_{N-1}!)`.

We want to calculate: `Sum_{valid counts (c_j)} [ (M! / (Prod c_j!)) * (Prod nums[j]^{c_j}) ] mod (10^9 + 7)`.

Directly iterating through all count combinations is too slow. We can use Digit DP based on the bits of the sum `S`.

### DP State

We process the contribution of indices `j` bit by bit, from `j=0` upwards. The state `dp[j][m][carry][k]` represents the intermediate result after considering indices `0` to `j-1` (corresponding to bits 0 to `j-1` of the sum `S`).

*   `j`: The current bit position (index) being processed.
*   `m`: The total number of elements chosen from `nums` using indices less than `j` (`Sum(c_i for i < j)`).
*   `carry`: The carry propagated *into* bit position `j` from the sum calculated using indices less than `j`.
*   `k`: The number of set bits (`1`s) encountered in the binary representation of the sum `Sum(c_i * 2^i for i < j)` at bit positions less than `j`.

`dp[j][m][carry][k]` stores the sum of terms `Sum [ (m! / Prod_{i<j} c_i!) * Prod_{i<j} nums[i]^{c_i} ]` over all valid assignments `(c_0, ..., c_{j-1})` that satisfy the state conditions (`m`, `carry`, `k`).

We use a dictionary `dp` mapping `(m, carry, k)` to the summed value at the current bit `j` to handle sparse states.

### DP Transition

We iterate `j` from `0` up to a maximum required bit position (`max_bits`, roughly `N + log2(M)`). For each state `(m, carry, k)` active at bit `j` with value `value = dp[j][m][carry][k]`, we consider choosing `c_j` occurrences of index `j` (where `0 <= c_j <= M - m`).

If `j >= N`, we are only processing remaining carries, so `c_j` must be 0, and `nums[j]` effectively becomes 1.

The next state `(m_next, carry_next, k_next)` at bit `j+1` is calculated:
*   `m_next = m + c_j`
*   `current_val = carry + c_j` (Value added at bit `j`)
*   `bit_j_value = current_val % 2` (The actual bit value at position `j`)
*   `carry_next = current_val // 2` (Carry propagated to bit `j+1`)
*   `k_next = k + bit_j_value` (Updated popcount)

If `m_next <= M` and `k_next <= K`, we update the DP state for `j+1`:

The contribution to `dp[j+1][m_next][carry_next][k_next]` is derived from the relationship:
`Term(m_next) = Term(m) * C(m_next, c_j) * nums[j]^c_j`

So, we add `value * C(m_next, c_j) * pow(nums[j], c_j, MOD)` to `dp[j+1][m_next][carry_next][k_next]`.

We use precomputed combinations `nCr_mod` and powers `pow(num, exp, MOD)` for efficiency.

### Base Case

`dp[0][0][0][0] = 1`. This represents the state before considering any index: 0 elements chosen, 0 carry, 0 set bits, corresponding to an empty product (value 1).

### Final Answer

After iterating through all `j` up to `max_bits`, the final sum is found in the state corresponding to having chosen exactly `M` elements, having a final carry of `0`, and having accumulated exactly `K` set bits: `dp[max_bits][M][0][K]`. We access this value from the final `dp` dictionary.

## Complexity Analysis

*   **Time Complexity:** `O(max_bits * M * M * K * M * log(M))` if powers are calculated on the fly, or `O(max_bits * M * M * K * M)` with precomputed powers. Precomputation takes `O(N * M * log(num))` or `O(N*M)` for powers and `O(M)` for combinations. The state space is roughly `max_bits * M * M * K`. The transition takes `O(M)`. Given `max_bits ~ N+logM`, `N<=50`, `M,K<=30`, the complexity is roughly `O((N+logM) * M^3 * K)`, which is feasible (around `55 * 30^4 ~ 4.5 * 10^7` operations inside the main loop, plus precomputation).
*   **Space Complexity:** `O(M * M * K)` for storing the DP states at each bit iteration. We only need the states from the previous bit `j` to calculate the states for `j+1`. So, space can be optimized to `O(M * M * K)`. Precomputation takes `O(M)` for factorials and `O(N * M)` for powers.

## Foundational KB Components
*   [[techniques/combinatorics/iterative_nCr_modulo.md]] (Implicitly used via `nCr_mod` function)
*   The core logic follows the [[patterns/digit_dp/digit_dp_carry_counts.md]] pattern. 