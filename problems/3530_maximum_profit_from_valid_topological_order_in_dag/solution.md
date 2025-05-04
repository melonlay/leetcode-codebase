# Solution for LeetCode 3530: Maximum Profit from Valid Topological Order in DAG

## Problem Summary

Given a Directed Acyclic Graph (DAG) with `n` nodes (0 to `n-1`) and associated scores, we need to find a topological ordering of the nodes. The profit is calculated as the sum of `score[i] * position[i]` for each node `i`, where `position[i]` is the 1-based index of node `i` in the chosen topological order. The goal is to find the maximum possible profit among all valid topological orders.

## Approach: Optimized Recursive DP (Future Score Memoization + Heuristic)

The constraints `n <= 22` allow for exponential time complexity, making standard iterative DP O(N*2^N) too slow in Python. The key to a fast solution lies in a more effective memoization strategy combined with a heuristic choice within a recursive (DFS-like) framework.

This approach uses recursion to explore valid topological orderings while memoizing the optimal *future* profit based on the set of visited nodes.

### Algorithm Breakdown

1.  **Initialization & Graph Setup:**
    *   Handle the edge case: If `edges` is empty, the graph is disconnected. The optimal profit is achieved by sorting the scores and assigning the lowest score to position 1, the next lowest to position 2, etc. Calculate `sum(sorted_scores[i] * (i+1))` and return.
    *   Build graph representations: Create `children` (adjacency list), `parents` (list of parent nodes for each node), and `is_root` (boolean map).
    *   Partition initial roots: Identify nodes with an in-degree of 0. Separate them into two sets: `childless_roots` (roots with no outgoing edges) and `roots_with_child` (roots with outgoing edges). These sets form the initial pool of nodes available to start the topological sort.

2.  **Memoization Table (`FUTURE_SCORE`):**
    *   Initialize an empty dictionary `FUTURE_SCORE = {}`.
    *   This dictionary will store the results of subproblems.
    *   **Key:** `visited_mask` (integer) - A bitmask representing the set of nodes that have already been placed in the current partial topological sort.
    *   **Value:** `FUTURE_SCORE[visited_mask]` stores the **maximum possible *additional* profit** that can be obtained from the *remaining unvisited nodes*, given that the nodes in `visited_mask` are already placed. This is the crucial concept – we store the optimal result for the *subproblem* defined by the remaining nodes.

3.  **Recursive Function `get_best_score`:**
    *   **Signature:** `get_best_score(current_profit_so_far, next_pos, options_with_child, childless_options, visited_mask)`
    *   **Parameters:**
        *   `current_profit_so_far`: The profit accumulated by the path taken to reach the current state (sum of `score * position` for nodes in `visited_mask`).
        *   `next_pos`: The next available 1-based position index to assign to a node.
        *   `options_with_child`: A `set` containing the nodes currently available (in-degree 0 relative to unvisited nodes) that *have* children.
        *   `childless_options`: A `set` containing the nodes currently available (in-degree 0 relative to unvisited nodes) that *do not* have children (terminal nodes in the remaining subgraph).
        *   `visited_mask`: The bitmask representing nodes already placed in this path.
    *   **Memoization Lookup (Step 1):**
        *   Check `if visited_mask in FUTURE_SCORE:`. If the optimal future score for this set of visited nodes has already been computed, we don't need to recompute.
        *   Return `current_profit_so_far + FUTURE_SCORE[visited_mask]`. This combines the profit of the path taken to reach this state with the pre-calculated optimal profit for completing the sort from this state.
    *   **Base Case (Implicit):** If both `childless_options` and `options_with_child` are empty, it means no more nodes can be placed from this state. The loops exploring options won't run. The function will eventually calculate and store the `future_profit` as 0 (explained below) and return the `current_profit_so_far`.
    *   **Heuristic Decision - Explore Min-Score Childless Node (Step 2):**
        *   `if childless_options:`: Check if any terminal nodes are available.
        *   Find `min_score_node = min(childless_options, key=lambda n: score[n])`. Identify the available terminal node with the lowest score. [[document/heuristics/greedy/min_score_terminal_node_heuristic.md]]
        *   **Simulate Placing:** Temporarily remove `min_score_node` from `childless_options`.
        *   **Recursive Call:** Call `get_best_score` for the state *after* placing this node:
            *   New profit: `current_profit_so_far + next_pos * score[min_score_node]`
            *   Next position: `next_pos + 1`
            *   Available sets: `options_with_child` (unchanged), modified `childless_options`.
            *   New visited mask: `visited_mask | (1 << min_score_node)`.
        *   **Backtrack:** Add `min_score_node` back to `childless_options` to restore the set for exploring other possibilities.
        *   Store the result of this recursive call (`score_after_min_childless`) and initialize `max_total_score` with it.
    *   **Exploration - Nodes With Children (Step 3):**
        *   Iterate through a *copy* (`list(options_with_child)`) of the available nodes that have children (`node_with_child`).
        *   **Simulate Placing:** Temporarily remove `node_with_child` from `options_with_child`.
        *   Calculate `new_visited_mask = visited_mask | (1 << node_with_child)`.
        *   **Update Dependencies:** Check the children of `node_with_child`. For each child `c`:
            *   Check if *all* parents of `c` are now included in `new_visited_mask`.
            *   If yes, child `c` becomes available. Add `c` to either `childless_options` or `options_with_child` *temporarily* for the recursive call, keeping track of which nodes were added (`added_childless`, `added_with_child`).
        *   **Recursive Call:** Call `get_best_score` for the state after placing `node_with_child`, using the temporarily updated available sets.
        *   Update `max_total_score = max(max_total_score, result_from_this_branch)`.
        *   **Backtrack:** Remove the newly added children (`added_childless`, `added_with_child`) from the sets and add `node_with_child` back to `options_with_child`.
    *   **Memoization Update (Step 4):**
        *   After exploring all possibilities (heuristic + nodes with children) from the current state, `max_total_score` holds the best total score found.
        *   Calculate the optimal profit achievable *from this state onwards*: `future_profit = max_total_score - current_profit_so_far`.
        *   Handle the base case where no nodes could be explored (leaf path): set `future_profit = 0`.
        *   Store this optimal future profit: `FUTURE_SCORE[visited_mask] = future_profit`.
    *   **Return Value:** Return the `max_total_score` found for the best path originating from the initial call's state.

4.  **Triggering the Calculation:**
    *   Call `get_best_score(0, 1, roots_with_child, childless_roots, 0)` to start the process. The initial state has 0 profit, next position 1, the initial root sets, and an empty visited mask.
    *   The return value of this initial call is the final maximum profit.

### Why this is the Fastest Approach

*   **Effective Memoization:** Using the `visited_mask` as the key and storing the optimal *future* score is highly effective. It correctly identifies that the optimal way to complete the topological sort only depends on *which* nodes remain, not the exact path taken to reach that state. This significantly reduces redundant computations compared to state definitions involving the last node placed or the exact available mask. [[document/optimizations/dynamic_programming/memoization_future_value.md]]
*   **Greedy Heuristic:** Prioritizing the minimum-score terminal node likely guides the search towards better solutions faster, potentially improving the practical performance even if the worst-case complexity remains exponential. [[document/heuristics/greedy/min_score_terminal_node_heuristic.md]]

## Complexity Analysis

*   **Time Complexity:** Worst case O(N * 2^N) if all states are visited. However, the number of reachable states relevant to the optimal solution, combined with effective memoization, makes the practical runtime much faster (closer to O(ReachableStates * N)).
*   **Space Complexity:** O(ReachableStates) for the `FUTURE_SCORE` memoization table, plus O(N) for graph structures and recursion stack depth.

## Foundational KB Components Used

*   [[document/algorithms/dynamic_programming/dynamic_programming.md]] (Top-Down DP)
*   [[document/techniques/recursion/memoization.md]] (Manual Memoization)
*   [[document/techniques/bit_manipulation/bitmask_state_tracking.md]] (Visited Mask)
*   [[document/techniques/dynamic_programming/dp_on_dag_subsets.md]] (Problem Pattern, Comparison)
*   [[document/heuristics/greedy/min_score_terminal_node_heuristic.md]] (Core Heuristic)
*   [[document/optimizations/dynamic_programming/memoization_future_value.md]] (Memoization Strategy) 