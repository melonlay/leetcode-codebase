# Algorithm: Constructing the k-th Lexicographical Multiset Permutation

## Abstract Definition

This algorithm constructs the k-th lexicographically smallest permutation of a multiset (a sequence containing potentially duplicate elements).

## Problem Context

Given a multiset of `n` elements (represented, for example, by a frequency map or Counter) and a 1-based rank `k`, find the permutation that would appear at index `k` if all distinct permutations were sorted lexicographically.

This differs from the k-th permutation of *distinct* elements ([[kth_permutation_factorial.md]]) because the presence of duplicates changes how many permutations start with a given element.

## Algorithmic Steps

1.  **Preprocessing:**
    *   Determine the frequency map (counts) of each distinct element in the multiset. Let the distinct sorted elements be `e1, e2, ..., em`.
    *   Calculate the total number of elements `n`.
    *   Precompute factorials up to `n!` (required by the permutation count helper).
    *   Calculate the total number of distinct permutations `total_perms` using the multiset permutation count formula. See [[../mathematical_concepts/combinatorics/multiset_permutation_count.md]].
    *   **Optimization Note:** For large N, calculating the exact `total_perms` might be too slow or overflow. It's better to use the [[../techniques/combinatorics/capped_multinomial.md]] technique with `limit = k` for the initial check: `capped_perms = multinomial_capped(n, counts, k)`. If `capped_perms < k`, then the actual `total_perms` must also be less than `k`.
    *   If `k > total_perms` (or `capped_perms < k`) or `k < 1`, the k-th permutation does not exist (return error, empty list, or handle as appropriate).
    *   Convert `k` to be 0-based: `k = k - 1`. (Note: If using capped approach, adjust `k` to `k-1` *after* the initial check, or use `limit = k-1` in the capped functions if `k` represents 0-based rank internally).

2.  **Iterative Construction:** Construct the permutation element by element from left to right (index `i` from 0 to `n-1`).
    *   Let `remaining_length = n - 1 - i` (length of the suffix to be formed).
    *   Iterate through the distinct available element types `c` in *sorted order* (e.g., 'a' through 'z').
    *   For each element type `c` that has a count greater than 0 (`counts[c] > 0`):
        *   **Calculate permutations starting with `c`:** Temporarily decrement `counts[c]` by 1.
        *   **TLE Risk:** Calculating `perms_starting_with_c = count_multiset_permutations(remaining_length, counts, precomputed_factorials)` directly involves large integer division and is often the bottleneck leading to TLE.
        *   **Optimization (Recommended):** Instead, use the capped calculation: `num_perms = multinomial_capped(remaining_length, [list of remaining counts], k)`. See [[../techniques/combinatorics/capped_multinomial.md]].
        *   Increment `counts[c]` back by 1 (restore the state for the next iteration).
        *   **Decision (using capped approach):**
            *   If `k <= num_perms`: This means the actual number of permutations starting with `c` is at least `k`. Since `num_perms` calculation stopped at `k+1` or returned the exact value `<=k`, this comparison is correct. `c` is the correct character.
                *   Append `c` to the result permutation.
                *   Permanently decrement `counts[c]` by 1.
                *   Break the inner loop and proceed to the next position `i+1`.
            *   If `k > num_perms`: This means the actual number of permutations starting with `c` is exactly `num_perms` (because the calculation was capped by `k`, and `k` was larger). Subtract this block: `k -= num_perms`.
                *   Continue the inner loop to the next element type `c'`.

3.  **Termination:** After `n` iterations (or when `i` reaches `n`), the result contains the k-th permutation.

## Complexity Analysis

*   **Time (Original):** O(N*M + P), where M is alphabet size. The inner `count_multiset_permutations` call takes O(M) assuming precomputed factorials, leading to O(L * M^2) = O(N * M^2) dominated by large integer division/multiplication.
*   **Time (Optimized with Capped Calculation):** O(N * M * k_iter_avg), where `k_iter_avg` is the average number of iterations performed within `nCr_capped` before the limit `k` is reached or the calculation completes. In the best case (limit hit early), this is much faster. In the worst case (limit `k` is large, close to actual permutation counts), it might approach the original complexity, but avoids the slowest large divisions. It's practically much faster and avoids TLE in many cases.
*   **Time (Optimized with Iterative Updates):** O(N*M). This advanced technique uses iterative updates for permutation counts and identifies fixed prefixes, often achieving the best practical performance. See [[../../optimizations/combinatorics/kth_permutation_iterative_update.md]].
*   **Space:** O(N + M) for factorials, counts dictionary, and the result.

## Use Cases

*   Problems requiring finding a specific ranked permutation when duplicates are allowed (e.g., LeetCode 3518 "Smallest Palindromic Rearrangement II" which reduces to this after handling the palindrome structure).
*   Generating permutations in lexicographical order without storing all of them.

## Implementation (Python Example)

```python
import math
from collections import Counter

# Assumes existence of factorials array and count_multiset_permutations function
# from [[../mathematical_concepts/combinatorics/multiset_permutation_count.md]]

# Example precomputation (should match the other file)
MAX_N = 5000 # Adjust as needed
factorials = [1] * (MAX_N + 1)
for i in range(2, MAX_N + 1):
    factorials[i] = factorials[i - 1] * i

def count_multiset_permutations(n: int, counts: dict, precomputed_factorials: list) -> int:
    # --- [Implementation from multiset_permutation_count.md] --- 
    if n < 0: return 0
    if n >= len(precomputed_factorials): 
        # For brevity, assume n is within bounds or handle error/dynamic calc
        try: numerator = math.factorial(n)
        except ValueError: return float('inf')
    else: numerator = precomputed_factorials[n]
    denominator = 1
    for count in counts.values():
        if count < 0: return 0
        if count >= len(precomputed_factorials):
            try: denominator *= math.factorial(count)
            except ValueError: return float('inf')
        elif count > 0: denominator *= precomputed_factorials[count]
        if denominator == 0: return float('inf') 
    if denominator == 0: return float('inf')
    return numerator // denominator
    # --- [End of Implementation] ---

def get_kth_multiset_permutation(initial_counts: dict, k: int, precomputed_factorials: list) -> list:
    """
    Finds the k-th lexicographical permutation of a multiset.

    Args:
        initial_counts: Counter or dict representing the multiset frequencies.
        k: The 1-based rank of the desired permutation.
        precomputed_factorials: Precomputed factorials up to n.

    Returns:
        A list representing the k-th permutation, or an empty list if k is invalid.
    """
    counts = initial_counts.copy()
    n = sum(counts.values())
    
    # Check if k is valid
    total_perms = count_multiset_permutations(n, counts, precomputed_factorials)
    if not (1 <= k <= total_perms):
        return [] # k is out of range

    k -= 1 # Convert to 0-based index
    result = []
    distinct_elements_sorted = sorted(counts.keys())

    for i in range(n):
        remaining_length = n - 1 - i
        for char in distinct_elements_sorted:
            if counts[char] > 0:
                # Try placing char here
                counts[char] -= 1
                perms_with_char = count_multiset_permutations(remaining_length, counts, precomputed_factorials)
                counts[char] += 1 # Backtrack count

                if k < perms_with_char:
                    # This is the character for the current position
                    result.append(char)
                    counts[char] -= 1 # Use this character permanently
                    break # Move to the next position i+1
                else:
                    # Skip the block of permutations starting with char
                    k -= perms_with_char
            # If counts[char] is 0, skip this character type
            
    return result

# Example Usage:
multiset_counts = Counter({'a': 2, 'b': 1, 'c': 1}) # Multiset {a, a, b, c}
n_example = sum(multiset_counts.values()) # n = 4
total_p = count_multiset_permutations(n_example, multiset_counts, factorials) # Should be 12
print(f"Total permutations for {multiset_counts}: {total_p}")

for k_test in range(1, total_p + 2):
    perm = get_kth_multiset_permutation(multiset_counts, k_test, factorials)
    print(f"k={k_test}: {perm}")

# Expected Output (k=1 to 12):
# k=1: ['a', 'a', 'b', 'c']
# k=2: ['a', 'a', 'c', 'b']
# k=3: ['a', 'b', 'a', 'c']
# k=4: ['a', 'b', 'c', 'a']
# k=5: ['a', 'c', 'a', 'b']
# k=6: ['a', 'c', 'b', 'a']
# k=7: ['b', 'a', 'a', 'c']
# k=8: ['b', 'a', 'c', 'a']
# k=9: ['b', 'c', 'a', 'a']
# k=10: ['c', 'a', 'a', 'b']
# k=11: ['c', 'a', 'b', 'a']
# k=12: ['c', 'b', 'a', 'a']
# k=13: [] (invalid k)

```

## Potential Pitfalls

*   **Off-by-one errors:** Handling 0-based vs 1-based `k` correctly, especially when using the capped calculation limit.
*   **Efficiency:** The **non-optimized** repeated calculation of multiset permutations is the primary cause of TLE. **Using the capped calculation technique ([[../techniques/combinatorics/capped_multinomial.md]]) is crucial for performance.** Even faster performance might be achievable using the [[../../optimizations/combinatorics/kth_permutation_iterative_update.md]] method.
*   **State Management:** Correctly decrementing counts when calculating `perms_starting_with_c` and restoring them (backtracking) is crucial before trying the next character.
*   **Large Numbers:** Intermediate permutation counts can exceed standard integer limits, but Python handles this. The capped calculation avoids the performance penalty associated with extremely large numbers.
