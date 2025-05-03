# Solution Explanation: 2035. Partition Array Into Two Arrays to Minimize Sum Difference

## 1. Problem Summary

Given an array `nums` of `2*n` integers, partition it into two subarrays `arr1` and `arr2`, each of length `n`, such that the absolute difference between their sums (`abs(sum(arr1) - sum(arr2))`) is minimized.

## 2. Approach: Meet-in-the-Middle with Two Pointers

Let `total_sum = sum(nums)`. We want to find a partition `(arr1, arr2)` such that `len(arr1) == len(arr2) == n` and `abs(sum(arr1) - sum(arr2))` is minimized. Since `sum(arr1) + sum(arr2) = total_sum`, minimizing `abs(sum(arr1) - sum(arr2))` is equivalent to minimizing `abs(2 * sum(arr1) - total_sum)`. This means we need to find a subset of size `n` whose sum `S = sum(arr1)` is as close as possible to `total_sum / 2`.

The constraint `n <= 15` (`2n <= 30`) suggests a **Meet-in-the-Middle** approach.

**Algorithm:**

1.  **Divide:** Split `nums` into `left_half` (`nums[0:n]`) and `right_half` (`nums[n:2n]`).
2.  **Generate Subset Sums:** Use a helper function `_get_subset_sums` (optimized with downward count iteration) to generate all possible sums for each half, grouped by the number of elements `k` used (`left_sums_map`, `right_sums_map`).
3.  **Early Exit Checks:** Check if the sum of the original `left_half` or `right_half` is exactly `total_sum // 2`. If so, the minimum difference is `total_sum % 2` and we can return early.
4.  **Combine (Optimized Two Pointers):** The goal is to find a sum `S = s1 + s2` (where `s1` is from a `k`-element subset of the left half and `s2` is from an `(n-k)`-element subset of the right half) such that `S` is as close as possible to `total_sum / 2`. Due to symmetry, the minimum absolute difference `min|2*S - total_sum|` can be found by determining the largest possible achievable partition sum `S` that is *less than or equal to* `total_sum // 2` (let's call this `max_sum_le_half`). The minimum difference will then be `total_sum - 2 * max_sum_le_half`.
    *   Create a nested function `calc(left_map, right_map)`.
    *   **Initialize `max_sum_le_half`:** Find the overall minimum possible partition sum by checking the smallest sum from `left_map[k]` + smallest sum from `right_map[n-k]` across all valid `k`. Initialize `max_sum_le_half` to this minimum possible sum. This ensures it starts with a valid value.
    *   Iterate through counts `k` from `0` to `n`.
    *   Let `j = n - k`.
    *   Retrieve the sets `left_sums_set = left_map[k]` and `right_sums_set = right_map[j]`.
    *   If both sets are non-empty, **sort them into lists `a` and `b`** (Note: Sorting inside this loop matched the user's faster code, though sorting once outside is asymptotically better).
    *   Use **Two Pointers** on `a` and `b`: `i` starts at `0` (smallest left sum), `j` starts at `len(b) - 1` (largest right sum).
    *   While `i < len(a)` and `j >= 0`:
        *   `current_sum = a[i] + b[j]`.
        *   If `current_sum == total_sum // 2`: An exact match is found, the minimum difference is `total_sum % 2`. Return `total_sum - 2 * current_sum`.
        *   If `current_sum < total_sum // 2`: This `current_sum` is a candidate. Update `max_sum_le_half = max(max_sum_le_half, current_sum)`. Increment `i` to potentially find a larger sum closer to the target.
        *   If `current_sum > total_sum // 2`: This sum is too large. Decrement `j` to try a smaller sum.
    *   After the loops, return `total_sum - 2 * max_sum_le_half`.

## 3. Complexity Analysis

*   **Time Complexity:** O(n * 2^n).
    *   Subset sum generation: `2 * O(n/2 * 2^(n/2)) = O(n * 2^(n/2))`.
    *   Combination step: Outer loop runs `n+1` times. Inside, sorting takes `O(M log M + L log L)` where `M, L <= C(n/2, k)`. Two-pointer scan is `O(M + L)`. The total number of elements across all sorted lists is `O(2^(n/2))`. If sorting happens inside the loop, the complexity is harder to pin down precisely but is bounded by the generation step or slightly worse. If sorting happened outside, it would be `O(n * 2^(n/2))` total sort time. The two-pointer scans sum up to less than `O(n * 2^(n/2))` across all `k`. The overall complexity is dominated by subset sum generation and sorting, resulting in roughly `O(n * 2^n)`. (Note: `2^(n/2)` is often written as `2^n` when `n` refers to the half-size).
*   **Space Complexity:** O(2^n) (or O(2^(n/2)) using half-size `n`). Storing the subset sums dominates.

## 4. Foundational Components / KB Links

*   **Pattern:** [[document/patterns/divide_and_conquer/meet_in_the_middle.md]]
*   **Algorithm:** [[document/algorithms/combinatorics/subset_sum_generation_by_count.md]]
*   **Pattern:** [[document/patterns/two_pointers.md]]
*   **Optimization:** [[document/optimizations/searching/mitm_subset_sum_combination_strategies.md]] (Discusses combination strategies, including the one used here)
*   **Data Structure:** [[document/data_structures/hash_table_dict.md]] 