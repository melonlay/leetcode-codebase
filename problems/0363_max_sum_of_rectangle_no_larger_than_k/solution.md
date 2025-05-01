# Solution Explanation for LeetCode 363: Max Sum of Rectangle No Larger Than K

## 1. Problem Summary

Given an `m x n` matrix and an integer `k`, the goal is to find the maximum sum of any rectangular submatrix within the given matrix such that this sum does not exceed `k`. The problem guarantees that at least one such rectangle exists.

## 2. Approach and Logic

A naive approach of calculating the sum for every possible rectangle using 2D prefix sums would be O(m^2 * n^2), which is too slow given the constraints (m, n <= 100).

We can optimize this by using a dimension reduction technique:

1.  **Iterate through Pairs of Columns (or Rows):** Instead of considering all four corners of the rectangle simultaneously, we fix two columns, say `c1` (left boundary) and `c2` (right boundary). We iterate through all possible pairs `(c1, c2)` where `0 <= c1 <= c2 < n`.
2.  **Calculate Row Sums:** For a fixed pair `(c1, c2)`, we can calculate the sum of elements in each row `r` between these columns (inclusive). Let `row_sums[r] = sum(matrix[r][c1]...matrix[r][c2])`. This creates a 1D array `row_sums` of size `m`.
3.  **Reduce to 1D Problem:** The problem now reduces to finding the maximum subarray sum within the 1D array `row_sums` such that the sum is no larger than `k`. This is a known subproblem.
4.  **Solve 1D Subproblem (`_find_max_subarray_sum_le_k`):**
    *   This subproblem can be solved efficiently using prefix sums and a data structure that allows finding a previous prefix sum quickly.
    *   We iterate through the `row_sums` array, calculating the `current_prefix_sum`.
    *   For each `current_prefix_sum`, we need to find a `previous_prefix_sum` encountered earlier such that `current_prefix_sum - previous_prefix_sum <= k`.
    *   Rearranging, we need `previous_prefix_sum >= current_prefix_sum - k`.
    *   We maintain a sorted list (`seen_sums`, initialized with `0`) of all prefix sums encountered so far.
    *   Using `bisect.bisect_left(seen_sums, current_prefix_sum - k)`, we can find the smallest `previous_prefix_sum` in the sorted list that satisfies the condition `previous_prefix_sum >= current_prefix_sum - k` in O(log M) time (where M is the current number of seen sums).
    *   If such a `previous_prefix_sum` is found, `current_prefix_sum - previous_prefix_sum` is a candidate sum `<= k`. We update our overall maximum (`max_s` within the helper, `max_sum` overall) if this candidate is larger.
    *   We then insert the `current_prefix_sum` into the `seen_sums` list using `bisect.insort`, which takes O(M) time.
5.  **Optimization - Iterate Smaller Dimension:** To minimize the overall complexity, we check if `rows > cols`. If so, we conceptually transpose the matrix by iterating through row pairs `(r1, r2)` first and calculating `col_sums` for the 1D subproblem. This ensures the outer loops run `min(m, n)^2` times and the inner 1D solver runs on an array of size `max(m, n)`. This optimization is implemented by swapping the roles of `m` and `n` based on the `transpose` flag.
6.  **Optimization - Early Exit:** If at any point the `max_sum` found equals `k`, we can immediately return `k` as no larger sum is possible.

## 3. Knowledge Base References

*   **Technique:** The core idea of calculating subarray sums efficiently relies on prefix sums, similar to the concepts outlined in `document/techniques/sequence/prefix_suffix_aggregates.md` (although this problem requires finding a *constrained* sum, not just any sum).
*   **Data Structure:** The use of `bisect` with a sorted list provides an efficient way (logarithmic search, linear insertion) to find the required `previous_prefix_sum`. While not a specific KB entry itself, the application leverages standard library features effectively, potentially related to `document/optimizations/python_builtin_modules.md`.

## 4. Complexity Analysis

Let `M = max(rows, cols)` and `N = min(rows, cols)`.

*   **Time Complexity:** O(N^2 * M^2)
    *   The outer loops iterate through pairs of columns (or rows), contributing O(N^2).
    *   Inside the second loop, we calculate the 1D `sums_in_m` array, which takes O(M) time.
    *   The `_find_max_subarray_sum_le_k` function iterates through the `sums_in_m` array (size M). Inside its loop, `bisect_left` is O(log M), but `bisect.insort` is O(M) because inserting into a Python list is linear. Thus, the helper function takes O(M^2).
    *   Total: O(N^2 * (M + M^2)) = O(N^2 * M^2).
    *   *Note:* If a data structure with O(log M) insertion (like a balanced BST or a `SortedList` from libraries like `sortedcontainers`) were used instead of `bisect.insort` on a list, the complexity would improve to O(N^2 * M log M).
*   **Space Complexity:** O(M)
    *   We store the `sums_in_m` array, which takes O(M) space.
    *   The `seen_sums` list in the helper function can store up to M prefix sums, taking O(M) space.
    *   Overall space complexity is dominated by these arrays, resulting in O(M). 