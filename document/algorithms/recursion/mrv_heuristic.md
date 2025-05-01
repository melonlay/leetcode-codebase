# Algorithm: Minimum Remaining Values (MRV) Heuristic

## Description

The Minimum Remaining Values (MRV) heuristic, also known as the "most constrained variable" or "fail-first" heuristic, is commonly used in constraint satisfaction problems (CSPs), particularly those solved using backtracking search.

Its core idea is to prioritize the assignment of variables that have the fewest remaining legal values in their domain. By choosing the most constrained variable next, the algorithm attempts to detect failures (situations where no legal value can be assigned) earlier in the search process, potentially pruning large portions of the search tree and improving efficiency.

## How it Works

In a typical backtracking algorithm for a CSP:

1.  **Variable Selection:** Instead of selecting the next variable to assign based on a fixed order (e.g., row-by-row in Sudoku), the MRV heuristic dynamically selects the unassigned variable that has the smallest number of valid choices remaining in its current domain.
2.  **Value Assignment:** Once a variable is selected, a value is chosen from its remaining domain (often combined with other heuristics like Least Constraining Value - LCV).
3.  **Constraint Propagation:** After assigning a value, constraints are propagated to update the domains of neighboring (related) variables, removing inconsistent values.
4.  **Backtracking:** If an assignment leads to a dead end (a variable has no remaining legal values), the algorithm backtracks, undoing the assignment and trying a different value.

**Calculating Remaining Values:**
To implement MRV, the algorithm needs to maintain the current domain of possible values for each unassigned variable. After each assignment and constraint propagation step, the sizes of these domains are re-evaluated to determine the next variable to choose.

## Example: Sudoku Solver

Consider solving a Sudoku puzzle using backtracking:

*   **Variables:** The 81 empty cells.
*   **Domains:** Initially, each empty cell can take values {1, 2, ..., 9}.
*   **Constraints:** No repeated numbers in any row, column, or 3x3 subgrid.

Using MRV:
1.  At each step, identify all unassigned cells.
2.  For each unassigned cell, calculate how many numbers (1-9) are still valid according to the current state of the board (considering row, column, and subgrid constraints).
3.  Select the cell with the *smallest* number of valid remaining values.
4.  Try assigning one of its valid values.
5.  Propagate constraints (update domains of affected cells).
6.  Recursively call the solver.
7.  If it fails, backtrack and try a different value for the selected cell.

By choosing the cell with fewest options (e.g., a cell that can only be a '5'), the algorithm quickly determines if that choice is viable or leads to a contradiction.

## When to Use

*   Constraint Satisfaction Problems (CSPs).
*   Backtracking search algorithms.
*   Problems where the order of variable assignment significantly impacts performance (e.g., Sudoku, N-Queens variations, map coloring).

## Advantages

*   **Efficiency:** Often significantly reduces the size of the search space explored compared to naive backtracking.
*   **Early Failure Detection:** Helps identify dead ends sooner, leading to faster pruning.

## Disadvantages

*   **Overhead:** Requires maintaining and updating the domains of unassigned variables, which adds computational overhead compared to simpler selection strategies.
*   **Tie-breaking:** A tie-breaking rule might be needed if multiple variables have the same minimum number of remaining values (e.g., select the one involved in the most constraints - Degree Heuristic).

## Related Concepts

*   Backtracking Search
*   Constraint Satisfaction Problems (CSPs)
*   Constraint Propagation
*   Heuristics
*   Least Constraining Value (LCV) Heuristic (often used for value selection after MRV selects the variable)
*   Degree Heuristic (often used as a tie-breaker for MRV) 