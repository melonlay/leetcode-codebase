# Solution Explanation: LeetCode 3527 - Find the Most Common Response

## 1. Problem Summary

Given a 2D list of daily survey responses, find the response that occurs most frequently across all days, considering each response only once per day. If there's a tie in frequency, return the lexicographically smallest response among the most frequent ones.

## 2. Algorithmic Approach

The solution uses a combination of set-based deduplication per day and hash map-based frequency counting across all days, followed by a two-step process to find the desired response.

1.  **Daily Deduplication and Frequency Aggregation:**
    *   Initialize a `collections.Counter` (a hash map specialized for counting) called `overall_freq`.
    *   Iterate through each `daily_responses` list in the input `responses`.
    *   Convert `daily_responses` to a `set` to get the unique responses for that day. Sets provide efficient deduplication. See [[../document/data_structures/hash_set.md]] (assuming this covers set basics).
    *   Iterate through the unique responses in the set.
    *   Increment the count for each unique response in the `overall_freq` counter. This accumulates the frequency, ensuring each response contributes at most once per day.
    *   The `Counter` effectively uses a hash map. See [[../document/data_structures/hash_table_dict.md]].

2.  **Finding the Most Common Response with Tie-breaking:**
    *   Identify the maximum frequency (`max_freq`) present in the `overall_freq` counter by iterating through its values.
    *   Iterate through the `(response, frequency)` pairs in `overall_freq`.
    *   Select the response that:
        *   Has a frequency equal to `max_freq` (Primary Criterion).
        *   Is lexicographically the smallest among all responses meeting the primary criterion (Secondary Criterion).
    *   This selection process follows the pattern described in [[../document/techniques/comparison/find_best_by_primary_secondary_criteria.md]].

## 3. Complexity Analysis

*   **Time Complexity:** O(T * L), where T is the total number of responses across all days *before* deduplication (`sum(len(day) for day in responses)`), and L is the maximum length of a response string (average time for hashing/comparison). Building sets and the counter involves processing roughly T elements.
*   **Space Complexity:** O(U * L), where U is the number of unique responses across all days *after* daily deduplication, to store the `overall_freq` counter. An additional O(M_unique * L) space is used temporarily for the set within the loop, where M_unique is the max number of unique responses in a single day.

## 4. Knowledge Base Links

*   **Data Structures:**
    *   [[../document/data_structures/hash_table_dict.md]] (Covers `dict` and `collections.Counter`)
    *   [[../document/data_structures/hash_set.md]] (Covers `set` for deduplication)
*   **Techniques:**
    *   [[../document/techniques/comparison/find_best_by_primary_secondary_criteria.md]] (Describes the tie-breaking logic) 