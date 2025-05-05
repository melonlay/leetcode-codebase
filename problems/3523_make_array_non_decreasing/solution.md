# 3523. Make Array Non-decreasing

## Problem Summary

Given an integer array `nums`, we can perform an operation any number of times: select a subarray `nums[i..j]` and replace it with a single element equal to its maximum value `max(nums[i..j])`.

The goal is to find the maximum possible size of the resulting array after performing zero or more operations such that the final array is non-decreasing.

## Algorithmic Approach (Optimal Greedy Scan)

The maximum possible size can be determined efficiently with a single pass using a greedy approach. We can directly count the number of elements that will constitute the final non-decreasing sequence.

The core idea is to iterate through the input array and maintain the maximum value (`lastMax`) seen in the *last element* of the conceptual final sequence constructed so far. An element `n` from the input array can form a *new* element in the final sequence only if it's greater than or equal to `lastMax`.

## Logic Explanation

1.  **Initialization:**
    *   Initialize the count of elements in the final sequence `ans = 0`.
    *   Initialize `lastMax = 0`. Since all `nums[i] >= 1`, 0 serves as a valid value strictly smaller than any possible first element of the final sequence.

2.  **Iteration and Counting:**
    *   Iterate through each number `n` in the input array `nums`.
    *   **Check if `n` starts/extends a new segment:** If `n >= lastMax`:
        *   This means `n` can be the next element in our conceptual non-decreasing sequence. It's either the first element (if `lastMax` was the initial 0) or it's greater than or equal to the maximum value of the previous segment.
        *   Increment the count: `ans += 1`.
        *   Update the maximum value of the last segment: `lastMax = n`.
    *   **Else (`n < lastMax`):**
        *   This means `n` must be merged into the previous segment represented by `lastMax`.
        *   The merged segment's maximum value is `max(lastMax, n)`, which is still `lastMax`.
        *   Crucially, no *new* element is added to the final sequence count, so `ans` is not incremented, and `lastMax` remains unchanged.

3.  **Return Result:**
    *   After iterating through all numbers, `ans` holds the count of elements in the final non-decreasing sequence.
    *   Return `ans`.

## Why This Works

This greedy approach correctly identifies the segments that form the final non-decreasing array. By only incrementing the count when a number `n` is greater than or equal to the `lastMax` of the previous segment, we effectively count the number of distinct non-decreasing steps or plateaus in the optimally merged sequence. Numbers smaller than `lastMax` are correctly absorbed into the previous segment without increasing the final sequence size.

## Knowledge Base References

*   **Optimization Comparison:** This optimal greedy scan approach is compared with simulation and descent-counting methods in [[../document/optimizations/simulation/sequence_reduction_size_simulation_vs_counting.md]].
*   **Greedy Algorithms:** This solution exemplifies a greedy strategy.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the input array `nums`. We perform a single pass through the array.
*   **Space Complexity:** O(1). We only use a few variables (`ans`, `lastMax`) for tracking. 