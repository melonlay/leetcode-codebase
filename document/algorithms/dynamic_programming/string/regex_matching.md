# Algorithm: Regular Expression Matching (`.` and `*`)

## Description

This algorithm solves the regular expression matching problem (LeetCode 10) using dynamic programming. It determines if a string `s` matches a pattern `p` containing literal characters, `.` (matches any single character), and `*` (matches zero or more of the *preceding* element).

It applies the general **Dynamic Programming** paradigm using a 2D table structure. See `../dynamic_programming.md` for general DP concepts.

## Core Idea (Specifics)

*   `dp[i][j]` = `True` if `s[0...i-1]` matches `p[0...j-1]`.
*   Table size is `(len(s) + 1) x (len(p) + 1)`.

## Algorithm Steps (Focus on Transitions & Base Cases)

1.  **Initialization & Base Cases:**
    *   `dp[0][0] = True` (empty matches empty).
    *   First Row (`dp[0][j]`): Handles pattern `p` matching an empty string `s`. Requires checking `*`. `dp[0][j] = True` if `p[j-1] == '*'` and the pattern excluding the `x*` part (`p[0...j-3]`) also matches empty (`dp[0][j-2]`).
    *   First Column (`dp[i][0]`): An empty pattern cannot match a non-empty string. `dp[i][0] = False` for `i > 0`.

2.  **Transitions (Filling `dp[i][j]` for `i > 0, j > 0`):**
    *   Let `s_char = s[i-1]`, `p_char = p[j-1]`.
    *   **Direct Match/`.`:** If `p_char == s_char` or `p_char == '.'`, the match depends on the previous prefixes: `dp[i][j] = dp[i-1][j-1]`.
    *   **`*` Character:** If `p_char == '*'`, let `preceding_p_char = p[j-2]`. This `x*` combo can match:
        *   **Zero occurrences of `x`:** The match depends on the pattern *excluding* the `x*`. `dp[i][j] = dp[i][j-2]`.
        *   **One or more occurrences of `x`:** This requires the current `s_char` to match `x` (`s_char == preceding_p_char` or `preceding_p_char == '.'`). If it matches, the result depends on the string *excluding* `s_char` matching the *current* pattern (which still includes `x*`). `match_one_or_more = (match(s_char, preceding_p_char) and dp[i-1][j])`.
        *   Combine: `dp[i][j] = dp[i][j-2] or match_one_or_more`.
    *   **Mismatch:** If `p_char` is a literal and not `*` or `.` and doesn't match `s_char`, `dp[i][j] = False`.

3.  **Result:** `dp[len(s)][len(p)]`.

## Complexity

*   Time: O(m * n)
*   Space: O(m * n) (Can be optimized to O(n))

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
                    # Helper to check match
                    def match(sc, pc): return pc == '.' or pc == sc
                    
                    # Zero occurrences
                    zero_match = dp[i][j-2]
                    # One or more occurrences
                    one_or_more_match = False
                    if match(s_char, preceding_p_char):
                        one_or_more_match = dp[i-1][j] 
                    dp[i][j] = zero_match or one_or_more_match
                # else: dp[i][j] remains False (default)

        return dp[m][n]
```

## Common Pitfalls

*   Incorrect base case logic for `x*` matching an empty string (`dp[0][j] = dp[0][j-2]`).
*   Off-by-one indexing errors, especially with `p[j-2]`. See `../../../common_mistakes/off_by_one_errors.md`.
*   Mixing up the logic for `*` transitions (zero vs. one-or-more occurrences).

## Related Concepts
*   Dynamic Programming (General Paradigm) - See `../dynamic_programming.md`.
*   Difference from Wildcard `*`: Note the distinct behavior of `*` here compared to `wildcard_matching.md`. 