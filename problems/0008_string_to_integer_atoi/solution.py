class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer following atoi rules.
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        index = 0

        # 1. Ignore leading whitespace
        while index < n and s[index] == ' ':
            index += 1

        # If string is empty or contains only whitespace
        if index == n:
            return 0

        # 2. Check for sign
        sign = 1
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        # 3. Convert digits, checking for overflow before multiplication/addition
        result = 0
        while index < n and s[index].isdigit():
            digit = int(s[index])

            # Check for overflow before updating result
            # Check if result > INT_MAX // 10
            # or if result == INT_MAX // 10 and digit > INT_MAX % 10 (which is 7)
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        # 4. Apply sign and return (clamping already handled by overflow check)
        return sign * result
