# Pattern: Stack Index Tracking for Subsequence Analysis

## General Description

This algorithmic pattern uses a **Stack** data structure (see `document/data_structures/stack.md`) during sequence traversal to store element *indices* rather than the elements themselves. This is effective for analyzing properties (like length, boundaries) of subsequences defined by related start/end markers (e.g., brackets) or identifying relationships based on position.

## Core Algorithmic Technique

This technique leverages the LIFO property of a stack combined with index storage:

1.  **Initialization:** Initialize a stack, typically pushing a sentinel index (e.g., -1) onto it. This sentinel acts as a base reference, simplifying calculations for subsequences that start at the beginning of the main sequence.
2.  **Traversal & Index Pushing:** Iterate through the input sequence. When an element signifying the potential start of a relevant subsequence is found, push its *index* onto the stack.
3.  **Index Popping & Analysis:** When an element signifying the potential end of a relevant subsequence is found:
    *   Check if the stack top holds the index of a corresponding start element (based on problem rules).
    *   If yes, **pop** the start index.
    *   **Key Calculation:** The crucial step is often calculating the difference between the *current element's index* and the index *now revealed at the top of the stack* (`stack[-1]`). This difference frequently represents a property (e.g., length) of the valid subsequence that was just completed. The index at `stack[-1]` marks the boundary just before this subsequence.
    *   Use this calculated property to update the overall result (e.g., tracking the maximum length).
4.  **Handling Mismatches/Boundaries:** If an end element is found without a corresponding start index on the stack (or the stack becomes empty after a pop), it indicates an invalid sequence or a boundary. The common strategy is to **push** the *current element's index* onto the stack. This index then serves as the new sentinel or boundary marker for subsequent calculations.

## Benefits

*   Provides an efficient O(N) time complexity solution for many subsequence analysis problems.
*   Naturally handles nested structures due to the LIFO nature of the stack.

## Pitfalls

*   **Off-by-one errors:** Precision is required when defining the sentinel value and calculating lengths based on `i - stack[-1]`.
*   **Empty Stack Logic:** Correctly implementing the behavior when a pop occurs on an empty or sentinel-only stack (often pushing the current index `i`) is vital for resetting calculations accurately.

## Example Application: LeetCode 32 - Longest Valid Parentheses

*   **Problem:** Find the length of the longest substring of valid (well-formed) parentheses.
*   **Applying the Pattern:**
    *   Initialize `stack = [-1]`. Stores indices of `'('`.
    *   Iterate through `s` at index `i`.
    *   If `s[i] == '('`, `stack.append(i)`.
    *   If `s[i] == ')'`:
        *   `stack.pop()`.
        *   If `stack` is empty: `stack.append(i)` (This `')'` marks a new boundary).
        *   If `stack` is not empty: `current_length = i - stack[-1]`. Update `max_length = max(max_length, current_length)`.
*   **Result:** `max_length` holds the answer. 