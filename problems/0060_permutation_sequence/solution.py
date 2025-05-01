import math
from typing import List


class Solution:
    """Solves LeetCode problem 60: Permutation Sequence."""

    def getPermutation(self, n: int, k: int) -> str:
        """Calculates the k-th lexicographical permutation of numbers 1 to n.

        Args:
            n: The upper bound of the numbers (inclusive).
            k: The 1-based index of the desired permutation.

        Returns:
            The k-th permutation sequence as a string.
        """
        factorials = [1] * (n + 1)
        for i in range(2, n + 1):
            factorials[i] = factorials[i - 1] * i

        # Available digits (1-based)
        digits = [i for i in range(1, n + 1)]
        result = []

        # Adjust k to be 0-based for calculations
        k -= 1

        for i in range(n, 0, -1):
            # Determine the index of the digit to pick
            fact = factorials[i - 1]
            index = k // fact

            # Append the chosen digit
            result.append(str(digits.pop(index)))

            # Update k for the next iteration (remainder)
            k %= fact

        return "".join(result)
