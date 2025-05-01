# Technique: DP Map State for Pairwise Relations

## Description

This technique provides efficient ways to implement Dynamic Programming solutions for problems involving subsequences defined by pairwise relations between adjacent elements (as described in the [[../patterns/sequence/counting_subsequences_by_pairwise_relation.md]] pattern).

It addresses the challenge where the DP state needs to track not only the ending index `i` of a subsequence but also a specific property derived from the last pair of elements (`nums[j]`, `nums[i]`) included in the subsequence.

Two common variations exist:

### Variation 1: State `dp[i][property_key]`

*   **Implementation:** Uses a 1D DP array (or list) where `dp[i]` is a hash map (e.g., `defaultdict`).
    ```python
    # Example structure (Python)
    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(n)]
    ```
*   **State Meaning:** `dp[i][property_key]` stores the count/length of subsequences ending at index `i`, where `property_key` (e.g., common difference) is derived from `nums[i]` and its predecessor.
*   **Transition:** Involves calculating `property_key = R(nums[j], nums[i])`, looking up `dp[j][property_key]`, and updating `dp[i][property_key]`. Often tracks subsequences of length >= 2.
*   **Complexity:**
    *   Time: O(n^2) guaranteed.
    *   Space: O(n^2) worst-case (depends on the number of distinct `property_key` values per index).
*   **Pros:** Guaranteed O(n^2) time.
*   **Cons:** Might involve redundant calculations if the same difference appears many times.

### Variation 2: State `dp[(j, i)]` with Index Lookup (`seen` map)

*   **Implementation:** Uses a single hash map `dp` keyed by index pairs `(j, i)`, and an auxiliary hash map `seen` mapping values to lists of their indices.
    ```python
    # Example structure (Python)
    from collections import defaultdict
    dp = defaultdict(int)
    seen = defaultdict(list)
    ```
*   **State Meaning:** `dp[(j, i)]` stores the count/length of subsequences **of length >= 3** ending *specifically* with the pair `(nums[j], nums[i])`.
*   **Transition:** For pair `(j, i)`, calculate the required preceding value `target_val = find_predecessor(nums[j], nums[i])`. Use `seen[target_val]` to find all relevant indices `k < j`. Update `dp[(j, i)]` by summing `1 + dp[(k, j)]` for all valid `k`. The total answer is accumulated directly during these updates.
*   **Complexity:**
    *   Time: O(n^3) worst-case (if many duplicates cause the loop over `k` to be O(n)). O(n^2) average-case (if duplicates are rare).
    *   Space: O(n^2) worst-case (for the `dp` map) + O(n) (for the `seen` map).
*   **Pros:** Can be significantly faster on average for inputs without excessive duplicates, potentially avoiding redundant difference calculations inherent in Variation 1. Directly calculates counts for length >= 3.
*   **Cons:** Worse theoretical worst-case time complexity (O(n^3)). Requires auxiliary `seen` map.

## Choosing Between Variations

*   **Variation 1 (`dp[i][property_key]`)** is simpler conceptually and provides a guaranteed O(n^2) time bound.
*   **Variation 2 (`dp[(j, i)]` + `seen`)** is often faster in practice (e.g., on typical competitive programming test cases) due to better average-case behavior but carries the risk of O(n^3) performance on pathological inputs (e.g., all elements identical).

## Advantages (General)

*   Handles sparse or large ranges for the `property_key` effectively using hash maps.
*   Adaptable to different pairwise relations.

## Related Patterns

*   [[../patterns/sequence/counting_subsequences_by_pairwise_relation.md]] (This technique is a common way to implement this pattern). 