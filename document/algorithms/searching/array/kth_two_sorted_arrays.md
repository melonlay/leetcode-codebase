# Algorithm: Finding the k-th Element in Two Sorted Arrays

## Description

This algorithm efficiently finds the k-th smallest element in the conceptual combined sorted array formed by two already sorted arrays, `A` and `B`, without actually merging them or using O(m+n) space. It leverages principles related to **Binary Search** by repeatedly discarding portions of the arrays that cannot contain the k-th element.

See `../binary_search.md` for the standard binary search algorithm.

## General Algorithm (Finding k-th smallest - Recursive Approach)

Let `m = len(A)` and `n = len(B)`. We want to find the k-th smallest element (1-indexed `k`).

1.  **Handle Empty Arrays:** If one array is empty, the k-th element is simply the k-th element of the other array.
2.  **Ensure Smaller Array:** Conventionally, ensure `A` is the shorter array (`m <= n`). If not, swap `A` and `B`.
3.  **Base Case `k=1`:** If `k=1`, the smallest element overall is `min(A[0], B[0])`.
4.  **Partitioning:** Divide `k` into two parts. Choose `i = min(k // 2, m)` elements to consider from `A` and `j = k - i` elements to consider from `B`.
    *   Note: We are comparing `A[i-1]` and `B[j-1]` (the potential largest elements *within* the first `k` elements if partitioned at these points).
5.  **Comparison and Discarding:**
    *   If `A[i-1] < B[j-1]`: The k-th element cannot be among `A[0...i-1]`. Discard these `i` elements from `A`. Recursively search for the `(k-i)`-th element in the remaining part of `A` (from index `i` onwards) and the full array `B`.
    *   If `A[i-1] >= B[j-1]`: The k-th element cannot be among `B[0...j-1]`. Discard these `j` elements from `B`. Recursively search for the `(k-j)`-th element in the full array `A` and the remaining part of `B` (from index `j` onwards).
6.  **Termination:** The recursion continues until a base case (`k=1` or an empty array) is reached.

## Complexity

*   **Time Complexity:** O(log(k)) or O(log(m) + log(n)), typically dominated by O(log(min(m, n))) when searching for the median via partitions. Each recursive step reduces the search space (effectively `k`) significantly.
*   **Space Complexity:** O(log(k)) or O(log(min(m,n))) for the recursion call stack. Can be implemented iteratively for O(1) space.

## Example Application: Median of Two Sorted Arrays (LeetCode 4)

The median is a specific case of finding the k-th element. If `total_len = m + n`:
*   If `total_len` is odd, the median is the `(total_len // 2 + 1)`-th element.
*   If `total_len` is even, the median is the average of the `(total_len // 2)`-th and `(total_len // 2 + 1)`-th elements.

*(The original file also described a direct binary search on partitions approach, which is another valid way to solve the median problem. This can be kept or refactored as needed)*

## Direct Binary Search on Partition (Alternative for Median)

1.  Ensure `A` is shorter. Target `half_len = (m + n + 1) // 2` elements in the combined left partition.
2.  Binary search for partition index `i` in `A` (`0` to `m`). Calculate `j = half_len - i`.
3.  Check if the partition is correct: `max_left_A <= min_right_B` and `max_left_B <= min_right_A`. Use `-inf`/`+inf` for boundary conditions (when `i` or `j` is 0 or `m`/`n`).
4.  Adjust the binary search range for `i` based on the comparison result.
5.  Once the correct partition is found, calculate the median from `max(max_left_A, max_left_B)` and potentially `min(min_right_A, min_right_B)`. 

```python
# Simplified snippet for the partition check in median finding
import math

# Assuming A, B, m, n, half_len are defined
# Assuming binary search provides a candidate partition i in A
# partition1 = i, partition2 = half_len - i

max_left1 = A[partition1 - 1] if partition1 > 0 else -math.inf
min_right1 = A[partition1] if partition1 < m else math.inf
max_left2 = B[partition2 - 1] if partition2 > 0 else -math.inf
min_right2 = B[partition2] if partition2 < n else math.inf

if max_left1 <= min_right2 and max_left2 <= min_right1:
    # Correct partition found
    # Calculate median based on odd/even total length...
    pass 
elif max_left1 > min_right2:
    # Partition i is too large, adjust binary search range lower
    pass
else: # max_left2 > min_right1
    # Partition i is too small, adjust binary search range higher
    pass
```

## Common Mistakes

*   **Off-by-one errors:** Handling indices `k`, `i`, `j`, and array access (`i-1`, `j-1`) requires care. See `../../../common_mistakes/off_by_one_errors.md`.
*   **Edge cases:** Empty arrays, `k=1`, partitions at the very beginning or end of arrays.
*   **Integer vs. Floating Point:** Correctly handling division for median calculations involving averages.
*   **Recursion Depth/Termination:** Ensuring the recursive calls correctly reduce the problem size and `k`, and base cases are properly defined.

## Related Concepts
*   Binary Search: `../binary_search.md`
*   Divide and Conquer Paradigm 