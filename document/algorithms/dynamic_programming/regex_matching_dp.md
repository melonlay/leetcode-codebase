# Algorithm: Dynamic Programming for Regular Expression Matching (`.` and `*`)

## Description

This dynamic programming approach solves the problem of matching a string `s` against a regular expression pattern `p` that supports the wildcard characters `.` (matches any single character) and `*` (matches zero or more of the preceding element). The goal is to determine if the pattern `p` matches the *entire* string `s`.

## Core Idea

We use a 2D DP table, `dp[i][j]`, which stores a boolean value indicating whether the first `i` characters of the string `s` match the first `j` characters of the pattern `p`.

*   `dp[i][j] = True` if `s[0...i-1]` matches `p[0...j-1]`.
*   `dp[i][j] = False` otherwise.

The table size is `(len(s) + 1) x (len(p) + 1)` to accommodate base cases involving empty strings/patterns.

## Algorithm Steps

1.  **Initialization:**
    *   Create the DP table `dp` of size `(m+1) x (n+1)` initialized to `False`, where `m = len(s)` and `n = len(p)`.
    *   **Base Case 1:** `dp[0][0] = True`. An empty string matches an empty pattern.
    *   **Base Case 2 (Pattern matching empty string):** Initialize the first row (`dp[0][j]`). A pattern `p` can match an empty string `s` only if it consists of characters followed by `*`. Iterate `j` from 1 to `n`. If `p[j-1] == '*'`, then `dp[0][j]` depends on whether the pattern excluding the last two characters (`p[0...j-3]`) matched the empty string. So, `dp[0][j] = dp[0][j-2]` (requires `j >= 2`).

2.  **Filling the Table:** Iterate through the table row by row (`i` from 1 to `m`) and column by column (`j` from 1 to `n`). For each cell `dp[i][j]`, consider `s_char = s[i-1]` and `p_char = p[j-1]`:

    *   **Case 1: Direct Match or `.`**
        If `p_char == s_char` or `p_char == '.'`: The current characters match. The result depends on whether the preceding substrings matched: `dp[i][j] = dp[i-1][j-1]`.

    *   **Case 2: `*` Character**
        If `p_char == '*'`: This `*` refers to the preceding pattern character `preceding_p_char = p[j-2]` (guaranteed to exist by problem constraints).
        There are two possibilities for the `*`:
        a.  **Zero Occurrences:** The `*` matches zero occurrences of `preceding_p_char`. In this case, the match depends on whether `s[0...i-1]` matches the pattern excluding the `preceding_p_char` and `*` (i.e., `p[0...j-3]`). So, check `dp[i][j-2]`.
        b.  **One or More Occurrences:** The `*` matches one or more occurrences of `preceding_p_char`. This is only possible if the current string character `s_char` matches `preceding_p_char` (i.e., `s_char == preceding_p_char` or `preceding_p_char == '.'`). If they match, it means `s_char` is consumed by the `*`. The result then depends on whether the string *up to the previous character* (`s[0...i-2]`) matched the *current* pattern (`p[0...j-1]`). So, check `dp[i-1][j]`.

        `dp[i][j]` is `True` if *either* the zero-occurrence case (`dp[i][j-2]`) or the one-or-more-occurrence case (`(match(s_char, preceding_p_char) and dp[i-1][j])`) is `True`.

    *   **Case 3: Mismatch**
        If `p_char` is not `.` or `*`, and `p_char != s_char`: The characters don't match, so `dp[i][j] = False`.

3.  **Result:** The final answer is `dp[m][n]`, indicating whether the entire string `s` matches the entire pattern `p`.

## Complexity

*   **Time Complexity:** O(m * n), where `m` is the length of `s` and `n` is the length of `p`. We fill each cell of the DP table once.
*   **Space Complexity:** O(m * n) for the DP table.

## Example Application: LeetCode 10 - Regular Expression Matching

See `problems/10_regular_expression_matching/solution.py` for a concrete implementation.

```python
# Snippet illustrating the core DP logic
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j-1] == '*':
                 if j >= 2: dp[0][j] = dp[0][j-2] # Handles a*, a*b*, etc. for empty string

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = s[i-1]
                p_char = p[j-1]

                if p_char == '.' or p_char == s_char:
                    dp[i][j] = dp[i-1][j-1]
                elif p_char == '*':
                    preceding_p_char = p[j-2]
                    # Zero occurrences
                    zero_match = dp[i][j-2]
                    # One or more occurrences
                    one_or_more_match = False
                    if preceding_p_char == '.' or preceding_p_char == s_char:
                        one_or_more_match = dp[i-1][j] 
                    dp[i][j] = zero_match or one_or_more_match
                # else: dp[i][j] remains False (default)

        return dp[m][n]
```

## Common Pitfalls

*   Incorrect base case handling, especially for patterns matching empty strings (`a*`, `.*`, `a*b*`).
*   Off-by-one errors when accessing string/pattern characters (`s[i-1]`, `p[j-1]`, `p[j-2]`) relative to DP indices (`i`, `j`).
*   Incorrect logic for the `*` case, forgetting either the zero-occurrence or the one-or-more-occurrence possibility, or mixing up the indices (`dp[i][j-2]` vs `dp[i-1][j]`). 