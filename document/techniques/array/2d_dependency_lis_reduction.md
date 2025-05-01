# Technique: 2D Dependency Reduction via LIS

## Concept

This technique addresses problems where we need to find the longest chain or sequence based on two dimensions (e.g., width and height) with a strict increasing requirement in *both* dimensions. A common example is nesting problems like the "Russian Doll Envelopes" (LeetCode 354).

The core idea is to reduce the 2D problem to a 1D Longest Increasing Subsequence (LIS) problem by carefully sorting the input items.

## Method

Given items represented as pairs `(dimension1, dimension2)` (e.g., `(width, height)`), where item `A = (d1_A, d2_A)` can "contain" or precede item `B = (d1_B, d2_B)` if and only if `d1_A < d1_B` AND `d2_A < d2_B`:

1.  **Sort the Items:** Sort the items based on the first dimension (`dimension1`) in **ascending** order. If there's a tie in the first dimension, sort by the second dimension (`dimension2`) in **descending** order.
    
    *Implementation 1: Compound Key*
    ```python
    # Single pass sort using a tuple key
    items.sort(key=lambda x: (x[0], -x[1]))
    ```

    *Implementation 2: Two-Pass Stable Sort*
    ```python
    # Requires a stable sort algorithm (like Python's Timsort)
    # 1. Sort by secondary key (dimension2 descending)
    items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
    # 2. Sort by primary key (dimension1 ascending) - stability preserves secondary order
    items_sorted = sorted(items_sorted, key=lambda x: x[0])
    # Note: using list.sort() in-place might be slightly different syntax/efficiency
    ```
    Both implementations achieve the required final order.

2.  **Extract Second Dimension:** Create a new list containing only the second dimension values from the sorted items.
    ```python
    # Use items_sorted if using Implementation 2
    second_dims = [item[1] for item in items_sorted] # Or 'items' if using Implementation 1
    ```
3.  **Find LIS:** Compute the Longest Increasing Subsequence (LIS) of the `second_dims` list using an efficient O(n log n) algorithm (see [[../../algorithms/dynamic_programming/array/longest_increasing_subsequence.md|Algorithm: Longest Increasing Subsequence (LIS)]]).

The length of the LIS of the second dimensions is the length of the longest chain satisfying the original 2D constraints.

## Implementation Notes

*   **Sorting:** The crucial sorting step (dimension 1 asc, dimension 2 desc for ties) can be implemented either via a single pass with a compound key or using a two-pass stable sort. Both achieve the correct logical order.
*   **LIS Algorithm:** For details on different efficient O(n log n) implementations of the Longest Increasing Subsequence algorithm itself (e.g., standard vs. optimized append check) and their specific trade-offs, refer to the [[../../algorithms/dynamic_programming/array/longest_increasing_subsequence.md|Algorithm: Longest Increasing Subsequence (LIS)]] document.

## Why does this work?

- **Ascending Sort (Dimension 1):** Sorting by `dimension1` ensures that when we consider items sequentially, any item `B` appearing after item `A` in the sorted list will have `d1_B >= d1_A`.
- **Descending Sort (Dimension 2 for Ties):** This is the crucial part. If we have two items with the same `dimension1`, say `A = (d1, d2_A)` and `B = (d1, d2_B)`, they cannot contain each other according to the strict inequality (`d1_A < d1_B`). By sorting `dimension2` in descending order for ties, the item with the larger `d2` value appears first in the sorted list. When we perform the LIS on the extracted `dimension2` values, `[..., d2_A, ..., d2_B, ...]`, if `d2_A > d2_B`, they cannot both be part of the *same* increasing subsequence. This correctly prevents items with the same `dimension1` from being considered as nestable/chainable.
- **LIS on Dimension 2:** After sorting, the problem reduces to: find the longest subsequence such that `dimension2` values are strictly increasing. Why? Because the sorting already handled the `dimension1` constraint implicitly. Any increasing subsequence we find in `second_dims` corresponds to items where `d1` is non-decreasing (due to the primary sort) *and* `d2` is strictly increasing (due to LIS). The descending tie-breaker ensures that if `d1` values were equal, the corresponding `d2` values cannot form an increasing subsequence, effectively enforcing the `d1_A < d1_B` condition.

## Example Application

- **LeetCode 354: Russian Doll Envelopes:** Given `envelopes = [[w, h]]`, find the maximum number that can be nested `(w1 < w2 and h1 < h2)`.
    - Sort by `w` ascending, `h` descending.
    - Find LIS of the sorted heights.

## Complexity

- **Sorting:** O(n log n)
- **LIS:** O(n log n)
- **Overall:** O(n log n) 