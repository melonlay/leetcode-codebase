import collections


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """
        Finds the lexicographically smallest palindromic permutation of s.
        Optimized to reduce intermediate list creation.

        Args:
            s: A palindromic string.

        Returns:
            The lexicographically smallest palindromic permutation of s.
        """
        counts = collections.Counter(s)
        first_half = []
        middle_char = ""

        # Build the first half (H) with smallest characters, appending char by char
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            count = counts[char]
            if count > 0:
                num_to_add = count // 2
                for _ in range(num_to_add):
                    first_half.append(char)  # Append character directly

                if count % 2 == 1:
                    middle_char = char

        # Construct the full palindrome using reversed() iterator
        first_half_str = "".join(first_half)
        # Use reversed() iterator instead of slicing [::-1]
        second_half_str = "".join(reversed(first_half))

        return first_half_str + middle_char + second_half_str
