## Problem Summary

Given an input string `s` and a pattern `p` containing lowercase letters, `'?'` (matches any single character), and `'*'` (matches any sequence of characters, including empty), determine if the pattern `p` matches the *entire* string `s`.

## Algorithmic Approach

The problem is solved using dynamic programming.

We define `dp[i][j]` as a boolean value indicating whether the first `i` characters of `s` (i.e., `s[:i]`) match the first `j` characters of `p` (i.e., `p[:j]`). The goal is to compute `dp[len(s)][len(p)]`.

The DP table has dimensions `(len(s) + 1) x (len(p) + 1)`.

**Base Cases:**

1.  `dp[0][0] = True`: An empty string matches an empty pattern.
2.  `dp[0][j]`: Represents matching an empty string `s` with the pattern `p[:j]`. This is only possible if `p[:j]` consists solely of `'*'` characters. So, `dp[0][j] = True` if `p[j-1] == '*'` and `dp[0][j-1] == True`.

**Transitions:**

We fill the table iteratively. For `dp[i][j]`, consider `s_char = s[i-1]` and `p_char = p[j-1]`:

1.  **Exact Match or `?`:** If `p_char == s_char` or `p_char == '?'`, the current characters match. The result depends on whether the preceding substrings matched: `dp[i][j] = dp[i-1][j-1]`.

2.  **`*` Character:** If `p_char == '*'`, the `*` can either:
    *   Match an empty sequence: In this case, we effectively ignore the `*` and check if `s[:i]` matches `p[:j-1]`. This corresponds to `dp[i][j-1]`.
    *   Match one or more characters: In this case, the `*` matches the current character `s_char`, and we need to check if the remaining pattern `p[:j]` (including the `*`) matches the preceding string `s[:i-1]`. This corresponds to `dp[i-1][j]`.
    Since either case leads to a match, `dp[i][j] = dp[i][j-1] or dp[i-1][j]`.

3.  **Mismatch:** If none of the above conditions are met (i.e., `p_char` is a letter different from `s_char`), then `dp[i][j] = False`.

**Final Result:**

The final answer is stored in `dp[len(s)][len(p)]`.

## Knowledge Base References

This dynamic programming approach is closely related to the one used for Regular Expression Matching, documented in `document/algorithms/dynamic_programming/regex_matching_dp.md`. The key difference is the simpler transition logic for the wildcard `'*'` compared to the regex `'*'` (which depends on the preceding character).

## Complexity Analysis

*   **Time Complexity:** O(m * n), where `m = len(s)` and `n = len(p)`. We fill each cell of the `(m+1) x (n+1)` DP table once, and each transition takes O(1) time.
*   **Space Complexity:** O(m * n) for the DP table. 