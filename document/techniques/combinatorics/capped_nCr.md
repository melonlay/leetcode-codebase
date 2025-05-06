# Technique: Capped Binomial Coefficient Calculation (nCr)

## Concept

Calculating binomial coefficients `C(n, k)` can involve very large intermediate numbers or results, especially when `n` is large. In certain applications, particularly when comparing a rank `k` against permutation counts, we don't need the exact value of `C(n, k)` if it significantly exceeds a relevant limit (like the rank `k`).

This technique computes `C(n, k)` iteratively using the identity `C(n, i) = C(n, i-1) * (n - i + 1) / i`, but **stops the calculation early** and returns a sentinel value (e.g., `limit + 1`) if the intermediate or final result exceeds a specified `limit`.

## Motivation

*   **Performance:** Avoids expensive large integer arithmetic (multiplication/division) when the exact large value is unnecessary. This is crucial for preventing Time Limit Exceeded (TLE) in problems involving sequences of combinatorial calculations (like finding the k-th permutation).
*   **Bounded Comparison:** Allows efficient checking of conditions like `rank < C(n, k)` without computing a potentially huge `C(n, k)`.

## Algorithm

1.  **Input:** `N`, `k`, `limit`.
2.  **Base Cases:** Handle `k < 0`, `k > N` (result 0), `k == 0` or `k == N` (result 1).
3.  **Symmetry:** Use `C(N, k) = C(N, N - k)` to ensure `k <= N / 2`.
4.  **Optimization:** Handle `k = 1` separately (`C(N, 1) = N`). Return `N` if `N <= limit`, else `limit + 1`.
5.  **Iterative Calculation:**
    *   Initialize `res = 1`.
    *   Loop `i` from `0` to `k-1`:
        *   Calculate `next_res = res * (N - i) // (i + 1)`.
        *   **Check Cap:** If `next_res > limit`, return `limit + 1`.
        *   Update `res = next_res`.
6.  **Return:** Return `res`.

## Implementation (Python Example)

```python
# Returns the exact value of nCr(N, k) if it's <= limit,
# otherwise returns limit + 1.
def nCr_capped(N, k, limit):
    if k < 0 or k > N: return 0
    if k == 0 or k == N: return 1
    if k > N // 2: k = N - k
    
    if k == 1:
        return N if N <= limit else limit + 1

    res = 1
    for i in range(k):
        # Potential improvement: check overflow possibility before mult/div
        # if limit is very large, but Python handles arbitrary precision.
        numerator_product = res * (N - i)
        # Check if denominator is zero (shouldn't happen for i >= 0)
        if (i + 1) == 0: raise ZeroDivisionError
            
        res = numerator_product // (i + 1)
        
        # Check cap
        if res > limit:
            return limit + 1
            
    return res

# Example Usage
limit = 100
print(f"C(10, 3) capped at {limit}: {nCr_capped(10, 3, limit)}")   # Output: 120 -> 101
print(f"C(10, 5) capped at {limit}: {nCr_capped(10, 5, limit)}")   # Output: 252 -> 101
print(f"C(8, 2) capped at {limit}: {nCr_capped(8, 2, limit)}")    # Output: 28
print(f"C(100, 2) capped at {limit}: {nCr_capped(100, 2, limit)}") # Output: 4950 -> 101
print(f"C(15, 1) capped at {limit}: {nCr_capped(15, 1, limit)}") # Output: 15
```

## Complexity Analysis

*   **Time:** O(k), as the loop runs `k` times, and large integer operations inside take amortized time related to the number of digits, which grows relatively slowly. This is much faster than methods involving full factorial calculations or modular inverses when the cap is hit early.
*   **Space:** O(1) beyond input storage.

## Use Cases

*   Calculating terms in the expansion `P(n; n1..nk) = C(n, n1) * C(n-n1, n2) * ...` when only needed up to a limit `k`. See [[capped_multinomial.md]].
*   Optimizing algorithms that find the k-th lexicographical permutation/combination by avoiding full calculation of large permutation/combination counts. See [[../algorithms/combinatorics/kth_multiset_permutation.md]].

## Related Techniques

*   [[capped_multinomial.md]] (Builds upon this technique)
*   [[iterative_nCr_modulo.md]] (Iterative calculation for modulo results)

``` 