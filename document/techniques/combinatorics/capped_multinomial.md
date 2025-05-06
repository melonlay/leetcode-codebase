# Technique: Capped Multinomial Coefficient Calculation

## Concept

This technique calculates the multinomial coefficient `P(N; n1, n2, ..., nk) = N! / (n1! * n2! * ... * nk!)` but stops the calculation early if the result exceeds a specified `limit`. It leverages the identity:

`P(N; n1..nk) = C(N, n1) * C(N - n1, n2) * C(N - n1 - n2, n3) * ... * C(nk, nk)`

By computing each binomial coefficient term `C(current_N, count_val)` using the [[capped_nCr.md]] technique (with the same `limit`), we can efficiently determine if the final multinomial coefficient exceeds the `limit` without performing potentially massive intermediate calculations.

## Motivation

*   **Performance for K-th Selection:** Crucial for optimizing algorithms that find the k-th permutation of a multiset. Calculating the exact number of permutations starting with a specific character can be very expensive if the number is large. We often only need to know if this count is `>= k`.
*   **Avoiding Large Numbers:** Prevents TLE by avoiding the calculation and storage of extremely large multinomial coefficients when only a comparison against a limit (like `k`) is required.

## Algorithm

1.  **Input:** `N`, `counts` (list or iterable of positive counts `n1, n2, ...`), `limit`.
2.  **Initialization:** `res = 1`, `current_N = N`.
3.  **Iteration:** For each `count_val` in `counts`:
    *   Calculate `binom_val = nCr_capped(current_N, count_val, limit)`. See [[capped_nCr.md]].
    *   **Check Cap 1:** If `binom_val > limit`, the overall result must exceed `limit`. Return `limit + 1`.
    *   Calculate `potential_res = res * binom_val`.
    *   **Check Cap 2:** If `potential_res > limit`, return `limit + 1`.
    *   **Update:** `res = potential_res`, `current_N -= count_val`.
4.  **Return:** Return `res` (which is guaranteed to be `<= limit`).

## Implementation (Python Example)

```python
# Assumes nCr_capped function is defined as in capped_nCr.md

# Example nCr_capped (needed for the example to run)
def nCr_capped(N, k, limit):
    if k < 0 or k > N: return 0
    if k == 0 or k == N: return 1
    if k > N // 2: k = N - k
    if k == 1: return N if N <= limit else limit + 1
    res = 1
    for i in range(k):
        res = res * (N - i) // (i + 1)
        if res > limit: return limit + 1
    return res

# Returns the exact value of N! / (n1!...nk!) if <= limit,
# otherwise returns limit + 1.
def multinomial_capped(N, counts, limit):
    res = 1
    current_N = N
    # Process only positive counts
    active_counts = [c for c in counts if c > 0]

    for count_val in active_counts:
        if current_N < count_val:
             raise ValueError("Logic error: current_N < count_val")
             
        binom_val = nCr_capped(current_N, count_val, limit)
        
        if binom_val > limit:
            return limit + 1 

        # Check for potential overflow before multiplication if limit is huge?
        # Python handles large ints, usually okay.
        potential_res = res * binom_val
        
        if potential_res > limit:
             return limit + 1
        
        res = potential_res
        current_N -= count_val
        
    return res

# Example Usage
limit = 1000
counts1 = [2, 1, 1] # P(4; 2,1,1) = 4!/(2!1!1!) = 12
N1 = sum(counts1)
print(f"Multinomial({N1}; {counts1}) capped at {limit}: {multinomial_capped(N1, counts1, limit)}") # Output: 12

counts2 = [10, 5, 5] # P(20; 10,5,5) = 20!/(10!5!5!) = 7527520 -> exceeds limit
N2 = sum(counts2)
print(f"Multinomial({N2}; {counts2}) capped at {limit}: {multinomial_capped(N2, counts2, limit)}") # Output: 1001

counts3 = [2, 2] # P(4; 2,2) = 4!/(2!2!) = 6
N3 = sum(counts3)
print(f"Multinomial({N3}; {counts3}) capped at {limit}: {multinomial_capped(N3, counts3, limit)}") # Output: 6

```

## Complexity Analysis

*   **Time:** O(k_sum * k_avg), where `k_sum` is the sum of the counts (equal to `N`), and `k_avg` is roughly the average value of a count `ni`. This comes from the complexity of `nCr_capped` being O(k). The overall complexity is roughly proportional to the sum of the counts used in the `nCr` calls, which sums to `N`. However, the cost of large integer arithmetic inside `nCr_capped` matters if the cap `limit` is very large. If the cap is hit early, performance is much better.
*   **Space:** O(1) beyond input storage.

## Use Cases

*   **Primary:** Efficiently determining if the number of permutations of a remaining multiset is greater than or equal to a rank `k` in k-th permutation algorithms. See [[../algorithms/combinatorics/kth_multiset_permutation.md]].

## Related Techniques

*   [[capped_nCr.md]] (Core component)
*   [[../mathematical_concepts/combinatorics/multiset_permutation_count.md]] (Calculates the exact multinomial coefficient)

``` 