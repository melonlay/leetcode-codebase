# Algorithm: Backtracking

## General Description

Backtracking is a general algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point in time (backtracking).

It explores the solution space by constructing a state-space tree. Each node in the tree represents a partial solution. The algorithm explores branches of this tree. If a branch leads to a dead end (violates constraints or cannot be completed), the algorithm backtracks to the previous node and explores a different branch.

## Core Algorithm/Mechanism

1.  **Choice:** Identify a set of choices for the next step in building the solution.
2.  **Constraint:** Define constraints that a partial solution must satisfy.
3.  **Goal:** Define the criteria for a complete, valid solution.

A typical recursive structure:

```python
def backtrack(state):
    if is_goal_state(state):
        # Found a solution
        record_solution(state)
        return True # Or False if exploring all solutions

    for choice in generate_valid_choices(state):
        # Apply choice
        new_state = apply_choice(state, choice)

        # Recurse
        if backtrack(new_state):
            return True # Found solution down this path

        # Backtrack: Undo choice (critical step)
        undo_choice(state, choice) # Restore state

    # No valid choice from this state leads to a solution
    return False
```

*   `state`: Represents the current partial solution and relevant context.
*   `is_goal_state`: Checks if the current state represents a complete solution.
*   `generate_valid_choices`: Returns possible next steps that satisfy constraints *at the current stage*.
*   `apply_choice`: Modifies the state to incorporate the choice.
*   `undo_choice`: Reverts the state changes made by `apply_choice`. This is crucial for exploring other branches.

## Complexity

*   **Time Complexity:** Often exponential in the worst case (e.g., O(b^d), where b is the branching factor and d is the depth of the state-space tree). The actual performance heavily depends on the effectiveness of pruning (eliminating invalid choices early).
*   **Space Complexity:** Typically O(d) for the recursion stack, plus space needed to store the state.

## Optimizations

*   **Heuristics:** Use rules to prioritize certain choices over others (e.g., [[./mrv_heuristic.md|Minimum Remaining Values (MRV)]]).
*   **Constraint Propagation:** Update constraints proactively based on choices made.
*   **Pruning:** Identify and eliminate branches that cannot possibly lead to a solution as early as possible.

## Common Applications

*   Generating permutations and combinations.
*   Constraint Satisfaction Problems (CSP) like Sudoku (see `problems/0037_sudoku_solver`), N-Queens.
*   Pathfinding in graphs/mazes.
*   Parsing.

## Illustrative Example: Sudoku Solver (Simple Version)

The initial, non-optimized Sudoku solver demonstrates backtracking:
*   `state`: The Sudoku board, current sets of used numbers.
*   `choice`: Trying digits 1-9 for the next empty cell.
*   `constraint`: `is_valid` check (number not in row, col, box).
*   `goal`: All empty cells are filled.
*   `apply_choice`: Place digit, update sets.
*   `undo_choice`: Remove digit (set back to '.'), remove from sets.

(See `problems/0037_sudoku_solver/solution.py` for the optimized version using MRV and bitmasks).

## Illustrative Example: N-Queens Problem

Place N queens on an N x N board so none attack each other.
*   `state`: Current row index `row`, placement of queens in previous rows (`queen_cols` list), sets tracking occupied columns and diagonals (`occupied_cols`, `occupied_pos_diagonals`, `occupied_neg_diagonals`).
*   `choice`: Choosing a column `col` for the queen in the current `row`.
*   `constraint`: Check if `col` is in `occupied_cols`, `row + col` is in `occupied_pos_diagonals`, or `row - col` is in `occupied_neg_diagonals`. These O(1) checks using sets are crucial for efficiency.
*   `goal`: `row == N` (all rows filled).
*   `apply_choice`: Set `queen_cols[row] = col`, add `col`, `row + col`, `row - col` to respective sets.
*   `undo_choice`: Remove `col`, `row + col`, `row - col` from sets.

(See `problems/0051_n_queens/solution.py` for full implementation). 