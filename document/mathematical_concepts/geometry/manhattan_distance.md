# Manhattan Distance

**Category:** Mathematical Concepts > Geometry

## Definition

Manhattan distance, also known as taxicab geometry, L1 distance, or city block distance, calculates the distance between two points in a grid-based path (like navigating city blocks).

For two points `p1 = (x1, y1)` and `p2 = (x2, y2)` in a 2D plane, the Manhattan distance is defined as:

`d(p1, p2) = |x1 - x2| + |y1 - y2|`

It represents the total number of horizontal and vertical steps required to move from `p1` to `p2`.

## Key Property: Separability

A crucial property of Manhattan distance, especially relevant in optimization problems, is its **separability**. The total distance is the sum of the absolute differences in each dimension independently.

Consider minimizing the total Manhattan distance from a set of points `P = {(x1, y1), (x2, y2), ..., (xn, yn)}` to a single target point `T = (tx, ty)`:

Minimize: `Total Distance = sum_{i=1}^{n} (|xi - tx| + |yi - ty|)`

This can be separated into two independent 1D minimization problems:

Minimize: `sum_{i=1}^{n} |xi - tx|`  (Find the optimal `tx`)
Minimize: `sum_{i=1}^{n} |yi - ty|`  (Find the optimal `ty`)

The optimal `tx` and `ty` can be found independently and then combined to form the optimal target point `T`. The value that minimizes the sum of absolute differences in 1D is the median.

## Relevance

This property is fundamental in problems like:

*   **Best Meeting Point (LeetCode 296):** Finding a point that minimizes total travel distance for friends on a grid.
*   Certain clustering algorithms or facility location problems where movement is constrained to a grid.

## Related Concepts

*   [[../statistics/median_minimizes_l1_norm.md|Median Minimizes L1 Norm]] (Explains why the median is the optimal choice for the 1D subproblems).
*   [[../../techniques/array/sum_distance_to_median_sorted.md|Efficient Calculation of Sum of Distances to Median]] (A technique to calculate the minimized sum without explicitly finding the median value). 