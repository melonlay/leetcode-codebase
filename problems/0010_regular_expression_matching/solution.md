# LeetCode 10: Regular Expression Matching - Solution Explanation

## Problem Summary

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` (matches any single character) and `'*'` (matches zero or more of the preceding element). The matching should cover the *entire* input string (not partial).

## Algorithmic Approach

This problem is a classic application of **Dynamic Programming**. We use a 2D DP table, `dp[i][j]`, where `dp[i][j]` stores a boolean value indicating whether the first `i` characters of the string `s` (i.e., `s[0...i-1]`) match the first `j` characters of the pattern `p` (i.e., `p[0...j-1]`).

The table size is `(m+1) x (n+1)`, where `m = len(s)` and `n = len(p)`, to handle empty string/pattern cases.

## Logic Explanation

1.  **Initialization:**
    *   Create the `(m+1) x (n+1)` DP table initialized to `False`.
    *   **Base Case 1:** `dp[0][0] = True` (an empty string matches an empty pattern).
    *   **Base Case 2 (Pattern Matching Empty String):** Fill the first row (`dp[0][j]`). A pattern can match an empty string only if it consists of `char*` sequences. Iterate `j` from 1 to `n`. If `p[j-1]` is `'*'`, it means the pattern up to `j` could potentially match an empty string if the pattern up to `j-2` (excluding the `char*`) also matched an empty string. So, if `p[j-1] == '*'`, set `dp[0][j] = dp[0][j-2]` (requires `j >= 2`).
2.  **Filling the DP Table:** Iterate through `i` from 1 to `m` and `j` from 1 to `n`:
    *   Get the current characters: `s_char = s[i-1]` and `p_char = p[j-1]`.
    *   **Case 1: Direct Match or `.`:** If `p_char == s_char` or `p_char == '.'`:
        The current characters match. The result depends solely on whether the prefixes `s[0...i-2]` and `p[0...j-2]` matched. Set `dp[i][j] = dp[i-1][j-1]`.
    *   **Case 2: `*` Character:** If `p_char == '*'`:
        Let `preceding_p_char = p[j-2]` (the character before `*`).
        There are two ways the `*` can result in a match:
        a.  **Zero Occurrences:** The `preceding_p_char*` sequence matches zero times. The result depends on whether `s[0...i-1]` matches the pattern *excluding* `preceding_p_char*` (i.e., `p[0...j-3]`). Check `dp[i][j-2]`.
        b.  **One or More Occurrences:** The `preceding_p_char*` sequence matches one or more times. This requires that the current string character `s_char` matches `preceding_p_char` (or `preceding_p_char == '.'`). If they match, the result depends on whether the pattern `p[0...j-1]` (including the `*`) matched the string *up to the previous character* `s[0...i-2]`. Check `dp[i-1][j]`.
        Set `dp[i][j]` to `True` if *either* the zero-occurrence condition (`dp[i][j-2]`) is true OR the one-or-more-occurrence condition (`match(s_char, preceding_p_char) and dp[i-1][j]`) is true.
    *   **Case 3: Mismatch:** If `p_char` is not `.` or `*` and `p_char != s_char`, then `dp[i][j]` remains `False`.
3.  **Return Result:** The final answer is `dp[m][n]`, indicating if the entire string `s` matches the entire pattern `p`.

## Knowledge Base References

*   **Dynamic Programming for Regex Matching:** The entire solution follows this DP approach. The state definition, base cases, and transition logic (especially for `.`, `*`, zero occurrences, and one-or-more occurrences) are detailed in `document/algorithms/dynamic_programming/regex_matching_dp.md`.
*   **Common Mistakes (Testing Regex):** When testing, misinterpreting regex semantics (like the meaning of `*`) can lead to incorrect expected values. See `document/common_mistakes/test_case_logic_errors.md` for examples.

## Complexity Analysis

*   **Time Complexity:** O(M * N), where M is the length of `s` and N is the length of `p`. Each cell in the DP table is computed once.
*   **Space Complexity:** O(M * N) for the DP table. 