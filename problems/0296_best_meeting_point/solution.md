# 296. Best Meeting Point Solution

## Problem Summary

Given an `m x n` grid where `1`s mark friend locations, find a meeting point `(r, c)` such that the sum of Manhattan distances from all friends to this point is minimized. Return this minimum total distance.

## Algorithmic Approach

1.  **Collect Coordinates:** Iterate through the grid and collect the row indices (`rows`) and column indices (`cols`) of all cells containing a `1` (friend locations).
2.  **Manhattan Distance Separability:** Recognize that the total Manhattan distance `sum(|ri - r| + |ci - c|)` can be split into two independent 1D problems: minimizing `sum(|ri - r|)` and minimizing `sum(|ci - c|)`. This is a key property of [[../../document/mathematical_concepts/geometry/manhattan_distance.md|Manhattan Distance]].
3.  **Median Minimizes L1 Norm:** The value that minimizes the sum of absolute differences in 1D (`sum |xi - x|`) is the median of the coordinates `xi`. See [[../../document/mathematical_concepts/statistics/median_minimizes_l1_norm.md|Median Minimizes L1 Norm]]. Therefore, the optimal meeting point `(r, c)` corresponds to the median of the row coordinates and the median of the column coordinates.
4.  **Calculate Minimum 1D Distance:** We need to calculate `min_row_dist = sum(|ri - median(rows)|)` and `min_col_dist = sum(|ci - median(cols)|)`. The total minimum distance is `min_row_dist + min_col_dist`.
5.  **Efficient Calculation for Sorted Coordinates:**
    *   The `rows` list is naturally collected in sorted order by iterating through the grid row by row.
    *   The `cols` list needs to be explicitly sorted.
    *   Once sorted, the minimum sum of distances for each dimension can be calculated efficiently in O(N) time without explicitly finding the median value, using the two-pointer technique described in [[../../document/techniques/array/sum_distance_to_median_sorted.md|Efficient Calculation of Sum of Distances to Median (Sorted Array)]].

## Implementation Details

*   The `minTotalDistance` function implements the coordinate collection and calls a helper function `_calculate_min_distance_1d`.
*   `_calculate_min_distance_1d` takes a *sorted* list of coordinates and applies the O(N) two-pointer technique to calculate the minimum sum of distances.

```python
# Helper function from solution.py
def _calculate_min_distance_1d(self, sorted_coords: List[int]) -> int:
    total_distance = 0
    low, high = 0, len(sorted_coords) - 1
    while low < high:
        total_distance += sorted_coords[high] - sorted_coords[low]
        low += 1
        high -= 1
    return total_distance
```

## Complexity Analysis

*   **Time Complexity:** O(m * n + k log k), where `m` is the number of rows, `n` is the number of columns, and `k` is the number of friends (1s in the grid).
    *   O(m * n) to iterate through the grid and collect coordinates.
    *   O(k log k) to sort the column coordinates (`cols`). The row coordinates (`rows`) are already sorted.
    *   O(k) to calculate the minimum distance for rows using the two-pointer technique.
    *   O(k) to calculate the minimum distance for columns using the two-pointer technique.
    *   Overall, dominated by grid traversal and column sorting: O(m * n + k log k).
*   **Space Complexity:** O(k) to store the row and column coordinates.

## Knowledge Base Links

*   **Mathematical Concepts:**
    *   [[../../document/mathematical_concepts/geometry/manhattan_distance.md|Manhattan Distance]]
    *   [[../../document/mathematical_concepts/statistics/median_minimizes_l1_norm.md|Median Minimizes L1 Norm]]
*   **Techniques:**
    *   [[../../document/techniques/array/sum_distance_to_median_sorted.md|Efficient Calculation of Sum of Distances to Median (Sorted Array)]]

```python
# Helper function from solution.py
def _calculate_min_distance_1d(self, sorted_coords: List[int]) -> int:
    total_distance = 0
    low, high = 0, len(sorted_coords) - 1
    while low < high:
        total_distance += sorted_coords[high] - sorted_coords[low]
        low += 1
        high -= 1
    return total_distance
```

## Complexity Analysis

*   **Time Complexity:** O(m * n + k log k), where `m` is the number of rows, `n` is the number of columns, and `k` is the number of friends (1s in the grid).
    *   O(m * n) to iterate through the grid and collect coordinates.
    *   O(k log k) to sort the column coordinates (`cols`). The row coordinates (`rows`) are already sorted.
    *   O(k) to calculate the minimum distance for rows using the two-pointer technique.
    *   O(k) to calculate the minimum distance for columns using the two-pointer technique.
    *   Overall, dominated by grid traversal and column sorting: O(m * n + k log k).
*   **Space Complexity:** O(k) to store the row and column coordinates.

## Knowledge Base Links

*   **Mathematical Concepts:**
    *   [[../../document/mathematical_concepts/geometry/manhattan_distance.md|Manhattan Distance]]
    *   [[../../document/mathematical_concepts/statistics/median_minimizes_l1_norm.md|Median Minimizes L1 Norm]]
*   **Techniques:**
    *   [[../../document/techniques/array/sum_distance_to_median_sorted.md|Efficient Calculation of Sum of Distances to Median (Sorted Array)]]

``` 