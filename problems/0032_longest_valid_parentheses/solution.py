class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """Calculates the length of the longest valid parentheses substring.

        Uses a stack to keep track of the indices of opening parentheses.
        The stack stores indices, initialized with -1.
        When ')' is encountered and matches a '(' from the stack, the length
        is calculated as the difference between the current index and the
        index at the top of the stack *after* popping.
        If ')' is encountered without a matching '(', its index is pushed.
        """
        max_length = 0
        # Stack stores indices. Initialize with -1 as a base for length calculation.
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                # Pop the last opening bracket's index if available
                stack.pop()
                if not stack:
                    # If stack is empty, push current index as the new base
                    # for future length calculations. This index marks the end
                    # of the last valid sequence or the start of an invalid one.
                    stack.append(i)
                else:
                    # Calculate length from current index to the index
                    # before the matching '('
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)

        return max_length
