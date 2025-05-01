## Problem Summary

You are given a string `s` and an array of strings `words`, all of the same length. Find all starting indices of substrings in `s` that are a concatenation of each word in `words` exactly once and without any intervening characters. The order of words in the concatenation does not matter.

## Algorithmic Approach

The solution utilizes a **Sliding Window** approach combined with **Hash Maps** (specifically `collections.Counter` in Python) to efficiently track word frequencies.

The key idea is to maintain a window of the exact size required for the concatenation (`num_words * word_len`). We slide this window across the string `s` and check if the words within the window match the required frequencies from the `words` list.

Since words have a fixed length (`word_len`), the window can only start at indices `0, 1, ..., word_len - 1`. We need to run the sliding window process independently for each of these starting offsets.

## Logic Explanation

1.  **Initialization:**
    *   Handle edge cases: If `s`, `words`, or `words[0]` is empty, return `[]`.
    *   Calculate constants: `n = len(s)`, `num_words = len(words)`, `word_len = len(words[0])`, `total_len = num_words * word_len`.
    *   If `n < total_len`, return `[]`.
    *   Create the target frequency map: `word_freq = collections.Counter(words)`.
    *   Initialize `result = []` to store the starting indices.

2.  **Outer Loop (Starting Offsets):**
    *   Loop `start` from `0` to `word_len - 1`.
    *   Inside this loop, run the sliding window logic for the specific starting offset.

3.  **Sliding Window Logic (for each `start`):**
    *   Initialize `left = start` (the left boundary of the current window).
    *   Initialize `count = 0` (number of valid words from `word_freq` currently found within the window).
    *   Initialize `seen = collections.Counter()` (frequency map for words seen in the current window).
    *   **Inner Loop (Sliding Right):** Iterate `j` from `start` to `n - word_len + 1` with a step of `word_len`. `j` represents the start of the *next potential word* to add to the window.
        *   Extract the word: `word = s[j: j + word_len]`.
        *   **Check if `word` is relevant:**
            *   If `word in word_freq`:
                *   Increment `seen[word]` and `count`.
                *   **Handle Excess Words:** While `seen[word] > word_freq[word]`, shrink the window from the left. Get the `left_word = s[left: left + word_len]`, decrement `seen[left_word]`, decrement `count`, and advance `left += word_len`.
                *   **Check for Match:** If `count == num_words`, a valid concatenation is found within the window `[left, j + word_len)`. Add `left` to the `result` list.
                *   **Slide Window:** After finding a match, slide the window forward by one word to continue the search. Decrement `seen` and `count` for the `left_word` and advance `left += word_len`.
            *   If `word not in word_freq`:
                *   This word breaks any potential concatenation. Reset the window state: `seen.clear()`, `count = 0`, and move `left = j + word_len` to start a new window after this invalid word.

4.  **Return Result:** After iterating through all starting offsets, return the `result` list.

## Knowledge Base References

*   **Sliding Window Pattern:** The core approach of using a window (`left`, `j`) that slides across the input `s` is described in `document/patterns/sliding_window.md`.
*   **Hash Map Lookup:** Using `collections.Counter` (a hash map implementation) for `word_freq` and `seen` allows for efficient O(1) average time lookups and updates of word frequencies. See `document/data_structures/hash_table_dict.md`.
*   **Ambiguity (Concatenation vs. Frequency):** Note that the problem definition requires a concatenation, but the standard sliding window solution efficiently checks for *frequency matches* within the window. For this problem, given the fixed word length and sliding mechanism, a frequency match implies a valid concatenation. See `document/common_mistakes/ambiguity_definition_vs_frequency.md` for discussion on this potential distinction in other problems.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the string `s`.
    *   The outer loop runs `word_len` times.
    *   The inner sliding window loop processes each character of `s` at most twice (once when the right pointer `j` advances over it, and potentially once when the left pointer `left` advances over it during shrinking). String slicing takes O(word_len) time.
    *   Building `word_freq` takes O(K * L) where K is `num_words` and L is `word_len`.
    *   Hash map operations are O(1) on average.
    *   Assuming `word_len` is significantly smaller than `N`, the dominant factor is scanning the string `s`. While the total work looks like O(word_len * (N/word_len) * word_len), careful analysis shows each character index is considered by `left` and `right` pointers a constant number of times, leading to an overall O(N) runtime.
*   **Space Complexity:** O(K * L), where K is the number of words in `words` and L is the length of each word.
    *   This space is used to store the `word_freq` hash map and the `seen` hash map in the worst case. 