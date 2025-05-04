import math
from typing import List


class Solution:
    """
    Solves the Maximum Product of Two Digits problem.
    """

    def maximumProduct(self, n: int) -> int:
        """
        Finds the maximum product of any two digits in the integer n.

        Args:
            n: The positive integer input.

        Returns:
            The maximum product of any two digits in n.
        """
        if n < 10:
            # Should not happen based on constraints, but good practice.
            # Or handle based on specific problem definition if single-digit n were allowed.
            # For this problem, constraints say n >= 10.
            return 0  # Or raise error, depending on exact rules for < 10

        s = str(n)
        digits = [int(digit) for digit in s]

        # Sort the digits in ascending order
        digits.sort()

        # The two largest digits are the last two elements
        # Handles cases like n=22 correctly because both '2's will be in the list
        # Handles cases like n=31 correctly: digits=[1, 3], picks 1 and 3
        # Handles cases like n=124 correctly: digits=[1, 2, 4], picks 2 and 4
        return digits[-1] * digits[-2]
