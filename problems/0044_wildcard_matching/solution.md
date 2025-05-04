# LeetCode 44: Wildcard Matching - Solution Explanation

## Problem Summary

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for:
*   `?`: Matches any single character.
*   `*`: Matches any sequence of characters (including the empty sequence).

The matching must cover the entire input string (not partial).

## Algorithmic Approach: Dynamic Programming

This problem is solved using a standard 2D Dynamic Programming approach, similar to regular expression matching but with simpler rules for `*`.

The core idea is to build a table `dp[i][j]` representing whether the first `i` characters of `s` match the first `j` characters of `p`.

## Logic Explanation

The detailed DP state, transitions, and base cases are described in the Knowledge Base algorithm document:

*   **Reference:** `[[../document/algorithms/dynamic_programming/string/wildcard_matching.md]]`

Here is a summary of the logic matching the code:

1.  **State:** `dp[i][j]` = True if `s[:i]` matches `p[:j]`, False otherwise.
2.  **Initialization:**
    *   `dp[0][0] = True` (empty matches empty).
    *   `dp[0][j]` (pattern `p` matching empty string `s`): True only if `p[:j]` consists of only `*`. Calculate iteratively: `dp[0][j] = dp[0][j-1]` if `p[j-1] == '*'`, else `False`.
    *   `dp[i][0] = False` for `i > 0` (empty pattern cannot match non-empty string).
3.  **Transitions (for `i > 0, j > 0`):**
    *   **Case 1: `p[j-1]` == `s[i-1]` or `p[j-1] == '?'`:** Match depends on previous state: `dp[i][j] = dp[i-1][j-1]`.
    *   **Case 2: `p[j-1] == '*'`:**
        *   `*` matches empty sequence: `dp[i][j-1]`
        *   `*` matches `s[i-1]`: `dp[i-1][j]`
        *   Combine: `dp[i][j] = dp[i][j-1] or dp[i-1][j]`.
    *   **Case 3: Mismatch:** `dp[i][j] = False`.
4.  **Result:** `dp[len(s)][len(p)]`.

## Knowledge Base References

*   **Core Algorithm:** `[[../document/algorithms/dynamic_programming/string/wildcard_matching.md]]` (Details the specific DP approach for this problem).
*   **General Paradigm:** `[[../document/algorithms/dynamic_programming/dynamic_programming.md]]`

## Complexity Analysis

*   **Time Complexity:** O(M * N), where M is the length of `s` and N is the length of `p`.
*   **Space Complexity:** O(M * N). Can be optimized to O(N) by storing only the previous row of the DP table. 