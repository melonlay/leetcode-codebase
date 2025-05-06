# Optimization: K-th Multiset Permutation via Iterative Updates and Prefix Identification

## Concept

Finding the k-th lexicographical permutation of a multiset often involves repeatedly calculating the number of permutations starting with a given prefix. Standard methods, whether using the direct multinomial formula (`n! / (n1!...nk!)`) or the product-of-capped-`nCr` approach ([[../techniques/combinatorics/capped_multinomial.md]]), can still lead to Time Limit Exceeded (TLE) on large inputs due to the overhead of large integer arithmetic or repeated calculations.

This advanced optimization technique significantly speeds up the process by:

1.  **Iteratively Calculating Permutation Counts:** Using the multiplicative relationship `NewPerms = OldPerms * k / count_of_kth_element_added` to update permutation counts incrementally.
2.  **Identifying a Fixed Prefix:** Determining the longest prefix common to the target k-th permutation and the overall lexicographically *largest* permutation, reducing the number of characters that need to be determined step-by-step.
3.  **Efficient Suffix Construction:** Using the iterative update rule to calculate the size of permutation blocks within the remaining suffix construction phase.

## Algorithmic Steps

The approach typically involves two phases:

**Phase 1: Calculate Permutation Count Iteratively & Find Fixed Prefix**

1.  Initialize `perm = 1`, `counts_so_far = {0}` (representing counts for an empty set), `length_so_far = 0`.
2.  Iterate through potential elements **in reverse lexicographical order** (or conceptually, building the counts for the largest possible permutation suffix).
3.  For each element added (maintaining its count `c` in `counts_so_far`):
    *   Update the total number of permutations for the set considered so far using the iterative rule: `perm = perm * length_so_far // c` (where `length_so_far` increments with each element conceptually added).
    *   **Early Exit:** Stop this phase as soon as `perm >= k`.
4.  **Result of Phase 1:**
    *   The final `perm` value (if loop completed without reaching `k`) indicates the total number of permutations, confirming if `k` is valid.
    *   The `counts_so_far` represents the counts of characters forming the largest suffix considered.
    *   The characters *not* included in `counts_so_far` (i.e., `total_counts[char] - counts_so_far[char]`) form the **fixed prefix** of the k-th permutation.
    *   Let the length of this fixed prefix be `len_prefix`.
    *   Let `k` remain the rank relative to the start of the suffix.
    *   Let `perm` be the total number of permutations for the suffix represented by `counts_so_far`.

**Phase 2: Construct the Suffix Iteratively**

1.  Initialize the result with the fixed prefix found in Phase 1.
2.  Let `remaining_counts = counts_so_far` and `remaining_length` be the length of the suffix to construct.
3.  Iterate from `i = len_prefix` to `total_length - 1`:
    *   Iterate through candidate characters `char` **in lexicographical order** ('a' to 'z').
    *   If `remaining_counts[char] > 0`:
        *   Calculate the number of permutations of the suffix *starting with* `char`: `perms_with_char = perm * remaining_counts[char] // remaining_length`.
        *   **Decision:**
            *   If `perms_with_char >= k`: This `char` is the next character in the suffix. Append it to the result. Update `perm = perms_with_char` (this is the total permutations for the *next* smaller suffix). Decrement `remaining_counts[char]`. Decrement `remaining_length`. Break the inner character loop.
            *   If `perms_with_char < k`: This character is not the one. Subtract the skipped block: `k -= perms_with_char`. Continue to the next character.

## Benefits

*   **Performance:** Significantly faster than previous methods. Avoids most large factorial/division calculations by using iterative multiplicative updates.
*   **Prefix Optimization:** Reduces the length of the sequence that needs explicit step-by-step construction.

## Complexity

*   **Time Complexity:** O(N + L*M) = **O(N*M)**, where `N` is the total length, `L=N/2` is the half-length, and `M` is the alphabet size. Phase 1 takes roughly O(L) or O(L*M) depending on implementation details. Phase 2 iterates `L` positions, and the inner loop runs `M` times with O(1) updates. The large integer multiplications/divisions involve numbers related to `perm` (up to `k`) and `length`, which is much faster than dealing with factorials.
*   **Space Complexity:** O(M) or O(N) for counts and the result string.

## Implementation Notes (Example: LC 3518 Code Structure)

The provided fast solution for LC 3518 implements this slightly differently but captures the core ideas:

*   **Phase 1 (`while i >= 0 and perm < k`):** Calculates total `perm` iteratively while determining `cnt` (counts for the largest relevant suffix). `i` tracks the length processed from the end.
*   **Prefix Calculation:** Implicitly calculates the prefix `left_s` by taking `total[ch] - cnt[ch]` after Phase 1.
*   **Phase 2 (`for i in range(i + 1, m)`):** Constructs the suffix using the iterative update `p = perm * cnt[j] // (m - i)`, where `perm` is the total permutations for the current suffix subproblem.

## Use Cases

*   Finding the k-th lexicographical permutation of large multisets where standard methods TLE.

## Relation to Other Concepts

*   Builds upon the standard k-th multiset permutation algorithm [[../algorithms/combinatorics/kth_multiset_permutation.md]].
*   Uses an iterative formula related to multinomial coefficients [[../mathematical_concepts/combinatorics/multiset_permutation_count.md]] but avoids direct calculation. 