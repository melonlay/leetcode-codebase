# Algorithm: Palindrome Substring Checking

## Description

This algorithm precomputes a table using dynamic programming to efficiently check if any substring `s[j...i]` of a given string `s` is a palindrome. It's useful when multiple palindrome checks are needed, like in palindrome partitioning or finding the longest palindromic substring.

It applies the general **Dynamic Programming** paradigm using a 2D table structure. See `../dynamic_programming.md` for general DP concepts.

## Core Idea (Specifics)

*   `is_pal[j][i]` = `True` if substring `s[j...i]` (inclusive) is a palindrome.
*   Table size is `n x n`.

## Algorithm Steps (Focus on Transitions & Base Cases)

1.  **Initialization:** Create `is_pal` table (size `n x n`), initialize to `False`.

2.  **Base Cases & Transitions (Iterating by Length):**
    *   **Length 1:** `is_pal[i][i] = True` for all `i`.
    *   **Length 2:** `is_pal[i][i+1] = (s[i] == s[i+1])`.
    *   **Length 3 to n:** For length `l` starting at `j` (ending at `i = j + l - 1`):
        `is_pal[j][i] = (s[j] == s[i]) and is_pal[j+1][i-1]`
        This relies on the result for the shorter, inner substring being computed already.

3.  **Result:** The table `is_pal` allows O(1) checks for any substring `s[j...i]`.

## Implementation Order

Crucial to compute shorter lengths before longer ones. Iterating by length `l` from 1 to `n`, and then by start index `j`, ensures this.

```python
# Example Implementation
def precompute_palindromes(s: str) -> list[list[bool]]:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]

    # Iterate by length is often intuitive
    for length in range(1, n + 1):
        for j in range(n - length + 1):
            i = j + length - 1
            if length == 1:
                is_pal[j][i] = True
            elif length == 2:
                is_pal[j][i] = (s[j] == s[i])
            else:
                # Rely on previously computed smaller lengths
                is_pal[j][i] = (s[j] == s[i]) and is_pal[j + 1][i - 1]
    return is_pal
```

## Complexity

*   Time: O(n^2)
*   Space: O(n^2)

## Use Cases

*   LeetCode 5: Longest Palindromic Substring
*   LeetCode 131: Palindrome Partitioning
*   LeetCode 132: Palindrome Partitioning II

## Related Concepts

*   Dynamic Programming (General Paradigm) - See `../dynamic_programming.md`.
*   Alternative Pattern: `../../patterns/expand_around_center.md`. 