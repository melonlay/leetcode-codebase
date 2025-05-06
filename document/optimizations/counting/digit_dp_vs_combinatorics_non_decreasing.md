# Optimization: Digit DP vs. Combinatorics for Non-Decreasing Numbers

## Problem Context

When counting numbers within a range `[L, R]` that satisfy a property like having **non-decreasing digits** in a given base `b`.

## Approaches

1.  **Digit DP:**
    *   **Method:** Standard Digit DP using `count(<=R) - count(<=L-1)`. The core DP state typically involves `dp(index, prev_digit, is_less, is_leading)`.
    *   **Logic:** Builds numbers digit by digit, checking the non-decreasing constraint (`current_digit >= prev_digit`) at each step.
    *   **Complexity:** `O(log_b(N) * b^2)` per count calculation, where `N=max(R)`.
    *   **Pros:** General approach applicable to many digit-based properties.
    *   **Cons:** Can be slower due to state space size and recursion/iteration overhead, especially the `b^2` factor.
    *   **Reference:** [[../../patterns/digit_dp/digit_dp.md]]

2.  **Combinatorial Counting:**
    *   **Method:** Uses combinations with repetition (Stars and Bars) combined with digit-by-digit iteration over the target number `N` (in base `b`). Calculates `count(<=R) - count(<=L-1)`.
    *   **Logic (`count_le(N, b)`):**
        *   Counts positive non-decreasing numbers with length `< len(N)` using `CWR(b-1, length)`. (Counts sequences using digits 1..b-1).
        *   Iterates through digits `s[i]` of `N`. For each position `i`, sums counts for numbers starting with a smaller valid digit `d` at `i`. The count for placing `d` is `CWR(b-d, rem_len)`, representing choosing the remaining `rem_len` digits from `d..b-1`.
        *   Handles the number `N` itself if its prefix is non-decreasing.
        *   Adds 1 at the end to account for the number 0.
    *   **Complexity:** `O(log_b(N) * b + Precomputation)` per count calculation. Precomputation for `nCr` is typically `O(MaxN)` or `O(log_b(N) + b)`.
    *   **Pros:** Often significantly faster due to better complexity (`b` vs `b^2`). Direct calculation avoids deep recursion.
    *   **Cons:** Less general; only applicable when the property has a direct combinatorial structure (like non-decreasing/non-increasing).
    *   **Reference:** [[../../mathematical_concepts/combinatorics/combinations_with_repetition.md]], [[../../techniques/combinatorics/iterative_nCr_modulo.md]]

## Conclusion

For problems involving counting numbers with simple monotonic digit properties like non-decreasing or non-increasing, the **Combinatorial Counting approach is generally preferred** due to better performance compared to a standard Digit DP.

However, Digit DP remains a valuable and more general technique for complex digit properties that lack a simple combinatorial formula.

## Common Mistakes

*   When implementing the combinatorial approach, ensure the correct formulas are used for counting (e.g., using `CWR(b-1, k)` for *positive* numbers of length `k`, versus `CWR(b, k)` which includes 0).
*   Ensure sufficient size for precomputed arrays (e.g., factorials) when base conversion is involved (see [[../implementation/precomputation_array_size_base_conversion.md]]). 