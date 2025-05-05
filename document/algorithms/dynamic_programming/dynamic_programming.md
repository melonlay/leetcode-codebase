# Algorithm Paradigm: Dynamic Programming (DP)

## Description

Dynamic Programming is a powerful algorithmic technique for solving optimization and counting problems by breaking them down into simpler, overlapping subproblems. It solves each subproblem only once and stores its result (memoization) or builds solutions iteratively (tabulation) to avoid redundant computations.

## Core Concepts

1.  **Optimal Substructure:** An optimal solution to the overall problem can be constructed from optimal solutions to its subproblems.
2.  **Overlapping Subproblems:** The same subproblems are encountered multiple times during the recursive computation of the solution. DP exploits this by storing the results.

## Approaches

1.  **Top-Down (Memoization):**
    *   Implement the solution recursively, mirroring the natural problem structure.
    *   Store the result of each subproblem in a lookup table (e.g., array, hash map).
    *   Before computing a subproblem, check if its result is already in the table. If so, return the stored result; otherwise, compute it, store it, and then return it.

2.  **Bottom-Up (Tabulation - Forward):**
    *   Determine the order in which subproblems need to be solved, **typically starting from the smallest/simplest base cases and building up towards the final solution**.
    *   Create a table (e.g., array) to store the results of subproblems.
    *   Iteratively fill the table, solving subproblems in the determined order, ensuring that the results for dependencies (`dp[i-1]`, `dp[j-1]`, etc.) are computed *before* they are needed for the current state `dp[i][j]`.
    *   This often involves forward loops (e.g., `for i from 0 to n`).

3.  **Bottom-Up (Tabulation - Backward):**
    *   This variation is useful when the problem asks for a result at the *start* state (e.g., `dp[0]` or `dp[0][0]`) that depends on computations propagating from the *end* state or target.
    *   Often used in problems asking for minimum cost/effort/requirements to reach a destination, where the state `dp[i][j]` represents the optimal value *starting from state `(i, j)`* until the end.
    *   Determine the order of subproblems, **typically starting from the target state or base cases at the end, and iterating backward towards the initial state**.
    *   Create a table to store results.
    *   Iteratively fill the table, ensuring dependencies (`dp[i+1]`, `dp[j+1]`, etc.) are computed *before* the current state `dp[i][j]`.
    *   This often involves reverse loops (e.g., `for i from n-1 down to 0`).
    *   **Example Context:** Finding the minimum starting health in the Dungeon Game (LC 174), where `dp[i][j]` is the min health needed *upon entering* `(i, j)` to reach the end.

## Common Characteristics of DP Problems

*   Problems asking for minimum/maximum values, counts of ways, or checking feasibility (can it be done?).
*   Decisions/choices need to be made at each step.
*   The problem can be defined in terms of states, and transitions between states can be formulated.

## General Structure (Tabulation Example - 2D)

Many problems involving two sequences or dimensions use a 2D table:

*   `dp[i][j]` often represents the solution considering prefixes `seq1[0...i-1]` and `seq2[0...j-1]`.
*   Requires careful definition of base cases (e.g., `dp[0][0]`, first row, first column).
*   Transitions compute `dp[i][j]` based on previous states like `dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]`.
*   *(See specific algorithms like `string/wildcard_matching.md` or `string/regex_matching.md` for concrete examples of this structure.)*

## Complexity

*   **Time:** Usually related to the number of distinct subproblems multiplied by the time taken per subproblem transition. Often polynomial (e.g., O(n), O(n^2), O(n*m)).
*   **Space:** Usually related to the space needed to store the results of subproblems (the DP table).

## Space Optimization Techniques

While the primary goal of DP is often time efficiency by avoiding recomputation, space complexity can also be a concern, especially with large inputs.

1.  **Reducing DP Table Dimensions:** If the computation of `dp[i]` only depends on `dp[i-1]` (or a fixed number of previous states), the DP table dimension can often be reduced. For example, a 2D table `dp[i][j]` might be reduced to 1D `dp[j]` if only the previous row (`i-1`) is needed.

2.  **Avoiding Large Precomputation Tables:** Some DP solutions involve precomputing auxiliary information (e.g., a table of all palindrome substrings in O(N^2) space). If this auxiliary information is not needed all at once, consider calculating it *on-the-fly* during the main DP transitions. This can significantly reduce space complexity, though it might require integrating a different technique into the DP loop.
    *   **Example:** In Palindrome Partitioning II (LC132), instead of storing an O(N^2) `is_palindrome` table, the palindrome checks can be done efficiently using the "Expand From Center" technique directly within the DP loop, reducing space to O(N). See `../../techniques/string/expand_from_center_palindrome.md`.
    *   **Trade-off:** This might slightly increase the constant factors in the time complexity per state transition but can be crucial when space is limited.

## Pitfalls

*   Identifying the correct subproblem structure and state definition.
*   Formulating the correct recurrence relation (transition logic).
*   Defining the base cases accurately.
*   Ensuring the iteration order in tabulation correctly computes prerequisites.
*   Off-by-one errors in indexing. See `../../common_mistakes/off_by_one_errors.md`.

## Related Patterns, Techniques, Optimizations & Mistakes

This section provides links to specific DP patterns, implementation techniques, optimizations, and common mistakes documented elsewhere in the KB.

*   **Specific DP Patterns:**
    *   Matrix/Grid: [[../../patterns/matrix/dual_path_grid_dp.md]]
    *   Sequence: [[./sequence/longest_increasing_subsequence.md]], [[./sequence/k_merges_variable_cost_dp.md]]
    *   Digit DP: [[../../patterns/digit_dp/digit_dp.md]], [[../../patterns/digit_dp/digit_dp_carry_counts.md]]
    *   Bitwise Sum Constraint: [[../../patterns/dynamic_programming/dp_on_items_bitwise_sum_constraint.md]]
*   **Implementation Techniques:**
    *   Memoization: [[../../techniques/recursion/memoization.md]]
    *   State Representation: [[../../techniques/bit_manipulation/bitmask_state_tracking.md]], [[../../techniques/dynamic_programming/dp_map_state_for_pairwise_relations.md]], [[../../techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]]
    *   Handling Constraints: [[../../techniques/dynamic_programming/dp_lower_bound_constraint.md]]
    *   Reductions: [[../../techniques/dynamic_programming/2d_dependency_lis_reduction.md]]
    *   Polynomials: [[../../techniques/polynomial/elementary_symmetric_polynomial_dp.md]]
*   **Optimizations & Comparisons:**
    *   Pruning: [[../../optimizations/pruning/dp_pruning_by_path_value.md]]
    *   State Comparison: [[../../optimizations/dynamic_programming/dp_state_comparison_equal_partition_sums.md]]
    *   Top-Down vs Bottom-Up: [[../../optimizations/dynamic_programming/digit_dp_carry_counts_topdown_vs_bottomup.md]], [[../../optimizations/grid_traversal/dual_path_dp_topdown_vs_bottomup.md]]
    *   Future Value Memoization: [[../../optimizations/dynamic_programming/memoization_future_value.md]]
*   **Common Mistakes:**
    *   Off-by-one errors (mentioned above)
    *   Product Limit with Zero: [[../../common_mistakes/dp_product_limit_zero_interaction.md]]
    *   Incorrect Base Cases or Transitions.
    *   State Insufficiency (Failing to capture all necessary info for transitions).

*(This list is not exhaustive; explore relevant subdirectories for more specific documents.)* 