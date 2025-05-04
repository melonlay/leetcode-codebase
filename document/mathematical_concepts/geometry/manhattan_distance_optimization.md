# Mathematical Concept: Manhattan Distance Optimization (Dimension Decoupling)

## Description

The **Manhattan Distance** (also known as L1 distance, taxicab distance, or city block distance) between two points \(P_1 = (x_1, y_1)\) and \(P_2 = (x_2, y_2)\) in a 2D grid is defined as:

\[ d_1(P_1, P_2) = |x_1 - x_2| + |y_1 - y_2| \]

A key property of the Manhattan distance is that the x-component and y-component are independent and additive.

## Optimization Property

Consider a problem involving finding a meeting point \(P_m = (x_m, y_m)\) that minimizes the **total Manhattan distance** to a set of `n` points \(P_i = (x_i, y_i)\).

Minimize: \( \sum_{i=1}^{n} d_1(P_i, P_m) = \sum_{i=1}^{n} (|x_i - x_m| + |y_i - y_m|) \)

Due to the additive nature of the Manhattan distance formula, we can separate the minimization problem into two independent 1D problems:

\[ \min_{x_m, y_m} \sum_{i=1}^{n} (|x_i - x_m| + |y_i - y_m|) = \left( \min_{x_m} \sum_{i=1}^{n} |x_i - x_m| \right) + \left( \min_{y_m} \sum_{i=1}^{n} |y_i - y_m| \right) \]

This means:
1.  The optimal x-coordinate \(x_m\) is the one that minimizes the sum of absolute differences to all `x_i` coordinates.
2.  The optimal y-coordinate \(y_m\) is the one that minimizes the sum of absolute differences to all `y_i` coordinates.

## Solution via Median

As established in [[../statistics/median_l1_norm_minimization.md]], the value that minimizes the sum of absolute differences in 1D is the **median**.

Therefore, the optimal meeting point \((x_m, y_m)\) has coordinates:
*   \(x_m\) = median of `{x_1, x_2, ..., x_n}`
*   \(y_m\) = median of `{y_1, y_2, ..., y_n}`

## Algorithmic Application: Best Meeting Point (LeetCode 296)

*   **Problem:** Given a grid with houses (1s), find a meeting point (any grid cell) to minimize the total Manhattan distance from all houses.
*   **Solution:**
    1. Collect the row coordinates (`rows`) and column coordinates (`cols`) of all houses.
    2. Independently find the minimum total distance for the row dimension using the median property (can be calculated efficiently from sorted `rows` using the two-pointer pairing method).
    3. Independently find the minimum total distance for the column dimension using the median property (sort `cols` first, then use the two-pointer pairing method).
    4. The overall minimum total distance is the sum of the minimum row distance and minimum column distance.

This decoupling significantly simplifies the problem from a 2D search to two independent 1D median-related problems.

## Generalization

This principle extends to higher dimensions for Manhattan distance.

## Related Concepts
*   Manhattan Distance (L1 Norm)
*   Median ([../statistics/median_l1_norm_minimization.md])
*   Coordinate Geometry
*   Optimization 