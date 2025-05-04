# LeetCode 2035: Partition Array Into Two Arrays to Minimize Sum Difference - Solution Explanation

## Problem Summary

Given an integer array `nums` of size `2n`, partition it into two arrays of size `n` such that the absolute difference between the sum of the two arrays is minimized. Return this minimum absolute difference.

## Problem Transformation

Let the total sum be `S`. Let the sum of the first chosen array (size `n`) be `sum1`. The sum of the second array will be `sum2 = S - sum1`. We want to minimize `abs(sum1 - sum2) = abs(sum1 - (S - sum1)) = abs(2 * sum1 - S)`.

Minimizing `abs(2 * sum1 - S)` is equivalent to finding a subset of size `n` whose sum `sum1` is as close as possible to `S / 2`.

Specifically, we want to find the maximum possible `sum1 <= S / 2` achievable using a subset of size `n`. Let this be `max_sum_le_half`. The minimum difference will then be `S - 2 * max_sum_le_half`.

## Algorithmic Approach: Meet-in-the-Middle

Since `2n <= 30`, `n <= 15`. A brute-force check of all `C(2n, n)` combinations is too slow. Meet-in-the-Middle is suitable here.

1.  **Divide:** Split `nums` into two halves, `left_arr = nums[:n]` and `right_arr = nums[n:]`, each of size `n`.
2.  **Generate Subset Sums by Count:**
    *   Generate all possible subset sums for `left_arr`, grouped by the number of elements used (`k`). Store this in `left_sums_map = {k: {sum1, sum2, ...}}`.
    *   Generate all possible subset sums for `right_arr`, grouped by count `j`. Store in `right_sums_map = {j: {sum1, sum2, ...}}`.
    *   This uses the technique described in `[[../document/algorithms/combinatorics/subset_sum_generation_by_count.md]]`.
3.  **Combine (Meet):** We need to find a sum `s1` from the left half (using `k` elements) and a sum `s2` from the right half (using `j` elements) such that `k + j == n` (total elements is `n`) and `s1 + s2` is maximized but does not exceed `target = S // 2`.
    *   Iterate through all possible counts `k` for the left half (from 0 to `n`).
    *   Let the required count for the right half be `j = n - k`.
    *   If sums exist for both `k` in `left_sums_map` and `j` in `right_sums_map`:
        *   Get the sets of sums `left_sums = left_sums_map[k]` and `right_sums = right_sums_map[j]`.
        *   Convert them to sorted lists `a = sorted(list(left_sums))` and `b = sorted(list(right_sums))`.
        *   Use the **Two Pointers** technique on `a` and `b` to find the maximum `a[i] + b[j]` that is less than or equal to `target`.
            *   Initialize `i = 0` (start of `a`), `ptr_j = len(b) - 1` (end of `b`).
            *   While `i < len(a)` and `ptr_j >= 0`:
                *   `current_sum = a[i] + b[ptr_j]`.
                *   If `current_sum <= target`: This is a potential candidate for `max_sum_le_half`. Update `max_sum_le_half = max(max_sum_le_half, current_sum)`. Advance `i` to potentially find a larger sum from `a`.
                *   If `current_sum > target`: The sum is too large. Decrease `ptr_j` to try a smaller sum from `b`.
4.  **Calculate Result:** The minimum absolute difference is `S - 2 * max_sum_le_half`.

## Knowledge Base References

*   **Overall Pattern:** [[../document/patterns/divide_and_conquer/meet_in_the_middle.md]]
*   **Subset Sum Generation:** [[../document/algorithms/combinatorics/subset_sum_generation_by_count.md]]
*   **Combination Strategy:** [[../document/optimizations/searching/mitm_subset_sum_combination_strategies.md]] (recommends Two Pointers for the max sum <= target scenario)
*   **Core Combination Technique:** [[../document/patterns/two_pointers.md]]

## Complexity Analysis

*   **Time Complexity:** O(N * 2^(N/2)), where `N = 2n` is the original array length. Dominated by subset sum generation (`O(n * 2^n)` where `n=N/2`) and potentially sorting (`O(2^n * log(2^n)) = O(n * 2^n)`).
*   **Space Complexity:** O(2^(N/2)) to store the subset sums for each half. 