# Technique: In-Place Array Hashing

## Description

In-Place Array Hashing is a technique used to store frequency information or mark the presence/absence of elements within a limited range directly within the input array/sequence itself, without using extra space for a separate hash map or frequency array. This is particularly useful when the element values are constrained, and modifying the input sequence is allowed.

The core idea is to use the array indices as hash keys and modify the values at those indices (often using sign changes or arithmetic operations involving the array size) to store information.

## Core Idea & Common Variants

Given an array `nums` of size `n`, where elements are typically within a specific range (e.g., `1` to `n`, or positive integers).

1.  **Using Sign as Presence Marker (Range `1` to `n`):**
    *   **Goal:** Find duplicates or missing numbers in an array where elements should be `1` to `n`.
    *   **Logic:** Iterate through `nums`. For each number `num`, get the corresponding index `index = abs(num) - 1`. If `nums[index]` is positive, flip its sign (`nums[index] = -nums[index]`) to mark that the number `abs(num)` has been seen. If `nums[index]` is already negative, it means `abs(num)` is a duplicate.
    *   **Finding Missing:** After the first pass, iterate again. If `nums[i]` is positive, it means the number `i + 1` was never encountered, so it's missing.
    *   **Constraint:** Requires numbers to be positive and within the range `[1, n]` so they map to valid indices `[0, n-1]`.

2.  **Using Modulo Arithmetic for Frequency (Positive Integers):**
    *   **Goal:** Store frequency counts or mark presence when sign flipping isn't enough or range isn't `1` to `n`.
    *   **Logic:** Iterate through `nums`. For each `num`, use the index `index = num % n` (assuming values relate to indices modulo `n`). To mark the presence or increase frequency count for `index`, add `n` to the value at that index: `nums[index] = nums[index] + n`.
    *   **Retrieving Information:** After the first pass, iterate again. The original value at index `i` is `nums[i] % n`. The frequency count (or presence marker) is `nums[i] // n`.
    *   **Constraint:** Relies on values being large enough relative to `n` so that adding `n` doesn't cause overflow issues and that the original value can be recovered via modulo. Requires careful handling if original numbers can be `>= n`.

## When to Use

*   Strict space complexity constraints (O(1) auxiliary space required).
*   The problem allows modification of the input sequence.
*   Sequence values are within a range that can be mapped predictably to sequence indices (e.g., `1` to `n`, or usable with modulo).
*   Problems like finding duplicates, finding the first missing positive, finding missing numbers in a range.

## Tradeoffs

*   **Space:** Excellent O(1) auxiliary space complexity.
*   **Input Modification:** Destroys the original content of the sequence.
*   **Constraints:** Highly dependent on the range and nature of sequence values. Cannot be used if values are negative (without offset), zero, or too large for modulo arithmetic tricks.
*   **Readability:** Can be less intuitive than using an explicit hash map or frequency array.

## Examples

*   LeetCode 448: Find All Numbers Disappeared in an Array (Sign flipping)
*   LeetCode 442: Find All Duplicates in an Array (Sign flipping)
*   LeetCode 41: First Missing Positive (Sign flipping / value placement)
*   LeetCode 287: Find the Duplicate Number (Can also be solved this way, though cycle detection is more common).

## Related Concepts

*   Hashing
*   Array/Sequence Manipulation
*   Modulo Arithmetic 