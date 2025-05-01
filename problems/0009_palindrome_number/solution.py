class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Checks if an integer is a palindrome without converting it to a string.

        Args:
            x: The integer to check.

        Returns:
            True if x is a palindrome, False otherwise.
        """
        # Negative numbers are not palindromes
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Handle single-digit numbers (which are always palindromes)
        if x < 10:
            return True

        reversed_half = 0
        original_num = x

        # Reverse the second half of the number
        while original_num > reversed_half:
            digit = original_num % 10
            reversed_half = reversed_half * 10 + digit
            original_num //= 10

        # When the length is an odd number, we can get rid of the middle digit by division.
        # For example when the input is 12321, at the end of the while loop we get
        # original_num = 12, reversed_half = 123.
        # Since the middle digit doesn't matter in palidrome(it will always equal to itself),
        # we can simply remove it by original_num == reversed_half // 10.
        # When the length is an even number, original_num and reversed_half will be equal.
        # For example when the input is 1221, at the end of the while loop we get
        # original_num = 12, reversed_half = 12.
        return original_num == reversed_half or original_num == reversed_half // 10
