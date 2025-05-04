# Heuristic: Prioritize Minimum Score Terminal Node

## Description

This greedy heuristic is applicable in recursive/backtracking algorithms that construct sequences (like topological sorts) where elements have associated scores and the goal is to maximize a value based on both score and position (e.g., `Sum(score[i] * position[i])`).

When multiple nodes are available to be placed at the next position, and some of these nodes are "terminal" (they don't enable any subsequent nodes, like childless nodes in a DAG), this heuristic suggests choosing the terminal node with the **minimum score** to place next.

## Rationale

Terminal nodes represent dead ends in terms of enabling future choices. By placing the *lowest-scoring* available terminal node at the current position, we "get it out of the way" using the lowest possible position multiplier available at this step.

This saves higher position multipliers for potentially higher-scoring nodes, or for nodes that *must* be placed to enable other dependencies later in the sequence.

The core idea is to avoid wasting a high position multiplier on a low-scoring node that provides no future benefit in terms of unlocking other nodes.

## Implementation (within a Recursive Step)

```python
def solve(current_profit, next_pos, available_terminal_nodes, available_non_terminal_nodes, ...):
    
    best_outcome = -float('inf')

    # --- Apply Heuristic --- 
    if available_terminal_nodes:
        # Find the terminal node with the minimum score
        min_score_terminal_node = min(available_terminal_nodes, key=lambda node: score[node])
        
        # Explore the path resulting from placing this node
        available_terminal_nodes.remove(min_score_terminal_node)
        outcome_heuristic = solve(
            current_profit + next_pos * score[min_score_terminal_node],
            next_pos + 1,
            available_terminal_nodes,
            available_non_terminal_nodes,
            # ... other state updates ...
        )
        available_terminal_nodes.add(min_score_terminal_node) # Backtrack
        best_outcome = max(best_outcome, outcome_heuristic)

    # --- Explore Non-Terminal Nodes --- 
    for node in list(available_non_terminal_nodes):
        # ... (Simulate placing non-terminal node, update available sets) ...
        outcome_non_terminal = solve(
            current_profit + next_pos * score[node],
            next_pos + 1,
            # ... updated available sets ... 
        )
        # ... (Backtrack non-terminal node placement) ...
        best_outcome = max(best_outcome, outcome_non_terminal)

    # --- Handle base case / return --- 
    if not available_terminal_nodes and not available_non_terminal_nodes:
        return current_profit # Reached end of sequence
        
    return best_outcome # Or memoize future score relative to current_profit
```

## Benefits

*   Can significantly guide the search towards better solutions faster.
*   May implicitly prune the search space by exploring a more promising path first.
*   Simple greedy logic to implement.

## Drawbacks

*   **Not Guaranteed Optimal:** This is a heuristic. While often effective for position-weighted score maximization, it doesn't guarantee that placing the min-score terminal node first *always* leads to the globally optimal solution. However, when used within an exhaustive search framework (like the recursive DP with full memoization), it directs the *order* of exploration but doesn't prevent the optimal solution from being found.
*   Requires distinguishing between terminal and non-terminal available nodes.

## When to Use

*   Recursive search / DP for maximizing position-weighted scores.
*   When choices exist between placing terminal vs non-terminal nodes.
*   As a way to potentially improve the practical performance of an exponential-time algorithm.

## Related Concepts

*   Greedy Algorithms
*   Heuristics
*   [[../../techniques/dynamic_programming/dp_on_dag_subsets.md]] (Example Application)
*   [[../../algorithms/recursion/backtracking.md]] 