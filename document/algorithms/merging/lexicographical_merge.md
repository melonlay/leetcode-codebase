# Algorithm: Lexicographical Merge

## Description

Lexicographical Merge refers to combining two or more sequences (typically strings or arrays/lists) into a single sequence while maintaining the relative order of elements *within* each original sequence, and choosing which element to take next based on lexicographical comparison (dictionary order).

This is different from standard sorting merges (like in Merge Sort) where elements are chosen based on numerical or standard comparison order. Here, the choice often involves comparing the *remaining subsequences* starting from the current pointers.

## Core Problem

Given two sequences, `A` and `B`, create the lexicographically smallest (or sometimes largest) sequence `C` by interleaving elements from `A` and `B`, such that the relative order of elements originally from `A` is preserved, and the relative order of elements originally from `B` is preserved.

## Algorithm Idea (Smallest Sequence)

Use two pointers, `ptr_a` for sequence `A` and `ptr_b` for sequence `B`.

In a loop, while either pointer is within bounds:

1.  **Compare Remaining Subsequences:** Compare the suffix of `A` starting at `ptr_a` (`A[ptr_a:]`) with the suffix of `B` starting at `ptr_b` (`B[ptr_b:]`).
2.  **Choose Smaller:**
    *   If `A[ptr_a:]` is lexicographically smaller than `B[ptr_b:]`, append `A[ptr_a]` to the result `C` and increment `ptr_a`.
    *   If `B[ptr_b:]` is lexicographically smaller than `A[ptr_a:]`, append `B[ptr_b]` to the result `C` and increment `ptr_b`.
    *   If one sequence is exhausted, append the remaining elements of the other sequence.
    *   **Tie-breaking (Equal Prefixes):** If the suffixes are equal initially (e.g., `A`=[1,3], `B`=[1,2]), you need to look further or use a defined tie-breaking rule. The comparison should inherently handle this: `[1, 3]` vs `[1, 2]` -> `[1, 2]` is smaller.

**Optimization:** Comparing entire suffixes repeatedly can be inefficient (O(N*M) or worse). Often, comparing just the current elements `A[ptr_a]` and `B[ptr_b]` is sufficient *if* we only need the relative order maintained. However, for the true lexicographically smallest *merged* sequence, suffix comparison might be needed in ambiguous cases (e.g., `A`="ab", `B`="ac" -> compare "ab" vs "ac"; `A`="ag", `B`="a" -> compare "ag" vs "a").

## Variants

*   **Merging `k` sequences:** Can be generalized using a min-heap to track the current smallest element/suffix from `k` pointers.
*   **Largest Lexicographical Merge:** Modify the comparison logic to choose the larger suffix/element.

## Example: LeetCode 316/1081 (Remove Duplicate Letters / Smallest Subsequence of Distinct Characters)

While not a direct merge, the core idea is related. To find the lexicographically smallest subsequence with unique characters:
*   Use a stack.
*   Iterate through the string.
*   For character `c`:
    *   While the stack is not empty, `c` is smaller than the stack top, and the character at the stack top *appears later* in the string: pop from the stack (we can potentially get a smaller result by using `c` now and picking up the popped character later).
    *   Push `c` onto the stack (if not already present).
*   This implicitly performs a lexicographical comparison and chooses the best character to keep at each step.

## Example: LeetCode 1663 (Smallest String With A Given Numeric Value)

Constructing the lexicographically smallest string often involves placing the smallest possible characters ('a') at the beginning as much as possible, subject to constraints. This greedy choice based on lexicographical order is related.

## When to Use

*   Problems requiring merging sequences based on dictionary/lexicographical order.
*   Constructing the lexicographically smallest/largest string/sequence under certain constraints.
*   Subsequence problems where the relative order must be maintained, and lexicographical comparison guides choices.

## Complexity

*   **Naive Suffix Comparison:** Can be O((N+M)^2) or worse if implemented poorly.
*   **Optimized/Greedy:** Often achievable in O(N+M) or related linear time, depending on the specific constraints and whether full suffix comparison is truly needed at each step (as in the stack-based subsequence examples).

## Related Concepts

*   Lexicographical Order
*   String/Array Comparison
*   Greedy Algorithms
*   Two Pointers
*   [Data Structure: Stack](../../data_structures/stack.md)
*   Suffix Arrays/Suffix Trees (for more advanced suffix comparisons, usually overkill) 