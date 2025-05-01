# Solution Explanation: 321. Create Maximum Number

## Problem Summary

Given two arrays of digits, `nums1` and `nums2`, and an integer `k`, find the lexicographically largest number (represented as an array of digits) of length `k` that can be formed by selecting digits from the two arrays while preserving the relative order of digits from the same array.

## Approach (Optimized, String-based)

This solution achieves high performance by performing the core subsequence generation and merging logic using optimized string operations.

1.  **Initial Conversion:** Convert the input `List[int]` arrays `nums1` and `nums2` into strings `s_num1` and `s_num2` using `''.join(map(str, ...))`.

2.  **Pre-calculating Maximum Subsequences (`_get_all_max_subsequences_str(s, k)`):**
    *   This helper function takes a string `s` and the global target length `k`.
    *   It calculates the lexicographically largest subsequences (as strings) for all relevant lengths in a single O(N) pass (N=`len(s)`).
    *   The logic mirrors the efficient `get_strs` function provided previously, involving an initial monotonic stack pass constrained by `k`, followed by iterative derivation of shorter subsequences. Crucially, it uses string slicing and `" ".join()` for internal operations.
    *   Returns a dictionary mapping length `l` to its maximum subsequence string.
    *   Reference: This technique is an optimized application of monotonic stack principles, related to concepts in `document/techniques/monotonic_queue.md`, but leverages string performance benefits described in `document/optimizations/string_vs_list_manipulation.md`.

3.  **Main Logic (`maxNumber`)**:
    *   Call `_get_all_max_subsequences_str` for `s_num1` and `s_num2`.
    *   Iterate through all possible split lengths `i` for `s_num1`.
    *   Retrieve the pre-calculated subsequence strings `sub1_str` and `sub2_str` from the dictionaries.
    *   If both exist, merge them using `_merge_str(sub1_str, sub2_str)`.
    *   Keep track of the overall best `max_merged_str`.

4.  **Merging Subsequences (`_merge_str(s1, s2)`):**
    *   Performs lexicographical merge on two strings.
    *   Uses string slicing comparison (`s1[p1:] > s2[p2:]`) to determine the next character.
    *   Builds the result efficiently using a list and `''.join()`.
    *   Reference: The merge logic is detailed in `document/techniques/array/lexicographical_merge.md` (concept applies to strings too).

5.  **Final Conversion:** Convert the final `max_merged_str` back to a `List[int]` using a list comprehension `[int(digit) for digit in max_merged_str]` before returning.

## Complexity Analysis (Optimized, String-based)

*   **Time Complexity:**
    *   String conversions: O(m) + O(n).
    *   `_get_all_max_subsequences_str`: O(m) + O(n).
    *   `_merge_str`: O(k^2) using string slicing comparison. (Can be O(k) with custom comparison).
    *   `maxNumber` loop: O(k) iterations.
    *   Inside Loop: O(1) dictionary lookups + O(k^2) merge.
    *   Final conversion: O(k).
    *   Total: O(m + n + k * k^2) = **O(m + n + k^3)**.
    *   With O(k) merge: O(m + n + k * k) = **O(m + n + k^2)**.
*   **Space Complexity:**
    *   String conversions: O(m + n).
    *   `_get_all_max_subsequences_str`: O(m + n) to store intermediate stacks and results dictionaries.
    *   `_merge_str`: O(k) for the result list/string.
    *   `maxNumber`: O(m + n) for dictionaries + O(k) for final result.
    *   Overall: **O(m + n)**.

## Knowledge Base Links

*   **Technique:** `_get_all_max_subsequences_str` uses an optimized monotonic stack approach (`document/techniques/monotonic_queue.md`).
*   **Technique:** `_merge_str` uses lexicographical merge (`document/techniques/array/lexicographical_merge.md`).
*   **Optimization:** The use of strings leverages performance benefits discussed in `document/optimizations/string_vs_list_manipulation.md`. 