# Median Minimizes Sum of Absolute Deviations (L1 Norm)

**Category:** Mathematical Concepts > Statistics

## Property

Given a set of numbers `X = {x1, x2, ..., xn}`, the value `m` that minimizes the sum of absolute deviations (also known as the L1 norm of the differences) is the **median** of the set `X`.

Minimize: `f(m) = sum_{i=1}^{n} |xi - m|`

The minimum value of `f(m)` occurs when `m = median(X)`.

*   If `n` is odd, the median is unique, and it's the unique minimizer.
*   If `n` is even, any value between the two middle elements (inclusive) after sorting `X` will minimize the sum. Conventionally, the median is often taken as the average of the two middle elements, but any point in the interval works as a minimizer for the sum of absolute deviations.

## Intuition / Proof Sketch

Consider the sorted list `x1 <= x2 <= ... <= xn`.

Let `f(m) = sum |xi - m|`. The derivative of `|x - m|` with respect to `m` is `-1` if `m > x`, `+1` if `m < x`, and undefined at `m = x`.

The derivative of `f(m)` is `f'(m) = sum_{xi < m} 1 - sum_{xi > m} 1`. This represents the difference between the count of points to the right of `m` and the count of points to the left of `m`.

To find the minimum, we set `f'(m) = 0`. This happens when the number of points less than `m` equals the number of points greater than `m`. This condition is precisely met when `m` is the median.

*   If `n` is odd, `m` must be the middle element.
*   If `n` is even, `f'(m) = 0` for any `m` between the two middle elements.

Moving `m` slightly away from the median increases the sum of distances to the points on one side more than it decreases the sum of distances to points on the other side (or keeps it the same in the even `n` case within the median interval), thus increasing the total sum `f(m)`.

## Contrast with Mean (L2 Norm)

It's important to distinguish this from the property of the **mean**. The mean is the value `m` that minimizes the sum of *squared* deviations (L2 norm):

Minimize: `g(m) = sum_{i=1}^{n} (xi - m)^2`

This is minimized when `m = mean(X)`.

## Relevance

This property is key when solving problems involving minimizing the sum of L1 distances, particularly when combined with separable metrics like Manhattan distance.

## Related Concepts

*   [[../geometry/manhattan_distance.md|Manhattan Distance]] (A metric whose minimization often relies on this property due to separability).
*   [[../../techniques/array/sum_distance_to_median_sorted.md|Efficient Calculation of Sum of Distances to Median]] 