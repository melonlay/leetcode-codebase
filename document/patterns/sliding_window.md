# Sliding Window Pattern

## Description

The Sliding Window pattern is used to perform operations on a specific window size (subset) of a linear data structure like an array or string. It efficiently avoids re-computation by "sliding" the window across the data structure, typically using two pointers (often `left` and `right`, or `start` and `end`).

The window represents a contiguous range of elements. It expands by moving one pointer (e.g., `right`) and shrinks by moving the other pointer (e.g., `left`).

## Types

1.  **Fixed-Size Window:** The window size remains constant. Both `left` and `right` pointers usually move together. Used for problems like finding the maximum sum of a subarray of size `k`.
2.  **Variable-Size Window:** The window size changes based on certain conditions. Often, the `right` pointer expands the window, and the `left` pointer shrinks it when a condition is violated or needs adjustment. Used for problems like finding the *smallest* or *longest* subarray/substring satisfying a condition (e.g., Longest Substring Without Repeating Characters, Minimum Size Subarray Sum).

## General Approach (Variable-Size Window)

1.  Initialize `left = 0`, `max_length/min_length = initial_value`, and any necessary data structures (e.g., hash map, set) to track window state.
2.  Iterate with the `right` pointer from `0` to `len(data) - 1`:
    a.  Update the window state by including the element at `data[right]`.
    b.  **Shrinking Condition:** While the current window `data[left...right]` violates the problem's constraint:
        i.   Update the window state by excluding `data[left]`.
        ii.  Increment `left` (shrink the window from the left).
    c.  **Update Result:** Once the window is valid, update the `max_length`/`min_length` or other result based on the current window size (`right - left + 1`) or content.
3.  Return the final result.

## Complexity

*   **Time Complexity:** Typically O(N), where N is the size of the input data structure. Although there's a nested `while` loop, each element is processed at most twice (once by the `right` pointer and once by the `left` pointer).
*   **Space Complexity:** Often O(K) or O(distinct elements), where K is the size of the auxiliary data structure used to track the window's state (e.g., the size of the character set in the "Longest Substring Without Repeating Characters" problem).

## Example Use Case: Longest Substring Without Repeating Characters

See `problems/0003_longest_substring_without_repeating_characters/solution.py` for a concrete implementation. In this case:
*   The window state is tracked using a `set` (`char_set`).
*   The window expands by adding `s[right]` to the set.
*   The shrinking condition is `s[right]` already being in `char_set`.
*   Shrinking involves removing `s[left]` from the set and incrementing `left`.
*   The result (`max_length`) is updated after each expansion.

This pattern is highly effective for problems involving contiguous subarrays or substrings where brute-force checking of all possibilities would be too slow (e.g., O(N^2) or O(N^3)).

## Variation: Substring Permutation with Fixed Length Words (LeetCode 30)

**Context:** This variation addresses problems where you need to find substrings in a larger string `s` that are exact concatenations of *any permutation* of a given list of `words`, where all words have the same length (`word_len`).

**Algorithm:**

1.  **Preprocessing:**
    *   Calculate `word_len`, `num_words`, and `total_len` (`num_words * word_len`).
    *   Create a target frequency map (`word_freq`) of the words in the `words` list (e.g., using `collections.Counter`). Handle edge cases (empty `s` or `words`, `s` shorter than `total_len`).
2.  **Iterate Offsets:** Since the concatenated substring must align with word boundaries, iterate through all possible starting offsets within the first word (`start` from `0` to `word_len - 1`).
3.  **Sliding Window per Offset:** For each `start`:
    *   Initialize `left = start`.
    *   Initialize `seen = collections.Counter()` to track word frequencies within the current window.
    *   Initialize `count = 0` to track the number of words from `word_freq` currently accounted for in the window (respecting frequency limits).
    *   Iterate `j` (right end of the current word being considered) from `start` to `n - word_len` with a step of `word_len`.
    *   Extract `word = s[j : j + word_len]`.
    *   **If `word` is in `word_freq`:**
        *   Increment `seen[word]` and `count`.
        *   **Shrink Condition (Excess Word):** While `seen[word] > word_freq[word]`, remove the word at the `left` pointer (`left_word = s[left : left + word_len]`), decrement `seen[left_word]`, decrement `count`, and advance `left` by `word_len`.
        *   **Match Check:** If `count == num_words`, it signifies that the window `s[left : j + word_len]` contains exactly `num_words` valid words matching the target frequencies. Record `left` as a starting index.
        *   **Slide After Match (Standard Approach):** Remove the word at the `left` pointer (`left_word = s[left : left + word_len]`), decrement `seen[left_word]`, decrement `count`, and advance `left` by `word_len`. This prepares the window for the next iteration `j`.
    *   **If `word` is not in `word_freq`:** Reset the window state (`seen.clear()`, `count = 0`, `left = j + word_len`).
4.  Return the collected starting indices.

**Complexity:**
*   Time: O(N), where N is the length of `s`. The outer loop runs `word_len` times, and the inner sliding window processes each character of `s` at most twice (once by `j`, once by `left`). String slicing takes O(word_len), but since the total work across all offsets involves examining each character a constant number of times, the overall complexity remains O(N).
*   Space: O(M * word_len), where M is the number of unique words in the `words` list, to store the frequency maps.

**Important Considerations & Potential Pitfalls:**

*   **Offset Iteration:** Crucial because the concatenated substring doesn't necessarily start at index 0.
*   **Frequency vs. Exact Concatenation:** This standard algorithm relies on matching word *frequencies* within a window of the correct total length. It assumes this is equivalent to finding a valid concatenation. However, strictly speaking, a substring might have the correct frequencies but not be a valid concatenation (e.g., `s="baba"` for `words=["ab", "ba"]`). This algorithm would find index 1 in that case.
*   **Overlap Handling (Standard Approach Limitation):** The "Slide After Match" step, while standard, **prevents the correct detection of certain subsequent overlapping matches**. For example, in `s="ababaab"` with `words=["ab", "ba"]`, the algorithm finds the frequency match starting at index 1 (`"baba"`) but sliding `left` prevents it from later identifying the true concatenated match `"baab"` starting at index 3. If precise overlap detection is needed according to the strict concatenation definition, a more complex algorithm or verification step might be required. See `problems/0030_substring_with_concatenation_of_all_words/test_solution.py` for discussion on test cases `test_overlapping_matches` and `test_duplicate_words_in_list`. 