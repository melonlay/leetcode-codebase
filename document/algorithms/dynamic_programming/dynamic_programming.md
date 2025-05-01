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
2.  **Bottom-Up (Tabulation):**
    *   Determine the order in which subproblems need to be solved (usually starting from the smallest/simplest).
    *   Create a table (e.g., array) to store the results of subproblems.
    *   Iteratively fill the table, solving subproblems in the determined order, until the solution for the overall problem is computed. This often involves loops instead of recursion.

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

## Pitfalls

*   Identifying the correct subproblem structure and state definition.
*   Formulating the correct recurrence relation (transition logic).
*   Defining the base cases accurately.
*   Ensuring the iteration order in tabulation correctly computes prerequisites.
*   Off-by-one errors in indexing. See `../../common_mistakes/off_by_one_errors.md`. 