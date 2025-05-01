class Solution:
    def reverse(self, x: int) -> int:
        """Reverses the digits of a signed 32-bit integer.

        Returns 0 if the reversed integer overflows the 32-bit signed range.
        """
        INT_MAX = 2**31 - 1
        # INT_MIN = -2**31 # Not explicitly needed for check

        sign = 1 if x >= 0 else -1
        x_abs = abs(x)

        reversed_num = 0
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10

            # Check for potential positive overflow BEFORE modifying reversed_num
            # If reversed_num > INT_MAX / 10, then reversed_num * 10 will overflow
            # If reversed_num == INT_MAX / 10, then reversed_num * 10 + digit will overflow
            # if digit > 7 (since INT_MAX ends in 7)
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
