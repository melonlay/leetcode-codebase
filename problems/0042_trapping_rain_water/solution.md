# LeetCode 42: Trapping Rain Water

## Problem Summary

Given an array of non-negative integers representing an elevation map, where each bar has a width of 1, calculate the total amount of rainwater that can be trapped between the bars.

## Solution Approach: Two Pointers

The most efficient approach for this problem uses the Two Pointers technique.

1.  **Initialization:**
    *   Initialize two pointers, `left = 0` and `right = n - 1`, where `n` is the number of bars.
    *   Initialize `left_max = 0` and `right_max = 0` to track the maximum height encountered so far from the left and right ends, respectively.
    *   Initialize `total_water = 0` to accumulate the trapped water.

2.  **Iteration:**
    *   Use a `while left < right` loop.
    *   Inside the loop, compare `height[left]` and `height[right]`.
    *   **If `height[left] < height[right]`:**
        *   This means the potential water level at the `left` pointer is limited by the `left_max` height, because we know there's a taller or equal bar (`height[right]`) acting as the right boundary.
        *   If `height[left]` is greater than or equal to `left_max`, update `left_max = height[left]`. This bar is part of the wall and cannot trap water relative to the current `left_max`.
        *   Otherwise (`height[left] < left_max`), the bar `height[left]` is lower than the left wall. The trapped water above this bar is `left_max - height[left]`. Add this amount to `total_water`.
        *   Increment `left`.
    *   **Else (`height[right] <= height[left]`):**
        *   This means the potential water level at the `right` pointer is limited by the `right_max` height, because `height[left]` provides a sufficient left boundary.
        *   If `height[right]` is greater than or equal to `right_max`, update `right_max = height[right]`.
        *   Otherwise (`height[right] < right_max`), the trapped water above this bar is `right_max - height[right]`. Add this to `total_water`.
        *   Decrement `right`.

3.  **Termination:**
    *   The loop continues until `left` meets or crosses `right`.
    *   Return `total_water`.

## Why it Works

The key insight is that the amount of water trapped above any bar `i` is determined by `min(max_left, max_right) - height[i]`. The two-pointer approach cleverly calculates this without needing separate precomputation passes.

When `height[left] < height[right]`, we know that `max_right` (the true maximum height to the right of `left`) is *at least* `height[right]`. Since `height[left]` is the bottleneck height being considered, the water level above `height[left]` is solely determined by `left_max` (the maximum height encountered so far from the left). If `height[left]` itself is the new `left_max`, no water is trapped *at this position*. If `height[left]` is less than `left_max`, the difference `left_max - height[left]` can be trapped because we are guaranteed a right wall (`height[right]`) that's high enough.

A symmetric argument applies when `height[right] <= height[left]`, where the water level is determined by `right_max`.

## Complexity Analysis

*   **Time Complexity:** O(n), where n is the number of bars. Each pointer traverses the array exactly once.
*   **Space Complexity:** O(1). We only use a few extra variables (`left`, `right`, `left_max`, `right_max`, `total_water`).

## Knowledge Base Connections

*   **Pattern:** This solution applies the [Find Capacity Between Boundaries](../../document/patterns/array/find_capacity_between_boundaries.md) pattern, implemented using the inward-moving variant of the [Two Pointers](../../document/patterns/two_pointers.md) pattern.
*   **Alternative (DP):** A Dynamic Programming approach using [Prefix/Suffix Maximums](../../document/techniques/array/prefix_suffix_max.md) can also solve this in O(n) time but requires O(n) space.
*   **Alternative (Stack):** A [Monotonic Stack](../../document/techniques/monotonic_queue.md) (*Link assumes file exists*) approach provides another O(n) time, O(n) space solution. 