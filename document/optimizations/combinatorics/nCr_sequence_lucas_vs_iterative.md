# Optimization: Lucas+CRT vs. Iterative for Binomial Coefficient Sequences

## Optimization Goal

To efficiently compute sums that involve a sequence of binomial coefficients modulo `M`, typically of the form: `Sum = sum_{k=0}^n C(n, k) * A[k] mod M`.

## Context

Many combinatorial problems require calculating such sums. The naive approach of calculating each `C(n, k) mod M` independently can be too slow if `n` is large.

## Suboptimal Approach: Independent Calculation (e.g., Lucas + CRT)

*   **Method:** Calculate each `C(n, k) mod M` term separately.
    *   If `M` is prime, Factorials + Modular Inverse or Lucas's Theorem can be used.
    *   If `M` is composite (e.g., `M=10`), factorize `M`. Use Lucas's Theorem for each prime factor (`p`) to find `C(n, k) mod p`. Combine the results using the Chinese Remainder Theorem (CRT).
*   **Complexity:** `O(n * log k)` or `O(n log n)`. Each call to Lucas takes `O(log_p k)` time. Precomputing factorials modulo `M` might take `O(n)` but requires `M` to be prime or careful handling of inverses for composites.
*   **When Suitable:** Might be acceptable for small `n` or if only a *few, sparse* `C(n, k)` values are needed.
*   **Reference:** [[../../techniques/combinatorics/binomial_coefficient_modulo.md]] (General C(n,k) mod M techniques)

## Optimized Approach: Iterative Calculation

*   **Method:** Leverage the identity `C(n, k) = C(n, k-1) * (n - k + 1) / k`. Compute `C(n, k) mod M` iteratively based on the value of `C(n, k-1) mod M`.
    *   Requires careful handling of division via modular inverse.
    *   For composite `M`, track the exponent of each prime factor `p` of `M` within `C(n, k)` (e.g., `v_p(n-k+1) - v_p(k)`) and the remaining part modulo `p`. Combine results using CRT at each step or at the end.
*   **Complexity:** `O(n)` amortized time to compute the sequence `C(n, 0)` through `C(n, n)` modulo `M`. Each step takes amortized `O(1)` time.
*   **When Suitable:** Significantly better when the full sequence or a large contiguous portion of `C(n, k)` values are required for a fixed `n`, especially when `n` is large (e.g., `10^5`).
*   **Reference:** [[../../techniques/combinatorics/iterative_nCr_modulo.md]] (Detailed explanation of the iterative technique)

## Comparison & Trade-offs

| Feature              | Independent (Lucas+CRT) | Iterative                     |
| :------------------- | :---------------------- | :---------------------------- |
| **Time (Sequence)**  | `O(n log n)`            | `O(n)`                        |
| **Time (Single C(n,k))**| `O(log k)`              | `O(k)` (needs previous terms) |
| **Implementation**   | Moderate                | Higher (state tracking)       |
| **State Required**   | Low                     | Higher (e.g., `cnt_p`, `r_p`) |

**Recommendation:** For problems like LeetCode 3463 involving sums over `k=0..n` with large `n`, the **Iterative Approach** provides a crucial asymptotic advantage (`O(n)` vs `O(n log n)`), making it the preferred method despite potentially higher implementation complexity.

## Related Optimizations

This optimization is often used in conjunction with:

*   **Difference Array:** Reformulating the target sum. [[../../techniques/sequence/difference_array.md]]
*   **Symmetry `C(n,k)=C(n,n-k)`:** Halving the number of coefficients to compute. <!-- TODO: [[../loop_optimization/symmetry_exploitation.md]] --> 