# LeetCode 42: Trapping Rain Water - Solution Explanation

## Problem Summary

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Algorithmic Approach: Two Pointers

This solution implements the O(1) space **Two Pointers** approach, which is one of the optimal ways to solve this problem.

The core idea is that the amount of water trapped above any bar `i` is limited by `min(max_height_to_left[i], max_height_to_right[i]) - height[i]`.

The Two Pointers approach cleverly calculates this without explicitly storing the max-left and max-right arrays.

## Logic Explanation

1.  **Initialization:**
    *   `left = 0`, `right = len(height) - 1`
    *   `left_max = 0`, `right_max = 0` (track max height seen so far from each side)
    *   `total_water = 0`
2.  **Iteration:** While `left < right`:
    *   **Identify Limiting Boundary:** Compare `height[left]` and `height[right]`. The lower of these two bars is the limiting factor for trapping water at the current position being processed.
    *   **Process Left Side (`height[left] < height[right]`):**
        *   The water level at `left` is determined by `left_max` because we know there's a taller or equal boundary (`height[right]`) on the right.
        *   If `height[left] >= left_max`: Update `left_max = height[left]` (this bar becomes a new boundary, no water trapped *above* it relative to `left_max`).
        *   Else (`height[left] < left_max`): Water can be trapped. Add `left_max - height[left]` to `total_water`.
        *   Move pointer: `left += 1`.
    *   **Process Right Side (`height[right] <= height[left]`):**
        *   Symmetric logic. The water level at `right` is determined by `right_max`.
        *   If `height[right] >= right_max`: Update `right_max = height[right]`.
        *   Else (`height[right] < right_max`): Add `right_max - height[right]` to `total_water`.
        *   Move pointer: `right -= 1`.
3.  **Return `total_water`.**

## Knowledge Base References

*   **Overall Pattern:** [[../document/patterns/array/find_capacity_between_boundaries.md]] (This pattern document details the problem structure and the Two Pointers, DP, and Stack solutions).
*   **Core Technique:** [[../document/patterns/two_pointers.md]] (General Two Pointers pattern, inward moving variant).
*   **Strategy Comparison:** [[../document/optimizations/array/trapping_rain_water_1d_strategies.md]] (Compares the different O(n) time solutions for this problem).

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the number of bars. The `left` and `right` pointers traverse the array once.
*   **Space Complexity:** O(1), as only a few variables are used. 