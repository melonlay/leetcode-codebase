# LeetCode 321: Create Maximum Number - Solution Explanation

## Problem Summary

Given two arrays `nums1` and `nums2` of digits (0-9) representing two numbers, create the maximum number of length `k` (where `k <= len(nums1) + len(nums2)`) using digits from both arrays. The relative order of digits from the same array must be preserved.

## Algorithmic Approach: Decomposition + Max Subsequence + Lexicographical Merge

The problem can be solved by decomposing it into subproblems:

1.  **Iterate Possible Splits:** Try all possible ways to pick `i` digits from `nums1` and `k - i` digits from `nums2`, where `i` ranges from `max(0, k - len(nums2))` to `min(k, len(nums1))`.
2.  **Find Max Subsequences:** For each split `(i, k - i)`:
    *   Find the lexicographically largest subsequence of length `i` from `nums1` (`max_sub1`).
    *   Find the lexicographically largest subsequence of length `k - i` from `nums2` (`max_sub2`).
3.  **Merge Subsequences:** Merge `max_sub1` and `max_sub2` to create the lexicographically largest possible sequence of length `k` (`merged`).
4.  **Combine Results:** Keep track of the overall best `merged` sequence found across all possible splits `i`.

## Logic Details

1.  **Finding Max Subsequence (Length `l` from `nums`):**
    *   This is done using a monotonic decreasing stack.
    *   Iterate through `nums`. For each digit `d`:
        *   While the stack is not empty, the top element `stack[-1]` is smaller than `d`, AND we still have enough digits remaining in `nums` plus those already in the stack to form a sequence of length `l` (i.e., `len(stack) - 1 + remaining_digits >= l`), pop the smaller digit from the stack.
        *   If `len(stack) < l`, push `d` onto the stack.
    *   The resulting stack (potentially truncated to length `l`) contains the lexicographically largest subsequence.
    *   **Reference:** See application #7 in [[../document/techniques/sequence/monotonic_queue.md]].
    *   (The provided solution uses a complex, optimized string-based function `_get_all_max_subsequences_str` to precompute these for relevant lengths).

2.  **Merging Two Subsequences (`sub1`, `sub2`) for Max Result:**
    *   Use two pointers, `p1` for `sub1` and `p2` for `sub2`.
    *   While building the merged result of length `k`:
        *   Compare the remaining subsequences `sub1[p1:]` and `sub2[p2:]` lexicographically.
        *   Append the digit from the start of the **larger** remaining subsequence to the result and advance the corresponding pointer.
    *   **Reference:** See [[../document/algorithms/merging/lexicographical_merge.md]] (adapt comparison for largest result).
    *   (The provided solution implements this in `_merge_str` using string suffix comparisons).

3.  **Iteration and Comparison:**
    *   Loop through all valid `i`.
    *   Generate `max_sub1` and `max_sub2`.
    *   Merge them to get `current_merged`.
    *   Compare `current_merged` with the best `overall_max` found so far and update if `current_merged` is lexicographically larger.

## Knowledge Base References

*   **Max Subsequence Technique:** [[../document/techniques/sequence/monotonic_queue.md]] (Application #7 covers finding the max subsequence using a stack).
*   **Merge Technique:** [[../document/algorithms/merging/lexicographical_merge.md]] (Describes merging based on lexicographical comparison; adapt for largest result by comparing suffixes).
*   **Data Structures:** [[../document/data_structures/stack.md]]

## Complexity Analysis

Let `M = len(nums1)`, `N = len(nums2)`.
*   **Max Subsequence (Standard):** O(M) or O(N) per call.
*   **Merge:** O(k^2) with naive suffix comparison, O(k) with optimized comparison.
*   **Outer Loop:** Runs O(k+1) times.
*   **Overall (Standard Stack + Optimized Merge):** O((M + N) * k + k^2) - The `(M+N)*k` comes from generating subsequences inside the loop. Pre-calculating subsequences reduces this. With pre-calculation and O(k) merge, complexity is dominated by subsequence generation (e.g., O(M+N)) and the O(k) iterations of O(k) merge -> **O(M + N + k^2)**.
*   **(Code's Complexity):** Stated as O(M+N + k^3) assuming O(k^2) merge, potentially O(M+N+k^2) if merge is O(k). The `_get_all_max_subsequences_str` complexity might be higher than standard O(M)/O(N) depending on internal logic.
*   **Space Complexity:** O(M+N) for pre-calculated subsequences (or O(k) without pre-calculation), plus O(k) for merge result. 