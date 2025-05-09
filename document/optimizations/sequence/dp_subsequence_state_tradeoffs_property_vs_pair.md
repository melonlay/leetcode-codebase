# Optimization: DP State Trade-offs for Pairwise Subsequence Counting

## Context

When solving problems involving counting or analyzing subsequences based on pairwise relations (see [[../../patterns/sequence/counting_subsequences_by_pairwise_relation.md]]), dynamic programming is often used. The choice of DP state representation can lead to significant performance trade-offs, particularly concerning time complexity.

This document compares two common state management techniques discussed in [[../../techniques/sequence/dp_map_state_for_pairwise_relations.md]].

## Strategy 1: State `dp[i][property_key]`

*   **State:** `dp[i]` is a map where `dp[i][p]` stores the count/length of subsequences ending at index `i` with pairwise property `p` (e.g., common difference).
*   **Pros:**
    *   Guaranteed O(n^2) time complexity.
    *   Conceptually straightforward.
*   **Cons:**
    *   Space complexity can be O(n^2) worst-case.
    *   May perform redundant calculations if the same property `p` is recalculated for many pairs `(j, i)`.
    *   Often tracks subsequences of length >= 2, requiring accumulation logic specifically for the target length (e.g., >= 3).

## Strategy 2: State `dp[(j, i)]` with Index Lookup (`seen` map)

*   **State:** `dp` is a map keyed by index pairs `(j, i)`. `dp[(j, i)]` stores the count/length of subsequences (often specifically length >= 3) ending exactly with the pair `(nums[j], nums[i])`. Requires an auxiliary `seen` map for value->index lookups.
*   **Pros:**
    *   Often faster average-case time complexity (O(n^2)) on typical inputs (few duplicates) by directly looking up potential predecessors `k` via the `seen` map.
    *   Can directly compute counts for the target length (e.g., >= 3) within the transition.
*   **Cons:**
    *   **Worst-case O(n^3) time complexity** if duplicates are frequent, causing the inner loop over predecessor indices `k` to become O(n).
    *   Requires auxiliary `seen` map (O(n) space).
    *   DP state map `dp` can store up to O(n^2) entries.
    *   Slightly more complex implementation logic.

## Comparison and When to Use

| Feature             | Strategy 1 (`dp[i][prop]`) | Strategy 2 (`dp[(j,i)]+seen`) |
|---------------------|---------------------------|------------------------------|
| **Time (Worst)**    | O(n^2)                    | O(n^3)                       |
| **Time (Average)**  | O(n^2)                    | O(n^2)                       |
| **Space (Worst)**   | O(n^2)                    | O(n^2)                       |
| **Implementation**  | Simpler                   | More Complex                 |
| **Auxiliary Map**   | No                        | Yes (`seen` map)             |
| **Avg. Speedup**    | Baseline                  | Potentially Faster           |
| **Worst-Case Risk** | None                      | Significant (O(n^3))         |

*   **Choose Strategy 1 (`dp[i][prop]`) if:**
    *   A guaranteed O(n^2) time complexity is strictly required.
    *   Simplicity is prioritized.
    *   The range of property keys is expected to be manageable.
*   **Choose Strategy 2 (`dp[(j,i)]+seen`) if:**
    *   Average-case performance is critical (e.g., competitive programming, benchmarks on typical data).
    *   Inputs are not expected to have pathological distributions of duplicate values.
    *   The potential for O(n^3) worst-case performance is acceptable.

## Related Concepts

*   [[../../patterns/sequence/counting_subsequences_by_pairwise_relation.md]]
*   [[../../techniques/sequence/dp_map_state_for_pairwise_relations.md]] 