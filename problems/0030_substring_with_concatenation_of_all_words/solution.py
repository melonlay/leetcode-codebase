import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """Finds all starting indices of substrings in s that are a concatenation
           of all words in `words` exactly once, in any order.
           Uses the standard sliding window approach.
        """
        if not s or not words or not words[0]:
            return []

        n = len(s)
        num_words = len(words)
        word_len = len(words[0])
        total_len = num_words * word_len

        if n < total_len:
            return []

        word_freq = collections.Counter(words)
        result = []

        for start in range(word_len):
            left = start
            count = 0  # Number of words from word_freq found so far in the window
            seen = collections.Counter()

            # Iterate with the right end of the window (j)
            for j in range(start, n - word_len + 1, word_len):
                word = s[j: j + word_len]

                if word in word_freq:
                    seen[word] += 1
                    count += 1

                    # If we've seen too many of this word, shrink window from left
                    while seen[word] > word_freq[word]:
                        left_word = s[left: left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If we have found exactly the right number of words
                    if count == num_words:
                        result.append(left)
                        # Slide the window forward: remove the leftmost word
                        # This prepares the window for the next iteration j
                        # NOTE: This step prevents finding certain overlapping matches (e.g., "ababaab")
                        left_word = s[left: left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # Word not in word_freq, reset the window
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result  # Return list directly, duplicates shouldn't occur with this logic
