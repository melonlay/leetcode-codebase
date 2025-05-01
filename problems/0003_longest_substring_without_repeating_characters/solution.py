class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the character at the right pointer is already in the set,
            # shrink the window from the left until the duplicate is removed.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set and expand the window.
            char_set.add(s[right])

            # Update the maximum length found so far.
            max_length = max(max_length, right - left + 1)

        return max_length
