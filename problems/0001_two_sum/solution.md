# LeetCode 1: Two Sum - Solution Explanation

## Problem Summary

Given an array of integers `nums` and an integer `target`, find the indices of the two numbers such that they add up to `target`. Assume that each input has exactly one solution, and you may not use the same element twice.

## Algorithmic Approach

The most efficient approach for this problem involves using a hash map (dictionary in Python) to store the numbers encountered so far and their corresponding indices. This allows for quick lookups to find the required complement for each number.

## Logic Explanation

1.  **Initialization:** Create an empty dictionary `num_map` to store `{number: index}` pairs.
2.  **Iteration:** Iterate through the input list `nums` using enumeration to get both the index `i` and the value `num`.
3.  **Complement Calculation:** For each `num`, calculate the `complement` needed to reach the `target` (`complement = target - num`).
4.  **Lookup:** Check if the `complement` exists as a key in the `num_map`.
    *   **If found:** This means the complement number was encountered earlier in the list. Return the index stored in the map for the complement (`num_map[complement]`) and the current index `i`.
    *   **If not found:** Add the current number `num` and its index `i` to the `num_map`. This stores the current number for potential future lookups if it turns out to be the complement for a later number in the list.
5.  **No Solution (Theoretical):** Based on the problem constraints (exactly one solution), the function should always find a pair and return within the loop. An empty list return is included as a fallback but shouldn't be reached.

## Knowledge Base References

*   **Hash Map Lookup Pattern:** The core strategy relies on the hash map lookup pattern to achieve efficient O(1) average time complexity for checking if the complement exists. This pattern is detailed in `document/patterns/hash_map_lookup.md`.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the number of elements in the `nums` list. We iterate through the list once, and hash map insertion and lookup operations take O(1) on average.
*   **Space Complexity:** O(N), as in the worst-case scenario, the `num_map` might store up to N elements if the solution pair is found near the end of the list. 