# Pattern: Counting Subsequences by Pairwise Relation

## Description

This pattern applies to problems that require counting or finding properties (like the longest length) of **subsequences** where the inclusion of an element depends on a specific **relationship** holding between it and the **immediately preceding element** chosen for that subsequence.

The core idea is that the validity or property of a subsequence is built incrementally based on local conditions between adjacent elements within the subsequence itself, not just the elements' values or original indices.

## Problem Structure

Given an input sequence (e.g., an array `nums`):

1.  **Goal:** Count all valid subsequences, or find the longest valid subsequence, or find a subsequence with an optimal property.
2.  **Constraint:** A subsequence is considered "valid" if for every pair of consecutive elements `(..., x, y, ...)` within the subsequence, a specific relation `R(x, y)` holds true.
3.  **Optional Constraints:** Often includes a minimum length requirement for the subsequences being counted.

## Common Examples of Relations R(x, y)

*   **Arithmetic Progression:** `y - x == constant` (as seen in [[LeetCode 446: Arithmetic Slices II - Subsequence](../../problems/0446_arithmetic_slices_ii_subsequence/solution.md)])
*   **Geometric Progression:** `y / x == constant`
*   **Divisibility:** `y % x == 0`
*   **Specific Sum/Difference:** `y + x == k` or `y - x == k`
*   **Bitwise Properties:** `y & x == x` (y has all bits of x set)

## General Approach: Dynamic Programming

A common way to solve problems following this pattern is using Dynamic Programming.

*   **State Definition:** The DP state often needs to capture information about subsequences *ending* at a particular index `i` and satisfying the property up to that point. Because the property `R(x, y)` depends on the *previous* element `x`, the state often needs to incorporate information about that relationship.
A frequent state structure involves `dp[i]`, where `dp[i]` itself stores information keyed by the property derived from the last step. For example:
    *   `dp[i][property_value]`: Stores the count (or length) of subsequences ending at index `i`, where `property_value` is derived from the relation between `nums[i]` and the element preceding it in the subsequence (e.g., the common difference `d` in arithmetic subsequences).
*   **Transitions:** To calculate `dp[i]`, iterate through all preceding indices `j < i`.
    1.  Calculate the relevant property `p = property(nums[j], nums[i])` based on the required relation `R`.
    2.  Check if this pair potentially extends existing valid subsequences ending at `j`. This often involves looking up `dp[j]` based on the *same* property `p`.
    3.  Update `dp[i][p]` based on the information found in `dp[j][p]` and potentially the base case of the pair `(nums[j], nums[i])` forming a new subsequence of length 2.
    4.  If counting subsequences meeting a minimum length (e.g., >= 3), accumulate the count whenever a transition successfully extends a subsequence to meet or exceed that length.
*   **Implementation Detail:** Since the `property_value` (like the difference `d`) can be sparse or cover a wide range, using a **hash map (dictionary)** for the inner part of the DP state (`dp[i] = map<property_value, count/length>`) is often efficient. See [[../data_structures/hash_table_dict.md]] (assuming this exists).

## Complexity

*   **Time:** Typically O(n^2) due to the nested loops iterating through pairs `(j, i)`.
*   **Space:** Can be O(n^2) in the worst case if the number of distinct property values stored at each index `i` grows linearly with `i`.

## Related Techniques

*   [[../techniques/sequence/dp_map_state_for_pairwise_relations.md]] (Details the common DP state implementation using a map keyed by the pairwise property). 