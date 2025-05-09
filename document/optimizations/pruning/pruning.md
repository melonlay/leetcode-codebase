# Optimization Technique: Pruning

**Category:** Optimization (`optimizations/pruning/`)

## 1. General Concept

Pruning refers to a collection of techniques used to optimize search algorithms (like Backtracking, DFS, BFS) and dynamic programming by eliminating states, branches, or calculations that are determined to be unnecessary, invalid, or suboptimal *before* they are fully explored or computed. The goal is to reduce the effective size of the search space or the number of DP states considered, thereby improving performance, often dramatically.

## 2. Abstract Pruning Strategies

Several core strategies underlie most pruning techniques:

### a. Constraint Violation Pruning (Early Feasibility Check)
*   **Concept:** Stop exploring a path or state as soon as it violates fundamental problem constraints.
*   **Mechanism:** Explicit checks against rules (e.g., `is_valid` in Sudoku, capacity limits, sequence rules, boundary conditions). This is often the first line of defense in backtracking.
*   **Application:** Backtracking, search algorithms.
*   **Related KB:** [[../../algorithms/recursion/backtracking.md]]

### b. Optimality Pruning (Branch and Bound / Global Optimality Bound Check)
*   **Concept:** Eliminate search branches that cannot possibly lead to a solution better than the best *complete* solution found so far globally.
*   **Mechanism:** Maintain a global best solution value (`global_best`). Calculate a heuristic bound (an optimistic estimate) for the potential remaining value/cost from the current state. Prune if `current_value + bound` cannot improve upon `global_best`. Requires a good (often admissible) heuristic.
*   **Application:** Optimization problems (min/max) solved via search (DFS, BFS).
*   **Related KB:** [[./dfs_branch_and_bound_heuristic.md]]

### c. Subproblem Optimality Pruning (DP Path Pruning / State-Based Subproblem Dominance Check)
*   **Concept:** Avoid re-computing or exploring from an intermediate state if a *better* path to reach that *same state* has already been found.
*   **Mechanism:** Use memoization to store the best value found so far to reach a specific state (`dp[state] = best_value_to_reach`). Prune if the current path reaches the state with a value that is not better than the stored one.
*   **Application:** Dynamic programming (especially top-down/memoized recursion), state-space searches where reaching the same intermediate state via different paths is possible.
*   **Related KB:** [[./dp_pruning_by_path_value.md]]

### d. Heuristic-Guided Pruning (Variable/Value Ordering / Heuristic Search Prioritization)
*   **Concept:** Prioritize exploring variables or choices that are most constrained or most likely to lead to failure/success quickly. This *implicitly* prunes the search space by finding dead ends or solutions sooner.
*   **Mechanism:** Use heuristics to order the choice of the next variable to assign or the next value to try (e.g., Minimum Remaining Values (MRV), Least Constraining Value (LCV), domain-specific greedy choices).
*   **Application:** Constraint Satisfaction Problems (CSPs), backtracking, search algorithms.
*   **Related KB:** [[../../algorithms/recursion/mrv_heuristic.md]], [[../../heuristics/greedy/min_score_terminal_node_heuristic.md]]

### e. State Infeasibility Pruning (Logical / Logical Future State Infeasibility Check)
*   **Concept:** Prune branches where the current state logically cannot lead to a valid final state based on remaining resources vs. remaining requirements, even if it doesn't strictly violate constraints yet or isn't compared against a global optimum.
*   **Mechanism:** Domain-specific logical checks (e.g., in Digit DP: checking if `remaining_count + potential_from_carry < needed_count`).
*   **Application:** Dynamic programming (especially Digit DP), combinatorial search.
*   **Related KB:** [[../../optimizations/dynamic_programming/digit_dp_carry_counts_topdown_vs_bottomup.md]]

### f. Structural Pruning (Symmetry/Equivalence / State Space Reduction via Equivalence)
*   **Concept:** Avoid exploring states that are equivalent (e.g., symmetrical) to states already explored or guaranteed to be explored elsewhere.
*   **Mechanism:** Identify symmetries or equivalences in the state definition. Enforce a canonical representation for states or add checks to skip exploration if an equivalent state is handled by another branch (e.g., in grid DP, only compute `dp[r1][c1][r2][c2]` where `r1 <= r2`).
*   **Application:** Grid DP, problems with inherent symmetries.
*   **Related KB:** [[../../optimizations/grid_traversal/dual_path_dp_topdown_vs_bottomup.md]]

### g. Data Structure Pruning (Lazy/Proactive / Auxiliary Data Structure Maintenance)
*   **Concept:** Removing outdated or irrelevant entries from auxiliary data structures (like heaps, balanced trees) used within an algorithm to maintain their efficiency and relevance.
*   **Mechanism:** Checking validity upon extraction (lazy deletion) or removing entries when they become invalid (proactive pruning).
*   **Application:** Algorithms using auxiliary structures to manage candidates or events, like sweep-line algorithms.
*   **Related KB:** [[../../techniques/sweep_line/sweep_line_max_height_profile.md]]

## 3. Important Considerations

*   **Correctness:** Ensure pruning logic doesn't incorrectly discard valid solutions. Pay special attention to edge cases (e.g., interactions with zero as in [[../../common_mistakes/dp_product_limit_zero_interaction.md]]).
*   **Overhead:** Calculating bounds or performing complex checks for pruning adds overhead. The benefit of reduced search must outweigh the cost of the pruning check itself.
*   **Heuristic Quality (for Branch and Bound):** The effectiveness of Branch and Bound heavily relies on the tightness and computational cost of the heuristic bound function.

## 4. When to Use Pruning

Pruning is essential when dealing with problems that have large search spaces or numerous DP states, where exhaustive computation is infeasible. It's a key technique for:
*   Combinatorial search problems (permutations, combinations, subsets).
*   Constraint Satisfaction Problems (CSPs).
*   Optimization problems (finding min/max values) solved via search or DP.
*   Speeding up dynamic programming, especially recursive implementations. 