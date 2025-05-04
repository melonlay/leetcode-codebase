# Optimization: Meet-in-the-Middle Combination Strategies (Subset Sum Variations)

**Related Patterns:** [[../../patterns/divide_and_conquer/meet_in_the_middle.md]]
**Related Techniques:** [[../../algorithms/searching/binary_search.md]], [[../../patterns/two_pointers.md]], [[../../data_structures/hash_table_dict.md]]

## Context

The Meet-in-the-Middle (MitM) pattern involves generating results (e.g., subset sums) for two halves of a problem (`sums1`, `sums2`) and then combining them to find a final solution satisfying a target condition. The efficiency of this combination step is crucial.

This document compares common strategies for the combination step, specifically for variations of the subset sum problem.

Let `M = |sums1|`, `L = |sums2|`.

## Strategies

1.  **Hash Map Lookup (Exact Match)**
    *   **Problem:** Find if there exists `s1` in `sums1` and `s2` in `sums2` such that `s1 + s2 == target`.
    *   **Approach:** Store one set of sums (e.g., `sums1`) in a hash set or hash map. Iterate through the other set (`sums2`). For each `s2`, check if the complement (`target - s2`) exists in the hash set/map.
    *   **Complexity:** O(M + L) on average (for building and querying the hash set).
    *   **Pros:** Simple, efficient for exact matches.
    *   **Cons:** Not directly applicable for "closest sum" or "max sum <= target" problems.

2.  **Binary Search (One Sorted List)**
    *   **Problem:** Find if `s1 + s2 == target`, or find `s1 + s2` closest to `target`, or find max `s1 + s2 <= target`.
    *   **Approach:** Convert one set of sums (e.g., `sums2`) into a sorted list (`sorted_sums2`). Iterate through the other set (`sums1`). For each `s1`, perform a binary search (`bisect_left`, `bisect_right`) on `sorted_sums2` for the complement (`target - s1`) or the appropriate value for closest/max sum.
    *   **Complexity:** O(L log L) for sorting + O(M log L) for searching = **O((M+L) log L)** (assuming L >= M).
    *   **Pros:** Works for exact, closest, and max sum variants.
    *   **Cons:** Less efficient than Two Pointers when both lists need to be considered systematically for range-based targets (like max sum <= target).

3.  **Two Pointers (Two Sorted Lists)**
    *   **Problem:** Find if `s1 + s2 == target`, or find max `s1 + s2 <= target`.
    *   **Approach:** Convert *both* sets (`sums1`, `sums2`) into sorted lists (`a`, `b`). Initialize one pointer `i` at the start of `a` (`i=0`) and another pointer `j` at the end of `b` (`j = L-1`).
        *   While `i < M` and `j >= 0`:
            *   `current_sum = a[i] + b[j]`
            *   If `current_sum == target`: Found exact match. (Handle according to problem: return true, count, etc.). Adjust pointers `i++` or `j--` based on problem requirements (e.g., finding all pairs vs. just one).
            *   If `current_sum < target`:
                *   For "max sum <= target": Update `max_found = max(max_found, current_sum)`. Need to potentially increase the sum, so advance `i++`.
                *   For exact match: Advance `i++`.
            *   If `current_sum > target`: Need to decrease the sum, so advance `j--`.
    *   **Complexity:** O(M log M + L log L) for sorting + O(M + L) for the two-pointer scan = **O(N log N)** where N=M+L (or slightly better if M, L differ significantly).
    *   **Pros:** Often the most efficient for "max sum <= target" (like Problem 2035) after sorting. Scans linearly. Conceptually clean for range-based conditions.
    *   **Cons:** Requires sorting both lists.

## Recommendations

*   **Exact Match `s1 + s2 == target`?**
    *   Use **Hash Map Lookup** (Strategy 1) for best average time complexity O(M+L).
*   **Closest Sum to `target`?**
    *   Use **Binary Search** (Strategy 2) or **Two Pointers** (Strategy 3). Complexity is similar (dominated by sorting). Binary search might be slightly simpler to implement using `bisect` to find neighbors around `target - s1`.
*   **Maximum Sum `s1 + s2 <= target`? (e.g., Problem 2035)**
    *   Use **Two Pointers** (Strategy 3) on two sorted lists. It systematically explores potential pairs and efficiently maintains the maximum sum found so far within the O(M+L) scan after sorting.

**Note:** The choice also depends on whether the generated `sums1` and `sums2` are already sorted or need sorting anyway. 