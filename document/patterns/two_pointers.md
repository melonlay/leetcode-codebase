# Pattern: Two Pointers

## Description

The Two Pointers pattern is a common algorithmic technique used primarily with sequential data structures like arrays or strings. It involves using two index pointers that iterate through the data structure, often interacting with each other, to solve a problem efficiently, typically in linear time (O(n)).

This pattern is versatile and can be adapted for various tasks, including searching, subarray/substring problems, sequence comparison, and problems involving finding pairs or triplets that satisfy certain conditions.

## Core Idea

Instead of nested loops (which often lead to O(n^2) complexity), the two pointers move through the data in a coordinated way, reducing the number of operations required.

The specific movement logic depends heavily on the problem requirements.

## Common Variants

1.  **Opposite Ends (Inward Moving):**
    *   **Initialization:** One pointer starts at the beginning (`left = 0`) and the other at the end (`right = n - 1`).
    *   **Movement:** The pointers move towards each other (`left++`, `right--`) based on conditions related to the elements they point to or some target value.
    *   **Use Cases:** Searching for pairs in a sorted array (e.g., 2-Sum), reversing arrays/strings, finding palindromes, problems where processing from boundaries inward is beneficial (e.g., Trapping Rain Water).
    *   **Example:** In problems like Trapping Rain Water ([Problem 42](../../problems/0042_trapping_rain_water/solution.md)), this variant is used to maintain maximum boundary heights seen so far from both ends (`left_max`, `right_max`), efficiently calculating the trapped water at each step.
    *   **Related:** [Pattern: Find Capacity Between Boundaries](../patterns/array/find_capacity_between_boundaries.md) (often solved using this variant).

2.  **Same Direction (Fast & Slow / Sliding Window):**
    *   **Initialization:** Both pointers often start at or near the beginning.
    *   **Movement:** One pointer (e.g., `fast` or `right`) explores ahead, while the other pointer (e.g., `slow` or `left`) defines the start of a window or sequence.
The `slow` pointer usually advances based on conditions met by the `fast` pointer or the window it defines.
    *   **Use Cases:** Detecting cycles in linked lists, finding the middle of a linked list, solving sliding window problems ([Pattern: Sliding Window](../patterns/sliding_window.md)), finding longest substrings without repeating characters, removing duplicates from sorted arrays.

3.  **Multiple Sequences:**
    *   **Initialization:** Pointers are initialized at the start (or end) of two or more separate sequences (arrays, strings).
    *   **Movement:** Pointers advance through their respective sequences based on comparison results or merging logic.
    *   **Use Cases:** Merging sorted arrays, finding intersections/unions of sorted arrays, comparing strings.

## When to Use

*   Problems involving sorted arrays where pair-finding or target sums are needed.
*   Problems requiring analysis of subarrays or substrings based on certain criteria (often combined with sliding window).
*   Problems where processing elements from both ends inwards simplifies logic or state management.
*   Sequence comparison or merging tasks.
*   Optimizing brute-force solutions that use nested loops on sequences.

## Complexity

*   **Time:** Typically O(n), as each pointer usually traverses the data structure or a portion of it at most once.
*   **Space:** Typically O(1) auxiliary space, as only pointer variables are needed.

## Related Concepts

*   [Pattern: Sliding Window](../patterns/sliding_window.md)
*   Arrays, Strings, Linked Lists 