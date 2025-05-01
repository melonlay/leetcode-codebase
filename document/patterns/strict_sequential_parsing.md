# Pattern: Strict Sequential Parsing

## Context

Some string parsing problems, like implementing C-style `atoi` (String to Integer), require processing characters strictly sequentially according to a predefined set of rules or states. Unlike more flexible parsing, the process often terminates immediately upon encountering the first character that violates the expected sequence or character type for the current state.

## Core Idea

1.  **State Machine (Implicit or Explicit):** The parsing follows a simple state machine logic. Common states include:
    *   Initial/Leading Whitespace
    *   Sign Detection
    *   Digit Accumulation
    *   Termination
2.  **Sequential Processing:** Iterate through the string character by character, usually with an index pointer.
3.  **Strict Transitions:** Transitions between states are governed by strict rules.
    *   Leading whitespace is skipped.
    *   An optional sign (`+` or `-`) is consumed *only* immediately after whitespace (or at the start).
    *   Digits are accumulated into a result *only* immediately after optional whitespace/sign.
4.  **Early Termination:** Processing stops as soon as a character is encountered that is not valid for the *current* state (e.g., a letter encountered during digit accumulation, whitespace encountered after a sign but before digits).
5.  **Edge Case Handling:** Need careful handling of empty strings, strings with only whitespace, strings with only signs, and values exceeding numerical limits (often requiring pre-emptive checks).

## Example: Simplified `atoi` Logic

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        n = len(s)
        index = 0
        sign = 1
        result = 0

        # State 1: Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1

        # State 2: Check for optional sign
        if index < n and s[index] in ['+', '-']:
            if s[index] == '-':
                sign = -1
            index += 1
        # If anything else is encountered here (e.g., " +-1", space after sign), 
        # the next state won't find digits, resulting in 0.

        # State 3: Accumulate digits & check overflow
        while index < n and s[index].isdigit():
            digit = int(s[index])

            # Pre-emptive overflow check (see integer_overflow_check.md)
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            index += 1
        # Loop terminates immediately on first non-digit.

        # State 4: Final result
        return sign * result

```

## Applicability

This pattern is crucial for problems requiring precise emulation of specific, often legacy, parsing behaviors where flexibility is not allowed, and the sequence of character types matters significantly.

## Common Pitfalls

*   Incorrect state transitions (e.g., allowing digits before a sign is processed).
*   Not handling early termination correctly (reading past the first invalid character).
*   Missing overflow/underflow checks during digit accumulation.
*   Incorrectly handling edge cases like empty strings or strings containing only non-digit characters after whitespace/sign.
*   Misinterpreting rules about what constitutes an invalid sequence (e.g., `" +-1"` should typically result in `0` because the space after the `+` terminates the parsing before digits are found). 