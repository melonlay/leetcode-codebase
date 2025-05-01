# Technique: Strict Sequential Parsing

## Description

Strict Sequential Parsing refers to processing a sequence (like a string or array) element by element, where the interpretation or action taken at the current element depends strictly on the immediately preceding elements or a very localized state derived from them. There's often little need to look far ahead or far behind, beyond what's necessary to interpret the current local structure.

This contrasts with techniques like sliding windows (which look at variable-sized contiguous blocks) or dynamic programming (which might build solutions based on results from arbitrarily earlier subproblems).

## Core Idea

Maintain a minimal state based on the elements just processed. Iterate through the sequence, updating the state and taking actions based on the current element and the current state. The key is that the decision-making horizon is very short.

## Examples & Use Cases

1.  **Basic String to Integer Conversion (`atoi`):**
    *   Iterate through the string.
    *   Skip leading whitespace (state: `skipping_whitespace`).
    *   Identify an optional sign (`+` or `-`) (state: `found_sign`). Store the sign.
    *   Read consecutive digits, building the number (state: `reading_digits`). Multiply the current result by 10 and add the new digit. Check for overflow at each step.
    *   Stop when a non-digit character is encountered or the string ends.
    *   The action at each character depends only on its type (whitespace, sign, digit, other) and the simple state.

2.  **Validating Parentheses/Brackets:**
    *   Use a stack to track opening brackets.
    *   Iterate through the string.
    *   If an opening bracket `(`, `{`, `[` is found, push it onto the stack.
    *   If a closing bracket `)`, `}`, `]` is found:
        *   Check if the stack is empty (invalid).
        *   Pop the top element from the stack.
        *   Check if the popped opening bracket matches the current closing bracket (invalid if not).
    *   The validity check at each closing bracket depends only on the *last* unmatched opening bracket (top of the stack).
    *   After the loop, the stack must be empty for the string to be valid.

3.  **Roman to Integer Conversion:**
    *   Iterate through the Roman numeral string.
    *   The value of the current character depends on the *next* character.
    *   If `value(current) < value(next)`, subtract `value(current)` (e.g., 'IV' is 5 - 1 = 4).
    *   Otherwise, add `value(current)`.
    *   Requires looking ahead just one character.

4.  **Simple State Machines:** Parsing basic patterns or commands where the next state depends only on the current state and the current input symbol.

## When to Use

*   Problems involving direct translation or validation of sequences based on local rules.
*   Parsing simple, well-defined formats.
*   When the decision at step `i` primarily depends on step `i-1` or a very small, fixed-size lookback/lookahead.
*   Implementing basic state machines for sequence processing.

## Characteristics

*   **Linear Time:** Typically O(n), as the sequence is processed once.
*   **Low Space:** Often O(1) or O(k) where k is small (like stack depth for parentheses), as complex state or large lookback tables are not needed.
*   **Simplicity:** Can lead to straightforward iterative code.

## Related Concepts

*   Finite State Machines (FSM)
*   String/Array Manipulation
*   [Data Structure: Stack](../../data_structures/stack.md) (often used to manage local context) 