import collections
from typing import List


class Solution:
    """ Solves LeetCode 3527: Find the Most Common Response. """

    def findCommonResponse(self, responses: List[List[str]]) -> str:
        """Finds the most frequent response across all days after deduplication.

        Deduplicates responses within each day, then aggregates frequencies
        across all days using a Counter. Finds the maximum frequency and returns
        the lexicographically smallest response among those with the max frequency.

        Args:
            responses: A 2D list of strings representing daily survey responses.

        Returns:
            The lexicographically smallest, most common response.
        """
        overall_freq = collections.Counter()

        for daily_responses in responses:
            unique_daily_responses = set(daily_responses)
            for resp in unique_daily_responses:
                overall_freq[resp] += 1

        if not overall_freq:
            # Should not happen based on constraints, but handle defensively
            return ""

        max_freq = 0
        most_common_resp = ""

        # Find max frequency first
        for freq in overall_freq.values():
            if freq > max_freq:
                max_freq = freq

        # Find the lexicographically smallest response with max frequency
        for resp, freq in overall_freq.items():
            if freq == max_freq:
                if most_common_resp == "" or resp < most_common_resp:
                    most_common_resp = resp

        return most_common_resp
