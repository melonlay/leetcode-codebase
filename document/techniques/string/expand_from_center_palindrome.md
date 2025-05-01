# Technique: Expand From Center (Palindrome Checking)

## Description

The "Expand From Center" technique is an efficient method to find all palindromic substrings within a given string `s` or check for palindromes centered at specific positions. It typically achieves this in O(N^2) time complexity while using only O(1) auxiliary space (excluding the space for storing the results if needed).

## Core Logic

The idea is to iterate through each possible center of a palindrome and expand outwards as long as the characters match.

There are `2N - 1` potential centers for palindromes in a string of length `N`:
1.  `N` centers corresponding to single characters (for odd-length palindromes like "aba").
2.  `N - 1` centers corresponding to the spaces between adjacent characters (for even-length palindromes like "abba").

The algorithm iterates through each of these `2N - 1` centers:

*   **Odd Length Palindromes:** For each index `i` from `0` to `N-1`, consider `i` as the center. Initialize `left = i`, `right = i`. While `left >= 0`, `right < N`, and `s[left] == s[right]`, the substring `s[left...right]` is a palindrome. Decrement `left` and increment `right` to expand.
*   **Even Length Palindromes:** For each index `i` from `0` to `N-2`, consider the space between `i` and `i+1` as the center. Initialize `left = i`, `right = i + 1`. While `left >= 0`, `right < N`, and `s[left] == s[right]`, the substring `s[left...right]` is a palindrome. Decrement `left` and increment `right` to expand.

## Complexity
*   **Time:** O(N^2). Each expansion from a center can take up to O(N) time, and there are O(N) centers.
*   **Space:** O(1) auxiliary space (if only checking or processing palindromes on the fly). If storing all found palindromes, space complexity depends on the number and length of palindromes found.

## Use Cases
*   **Longest Palindromic Substring (LeetCode 5):** Find the longest palindrome identified during expansion.
*   **Palindromic Substrings (LeetCode 647):** Count all palindromes identified during expansion.
*   **Optimizing DP Solutions:** Integrate the palindrome check directly into DP transitions to avoid large precomputation tables, as seen in Palindrome Partitioning II (LeetCode 132). See `../../algorithms/dynamic_programming/dynamic_programming.md` for discussion on DP space optimization.

## Implementation Notes
*   Be mindful of boundary conditions (`left >= 0` and `right < N`).
*   The two loops (odd and even centers) can often be combined or handled within a single loop iterating through the `2N - 1` potential centers. 