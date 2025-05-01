# Algorithm: Binary Search for k-th Element in Two Sorted Arrays

## Description

This pattern applies binary search to efficiently find the k-th smallest element in the conceptual combined sorted array formed by two already sorted arrays, `A` and `B`, without actually merging them or using O(m+n) space. The core idea is to find a partition point in each array such that all elements to the left of the partitions constitute the first `k` elements of the combined sorted array.

By repeatedly discarding half of the search space based on comparisons at the potential partition boundaries, we can find the k-th element in logarithmic time complexity relative to the size of the smaller array.

## General Algorithm (Finding k-th smallest)

Let `m = len(A)` and `n = len(B)`. We want to find the k-th smallest element (1-indexed `k`).

1.  **Base Cases:**
    *   If `m > n`, swap arrays `A` and `B` (search in the smaller array).
    *   If `m == 0`, the k-th element is simply `B[k-1]`.
    *   If `k == 1`, the k-th element is `min(A[0], B[0])`.
2.  **Partitioning:** We aim to find indices `i` in `A` and `j` in `B` such that `i + j = k - 1`.
    *   Choose a potential number of elements to take from `A`: `i = min(k // 2, m)`. 
    *   The corresponding elements to consider from `B` is `j = k - i`.
    *   Note: We compare `A[i-1]` and `B[j-1]` (the potential largest elements *within* the first `k` if partitioned this way).
3.  **Comparison and Discarding:**
    *   If `A[i-1] < B[j-1]`: This means all elements `A[0...i-1]` must be among the first `k` elements. The k-th element cannot be in this range of A. We can discard `A[0...i-1]` and effectively search for the `(k-i)`-th element in the remaining parts of `A` (from index `i`) and `B` (full array).
    *   If `A[i-1] >= B[j-1]`: This means all elements `B[0...j-1]` must be among the first `k` elements. We can discard `B[0...j-1]` and search for the `(k-j)`-th element in the remaining parts of `B` (from index `j`) and `A` (full array).
4.  **Recursion/Iteration:** Repeat the process with the reduced arrays/target `k` until a base case is hit.

## Complexity

*   **Time Complexity:** O(log(k)) or O(log(m) + log(n)). Since we discard roughly half of the elements considered for `k` in each step. If using the partitioning approach (like for median finding), it becomes O(log(min(m, n))). 
*   **Space Complexity:** O(1) if implemented iteratively, O(log(k)) or O(log(min(m, n))) if implemented recursively due to call stack.

## Example Application: Median of Two Sorted Arrays (LeetCode 4)

The median is a specific case of finding the k-th element. If `total_len = m + n`:
*   If `total_len` is odd, the median is the `(total_len // 2 + 1)`-th element.
*   If `total_len` is even, the median is the average of the `(total_len // 2)`-th and `(total_len // 2 + 1)`-th elements.

Alternatively, a direct binary search on partitions can be used:

1.  Ensure `A` is shorter. Target `half_len = (m + n + 1) // 2` elements in the left partition.
2.  Binary search for partition `i` in `A` (`0` to `m`). Calculate `j = half_len - i`.
3.  Check if `max_left_A <= min_right_B` and `max_left_B <= min_right_A`. Use `-inf`/`+inf` for boundary conditions.
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

*   **Off-by-one errors:** Handling indices `k`, `i`, `j`, and array access (`i-1`, `j-1`) requires care.
*   **Edge cases:** Empty arrays, `k=1`, partitions at the very beginning or end of arrays.
*   **Integer vs. Floating Point:** Correctly handling division for median calculations involving averages.
*   **Recursion Depth/Termination:** Ensuring the recursive calls correctly reduce the problem size and `k`, and base cases are properly defined. 