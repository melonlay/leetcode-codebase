# Technique: Expand From Center

## Description

The "Expand From Center" technique is an efficient method often used to find properties related to symmetric subsequences (like palindromes) within a given sequence `s`. It iterates through all possible centers of symmetry and expands outwards as long as a certain condition (e.g., matching characters for palindromes) holds.

This approach typically achieves O(N^2) time complexity while using only O(1) auxiliary space (excluding space for results).

## Core Logic

Iterate through each possible center of symmetry and expand outwards.

There are `2N - 1` potential centers in a sequence of length `N`:
1.  `N` centers corresponding to single elements (index `i`).
2.  `N - 1` centers corresponding to the spaces between adjacent elements (between indices `i` and `i+1`).

The algorithm iterates through each of these `2N - 1` centers:

*   **Center at element `i` (potential odd length):** Initialize `left = i`, `right = i`. While `left >= 0`, `right < N`, and the expansion condition holds (e.g., `s[left] == s[right]` for palindromes), process the valid range `s[left...right]`. Decrement `left` and increment `right`.
*   **Center between elements `i` and `i+1` (potential even length):** Initialize `left = i`, `right = i + 1`. While `left >= 0`, `right < N`, and the expansion condition holds (e.g., `s[left] == s[right]` for palindromes), process the valid range `s[left...right]`. Decrement `left` and increment `right`.

## Primary Application: Palindromes

This technique is most famously used for finding palindromic substrings:

*   **Longest Palindromic Substring (LeetCode 5):** Keep track of the longest palindrome found during expansion.
*   **Palindromic Substrings (LeetCode 647):** Count every palindrome identified during expansion.
*   **Integration with DP:** Check for palindromes within DP transitions (e.g., Palindrome Partitioning II, LeetCode 132) to potentially avoid precomputing a full palindrome table. See `../../algorithms/dynamic_programming/dynamic_programming.md`.

## Complexity
*   **Time:** O(N^2). Each expansion from a center can take up to O(N) time, and there are O(N) centers.
*   **Space:** O(1) auxiliary space (if only checking/processing on the fly). If storing results, space depends on the output.

## Implementation Notes
*   Be mindful of boundary conditions (`left >= 0` and `right < N`).
*   The two loops (odd and even centers) can often be combined or handled within a single loop iterating through the `2N - 1` potential centers using index mapping.

## Related Concepts
*   String/Sequence Manipulation
*   Palindromes
*   [[patterns/expand_around_center.md](../../patterns/expand_around_center.md)] (This pattern document might generalize this further) 