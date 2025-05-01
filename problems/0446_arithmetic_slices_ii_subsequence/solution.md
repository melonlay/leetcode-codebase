# Solution for LeetCode 446: Arithmetic Slices II - Subsequence

## Problem Summary

Given an integer array `nums`, the goal is to find the total number of arithmetic **subsequences**. An arithmetic sequence must contain at least three elements, and the difference between consecutive elements must be constant. A subsequence is derived from the original array by deleting zero or more elements without changing the order of the remaining elements.

## Approach: Optimized Dynamic Programming with Index Lookups

This problem asks for counting subsequences with a specific property, which suggests Dynamic Programming. The optimized approach uses a DP state based on index pairs and a lookup table (`seen`) for potential preceding elements.

1.  **`seen` Map:** A hash map (`defaultdict(list)`) stores the indices where each number appears (`seen[value] -> list_of_indices`). This allows O(1) average time checking for the existence of a number and retrieval of its locations.
2.  **`dp` Map:** A hash map (`defaultdict(int)`) stores the core DP state. `dp[(j, i)]` represents the number of **arithmetic subsequences of length >= 3** that end *specifically* with the pair of elements at indices `(j, i)` (i.e., `..., nums[j], nums[i]`).
3.  **Iteration:** We iterate through `i` from `0` to `n-1`. For each `i`, we iterate through `j` from `0` to `i-1`.
4.  **Target Calculation:** For the pair `(nums[j], nums[i])`, we calculate the required value of the preceding element `target_val = 2 * nums[j] - nums[i]` that would form an arithmetic triplet `(target_val, nums[j], nums[i])`.
5.  **Lookup and Extension:**
    *   We check if `target_val` exists in the `seen` map.
    *   If it exists, we iterate through all indices `k` such that `nums[k] == target_val` and `k < j`.
    *   For each such `k`, `(nums[k], nums[j], nums[i])` forms an arithmetic sequence. The number of arithmetic subsequences ending with `(nums[j], nums[i])` that are formed by extending sequences ending at `(k, j)` is `1 + dp[(k, j)]`.
        *   The `+ 1` counts the new base sequence `(nums[k], nums[j], nums[i])`.
        *   `dp[(k, j)]` counts the longer sequences ending in `(k, j)` that are now extended by `nums[i]`.
    *   **Accumulate Total (`ans`):** We add this `newly_formed_count = 1 + dp[(k, j)]` to the overall answer `ans`.
    *   **Update `dp[(j, i)]`:** We also add `newly_formed_count` to `dp[(j, i)]`, accumulating the counts for all valid preceding `k` values.
6.  **Populate `seen`:** The index `i` is added to `seen[nums[i]]` *before* the inner loop for `j` starts, ensuring lookups are valid.

## Optimization and Comparison

This approach differs from a more straightforward O(n^2) DP solution:

*   **Alternative DP (`dp[i][diff]`):**
    *   State: `dp[i][diff]` = count of arithmetic subsequences (length >= 2) ending at index `i` with common difference `diff`.
    *   Transition: `total_count += dp[j][diff]`, `dp[i][diff] += dp[j][diff] + 1`.
    *   Time: O(n^2) guaranteed.
    *   Space: O(n^2) worst-case (many distinct differences).

*   **Current Optimized DP (`dp[(j, i)]` + `seen`):**
    *   State: `dp[(j, i)]` = count of arithmetic subsequences (length >= 3) ending with the pair `(nums[j], nums[i])`.
    *   Transition: Uses `seen` map for O(1) lookup of `target_val`. Iterates through potential `k` indices for `target_val`. `ans += (1 + dp[(k, j)])`, `dp[(j, i)] += (1 + dp[(k, j)])`.
    *   Time: **O(n^3) worst-case** (if many duplicates exist, the inner loop over `k` can be O(n)). **O(n^2) average-case** (if duplicates are rare, the inner loop is effectively O(1) on average).
    *   Space: O(n^2) (for `dp` map storing O(n^2) pairs) plus O(n) for `seen` map.

*   **Trade-off:** The optimized approach sacrifices a guaranteed O(n^2) time for a potentially faster O(n^2) average time on typical inputs (where duplicates aren't pathologically frequent) but has a worse theoretical O(n^3) worst-case time complexity. In competitive programming contexts or benchmarks, this average-case speedup often proves beneficial despite the worse theoretical bound.

## Complexity Analysis (Optimized Approach)

*   **Time Complexity:** O(n^3) worst-case, O(n^2) average-case.
*   **Space Complexity:** O(n^2) due to the `dp` map potentially storing O(n^2) pairs and the O(n) space for the `seen` map.

## Knowledge Base Connection

*   **Pattern:** This problem follows the [[../patterns/sequence/counting_subsequences_by_pairwise_relation.md]] pattern.
*   **Technique:** The DP state `dp[(j, i)]` combined with the `seen` lookup map is an alternative implementation technique compared to the `dp[i][diff]` map state described in [[../techniques/sequence/dp_map_state_for_pairwise_relations.md]]. Both techniques aim to solve the same underlying pattern, but with different performance trade-offs.

*   **Potential KB Entry:** A new entry `document/techniques/sequence/dp_counting_arithmetic_subsequences.md` could be created to document this specific DP state definition (`dp[i][diff]` storing counts of sequences ending at `i` with difference `diff`) and the logic for accumulating the result (`total_count += dp[j][diff]`) and updating the state (`dp[i][diff] += dp[j][diff] + 1`). This technique is useful for problems involving counting subsequences with defined progression rules.
*   **Related Concepts:** This relates to general DP on sequences (often O(n^2)) and the use of hash maps (`defaultdict`) within DP states to handle potentially large or sparse state spaces (like the difference `d` here). 