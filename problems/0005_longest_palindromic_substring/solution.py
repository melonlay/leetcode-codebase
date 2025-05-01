class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        longest_start = 0
        max_len = 1  # A single character is the minimum palindrome

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            # Expands around the center defined by left and right pointers
            # Returns the start index and length of the palindrome found
            l, r = left, right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # The actual palindrome is s[l+1:r]
            return l + 1, r - (l + 1)

        for i in range(n):
            # Odd length palindromes (center at i)
            start1, len1 = expand_around_center(i, i)
            if len1 > max_len:
                max_len = len1
                longest_start = start1

            # Even length palindromes (center between i and i+1)
            start2, len2 = expand_around_center(i, i + 1)
            if len2 > max_len:
                max_len = len2
                longest_start = start2

        return s[longest_start: longest_start + max_len]
