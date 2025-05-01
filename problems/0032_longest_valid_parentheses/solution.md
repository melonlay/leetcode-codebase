## Problem Summary

Given a string `s` containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

## Algorithmic Approach

The problem can be efficiently solved using a **Stack**. The stack stores the *indices* of the characters in the string. Specifically, it helps track the indices of potential starting points for valid parentheses substrings.

## Logic Explanation

1.  **Initialization:**
    *   Initialize `max_length = 0` to store the maximum length found so far.
    *   Initialize a stack `stack = [-1]`. Pushing `-1` onto the stack initially serves as a sentinel value or a base index. It simplifies the length calculation: if we find a valid pair closing at index `i`, the length is `i - stack[-1]` (the index just *before* the matching opening parenthesis).

2.  **Iteration:**
    *   Iterate through the string `s` with index `i` and character `char`.
    *   **Case 1: `char == '('`:**
        *   Push the current index `i` onto the stack. This marks a potential start of a valid substring.
    *   **Case 2: `char == ')'`:**
        *   Pop the top element from the stack. This element represents the index of the most recently encountered unmatched opening parenthesis `'('`.
        *   **Subcase 2.a: Stack becomes empty after pop:**
            *   This means the current closing parenthesis `')'` at index `i` does not have a matching opening parenthesis (the stack only contained the base `-1` or indices of previous unmatched `')'`).
            *   Push the current index `i` onto the stack. This index now acts as the new base, marking the position *after* the end of the last valid sequence (or the start of the string if no valid sequence occurred).
        *   **Subcase 2.b: Stack is not empty after pop:**
            *   This means the popped element was the index of a matching `'('`. The element now at the top of the stack (`stack[-1]`) is the index *just before* the start of the currently completed valid substring.
            *   Calculate the length of this valid substring: `current_length = i - stack[-1]`.
            *   Update the overall maximum length: `max_length = max(max_length, current_length)`.

3.  **Return Result:** After iterating through the entire string, return `max_length`.

## Knowledge Base References

*   **Stack Data Structure:** The core of the solution relies on the LIFO property of stacks. See `document/data_structures/stack.md`.
*   **Stack for Parentheses Matching/Index Tracking:** While basic parentheses matching often just checks validity, this solution uses the stack to store *indices*, allowing length calculation. This technique is somewhat related to finding previous smaller/greater elements but applied differently here. A more specific pattern covering this index-based length calculation might be `document/patterns/stack_index_tracking_for_subsequences.md`, although the primary use here is finding the *boundary* index before the current valid sequence.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string once.
*   **Space Complexity:** O(N). In the worst case (e.g., a string of all opening parentheses `((((...`), the stack could store up to N indices. 