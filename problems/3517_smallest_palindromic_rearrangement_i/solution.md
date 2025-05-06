# 3517. Smallest Palindromic Rearrangement I

## Problem Summary

Given a palindromic string `s`, find its lexicographically smallest palindromic permutation.

## Solution Approach

The goal is to construct a palindrome `P` which is a permutation of `s` and is lexicographically minimal. A palindrome has the structure `H + [mid] + H_reversed`, where `H` is the first half and `mid` is the optional middle character (present if the length is odd).

To make `P` lexicographically smallest, we need to make its prefix, `H`, lexicographically smallest. The smallest possible `H` can be formed by taking half the counts of each character present in the original string `s` and arranging them in ascending alphabetical order.

Since `s` is guaranteed to be a palindrome, all characters must have an even count, except possibly for one character which can have an odd count (this will be the `mid` character).

The algorithm is as follows:

1.  **Count Characters:** Use `collections.Counter` to count the frequency of each character in `s`.
2.  **Build First Half (H):** Iterate through characters from 'a' to 'z'. For each character `c`, append `count[c] // 2` copies of `c` to a list representing the first half `H`. Keep track of the character `mid` that has an odd count (if any).
3.  **Construct Result:** Convert the list `H` to a string (`first_half_str`). Reverse the list `H` and convert it to a string (`second_half_str`). Concatenate them with the middle character: `first_half_str + mid + second_half_str`.

## Complexity Analysis

-   **Time Complexity:** `O(N)`, where `N` is the length of the string `s`.
    -   Counting characters: `O(N)`.
    -   Building the first half: `O(N)` (iterating through 26 characters, but total appends sum to `N/2`).
    -   Joining and reversing: `O(N)`.
-   **Space Complexity:** `O(N)`.
    -   `O(N)` for the character counts (at most 26 keys, but values can sum to N).
    -   `O(N)` for storing the `first_half` list and the final result string.

## Knowledge Base Links

*   **Core Technique:** [[../../techniques/palindrome/smallest_palindrome_from_half.md]]
*   General Pattern: [[../../patterns/construction/optimized_construction_via_input_guarantees.md]]
*   Character Counting: [[../../data_structures/hash_table_dict.md]]
*   Efficient String Building: [[../../optimizations/string/string_concatenation.md]]
*   Greedy Approach (general principle): [[../../algorithms/greedy/greedy.md]]