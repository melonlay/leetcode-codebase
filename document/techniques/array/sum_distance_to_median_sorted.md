# Efficient Calculation of Sum of Distances to Median (Sorted Array)

**Category:** Techniques > Array

## Problem

Given a **sorted** array (or list) of numbers `coords = [c1, c2, ..., cn]`, efficiently calculate the minimum sum of absolute differences between each element and the median of the array.

We want to compute: `min_sum = sum_{i=1}^{n} |ci - median(coords)|`

While we know the [[../../mathematical_concepts/statistics/median_minimizes_l1_norm.md|median minimizes this sum]], we don't necessarily need to find the median value itself to compute the minimum sum.

## Technique

If the array `coords` is already sorted (`c1 <= c2 <= ... <= cn`), the minimum sum can be calculated in O(n) time using a two-pointer approach without explicitly finding the median.

The key insight is that the sum can be rewritten by pairing the outermost elements:

`min_sum = (cn - c1) + (c(n-1) - c2) + ...`

**Algorithm:**

1.  Initialize `total_distance = 0`.
2.  Initialize two pointers: `low = 0` and `high = n - 1`.
3.  While `low < high`:
    *   Add the difference between the elements pointed to by `high` and `low` to `total_distance`: `total_distance += coords[high] - coords[low]`.
    *   Move the pointers inwards: `low += 1`, `high -= 1`.
4.  Return `total_distance`.

## Example

`coords = [1, 2, 6, 7, 10]` (Sorted)
Median = 6
Minimum Sum = |1-6| + |2-6| + |6-6| + |7-6| + |10-6| = 5 + 4 + 0 + 1 + 4 = 14

Using the technique:
`low = 0`, `high = 4`. `dist = 0`. `coords[high]=10`, `coords[low]=1`. `dist += (10 - 1) = 9`. `low=1`, `high=3`.
`low = 1`, `high = 3`. `coords[high]=7`, `coords[low]=2`. `dist += (7 - 2) = 5`. `dist = 9 + 5 = 14`. `low=2`, `high=2`.
`low = 2`, `high = 2`. `low < high` is false. Loop terminates.
Return `dist = 14`.

## Implementation

```python
def calculate_min_distance_1d(sorted_coords: list[int]) -> int:
    """
    Calculates the minimum sum of distances to the median in 1D.
    Assumes the input list `sorted_coords` is already sorted.
    """
    total_distance = 0
    low, high = 0, len(sorted_coords) - 1
    while low < high:
        total_distance += sorted_coords[high] - sorted_coords[low]
        low += 1
        high -= 1
    return total_distance
```

## Complexity

*   **Time:** O(n) because we iterate through the array once with two pointers (assuming the array is already sorted). If sorting is required first, the overall time complexity is dominated by the sort (e.g., O(n log n)).
*   **Space:** O(1) for the pointers and sum.

## Applicability

This technique is highly effective when:

1.  You need the *minimum sum* of L1 distances to the median, not the median value itself.
2.  The coordinates are already sorted or can be easily sorted (like row coordinates collected by iterating through a grid row by row).

It's used in problems like:

*   **Best Meeting Point (LeetCode 296):** Applied independently to sorted row coordinates and sorted column coordinates after separating the Manhattan distance.

## Related Concepts

*   [[../../mathematical_concepts/statistics/median_minimizes_l1_norm.md|Median Minimizes L1 Norm]]
*   [[../../mathematical_concepts/geometry/manhattan_distance.md|Manhattan Distance]] 