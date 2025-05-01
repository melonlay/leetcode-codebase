# Algorithm: Wildcard Matching (`?` and `*`)

## Description

This algorithm solves the wildcard matching problem (LeetCode 44) using dynamic programming. It determines if a string `s` matches a pattern `p` containing literal characters, `?` (matches any single character), and `*` (matches any sequence of characters, including empty).

It applies the general **Dynamic Programming** paradigm using a 2D table structure. See `../dynamic_programming.md` for general DP concepts.

## Core Idea (Specifics)

*   `dp[i][j]` = `True` if `s[0...i-1]` matches `p[0...j-1]`.
*   Table size is `(len(s) + 1) x (len(p) + 1)`.

## Algorithm Steps (Focus on Transitions & Base Cases)

1.  **Initialization & Base Cases:**
    *   `dp[0][0] = True` (empty matches empty).
    *   First Row (`dp[0][j]`): Handles pattern `p` matching an empty string `s`. `dp[0][j] = True` only if `p[0...j-1]` consists solely of `*`. So, `dp[0][j] = dp[0][j-1]` if `p[j-1] == '*'`, otherwise `False` (and subsequent entries in the row remain `False`).
    *   First Column (`dp[i][0]`): An empty pattern cannot match a non-empty string. `dp[i][0] = False` for `i > 0`.

2.  **Transitions (Filling `dp[i][j]` for `i > 0, j > 0`):**
    *   Let `s_char = s[i-1]`, `p_char = p[j-1]`.
    *   **Match/`?`:** If `p_char == s_char` or `p_char == '?'`, the match depends on the previous prefixes: `dp[i][j] = dp[i-1][j-1]`.
    *   **`*` Character:** If `p_char == '*'`, it can match:
        *   **Zero characters:** The match depends on the pattern *excluding* the `*`. `dp[i][j] = dp[i][j-1]`.
        *   **One or more characters:** The `*` matches `s_char`. The match depends on the string *excluding* `s_char` matching the *current* pattern (including `*`). `dp[i][j] = dp[i-1][j]`.
        *   Combine: `dp[i][j] = dp[i][j-1] or dp[i-1][j]`.
    *   **Mismatch:** If none of the above, `dp[i][j] = False`.

3.  **Result:** `dp[len(s)][len(p)]`.

## Complexity

*   Time: O(m * n)
*   Space: O(m * n) (Can be optimized to O(n))

## Example Application: LeetCode 44 - Wildcard Matching

See `problems/0044_wildcard_matching/solution.py` for a concrete implementation.

## Python Code Snippet

```python
# Snippet illustrating the core DP logic for Wildcard Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Base cases for pattern matching empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                 break # Optimization

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = s[i - 1]
                p_char = p[j - 1]

                if p_char == s_char or p_char == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p_char == '*':
                    # '*' matches empty sequence OR '*' matches current char s_char
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # else: dp[i][j] remains False

        return dp[m][n]
```

## Common Pitfalls

*   Incorrect base case logic for `*` matching an empty string.
*   Off-by-one indexing errors. See `../../../common_mistakes/off_by_one_errors.md`.
*   Mixing up the logic for `*` transitions (`dp[i][j-1]` vs `dp[i-1][j]`).

## Related Concepts
*   Dynamic Programming (General Paradigm) - See `../dynamic_programming.md`.
*   Difference from Regex `*`: Note the distinct behavior of `*` here compared to `regex_matching.md`. 