# 3522. Calculate Score After Performing Instructions

## Problem Summary

Given two arrays, `instructions` (containing "add" or "jump") and `values`, both of size `n`, simulate a process starting at index `i = 0` with `score = 0`.

**Rules:**
1.  If `instructions[i]` is "add": Add `values[i]` to `score`, move to index `i + 1`.
2.  If `instructions[i]` is "jump": Move to index `i + values[i]` without changing `score`.

**Termination:** The process stops if:
*   The current index `i` goes out of bounds (`i < 0` or `i >= n`).
*   An attempt is made to revisit an instruction index that has already been executed.

Return the final `score` when the process terminates.

## Approach: Direct Simulation

The problem description directly maps to a simulation algorithm. We can track the state (current index, current score) and use a set to detect revisited indices.

**Algorithm:**

1.  Initialize `current_index = 0`, `score = 0`.
2.  Initialize an empty set `visited` to store the indices of instructions that have been executed.
3.  Start a loop that continues indefinitely (`while True`) until a termination condition is met.
4.  **Inside the loop:**
    *   **Check Termination:**
        *   If `current_index < 0` or `current_index >= n` (out of bounds), break the loop.
        *   If `current_index` is already in the `visited` set (revisited index), break the loop.
    *   **Mark Visited:** Add `current_index` to the `visited` set.
    *   **Execute Instruction:**
        *   Get `instruction = instructions[current_index]` and `value = values[current_index]`.
        *   If `instruction == "add"`:
            *   Increment `score` by `value`.
            *   Increment `current_index` by 1.
        *   Else (`instruction == "jump"`):
            *   Increment `current_index` by `value`.
5.  **Return `score`** after the loop terminates.

## Complexity Analysis

*   **Time Complexity:** `O(n)`
    *   In the worst case, the simulation loop executes at most `n` times because each index from `0` to `n-1` can be visited at most once before the process terminates (due to the revisit rule).
    *   Inside the loop, checking bounds, set lookup (`in visited`), set insertion (`add`), array indexing, and arithmetic operations are all O(1) on average.
*   **Space Complexity:** `O(n)`
    *   The `visited` set stores the indices of executed instructions. In the worst case, it might store up to `n` distinct indices.

## Foundational Components

*   **Set:** Used for O(1) average time complexity detection of revisited indices. See [[../../document/data_structures/hash_table_dict.md]] (conceptual basis).
*   **Simulation:** The core approach follows the problem rules directly.

This approach is optimal given the constraints. 