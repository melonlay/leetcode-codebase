# Iterative Calculation of Binomial Coefficients Modulo M

## Concept

When we need to compute a sequence of binomial coefficients `C(n, k)` for a fixed `n` and varying `k` (e.g., `k = 0, 1, ..., n`) modulo some integer `M`, calculating each `C(n, k) mod M` independently using methods like Lucas's Theorem can be inefficient, often leading to `O(n log k)` or `O(n log n)` complexity for the sequence.

An often faster approach is to compute them iteratively using the identity:

`C(n, k) = C(n, k-1) * (n - k + 1) / k`

This allows us to find `C(n, k) mod M` if we know `C(n, k-1) mod M`, by performing the multiplication and division modulo `M`. Division requires finding the modular multiplicative inverse of `k` modulo `M`.

## Modulo Prime Power `p^a`

Directly calculating the modular inverse of `k` is only possible if `gcd(k, M) = 1`. When `M` is not prime, `k` might share factors with `M`. A common approach is to work with prime factorization. Let `M = p_1^{a_1} * ... * p_r^{a_r}`. We can compute `C(n, k) mod p_i^{a_i}` for each prime power factor and then combine the results using the Chinese Remainder Theorem (CRT).

To compute `C(n, k) mod p^a` iteratively:

1.  **Track Exponent of `p`:** Maintain a counter `cnt_p` representing the exponent of `p` in the prime factorization of `C(n, k)`. Based on the identity `C(n, k) = C(n, k-1) * (n - k + 1) / k`, the exponent changes based on the powers of `p` dividing `(n - k + 1)` and `k`. Let `v_p(x)` be the exponent of `p` in `x`. Then `cnt_p(k) = cnt_p(k-1) + v_p(n - k + 1) - v_p(k)`. `v_p(x)` can be found by repeatedly dividing `x` by `p`.
    *   **Legendre's Formula Connection:** While Legendre's formula (`v_p(n!) = sum_{i=1}^\infty floor(n / p^i)`) gives the exponent directly for factorials, the iterative update `v_p(n-k+1) - v_p(k)` effectively calculates the change in `v_p(C(n,k)) = v_p(n!) - v_p(k!) - v_p((n-k)!)` when moving from `k-1` to `k`.
2.  **Track Remaining Factor Modulo `p^a`:** Maintain the value `R = (C(n, k) / p^{cnt_p}) mod p^a`. This is the part of `C(n, k)` not divisible by `p`. To update `R` from step `k-1` to `k`, we multiply by `(n - k + 1) / p^{v_p(n-k+1)}` and divide by `k / p^{v_p(k)}`, all modulo `p^a`. The division requires the modular inverse of `(k / p^{v_p(k)})` modulo `p^a`, which exists because this term is now coprime to `p`.

## Modulo Composite `M` (Example: `M=10`)

Let's illustrate with `M = 10 = 2 * 5`. We need `C(n, k) mod 2` and `C(n, k) mod 5`.

*   **Modulo 2:** `C(n, k) mod 2` is 1 if `(n & k) == k` (Kummer's Theorem), and 0 otherwise. We can track this iteratively. Let `cnt2` be the exponent of 2 in `C(n, k)`. `C(n, k) mod 2 = 0` if `cnt2 > 0`, and `1` if `cnt2 == 0`. The change `v_2(n-k+1) - v_2(k)` can be efficiently found using bit manipulation tricks like `(x & -x).bit_length() - 1` which gives `v_2(x)`. We only need to track if `cnt2` is zero or positive.
*   **Modulo 5:** We track `cnt5 = v_5(C(n, k))` and `r5 = (C(n, k) / 5^{cnt5}) mod 5`.
    *   Update `cnt5`: `cnt5 += v_5(n-k+1) - v_5(k)`. Find `v_5(x)` by dividing `x` by 5 until it's not divisible.
    *   Update `r5`: Multiply `r5` by `(n-k+1) / 5^{v_5(n-k+1)} mod 5`. Divide `r5` by `(k / 5^{v_5(k)}) mod 5`. Division is multiplication by modular inverse modulo 5. The inverses `1^{-1}=1, 2^{-1}=3, 3^{-1}=2, 4^{-1}=4` (mod 5) can be precomputed.
*   **Combine with CRT:** Once we have `mod2 = C(n, k) % 2` (effectively `cnt2 == 0`) and `mod5 = C(n, k) % 5` (effectively `r5` if `cnt5 == 0`, else `0`), we use a precomputed CRT table to find `C(n, k) % 10`.
    ```python
    # Example: crt_table[mod2][mod5] -> result mod 10
    crt_table = [
        [0, 6, 2, 8, 4],  # mod2 = 0
        [5, 1, 7, 3, 9]   # mod2 = 1
    ]
    mod5_val = 0 if cnt5 > 0 else r5
    mod2_val = 1 if cnt2 == 0 else 0
    coeff_mod10 = crt_table[mod2_val][mod5_val]
    ```

## Symmetry Optimization

Since `C(n, k) = C(n, n-k)`, if we need the coefficients for a sum `sum_{k=0}^n C(n, k) * A[k]`, we can compute `C(n, k)` iteratively only for `k = 0` to `n // 2`. The sum can be rewritten by pairing terms:
`Sum = Sum_{k=0}^{floor((n-1)/2)} C(n, k) * (A[k] + A[n-k]) + (C(n, n/2) * A[n/2] if n is even)`

## Complexity

The iterative calculation of `C(n, k) mod M` for `k=0..n` takes roughly **O(n)** time (amortized). The divisions by prime factors `p` in the `v_p(x)` calculation happen infrequently enough across all `k`.
This is significantly faster than the `O(n log n)` complexity often resulting from repeated calls to Lucas's Theorem.

## Applicability

This technique is highly effective in scenarios requiring a full or partial sequence of binomial coefficients `C(n, k)` for a fixed `n`, modulo some `M`, especially in competitive programming problems where `n` can be large (e.g., up to 10^5 or 10^6) but an `O(n log n)` or `O(n^2)` approach would time out.

[[../../optimizations/combinatorics/nCr_sequence_lucas_vs_iterative.md]] (Comparison with independent calculation methods)
[[../../optimizations/loop_optimization/symmetry_exploitation.md]] (Link to symmetry optimization) 