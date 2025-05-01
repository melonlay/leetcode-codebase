# Optimization: String vs. List Manipulation for Sequences

## Description

When working with sequences of characters or digits in Python, particularly when the problem involves frequent slicing, concatenation, or comparisons, choosing between storing the sequence as a `List` (e.g., `List[int]`, `List[str]`) or a `str` can have significant performance implications.

## Core Idea

*   **Strings (`str`):** Python strings are immutable. Operations like slicing (`s[i:j]`), concatenation (`s1 + s2`), and comparison (`s1 > s2`) are often highly optimized, typically implemented in C. While creating new strings (e.g., via concatenation) involves memory allocation, the underlying operations on character arrays can be very fast.
*   **Lists (`List`):** Lists are mutable. Slicing (`l[i:j]`) creates a *new* list object, involving copying elements. Concatenation (`l1 + l2`) also creates a new list, copying elements from both operands. Comparisons (`l1 > l2`) involve element-wise checks. Repeatedly creating new lists via slicing or concatenation, especially within loops, can lead to significant overhead from memory allocation and data copying.

## When to Consider Strings

Consider performing core logic on strings if:

1.  **Input is easily convertible:** The input (e.g., `List[int]`) can be efficiently converted to a string upfront (e.g., using `''.join(map(str, nums))`) and the final result can be converted back if needed.
2.  **Frequent Slicing/Concatenation:** The algorithm involves many slicing or concatenation operations, particularly for comparisons (like comparing remaining suffixes in a merge) or building intermediate results.
3.  **Read-only Operations Dominate:** The primary operations involve reading/comparing parts of the sequence rather than modifying elements in place.
4.  **Characters/Digits:** The sequence consists of elements that have a natural and efficient string representation (like single digits or characters).

## Example Scenario (LeetCode 321 - Create Maximum Number)

An optimized solution involves:
*   Generating maximum subsequences for various lengths.
*   Merging two chosen subsequences lexicographically.

Performing both the subsequence generation (which can involve deriving shorter sequences from longer ones) and the merging (which compares suffixes `s1[p1:] > s2[p2:]`) using string operations can be significantly faster (e.g., 3x or more) than using list slicing and concatenation for the same logic, despite the initial and final conversion costs.

## Implementation Notes

*   **Building Strings:** When building strings iteratively, appending to a list of characters/strings and then using `''.join()` at the end is generally more efficient than repeated string concatenation (`+=`) in a loop.
*   **Trade-offs:** The initial/final conversion cost might negate the benefits if the sequence processing itself is minimal or dominated by other factors. Profile if unsure.

## Related Concepts

*   [String Concatenation](./string_concatenation.md) (Focuses specifically on joining efficiency).
*   Python's internal implementation details of `str` vs `list`. 