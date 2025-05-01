# LeetCode 3: Longest Substring Without Repeating Characters - Solution Explanation

## Problem Summary

Given a string `s`, find the length of the longest substring without repeating characters.

## Algorithmic Approach

This problem is efficiently solved using the **Sliding Window** pattern with a variable-sized window. We use two pointers, `left` and `right`, to define the current window (substring) being examined. A set data structure is used to keep track of the characters currently within the window, allowing for O(1) average time complexity checks for duplicates.

## Logic Explanation

1.  **Initialization:**
    *   Initialize `char_set = set()` to store unique characters in the current window.
    *   Initialize `left = 0` as the starting index of the window.
    *   Initialize `max_length = 0` to store the maximum length found so far.
2.  **Iteration (Window Expansion):** Iterate through the string `s` with the `right` pointer from `0` to `len(s) - 1`.
3.  **Check for Duplicates (Window Shrinking):** For the character `s[right]`:
    *   Use a `while` loop: As long as `s[right]` is already present in `char_set`, it means we have found a repeating character. To maintain a valid window (substring without repeats), we must shrink the window from the left.
    *   Inside the `while` loop: Remove the character at the `left` pointer (`s[left]`) from `char_set` and increment `left`.
    *   This `while` loop continues until the character `s[right]` is no longer a duplicate within the `char_set` (i.e., the previous occurrence of `s[right]` has been removed from the window by advancing `left`).
4.  **Add Character:** After the `while` loop ensures `s[right]` is not a duplicate in the current window (`left` to `right`), add `s[right]` to `char_set`.
5.  **Update Max Length:** Calculate the length of the current valid window (`right - left + 1`) and update `max_length = max(max_length, right - left + 1)`.
6.  **Return Result:** After the `right` pointer has traversed the entire string, `max_length` will hold the length of the longest substring without repeating characters.

## Knowledge Base References

*   **Sliding Window Pattern:** The entire solution is a direct implementation of the variable-size sliding window technique. The general pattern and its application to this specific problem are detailed in `document/patterns/sliding_window.md`.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the string `s`. Although there is a nested `while` loop, each character is added to and removed from the `char_set` at most once. Both the `right` pointer and the `left` pointer traverse the string linearly.
*   **Space Complexity:** O(min(N, M)), where N is the length of the string and M is the size of the character set (e.g., 26 for lowercase English letters, 128 for ASCII). In the worst case, the `char_set` might store all unique characters present in the string, up to the size of the character set. 