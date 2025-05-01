# Expand Around Center Pattern

## Description

The Expand Around Center pattern is an efficient technique used primarily for finding the longest palindromic substring within a given string `s`. Instead of checking every possible substring (which can be O(n^3) or O(n^2) with DP), this pattern focuses on the property that palindromes are symmetric around their center.

A palindrome's center can be either a single character (for odd-length palindromes like "racecar") or the space between two identical characters (for even-length palindromes like "abba"). There are `n` potential single-character centers and `n-1` potential centers between characters, leading to `2n - 1` total potential centers to check.

## Algorithm

1.  Initialize variables to track the `start` index and `max_length` of the longest palindrome found so far. Often initialize `start = 0`, `max_length = 1` (assuming the string has at least one character, which itself is a palindrome).
2.  Iterate through each possible center index `i` from `0` to `n-1`, where `n` is the length of the string `s`.
3.  For each `i`, consider two cases for the center:
    a.  **Odd length:** The center is the character `s[i]`. Expand outwards from this center by checking `s[i-1]` vs `s[i+1]`, `s[i-2]` vs `s[i+2]`, and so on, as long as the characters match and the indices are within bounds. Calculate the length of the palindrome found.
    b.  **Even length:** The center is between `s[i]` and `s[i+1]`. Expand outwards by checking `s[i]` vs `s[i+1]`, `s[i-1]` vs `s[i+2]`, and so on, as long as the characters match and the indices are within bounds. Calculate the length of the palindrome found.
4.  Compare the lengths found in steps 3a and 3b with the current `max_length`. If a longer palindrome is found, update `max_length` and the corresponding `start` index.
5.  After iterating through all centers, the longest palindromic substring is `s[start : start + max_length]`.

## Helper Function

It's often convenient to implement a helper function, say `expand(left, right)`, that takes the initial left and right boundaries of the center, expands outwards while `s[left] == s[right]` and indices are valid, and returns the length (or start index and length) of the palindrome found centered there.

```python
def expand_around_center(s: str, left: int, right: int) -> int:
    """Expands outwards from center [left, right] and returns palindrome length."""
    l, r = left, right
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    # The length is r - l - 1
    # Example: if s="aba", l=-1, r=3 -> length = 3 - (-1) - 1 = 3
    # Example: if s="abba", l=-1, r=4 -> length = 4 - (-1) - 1 = 4
    return r - l - 1

# Main loop usage:
# for i in range(n):
#    len1 = expand_around_center(s, i, i)      # Odd length
#    len2 = expand_around_center(s, i, i + 1)  # Even length
#    max_len = max(max_len, len1, len2)
#    # (Update start index logic needed)
```

## Complexity

*   **Time Complexity:** O(n^2). There are `2n - 1` centers, and expanding from each center can take up to O(n) time in the worst case (e.g., a string of all the same characters).
*   **Space Complexity:** O(1). Only a few variables are needed to store the state (start index, max length).

## Use Cases

*   Finding the longest palindromic substring (LeetCode 5).
*   Counting all palindromic substrings (LeetCode 647). 