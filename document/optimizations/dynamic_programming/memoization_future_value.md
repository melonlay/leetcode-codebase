# Optimization: Memoization Strategy - Future Value

## Description

This describes a specific, highly effective memoization strategy applicable to recursive dynamic programming or state-space search problems, particularly those involving constructing sequences or paths (like topological sorts, permutations).

The core idea is to memoize the optimal value achievable *from* a given state onwards, rather than memoizing the value of the path *leading to* that state or the final result *for* that state if it were the end.

## Key Concept: Subproblem Independence from Path

This strategy works best when the optimal solution for the remaining part of the problem, starting from an intermediate state, depends *only* on the state itself (e.g., which elements/nodes remain available) and not on the specific path taken to reach that state.

## State and Memoization

*   **State Representation:** Identify a state representation (`state_key`) that uniquely captures all necessary information about the *remaining* subproblem. For problems involving subsets or visited elements, the `visited_mask` is often the most effective `state_key`.
*   **Memoization Table:** Use a dictionary `MEMO = {}`.
*   **Value Stored:** `MEMO[state_key]` stores the **optimal *additional* value** (e.g., max future profit, min future cost) that can be obtained starting from the point where the system has reached `state_key`.
*   **Recursive Function:** Typically `solve(current_path_value, state_key, ...other_params)`.

## Implementation

```python
MEMO = {}

def solve(current_path_value, state_key, ...):
    # --- Memoization Lookup --- 
    if state_key in MEMO:
        # Optimal future value is known
        return current_path_value + MEMO[state_key]

    # ... (Handle base cases: if state_key represents a final state, 
    #      the future value is 0) ...
    # Example Base case check:
    # if is_final(state_key):
    #    MEMO[state_key] = 0
    #    return current_path_value 

    # --- Explore transitions --- 
    best_total_value_from_here = current_path_value # Initialize with current path value
    # Assuming maximization problem

    for next_step in possible_next_steps(state_key):
        # Calculate next_state_key, next_path_value
        result = solve(next_path_value, next_state_key, ...)
        best_total_value_from_here = max(best_total_value_from_here, result)

    # --- Memoization Update --- 
    # Calculate the optimal *additional* value from this state
    future_value = best_total_value_from_here - current_path_value 
    MEMO[state_key] = future_value
    
    return best_total_value_from_here # Return the best total path value found

```

## Comparison to Other Memoization

*   **Standard Memoization (`@lru_cache` on `solve(state_key)`):** Stores the final result *for* subproblem `state_key`. Cannot easily handle path-dependent values or pruning based on path value.
*   **Path Value Memoization (`dp[state_key] = best_path_value_so_far`):** Stores the best path value found *so far* to reach `state_key`. Used for pruning (`dp_pruning_by_path_value.md`), but doesn't represent the optimal subproblem result independent of path.

## Benefits

*   **Correct Subproblem Solution:** Stores the actual optimal solution for the subproblem defined by `state_key` (the future part), independent of the path taken to reach it.
*   **Effective State Reduction:** By using a key that only captures the necessary future state (like `visited_mask`), it often drastically reduces the number of distinct states compared to keys including path details (like `last_node` or `available_mask`).
*   **Performance:** Can lead to significant speedups by avoiding recomputation of optimal future paths.

## When to Use

*   Recursive DP / state-space search for optimization problems.
*   When the optimal future solution depends only on the current state demarcation (e.g., which nodes are left), not the specific sequence of choices made previously.
*   Problems on subsets, permutations, DAG paths where the remaining structure dictates the future optimum.
*   Example: LC 3530 (Max Profit Topo Sort). [[../../techniques/dynamic_programming/dp_on_dag_subsets.md]]

## Related Concepts

*   [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   [[../../techniques/recursion/memoization.md]]
*   Bellman Equation (Conceptually related - value of state depends on values of future states) 