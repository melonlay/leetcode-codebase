# Algorithm: Knuth-Morris-Pratt (KMP) String Search

**Related:** String Searching, Pattern Matching

## 1. Description

The Knuth-Morris-Pratt (KMP) algorithm is an efficient linear-time string searching algorithm. It finds all occurrences of a `pattern` string within a `text` string. Its efficiency comes from preprocessing the `pattern` to build a **Longest Proper Prefix which is also Suffix (LPS)** array. This LPS array allows the algorithm to avoid redundant comparisons by intelligently shifting the pattern upon a mismatch.

## 2. Core Concepts

*   **LPS Array (`lps`):** For a pattern `P` of length `m`, `lps[i]` stores the length of the longest *proper* prefix of `P[0...i]` that is also a suffix of `P[0...i]`. A proper prefix is not the entire string itself.
    *   Example: `pattern = "abab"`
        *   `lps[0] = 0` (prefix "a")
        *   `lps[1] = 0` (prefix "ab", suffixes "b")
        *   `lps[2] = 1` (prefix "aba", prefixes "a", "ab"; suffixes "a", "ba". Longest match: "a", length 1)
        *   `lps[3] = 2` (prefix "abab", prefixes "a", "ab", "aba"; suffixes "b", "ab", "bab". Longest match: "ab", length 2)
    *   The LPS array helps determine how far to shift the pattern after a mismatch. If a mismatch occurs at `pattern[j]` while comparing against `text[i]`, we don't need to restart the comparison from `pattern[0]`. Instead, we can shift the pattern such that the prefix of length `lps[j-1]` aligns with the suffix of the text just matched. The next comparison will be between `pattern[lps[j-1]]` and `text[i]`.

## 3. Algorithm Steps

### 3.1. LPS Array Computation (`_compute_lps`)

*   Input: `pattern` string of length `m`.
*   Output: `lps` array of length `m`.
*   Logic:
    1.  Initialize `lps = [0] * m`.
    2.  Initialize `length = 0` (length of the previous longest prefix suffix).
    3.  Initialize `i = 1` (index to iterate through the pattern).
    4.  While `i < m`:
        *   If `pattern[i] == pattern[length]`:
            *   It means we found a longer prefix-suffix match.
            *   Increment `length`.
            *   Set `lps[i] = length`.
            *   Increment `i`.
        *   Else (if `pattern[i] != pattern[length]`):
            *   If `length != 0`:
                *   We can't extend the previous prefix-suffix. Fall back to the length of the prefix-suffix for the *previous* character in the current prefix, which is stored in `lps[length - 1]`.
                *   Set `length = lps[length - 1]`. (Do *not* increment `i` yet, we need to re-check `pattern[i]` against the new, shorter `pattern[length]`).
            *   Else (`length == 0`):
                *   No prefix-suffix match ending at `i`.
                *   Set `lps[i] = 0`.
                *   Increment `i`.
*   Time Complexity: O(m) - Each character is visited a constant number of times on average.

### 3.2. KMP Search (`_kmp_search`)

*   Input: `text` string of length `n`, `pattern` string of length `m`, precomputed `lps` array.
*   Output: List of starting indices in `text` where `pattern` occurs.
*   Logic:
    1.  Initialize `indices = []`.
    2.  Initialize `i = 0` (index for `text`).
    3.  Initialize `j = 0` (index for `pattern`).
    4.  While `i < n`:
        *   If `pattern[j] == text[i]`:
            *   Characters match. Advance both pointers.
            *   Increment `i` and `j`.
        *   If `j == m`:
            *   A full match is found! The match starts at `i - j`.
            *   Append `i - j` to `indices`.
            *   Crucially, update `j` using the LPS array to continue searching for the *next* potential match immediately: `j = lps[j - 1]`. This avoids re-checking characters known to form a prefix of the pattern.
        *   Else if `i < n` and `pattern[j] != text[i]` (Mismatch after some matches):
            *   If `j != 0`:
                *   Mismatch occurred. Use the LPS array to find the next shorter prefix of the pattern that is also a suffix of the part already matched (`pattern[0...j-1]`). The length of this prefix is `lps[j-1]`. Move the pattern pointer `j` back to this length: `j = lps[j - 1]`. (Do *not* increment `i` yet).
            *   Else (`j == 0`):
                *   Mismatch occurred at the very first character of the pattern. Simply move to the next character in the text.
                *   Increment `i`.
*   Time Complexity: O(n) - The text pointer `i` only advances forward. The pattern pointer `j` can move backward, but the total number of backward moves is bounded by the number of forward moves of `i`.

## 4. Overall Complexity

*   **Time:** O(n + m) - O(m) for LPS computation + O(n) for search.
*   **Space:** O(m) - To store the LPS array.

## 5. Use Cases

*   Finding single or multiple occurrences of a substring within a larger text.
*   Used as a building block in other algorithms involving pattern matching.
*   Problems involving finding repeated patterns or overlaps.

## 6. Implementation Notes

*   Handle edge cases like empty text or pattern.
*   The indices returned are 0-based starting positions of the match in the `text`.
*   **Structure:** The KMP logic (LPS computation and search) can be implemented within a class as helper methods, as standalone functions, or even as nested functions within the main solving function, without altering the core algorithm or its complexity.

## 7. Example Application

*   [[https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/|LeetCode 28: Find the Index of the First Occurrence in a String]]
*   LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings (Used for searching flattened grid strings) - See `[[../../../problems/3529_count_cells_in_overlapping_horizontal_and_vertical_substrings/solution.md]]` 