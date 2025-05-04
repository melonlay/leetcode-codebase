# LeetCode 30: Substring with Concatenation of All Words - Solution Explanation

## Problem Summary

Given a string `s` and a list of words `words`, where all words in `words` have the same length, find all starting indices of substrings in `s` that are a concatenation of each word in `words` exactly once and without any intervening characters.

## Algorithmic Approach: Sliding Window with Offsets

This problem is solved using a sliding window approach tailored for fixed-length words and requiring frequency matching.

The core idea involves iterating through possible starting offsets and using a sliding window combined with frequency maps (`collections.Counter`) for each offset.

## Logic Explanation

The detailed logic, including handling offsets and the nuances of frequency matching vs. exact concatenation (especially regarding overlapping results), is comprehensively explained in the Knowledge Base pattern document:

*   **Reference:** See the section **"Variation: Substring Permutation with Fixed Length Words (LeetCode 30)"** within `[[../document/patterns/sliding_window.md]]`.

Here's a high-level summary matching the code:

1.  **Preprocessing:** Calculate `word_len`, `num_words`, `total_len`. Create target frequency map `word_freq = collections.Counter(words)`.
2.  **Offset Iteration:** Loop `start` from `0` to `word_len - 1`.
3.  **Sliding Window (per offset `start`):**
    *   Initialize `left = start`, `count = 0`, `seen = collections.Counter()`.
    *   Iterate `j` from `start` to `n - word_len + 1` with step `word_len`.
    *   Extract `word = s[j : j + word_len]`.
    *   **If `word` in `word_freq`:**
        *   Increment `seen[word]` and `count`.
        *   While `seen[word] > word_freq[word]` (excess word), shrink window from `left` (decrement `seen`/`count` for `left_word`, `left += word_len`).
        *   If `count == num_words`, record `left` in `result`. Then, slide window forward by removing the leftmost word (decrement `seen`/`count`, `left += word_len`). **Note:** This standard slide prevents finding certain overlaps.
    *   **Else (word not in `word_freq`):** Reset window (`seen.clear()`, `count=0`, `left = j + word_len`).
4.  **Return `result`.**

## Knowledge Base References

*   **Core Pattern & Specific Variation:** `[[../document/patterns/sliding_window.md]]` (Contains detailed explanation for this problem variant).
*   **Data Structure:** `[[../document/data_structures/hash_table_dict.md]]` (for `collections.Counter`).

## Complexity Analysis

*   **Time Complexity:** O(N * L), where N is the length of `s` and L is `word_len`. While often stated as O(N), the string slicing within the loop contributes the L factor.
*   **Space Complexity:** O(M * L), where M is the number of unique words in `words`, for storing the frequency maps. 