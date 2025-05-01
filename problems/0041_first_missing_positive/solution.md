## Problem Summary

Given an unsorted integer array `nums`, find the smallest positive integer (1, 2, 3, ...) that is not present in the array. The solution must run in O(n) time and use O(1) auxiliary space.

## Algorithmic Approach

The core idea is to use the array itself as a hash map to mark the presence of positive integers within the range `[1, n]`, where `n` is the length of the array. We achieve this using an in-place rearrangement often referred to as **cyclic sort** or **in-place hashing**.

1.  **Rearrangement Phase:**
    *   Iterate through the array from index `i = 0` to `n-1`.
    *   For each element `nums[i]`, if it's a positive integer within the valid range (`1 <= nums[i] <= n`) and it's not already in its correct position (i.e., `nums[nums[i] - 1]` is not equal to `nums[i]`), swap `nums[i]` with the element at index `nums[i] - 1`.
    *   Use a `while` loop for the swap condition (`1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]`) to ensure that after a swap, the new `nums[i]` is also checked and placed correctly if needed.
    *   The condition `nums[nums[i] - 1] != nums[i]` is crucial to prevent infinite loops when duplicate numbers are present (e.g., `[1, 1]`). If the number is already in its target spot, we move on.

2.  **Verification Phase:**
    *   After the rearrangement, iterate through the array again from index `i = 0` to `n-1`.
    *   The first index `i` where `nums[i]` is not equal to `i + 1` indicates that `i + 1` is the smallest missing positive integer. Return `i + 1`.

3.  **All Present Case:**
    *   If the verification loop completes without finding any mismatch, it means all integers from `1` to `n` are present in their correct positions. In this case, the smallest missing positive integer is `n + 1`. Return `n + 1`.

## Knowledge Base References

*   This approach uses the **In-Place Array Hashing (Cyclic Sort Variant)** technique, which leverages the array's indices and values to store presence information without extra space. This is detailed in `document/techniques/in_place_array_hashing.md`.
*   Care must be taken with index calculations to avoid `off-by-one` errors (relevant concept in `document/common_mistakes/off_by_one_errors.md`, particularly the `k` vs `k-1` mapping).
*   The `while` loop condition within the rearrangement phase is crucial to handle duplicates correctly and prevent infinite loops (`nums[nums[i] - 1] != nums[i]`).

## Complexity Analysis

*   **Time Complexity:** O(n).
    *   The outer `for` loop runs `n` times.
    *   The inner `while` loop performs swaps. Each swap places at least one number into its correct final position. A number is swapped at most once *into* its correct position. Therefore, the total number of swaps across the entire execution is at most `n`. 
    *   The second `for` loop runs `n` times.
    *   Overall complexity is O(n) + O(n) = O(n).
*   **Space Complexity:** O(1).
    *   The rearrangement is done in-place within the input array `nums`.
    *   Only a few extra variables (`n`, `i`, `target_index`) are used, requiring constant auxiliary space. 