# DP Pattern: K Merges with Variable Segment Costs

**Applies Pattern:** [[../../../patterns/array/k_limited_operations.md]]

## 1. Problem Context

This pattern applies to problems involving a sequence (often representing segments along a path) where:
*   Exactly `k` merge operations must be performed.
*   A merge operation combines adjacent segments/removes boundary points (signs).
*   Crucially, merging segments `i` and `i+1` (removing boundary `i`) affects the properties (e.g., cost per unit, time per km) of **subsequent** segments in a way that depends on the original properties of the merged segments.
*   The goal is typically to minimize the total cost after `k` merges.

This differs from simpler k-limited operations problems where performing an operation has a fixed cost or effect that doesn't alter the cost/nature of future independent operations.

**Alternative Framing: Partition DP**
This problem can also be viewed as partitioning the `n` signs into `m = n - k` segments by selecting `m-1` signs that are *not* merged. The DP aims to find the minimum cost partitioning.

## 2. Challenge & Why Greedy Fails

The primary challenge is that the cost/benefit of a merge operation (or choosing a partition point) depends on the current state created by previous merges/partitions. A locally optimal choice might lead to a state where future choices are much more expensive, making the overall result suboptimal. This invalidates simple greedy approaches.

## 3. Dynamic Programming Approach

A DP solution is required. The state must capture enough information to correctly calculate future costs.

### Essential State Components:

1.  **Current Location:** The index of the current sign/segment boundary being considered (e.g., `i`, `cur`, `cidx`).
2.  **Progress Towards Constraint:** Information tracking the number of merges used (`k`) or segments formed (`m=n-k`). Examples: merges used so far `c`, merges remaining `used`, signs visited `r`, steps/segments formed `s`.
3.  **Future Cost Determinant:** Information sufficient to determine the cost of the *next* segment transition. This is the most critical part. Four successful strategies observed:
    *   **Strategy A (Iterative DP - Store Effective Property):** Store the calculated *effective property* (e.g., time-per-km `cur` or `e`) of the segment leaving the current location `i` directly in the state. `dp[i][c][effective_property] = cost_so_far`.
    *   **Strategy B (Iterative DP - Store Previous Location):** Store the index of the *previous* visited (non-merged) sign `prev` in the state. `dp[prev][cur][used] = cost_so_far`. The effective property for the next transition (`cur -> nxt`) is recalculated during the transition using `prev` and `cur` (often with prefix sums on original properties).
    *   **Strategy C (Recursive DP - State via Parameters):** Define a recursive function `solve(current_index, effective_speed_in, accumulated_skip_speed, last_stop_index, merges_left) = cost_so_far`. State parameters capture effective speed *into* the current segment (`effective_speed_in`) and potential contribution to the *next* segment's speed (`accumulated_skip_speed`) from skips. Memoization (`@cache`) is crucial.
    *   **Strategy D (Recursive/Iterative DP - Partition View):** Define state based on segment formation. `dp[segments_formed][current_sign][previous_sign] = cost_to_go` (recursive) or `cost_so_far` (iterative). The `previous_sign` allows calculating the effective property of the segment leaving `current_sign` using prefix sums. The target is `segments_formed == n - k`.

### Common Technique: Prefix Sums

Calculating the effective property of a segment formed by merging original segments `a..b` often involves summing the original properties (e.g., `time[a] + ... + time[b]`). Using a prefix sum array on the original property array allows O(1) calculation of these sums.
*   See: `[[../../../techniques/sequence/prefix_suffix_aggregates.md]]`

### Example State Formulations (Conceptual):

*   **State A (`dp[i][c][cur]`):** `dp[i][c][cur]` = min cost to reach sign `i` using `c` merges, where the segment leaving `i` has effective time `cur`.
    *   Transitions iterate `i,c,cur`. For next sign `j`, cost `i -> j` uses `cur`. Effective time *leaving* `j` (`new_effective_time`) is calculated using prefix sums `s[j+1] - s[i+1]`. Update `dp[j][c + (j-i-1)][new_effective_time]`.
*   **State B (`dp[prev][cur][used]`):** `dp[prev][cur][used]` = min cost to reach sign `cur` directly from sign `prev`, using `used` merges total up to `cur`.
    *   Transitions calculate effective time for `cur -> nxt` using prefix sums based on `prev` and `cur`. Cost `cur -> nxt` uses this calculated effective time. Update `dp[cur][nxt][used + (nxt-cur-1)]`.
*   **State C (`solve(cidx, speed, extra, prev_hop, used_left)`):** Recursive state `cost_so_far`.
    *   Transitions make calls representing "take" vs "skip".
*   **State D (`dp[k_steps][i][last]` or `solve(k_steps, i, last)`):** `dp[k_steps][i][last]` = min cost starting from sign `i`, given `k_steps` segments already formed, and the previous segment started at `last`. Rate for `i -> next` is calculated as `pre[i] - pre[last]`. `cost_to_go` formulation.

### Complexity

The time complexity is typically O(N^2 * K) or O(N^3) depending on the state structure and transitions (N signs, K merges). Space complexity is similar.

## 4. Implementation Notes

*   Use `defaultdict(lambda: INF)` or careful initialization with `float('inf')` for iterative DP, especially when the state includes effective properties or indices that can be sparse. Use `@cache` or explicit memoization tables for recursive solutions.
*   Pay close attention to base cases.
*   Ensure the final answer collection correctly considers all states satisfying the exact constraints (e.g., reaching `n-1` with exactly `k` merges or `m=n-k` segments). 