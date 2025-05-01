## Problem Summary

LeetCode 132: Palindrome Partitioning II asks for the minimum number of cuts needed to partition a given string `s` such that all substrings in the partition are palindromes.

## Algorithmic Approach

This problem can be solved efficiently using dynamic programming.
The core idea is to find the minimum cuts for progressively larger prefixes of the string.

1.  **Palindrome Precomputation:**
    *   First, we precompute whether any substring `s[j...i]` is a palindrome.
    *   We use a 2D DP table `is_pal[j][i]`, where `is_pal[j][i]` is `True` if the substring from index `j` to `i` (inclusive) is a palindrome, and `False` otherwise.
    *   This table is filled in O(n^2) time using the recurrence:
        `is_pal[j][i] = (s[j] == s[i]) and (i - j < 2 or is_pal[j+1][i-1])`
    *   This approach is a standard way to check for all palindromic substrings. See related concept: `document/patterns/expand_around_center.md` (though we used DP here). A dedicated KB entry could be `document/algorithms/string/palindrome_checking_dp.md`.

2.  **Minimum Cuts Calculation:**
    *   We use a 1D DP array `cuts[i]` to store the minimum number of cuts needed for the prefix `s[0...i-1]` (length `i`). The size of this array is `n+1`.
    *   The base case is `cuts[0] = -1`, representing zero cuts for an empty prefix, which simplifies the recurrence.
    *   We initialize `cuts[i] = i - 1` for `i > 0`. This represents the worst-case scenario where we cut after every single character.
    *   We iterate `i` from 1 to `n` (representing the end of the prefix `s[0...i-1]`):
        *   For each `i`, we iterate through all possible start indices `j` (from 0 to `i-1`) of the *last* palindrome in an optimal partition ending at `i-1`.
        *   If the substring `s[j...i-1]` is a palindrome (checked using the precomputed `is_pal[j][i-1]` table), it means we can potentially form a partition ending with this palindrome.
        *   The number of cuts for this partition would be the minimum cuts needed for the prefix `s[0...j-1]` (which is `cuts[j]`) plus one cut before `s[j...i-1]`. So, `cuts[j] + 1`.
        *   We update `cuts[i]` to be the minimum of its current value and `cuts[j] + 1`:
            `cuts[i] = min(cuts[i], cuts[j] + 1)`
    *   The final answer is `cuts[n]`, which stores the minimum cuts needed for the entire string `s[0...n-1]`.
    *   Watch out for potential `document/common_mistakes/off_by_one_errors.md` when handling indices `i`, `j`, and the DP table dimensions.

## Complexity Analysis

*   **Time Complexity:** O(n^2)
    *   Precomputing the `is_pal` table takes O(n^2).
    *   Calculating the `cuts` array involves nested loops, taking O(n^2).
    *   Total time is dominated by these steps: O(n^2).
*   **Space Complexity:** O(n^2)
    *   The `is_pal` table requires O(n^2) space.
    *   The `cuts` array requires O(n) space.
    *   Total space is dominated by the `is_pal` table: O(n^2). 