# Pattern: Meet-in-the-Middle

**Related Paradigms:** [[divide_and_conquer.md]], Brute Force

## Description

Meet-in-the-Middle (MitM) is an algorithmic technique that improves the performance of brute-force searches, typically reducing exponential time complexity from O(X^N) to roughly O(X^(N/2)). It's often applicable to problems involving finding subsets, combinations, or states that satisfy a certain target condition, especially when the constraint `N` (e.g., number of items) is moderately large (e.g., 30-50), making O(X^N) infeasible but O(X^(N/2)) feasible.

## Core Idea

1.  **Divide:** Split the problem input (e.g., a set of `N` elements) into two roughly equal halves (size `N/2`).
2.  **Generate Independently:** Generate all possible states, sums, or combinations for *each half separately*. This involves performing the brute-force or exponential-time computation on the smaller `N/2` sized inputs. Store the results for each half, often in hash maps or sorted lists.
3.  **Combine / Meet:** Combine the results from the two halves to find the overall solution. This "meeting" step usually involves iterating through the results of one half and efficiently searching (e.g., using binary search on a sorted list or hash map lookups) in the results of the other half for a complementary state that satisfies the target condition. **The efficiency of this combination step is often critical to the overall performance, and different strategies may exist (see below).**

## Algorithm Steps (Generalized - Subset Sum Example)

**Problem:** Given a set `S` of `N` numbers, find if there's a subset that sums to `T`.

1.  **Divide:** Split `S` into `S1` (first N/2 elements) and `S2` (remaining elements).
2.  **Generate Left Sums:** Calculate all possible subset sums of `S1`. Store them (e.g., in a set `sums1`). Time: O(2^(N/2)).
3.  **Generate Right Sums:** Calculate all possible subset sums of `S2`. Store them (e.g., in a set `sums2`). Time: O(2^(N/2)).
4.  **Meet:** Combine `sums1` and `sums2` to find a pair `(s1, s2)` such that `s1 + s2` satisfies the target condition (e.g., equals `T`, is closest to `T`). Common strategies:
    *   **Binary Search:** Convert `sums2` to a sorted list. Iterate through `s1` in `sums1`. For each `s1`, binary search in `sorted_sums2` for the complementary value (`T - s1` or similar). Combination step is O(M log L) after sorting `sums2`, where `M=|sums1|, L=|sums2|`.
    *   **Two Pointers:** Convert *both* `sums1` and `sums2` to sorted lists. Use two pointers (one starting at the beginning of `sorted_sums1`, one at the end of `sorted_sums2`) to scan inwards, checking `s1 + s2` against the target. Combination step is O(M + L) after sorting both lists. **See [[../../optimizations/searching/mitm_subset_sum_combination_strategies.md]] for a detailed comparison of combination strategies and performance recommendations for subset sum variations.**

**Overall Complexity:** Roughly O(N * 2^(N/2)) (dominated by generation/sorting), a significant improvement over O(2^N).

## Variations & Applications

*   **Finding Closest Sum/Value:** (As in Problem 2035) Instead of exact match `T - s1`, search for the element(s) in `sums2` closest to `T - s1`. Requires storing `sums2` in a sorted list/structure for efficient binary search (e.g., `bisect_left`).
*   **Counting Solutions:** Modify step 4 to count how many pairs `(s1, s2)` satisfy the condition. Might require storing counts/frequencies of sums in hash maps.
*   **K-Sum Problems:** Generalizations for finding `k` elements summing to a target.
*   **State-Space Search:** Can be applied to problems where a state can be decomposed into two independent parts.
*   **Cryptography:** Used in attacks on block ciphers or hash functions.

## When to Use

*   Problems with exponential brute-force complexity O(X^N).
*   Input size `N` is moderate (e.g., 30 <= N <= 50), making O(X^N) too slow but O(X^(N/2)) feasible.
*   The problem can be naturally divided into two independent subproblems whose results can be combined efficiently.
*   Commonly seen in subset sum variations, partitioning problems, and some combinatorial search problems.

## Complexity

*   **Time:** Typically O(N * X^(N/2)) or O(X^(N/2) log(X^(N/2))) depending on the cost of generation and combining steps.
*   **Space:** Typically O(X^(N/2)) to store the results of the generated states for each half.

## Related Concepts

*   Divide and Conquer
*   Subset Sum Problem
*   Binary Search [[../../algorithms/searching/binary_search.md]]
*   Hash Tables [[../../data_structures/hash_table_dict.md]] 