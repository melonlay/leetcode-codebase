# Technique: Difference Array

**Related:** Prefix Sums, Sweep Line, Range Updates

## 1. Description

A Difference Array is a technique used primarily for efficiently handling multiple **range update operations** on an array and then querying the final state of the array. It allows adding a value `v` to a range `[L, R]` (inclusive) in O(1) time per update. After all updates are applied, the final array can be reconstructed from the difference array in O(N) time using prefix sums.

This technique can also be adapted to determine the **coverage** of intervals, as seen in the solution for LeetCode 3529.

## 2. Core Idea

Let the original array be `A` of size `N`.
We create a difference array `D` of size `N+1` (or `N` depending on indexing convention), where `D[i]` typically stores the difference `A[i] - A[i-1]` (with `D[0] = A[0]`).

*   **Relationship:** `A[i] = D[0] + D[1] + ... + D[i]`. The original array is the prefix sum of the difference array.
*   **Range Update `add(L, R, v)`:** To add `v` to all elements in `A` from index `L` to `R`:
    *   Increment `D[L]` by `v`. This ensures that when calculating prefix sums, all elements from `A[L]` onwards will include the added `v`.
    *   Decrement `D[R+1]` by `v`. This cancels out the added `v` for all elements *after* `A[R]`, effectively limiting the update to the range `[L, R]`.
    *   These two operations take O(1) time.
*   **Reconstruction:** After applying all range updates to `D`, reconstruct the final array `A` by computing the prefix sum of `D`: `A[i] = A[i-1] + D[i]` (adjusting for base index).

## 3. Adaptation for Interval Coverage

Instead of updating values, we can use the difference array to count how many intervals cover each point (or index).

*   **Problem:** Given a set of intervals `[start, end)` (0-based, exclusive end), determine for each index `i` if it is covered by at least one interval.
*   **Difference Array Setup:** Create `diff = [0] * (N + 1)`, where N is the maximum possible end index + 1.
*   **Applying Intervals:** For each interval `[start, end)`:
    *   `diff[start] += 1` (An interval begins at this point)
    *   `diff[end] -= 1` (An interval ends *before* this point)
*   **Calculating Coverage:**
    *   Initialize `coverage = [False] * N`.
    *   Initialize `current_coverage = 0`.
    *   Iterate `i` from 0 to `N-1`:
        *   `current_coverage += diff[i]`.
        *   If `current_coverage > 0`, it means index `i` is currently within at least one active interval, so set `coverage[i] = True`.
*   The `coverage` array now indicates which indices were covered by any interval. (Alternatively, integers like 0/1 can be used instead of booleans).

## 4. Complexity

*   **Initialization:** O(N) to create the difference array.
*   **Range Update / Interval Application:** O(1) per update/interval.
*   **Reconstruction / Coverage Calculation:** O(N) to compute the prefix sum.
*   **Overall:** If there are `K` updates/intervals, the total time is O(N + K).
*   **Space:** O(N) for the difference array.

## 5. Use Cases

*   Problems requiring multiple range addition/subtraction updates followed by point queries or querying the final array state.
*   Efficiently determining interval coverage or overlap counts across a range.
*   Can be seen as a 1D version of the sweep-line technique.

## 6. Example Application

*   Range update problems (e.g., add value V to elements from index L to R multiple times).
*   LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings (Used to efficiently determine which 1D indices were covered by pattern matches) - See `problems/3529_count_cells_in_overlapping_horizontal_and_vertical_substrings/solution.py`
*   Calculating the maximum number of overlapping intervals at any point. 