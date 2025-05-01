# LeetCode 132: Palindrome Partitioning II

## Problem Summary

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return the *minimum* cuts needed for a palindrome partitioning of `s`.

## Algorithmic Approach (Optimized DP)

This problem asks for the minimum number of cuts, which strongly suggests a Dynamic Programming approach.

1.  **DP State:** Let `dp[i]` be the minimum number of cuts required for the prefix of the string `s[0...i-1]`. Our goal is to find `dp[n]`, where `n` is the length of `s`.

2.  **Base Case:** `dp[0] = -1`. This represents the prefix before the first character (empty string), requiring 0 cuts. The -1 helps simplify the transition: `dp[l] + 1` correctly gives 0 cuts if `s[0...r]` is a palindrome (where `l=0`).

3.  **Initialization:** Initialize `dp[i] = i - 1` for `i > 0`. This represents the worst-case scenario where each character is its own partition, requiring `i-1` cuts for a prefix of length `i`.

4.  **Transitions & Palindrome Check (Optimized):**
    Instead of precomputing an O(N^2) space table for all palindromes, we integrate the palindrome check into the DP calculation using the **"Expand From Center" technique** (See `../../document/techniques/string/expand_from_center_palindrome.md`).

    Iterate through each possible center `i` from `0` to `n-1`:
    *   **Odd Length Palindromes:** Expand outwards from center `i` (`l=i, r=i`). For each palindrome `s[l...r]` found:
        *   We know `s[l...r]` is a palindrome. The minimum cuts needed to partition `s[0...r]` could potentially be improved by making the last cut before `l`. This means considering `1 + dp[l]` (1 cut after index `r` + minimum cuts for `s[0...l-1]`).
        *   Update `dp[r + 1] = min(dp[r + 1], dp[l] + 1)`.
    *   **Even Length Palindromes:** Expand outwards from center `i, i+1` (`l=i, r=i+1`). For each palindrome `s[l...r]` found:
        *   Similarly, update `dp[r + 1] = min(dp[r + 1], dp[l] + 1)`.

5.  **Result:** The final answer is `dp[n]`. This approach combines the DP state calculation with efficient on-the-fly palindrome checking.

## Knowledge Base References
*   **Algorithm Paradigm:** Dynamic Programming (See `../../document/algorithms/dynamic_programming/dynamic_programming.md`)
*   **Technique:** Expand From Center (Palindrome Checking) (See `../../document/techniques/string/expand_from_center_palindrome.md`)

## Complexity Analysis

*   **Time Complexity:** O(N^2).
    *   The outer loop iterates `N` times (centers `i`).
    *   The inner `while` loops (expanding from center) can iterate up to O(N) times in total across all centers. The palindrome check `s[l] == s[r]` is O(1).
*   **Space Complexity:** O(N).
    *   We only use the `dp` array of size `N+1`. 