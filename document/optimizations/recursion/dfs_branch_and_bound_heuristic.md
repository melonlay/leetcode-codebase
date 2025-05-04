# Optimization: DFS with Branch and Bound using Heuristics

## Description

Branch and Bound is a general algorithm design paradigm for finding optimal solutions, typically used with state space searches like Depth First Search (DFS) or Breadth First Search (BFS).

When applied to DFS for optimization problems (maximization or minimization), it involves calculating a **heuristic bound** at each node (state) in the search tree. This bound estimates the best possible value achievable from the current state to a complete solution. This bound is then used to prune branches of the search that cannot possibly lead to a solution better than the best one found globally so far.

## Core Idea (for DFS)

1.  **Global Best:** Maintain a variable `global_best_solution` initialized appropriately (e.g., `-inf` for max, `inf` for min).
2.  **Recursive DFS:** `dfs(current_state, current_path_value)`
3.  **Update Global Best:** When a complete solution is reached (e.g., base case of recursion), compare its value (`current_path_value`) with `global_best_solution` and update if better.
4.  **Heuristic Bound Calculation:** Before exploring children/next states, calculate a bound:
    *   Maximization: `bound = upper_bound_heuristic(current_state)` (an optimistic estimate of the maximum additional value achievable).
    *   Minimization: `bound = lower_bound_heuristic(current_state)` (an optimistic estimate of the minimum additional cost).
5.  **Pruning Check:**
    *   Maximization: `if current_path_value + bound <= global_best_solution: return` (If the best possible outcome from here isn't better than the global best, prune).
    *   Minimization: `if current_path_value + bound >= global_best_solution: return` (If the best possible outcome from here isn't better than the global best, prune).
6.  **Explore:** If not pruned, continue exploring next states recursively.

## Heuristic Function

*   The effectiveness of Branch and Bound heavily depends on the **quality and cost** of the heuristic bound function.
*   **Admissibility:** For finding the *optimal* solution, the heuristic must be admissible (never overestimates cost for minimization, never underestimates value for maximization). In our case, the greedy assignment of remaining scores to remaining positions is an admissible upper bound for the max profit problem.
*   **Tightness:** A tighter bound (closer to the true optimal value from the current state) leads to more pruning.
*   **Cost:** Calculating the bound adds overhead to each DFS node visit. A complex bound might slow down the search even if it prunes well. There's a trade-off.

## Example (LC 3530 - Max Profit Topo Sort)

```python
max_total = 0

def get_rmax_heuristic(n, score, current_mask, order):
    # Calculates optimistic upper bound
    # ... (Sort unused scores, assign greedily to positions order..n)
    return optimistic_remaining

def dfs(order, current_mask, current_total):
    nonlocal max_total

    # Check if path completed
    if order == n + 1:
        max_total = max(max_total, current_total)
        return

    # --- Branch and Bound Pruning --- 
    bound = get_rmax_heuristic(n, score, current_mask, order)
    if current_total + bound < max_total:
         return # Use < for maximization prune
    # --- End Pruning ---
    
    # ... (Find ready_nodes) ...

    # ... (Loop through ready_nodes and recurse) ...

# Initial call
dfs(1, 0, 0)
return max_total
```

## Comparison with Simple DFS/Backtracking

Simple backtracking explores the entire feasible search space. Branch and Bound significantly reduces this by eliminating branches guaranteed not to contain the optimal solution.

## Comparison with DP Pruning by Path Value

See [[../dynamic_programming/dp_pruning_by_path_value.md]] for a detailed comparison. Branch and Bound compares against the *global best*, while DP path pruning compares against the best way to reach the *current intermediate state*.

## When to Use

*   Optimization problems (min/max) solved using DFS or other state space search.
*   When the search space is too large for exhaustive search.
*   When a reasonably cheap and effective heuristic bound function can be devised.
*   Can be an alternative or supplement to standard DP memoization when DP states are too complex or numerous, but pruning is still desired.

## Related Concepts

*   [[../../algorithms/recursion/backtracking.md]]
*   [[../../algorithms/graph_search/dfs.md]]
*   Heuristics
*   A* Search
*   [[../dynamic_programming/dp_pruning_by_path_value.md]] 