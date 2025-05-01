# LeetCode 5: Longest Palindromic Substring - Solution Explanation

## Problem Summary

Given a string `s`, return the longest palindromic substring in `s`.

## Algorithmic Approach

This problem is commonly solved using the **Expand Around Center** pattern. The core idea is that any palindrome has a center. This center can be a single character (for odd-length palindromes like "aba") or the space between two characters (for even-length palindromes like "abba").

Instead of checking every possible substring (which would be O(N^2) or O(N^3)), we can iterate through all `2N - 1` potential centers (N single characters and N-1 spaces between characters) and expand outwards from each center to find the longest palindrome associated with it. We keep track of the longest palindrome found across all centers.

## Logic Explanation

1.  **Initialization:**
    *   Get the length `n` of the string `s`.
    *   Handle the base case: If `n < 2`, the string itself is the longest palindrome.
    *   Initialize `longest_start = 0` and `max_len = 1` to track the start index and length of the longest palindrome found so far (a single character is the minimum). 
2.  **Helper Function `expand_around_center(left, right)`:**
    *   This function takes the initial `left` and `right` pointers defining the center.
    *   It expands outwards (`left--`, `right++`) as long as `left` and `right` are within the string bounds and the characters `s[left]` and `s[right]` are equal.
    *   After the loop stops, the actual palindrome is the substring between `left + 1` and `right - 1` (inclusive).
    *   The function returns the `start` index (`left + 1`) and the `length` (`right - (left + 1)`) of the palindrome found for that center.
3.  **Iteration through Centers:**
    *   Loop through each index `i` from `0` to `n-1`.
    *   For each `i`:
        *   **Odd Length:** Call `expand_around_center(i, i)` to find the longest palindrome centered at `s[i]`. If its length (`len1`) is greater than `max_len`, update `max_len` and `longest_start`.
        *   **Even Length:** Call `expand_around_center(i, i + 1)` to find the longest palindrome centered between `s[i]` and `s[i+1]`. If its length (`len2`) is greater than `max_len`, update `max_len` and `longest_start`.
4.  **Return Result:** After checking all centers, the longest palindromic substring is `s[longest_start : longest_start + max_len]`.

## Knowledge Base References

*   **Expand Around Center Pattern:** The solution directly implements this pattern. The algorithm, including the concept of odd/even centers and the helper function, is detailed in `document/patterns/expand_around_center.md`.

## Complexity Analysis

*   **Time Complexity:** O(N^2). There are `2N - 1` potential centers. Expanding from each center can take up to O(N) time in the worst case (e.g., a string like "aaaaa").
*   **Space Complexity:** O(1). We only use a few variables to store the start index, max length, and pointers during expansion. 