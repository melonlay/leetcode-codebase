# Mathematical Concept: Multiset Permutation Count

## Definition

A multiset is a collection of elements where elements are allowed to appear more than once. The number of distinct permutations (arrangements) of a multiset is given by the multinomial coefficient formula.

Given a multiset with a total of `n` elements, where there are `n1` identical elements of type 1, `n2` identical elements of type 2, ..., `nk` identical elements of type k, such that `n1 + n2 + ... + nk = n`.

The number of distinct permutations is:

\[
P(n; n_1, n_2, \\ldots, n_k) = \\frac{n!}{n_1! n_2! \\cdots n_k!}
\]

## Derivation

Imagine temporarily labeling all identical items to make them distinct (e.g., `a1, a2, b1`). The total number of permutations would then be `n!`. However, since the identical items are actually indistinguishable, we have overcounted. For each type `i` with `ni` identical items, there are `ni!` ways to arrange just those items among themselves, which were counted as distinct permutations but are actually identical. To correct for this overcounting, we divide the total `n!` permutations by the product of the factorials of the counts for each distinct element type (`n1! * n2! * ... * nk!`).

## Implementation (Python)

This calculation often involves large factorials. Python's built-in support for arbitrary-precision integers makes this feasible. Pre-calculating factorials can improve efficiency if the calculation is needed multiple times.

```python
import math
from collections import Counter

# Precompute factorials for efficiency if called multiple times with similar n
MAX_N = 5000 # Example limit based on typical constraints
factorials = [1] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    factorials[i] = factorials[i - 1] * i

def count_multiset_permutations(n: int, counts: dict, precomputed_factorials: list) -> int:
    """
    Calculates the number of distinct permutations of a multiset.

    Args:
        n: The total number of elements in the multiset.
        counts: A dictionary mapping each distinct element type to its count (ni).
                Example: {'a': 2, 'b': 1} for the multiset {a, a, b}.
        precomputed_factorials: A list where precomputed_factorials[i] = i!.

    Returns:
        The total number of distinct permutations. Returns 0 if n is negative 
        or if precomputed factorials array is too small.
    """
    if n < 0:
        return 0
    if n >= len(precomputed_factorials):
        # Handle case where precomputation wasn't large enough, 
        # or calculate on the fly (might be slow)
        # For simplicity here, we assume precomputation covers n
        # Alternatively, raise an error or compute factorials dynamically.
         print(f"Warning: n={n} exceeds precomputed factorial limit {len(precomputed_factorials)}")
         # Attempt dynamic calculation (potentially slow)
         try:
             numerator = math.factorial(n)
         except ValueError: # n too large for math.factorial either
            # In a real scenario, might need a large number library 
            # or handle extremely large n differently. Return large number?
            return float('inf') # Or indicate error
    else:
        numerator = precomputed_factorials[n]

    denominator = 1
    for count in counts.values():
        if count < 0:
            return 0 # Invalid count
        if count >= len(precomputed_factorials):
             # Handle case where count exceeds precomputed limit
             print(f"Warning: count={count} exceeds precomputed factorial limit {len(precomputed_factorials)}")
             try:
                 denominator *= math.factorial(count)
             except ValueError:
                 return float('inf') # Or indicate error
        elif count > 0: # Factorial of 0 or 1 is 1, no need to multiply
             denominator *= precomputed_factorials[count]
        
        # Optimization: Check for potential division by zero if counts allow it,
        # although standard Counter usage avoids count=0 keys usually.
        if denominator == 0: return float('inf') # Avoid division by zero

    # Use integer division
    if denominator == 0: # Should ideally not happen with valid counts > 0
        return float('inf') 
    return numerator // denominator

# Example Usage: Multiset {a, a, b, c} -> n=4, counts={'a': 2, 'b': 1, 'c': 1}
n_example = 4
counts_example = {'a': 2, 'b': 1, 'c': 1}
# Ensure factorials are computed up to n_example
num_perms = count_multiset_permutations(n_example, counts_example, factorials)
# Expected: 4! / (2! * 1! * 1!) = 24 / (2 * 1 * 1) = 12
print(f"Permutations for {counts_example} (n={n_example}): {num_perms}")

# Example Usage: Multiset {a, a, a} -> n=3, counts={'a': 3}
n_example_2 = 3
counts_example_2 = {'a': 3}
num_perms_2 = count_multiset_permutations(n_example_2, counts_example_2, factorials)
# Expected: 3! / 3! = 1
print(f"Permutations for {counts_example_2} (n={n_example_2}): {num_perms_2}")

```

## Complexity Analysis

*   **Time:** O(N + K) where N is the maximum value for `n` needed for precomputing factorials, and K is the number of distinct element types (size of the `counts` dictionary keys, usually alphabet size <= 26). If factorials are not precomputed, it depends on the efficiency of `math.factorial` for large numbers.
*   **Space:** O(N) for storing precomputed factorials.

## Relation to Other Concepts

*   This formula is a generalization of the binomial coefficient `C(n, k) = n! / (k! * (n-k)!)`, which counts permutations of a multiset with two types of elements (k of one type, n-k of another).
*   Used as a sub-routine in algorithms like finding the [[../../algorithms/combinatorics/kth_multiset_permutation.md]].

``` 