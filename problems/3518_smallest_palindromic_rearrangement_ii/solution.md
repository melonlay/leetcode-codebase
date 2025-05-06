# 3518. Smallest Palindromic Rearrangement II

## Problem Summary

Given a palindromic string `s` and an integer `k`, find the `k`-th lexicographically smallest string that is a rearrangement of `s` and is also a palindrome. If fewer than `k` such distinct rearrangements exist, return an empty string.

## Solution Approach

The key insight remains that the palindrome is determined by its first half (`H`).

1.  **Counts & Middle:** Determine counts for `H` (`total`) and the middle character.
2.  **K-th Permutation:** Find the k-th permutation of the multiset `total`.
3.  **Algorithm - Optimized (Iterative Update & Prefix ID):** Direct calculation or even capped `nCr` methods can TLE. The fastest approach uses iterative updates:
    *   **Phase 1 (Identify Fixed Prefix):** Iteratively calculate the total permutations (`perm`) of the multiset represented by `total`, processing characters conceptually from largest to smallest. Simultaneously track the counts (`cnt`) needed for this suffix. Stop when `perm >= k`. The characters *not* in `cnt` form a fixed prefix (`left_s`).
    *   **Phase 2 (Construct Suffix):** Iteratively build the remaining suffix character by character ('a' to 'z'). At each step, calculate the number of permutations starting with the candidate character `j` using the iterative formula: `p = perm * cnt[j] // remaining_length`. `perm` here is the total permutations for the *current* suffix subproblem. If `p >= k`, choose `j`, append it, update `perm = p`. If `p < k`, skip `j` and update `k -= p`.
    *   **Reference:** See [[../document/optimizations/combinatorics/kth_permutation_iterative_update.md]] for a detailed explanation of this technique.
4.  **Final Assembly:** Combine prefix, suffix, middle char, and reversed prefix+suffix.

## Complexity Analysis

*   **Time Complexity:** **O(N*M)**, where N is the length of s (~L = N/2 relevant), M is the alphabet size (26). Both phases involve loops related to L and M, and the core calculations inside are effectively O(1) using large integer multiplication/division (which is much faster than factorial calculations).
*   **Space Complexity:** O(N) primarily for storing counts and the result string.

## Knowledge Base References

*   [[../document/algorithms/combinatorics/kth_multiset_permutation.md]] (Base algorithm)
*   [[../document/optimizations/combinatorics/kth_permutation_iterative_update.md]] (The efficient optimization used)
*   [[../document/techniques/combinatorics/capped_multinomial.md]] (Alternative, but likely slower, optimization)
*   [[../document/techniques/combinatorics/capped_nCr.md]] 