# Mathematical Concept: Median Minimizes Sum of Absolute Deviations (L1 Norm)

## Description

A fundamental property in statistics and optimization is that the **median** of a set of numbers `x_1, x_2, ..., x_n` is the value `m` that minimizes the sum of the absolute differences (also known as the sum of absolute deviations or the L1 norm distance) between `m` and each number in the set.

Minimize: \(\sum_{i=1}^{n} |x_i - m|\)

The value `m` that achieves this minimum is the median of the set `{x_i}`.

## Explanation

Imagine the numbers plotted on a number line. We are looking for a point `m` such that the total distance from `m` to all other points is minimized.

*   If we choose `m` below the median, moving `m` slightly to the right (towards the median) will decrease the distance to all points greater than `m` and increase the distance to all points less than `m`. Since there are more points greater than `m` than less than `m` (or an equal number if `n` is even and `m` is between the two middle elements), the total sum of distances decreases.
*   Similarly, if we choose `m` above the median, moving `m` slightly to the left (towards the median) will decrease the total sum of distances.
*   The sum is minimized when `m` is chosen such that there are an equal number of data points on either side of it. This point is the median.

**Formal Proof Hint:** The derivative of `|x - m|` with respect to `m` is `sign(m - x)`. The derivative of the sum is \(\sum sign(m - x_i)\). This sum is zero when `m` is the median (or any value between the two middle elements if `n` is even), indicating a minimum.

## Contrast with Mean (L2 Norm)

This contrasts with the **mean** (average), which minimizes the sum of *squared* differences (L2 norm distance):

Minimize: \(\sum_{i=1}^{n} (x_i - m)^2\)

The value `m` that achieves this minimum is the mean of the set `{x_i}`.

The median is less sensitive to outliers than the mean because it minimizes absolute differences rather than squared differences.

## Algorithmic Application: Minimum Moves to Equal Array Elements II (LeetCode 462)

*   **Problem:** Given an array `nums`, find the minimum number of moves required to make all array elements equal. In one move, you can increment or decrement an element by 1.
*   **Goal:** Find a target value `m` such that the total number of moves, \(\sum |nums_i - m|\), is minimized.
*   **Solution:** Based on the property above, the optimal target value `m` is the **median** of the array `nums`.
    1. Sort the array `nums`.
    2. Find the median element `m = nums[n // 2]` (where `n` is the length).
    3. Calculate the sum of absolute differences: `sum(|nums_i - m| for i in range(n))`. This sum represents the minimum number of moves.

## Calculation Technique for Sum of Distances

While the minimum *value* is achieved at the median, calculating the actual sum \(\sum |x_i - m|\) requires iterating through the array after finding the median.

If the array is sorted, this calculation takes O(n) time after an O(n log n) sort.

There isn't typically a simple closed-form formula to get the sum directly without iteration, unlike some properties related to the mean.

## Related Concepts

*   Median
*   Mean
*   Absolute Deviation
*   L1 Norm / Manhattan Distance
*   L2 Norm / Euclidean Distance (Squared)
*   Optimization
*   Order Statistics
*   Sorting Algorithms 