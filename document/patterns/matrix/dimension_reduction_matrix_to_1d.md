# Pattern: Dimension Reduction from 2D Matrix to 1D Array

## 1. Abstract Problem Structure

This pattern applies to 2D matrix problems where the goal involves finding optimal substructures (like maximum sum rectangles, counts of certain submatrices, etc.) defined by rectangular boundaries. The core idea is to reduce the dimensionality by iterating through potential boundaries along one dimension and solving a resulting 1D problem along the other dimension.

## 2. General Strategy

1.  **Identify Dimensions:** Let the matrix dimensions be `rows` and `cols`.
2.  **Choose Iteration Dimension:** Select one dimension to iterate through pairs of boundaries. Let this be dimension `N` (size `n`) and the other be dimension `M` (size `m`).
3.  **Iterate Boundary Pairs:** Loop through all possible start (`i`) and end (`j`) indices along dimension `N` (`0 <= i <= j < n`).
4.  **Calculate 1D Aggregate:** For each pair `(i, j)`, compute an aggregate value for each element along dimension `M`. This aggregate represents the sum, count, or other relevant property of the elements within the bounds `[i, j]` along dimension `N`. This results in a 1D array of size `m`.
    *   *Example (Max Sum Rectangle):* For fixed columns `c1=i`, `c2=j`, calculate `row_sums[r] = sum(matrix[r][c1]...matrix[r][c2])` for each row `r`. The 1D array is `row_sums`.
5.  **Solve 1D Subproblem:** Apply an appropriate 1D algorithm or technique to the generated 1D array to solve the subproblem corresponding to the fixed boundaries `(i, j)`.
    *   *Example (Max Sum Rectangle <= k):* Find the maximum subarray sum `<= k` in the `row_sums` array. See [[techniques/sequence/prefix_sum_difference_constraint.md]].
6.  **Combine Results:** Aggregate the results from the 1D subproblems to find the overall solution for the 2D problem (e.g., take the maximum value found across all boundary pairs).

## 3. Key Optimization: Iterate Smaller Dimension

**Crucially**, for optimal performance, choose the **smaller** dimension of the matrix as dimension `N` for the O(N^2) boundary pair iteration. Let `M = max(rows, cols)` and `N = min(rows, cols)`.
*   The outer loops run O(N^2) times.
*   Calculating the 1D aggregate array typically takes O(M) time within the inner loop.
*   Solving the 1D subproblem has its own complexity, say `f(M)`.
*   Total time complexity: O(N^2 * (M + f(M))).

By iterating over the smaller dimension squared, we minimize the overall runtime compared to iterating O(M^2) times.

## 4. Applicability

*   Finding maximum/minimum sum subrectangles (with or without constraints).
*   Counting subrectangles satisfying certain properties.
*   Problems where a 2D query can be broken down by fixing boundaries in one dimension.

## 5. Related Concepts

*   [[techniques/sequence/prefix_suffix_aggregates.md]] (Often used for calculating the 1D aggregate array efficiently)
*   Various 1D array techniques depending on the subproblem (e.g., [[techniques/sequence/prefix_sum_difference_constraint.md]], Kadane's Algorithm) 