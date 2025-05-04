# Technique: DP on DAG Subsets

## Description

This dynamic programming pattern solves problems on Directed Acyclic Graphs (DAGs) with a small number of nodes (`N`, typically <= 25). The goal is usually to find an optimal value (max profit, min cost, count) over all valid topological sorts or subset selections, often involving position-dependent scoring.

The state typically uses a bitmask to represent subsets of nodes.

## Core Idea

The objective is to explore the space of valid topological orderings efficiently. Since `N` is small, exponential complexity is acceptable, but naive approaches are often too slow in languages like Python. The key is effective state representation and memoization or pruning.

## Implementation Approaches (Performance Comparison)

Various approaches exist, ordered roughly from slowest to fastest in practice for this problem type (like LC 3530):

1.  **Iterative Bottom-Up (`dp[visited_mask]`):**
    *   Calculates max profit/value using *only* nodes in `visited_mask`, assuming they occupy the first `k=popcount(mask)` positions.
    *   Pros: Standard DP, avoids recursion limits.
    *   Cons: Explores all `2^N` states, often TLE (O(N*2^N)).
    *   Requires O(2^N) space.

2.  **Recursive DFS + Path-Value Pruning (`dfs(mask, current_score)`):**
    *   Uses `dp[mask]` to store the best path score found *so far* to reach `mask`.
    *   Prunes if `current_score <= dp[mask]`.
    *   Pros: Prunes some paths compared to simple DP.
    *   Cons: Pruning might be insufficient; state value is path-dependent, not necessarily optimal subproblem solution. O(N*2^N) worst-case time/space.
    *   See: [[../optimizations/dynamic_programming/dp_pruning_by_path_value.md]]

3.  **Recursive DFS + Branch & Bound (`dfs(mask, current_score)` + Heuristic):**
    *   Uses a global `max_total` and a heuristic upper bound on remaining profit.
    *   Prunes if `current_score + heuristic_bound < max_total`.
    *   Pros: Can prune effectively if heuristic is good; O(N) space (stack).
    *   Cons: Performance depends heavily on heuristic quality/cost. O(N*2^N) worst-case time.
    *   See: [[../optimizations/recursion/dfs_branch_and_bound_heuristic.md]]

4.  **Recursive Top-Down (`f(last_node, available_mask, pos)`):**
    *   State focuses on last placed node and available nodes.
    *   Uses standard `@lru_cache` memoization.
    *   Pros: Often faster than iterative DP by potentially visiting fewer states.
    *   Cons: State definition less optimal; may still be too slow or hit MLE.

5.  **Optimized Recursive DP (Future Score Memoization + Heuristic - Recommended):**
    *   State: `get_best_score(current_profit, next_pos, available_sets, visited_mask)`.
    *   **Memoization:** Uses `FUTURE_SCORE[visited_mask]` to store the optimal *additional* profit achievable given `visited_mask` is placed. This key is highly effective. See [[../optimizations/dynamic_programming/memoization_future_value.md]].
    *   **Heuristic:** Uses a greedy choice (e.g., placing min-score terminal node first) to guide search order. See [[../heuristics/greedy/min_score_terminal_node_heuristic.md]].
    *   Pros: Typically the fastest due to superior memoization key and heuristic guidance. Handles subproblems optimally.
    *   Cons: More complex implementation (manual memoization, state/set management).
    *   Complexity: O(ReachableStates * N) time, O(ReachableStates) space. `ReachableStates` is often << `2^N`.

## Recommended Approach Details (Future Score Memoization + Heuristic)

This approach leverages the insight that the optimal future profit depends only on the set of remaining (unvisited) nodes.

*   **State:** `get_best_score(s, i, options_with_child, childless_options, visited)`
    *   `s`: Current accumulated profit.
    *   `i`: Next 1-based position index.
    *   `options_with_child`: Set of available nodes (parents visited) that have children.
    *   `childless_options`: Set of available nodes (parents visited) that have no children.
    *   `visited`: Bitmask of placed nodes.
*   **Memoization:** `FUTURE_SCORE = {}`. `FUTURE_SCORE[visited]` stores the max *additional* profit.
    *   Lookup: `if visited in FUTURE_SCORE: return s + FUTURE_SCORE[visited]`.
    *   Update: `FUTURE_SCORE[visited] = max_total_score_from_here - s`.
*   **Heuristic:** Explores placing `min(score)` node from `childless_options` first.
*   **Exploration:** Explores placing nodes from `options_with_child`, dynamically updating available sets based on parent dependencies.
*   **Backtracking:** State (available sets) must be restored after recursive calls.

```python
# Example Structure (Optimized Recursive DP)

# ... (Build graph, parents, initial root sets) ...

FUTURE_SCORE = {}

def get_best_score(s, i, options_with_child, childless_options, visited):
    if visited in FUTURE_SCORE:
        return s + FUTURE_SCORE[visited]

    max_total_score = s # Best total score found *from this state onwards*
    is_leaf_path = True # Flag if no further nodes can be placed

    # --- Heuristic Choice --- 
    if childless_options:
        is_leaf_path = False
        min_score_node = min(childless_options, key=lambda n: score[n])
        # ... (explore placing min_score_node) ...
        max_total_score = max(max_total_score, score_after_min_childless)

    # --- Exploration --- 
    options_to_try = list(options_with_child)
    if options_to_try:
        is_leaf_path = False
    for node_with_child in options_to_try:
        # ... (explore placing node_with_child, update sets, recurse, backtrack sets)
        max_total_score = max(max_total_score, score_after_node)

    # --- Memoize Future Score ---
    future_profit = max_total_score - s
    # Ensure base case (leaf path) results in future_profit = 0 for correct memoization
    if is_leaf_path and not childless_options and not options_to_try:
         future_profit = 0 
    FUTURE_SCORE[visited] = future_profit
    return s + future_profit # Return total score achieved via this path

# Initial call
final_answer = get_best_score(0, 1, roots_with_child, childless_roots, 0)

```

## Complexity (Recommended Approach)

*   **Time:** O(ReachableStates * N), potentially much faster than O(N * 2^N).
*   **Space:** O(ReachableStates) for memoization + O(N) stack.

## Key Considerations

*   **State Representation:** The choice of DP state and memoization key is critical for performance.
*   **Memoization Value:** Storing optimal *future* value keyed by `visited_mask` is highly effective here.
*   **Heuristics:** Greedy choices can guide the search but must be integrated correctly within the DP/memoization framework.
*   **Dependency Tracking:** Correctly updating available nodes based on parent completion is crucial.

## Related Concepts
*   [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   [[../bit_manipulation/bitmask_state_tracking.md]]
*   Topological Sort
*   [[../heuristics/greedy/min_score_terminal_node_heuristic.md]]
*   [[../techniques/recursion/memoization.md]]
*   [[../optimizations/dynamic_programming/memoization_future_value.md]]
*   Directed Acyclic Graphs (DAGs) 