# Optimization: DP Pruning by Path Value vs. Branch and Bound

## Description

This document clarifies two related but distinct optimization techniques used primarily in recursive (DFS/top-down) searches for optimization problems:

1.  **DP Pruning by Path Value:** Using memoization to store the best path value found so far *to reach a specific intermediate state*, allowing pruning if another path reaches the *same state* with a worse value.
2.  **Branch and Bound with Heuristic:** Using a heuristic estimate (upper/lower bound) of the *remaining* solution cost/value from the current state, allowing pruning if the *current path value plus the bound* cannot possibly beat the *globally best complete solution* found so far.

## Technique 1: DP Pruning by Path Value

*   **Core Idea:** Memoize the best path value found so far *for each specific state*. Prune subsequent paths reaching the *same state* if their path value is not better.
*   **DP State:** `dp[state_key]` = Best value (max score, min cost) found so far for *any path* reaching `state_key`.
*   **Pruning Check (in `dfs(state_key, current_path_value)`):**
    *   Maximization: `if state_key in dp and dp[state_key] >= current_path_value: return`
    *   Minimization: `if state_key in dp and dp[state_key] <= current_path_value: return`
*   **Update:** If not pruned, `dp[state_key] = current_path_value`.
*   **Focus:** Avoids re-exploring from a state if we've already found a better way *to get to that specific state*.
*   **Requires:** Storing values for potentially many intermediate states (e.g., O(2^N) for bitmask DP).
*   **KB File:** [[./dp_pruning_by_path_value.md]] (This file)

## Technique 2: Branch and Bound with Heuristic

*   **Core Idea:** Calculate a heuristic bound (optimistic estimate) on the best possible value achievable from the *current state* to the *final solution*. Prune the current path if `current_path_value + bound` cannot beat the `global_best_solution` found so far.
*   **DP State:** Typically only requires storing the `global_best_solution` found so far.
*   **Pruning Check (in `dfs(current_state, current_path_value)`):**
    *   Calculate `bound = heuristic_bound_function(current_state)`.
    *   Maximization: `if current_path_value + bound < global_best_solution: return`
    *   Minimization: `if current_path_value + bound > global_best_solution: return`
*   **Update:** Update `global_best_solution` whenever a complete solution is found that is better.
*   **Focus:** Avoids exploring entire branches that cannot possibly lead to an improvement over the best *complete* solution already known.
*   **Requires:** A good heuristic function to calculate the bound. The tighter the bound, the more effective the pruning. Calculating the bound adds overhead.
*   **KB File:** [[../recursion/dfs_branch_and_bound_heuristic.md]]

## Comparison

| Feature                     | DP Pruning by Path Value                      | Branch and Bound w/ Heuristic                 |
| :-------------------------- | :-------------------------------------------- | :-------------------------------------------- |
| **Pruning Basis**         | Compares path value to best known for *state* | Compares potential path value to *global best*|
| **Memory Requirement**    | Stores best value per state (e.g., `dp` dict) | Stores global best value                    |
| **Heuristic Needed?**     | No                                            | Yes (effectiveness depends on it)           |
| **Guaranteed Subproblems?** | Yes (computes best path *to* state)         | No (only finds global optimum)              |
| **Typical Use Case**      | DP where state represents a subproblem        | Search (DFS/Backtracking) for global optimum|

**Synergy:** While distinct, these techniques aren't mutually exclusive. A complex search might use Branch and Bound for global pruning and also incorporate state-based memoization/pruning for specific subproblems if beneficial, although this adds complexity.

For problems like LC 3530 (Max Profit Topo Sort), the DFS using a heuristic bound (like `get_rmax`) falls under **Branch and Bound**. The previous DFS attempt used **DP Pruning by Path Value**.

## Related Concepts

*   [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   [[../techniques/recursion/memoization.md]]
*   [[../../algorithms/recursion/backtracking.md]]
*   [[../../techniques/dynamic_programming/dp_on_dag_subsets.md]]
*   A* Search (Uses heuristics to guide search towards the goal) 