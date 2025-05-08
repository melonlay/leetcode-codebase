import math


class Solution:
    """
    Determines which person (1 at x or 2 at y) reaches person 3 (at z) first.
    """

    def solve(self, x: int, y: int, z: int) -> int:
        """
        Calculates the time for each person to reach z and compares them.

        Args:
            x: Position of Person 1.
            y: Position of Person 2.
            z: Position of Person 3 (target).

        Returns:
            1 if Person 1 is faster, 2 if Person 2 is faster, 0 if equal time.
        """
        time1 = abs(z - x)
        time2 = abs(z - y)

        if time1 < time2:
            return 1
        elif time2 < time1:
            return 2
        else:
            return 0
