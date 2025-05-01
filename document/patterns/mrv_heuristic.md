# Pattern: Minimum Remaining Values (MRV) Heuristic

## General Description

The Minimum Remaining Values (MRV) heuristic is a common optimization strategy used within backtracking algorithms (see `document/algorithms/recursion/backtracking.md`) for solving Constraint Satisfaction Problems (CSPs).

It aims to prune the search tree more effectively by prioritizing the order in which decisions (variable assignments) are made.

## Core Idea

Choose the variable (or decision point) that has the *fewest* remaining legal values (possible choices) first.

Rationale: By tackling the most constrained variable early, the algorithm is more likely to encounter constraint violations sooner if a partial solution is on an incorrect path. This leads to earlier backtracking and avoids exploring large subtrees that are guaranteed to fail.

## How it Works

1.  **Identify Choices:** Determine the next set of variables that need assignment (e.g., empty cells in Sudoku).
2.  **Calculate Possibilities:** For each variable in the set, calculate the number of currently valid values it can take, considering existing constraints.
3.  **Select Minimum:** Choose the variable with the minimum number of possible values.
4.  **(Optional Tie-breaking):** If multiple variables have the same minimum number, other heuristics (like the Degree Heuristic - choosing the variable involved in the most constraints with other unassigned variables) can be used.
5.  **Proceed:** Use the selected variable as the next decision point in the backtracking search.

## Benefits

*   Significantly reduces the size of the explored search space compared to naive backtracking.
*   Often leads to much faster solutions for complex CSPs.

## Implementation Considerations

*   Requires an efficient way to calculate the number of remaining values for each potential choice. This might involve checking against current constraint sets or using specialized data structures (e.g., bitmasks - see `document/patterns/bitmask_constraint_tracking.md`).
*   The overhead of calculating possibilities needs to be balanced against the pruning benefit.

## Illustrative Example: Sudoku Solver Optimization

In the optimized Sudoku solver (`problems/0037_sudoku_solver/solution.py`), the `find_best_empty_cell` function implements MRV:

1.  It iterates through all currently `empty_cells`.
2.  For each cell `(r, c)`, it calculates the `possible_mask` using current row, column, and box constraints (often stored as bitmasks).
3.  It counts the number of set bits in `possible_mask` (using `count_set_bits`) to find the number of legal digits for that cell.
4.  It keeps track of the cell `(r, c, idx)` that has the minimum count of possible values.
5.  The backtracking function then proceeds to try assigning values only to this chosen cell.

```python
# Snippet from Sudoku Solver illustrating MRV
def find_best_empty_cell():
    min_possibilities = 10
    best_cell_info = None # Store (r, c, index)

    for i, (r, c) in enumerate(empty_cells):
        possible_mask = get_possible_values(r, c)
        num_possibilities = count_set_bits(possible_mask)

        if num_possibilities == 0:
            return None, -1 # Conflict

        if num_possibilities < min_possibilities:
            min_possibilities = num_possibilities
            best_cell_info = (r, c, i)
            if min_possibilities == 1:
                 break # Early exit optimization

    return best_cell_info, min_possibilities

def backtrack():
    # ... setup ...
    best_cell_info, _ = find_best_empty_cell()
    if best_cell_info is None:
        # ... handle end/conflict ...

    r, c, idx = best_cell_info
    cell_to_process = empty_cells.pop(idx) # Process only the chosen cell

    # ... try assignments for (r, c) ...

    empty_cells.insert(idx, cell_to_process) # Restore list state
    return False 