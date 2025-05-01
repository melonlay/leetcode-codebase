# LeetCode 4: Median of Two Sorted Arrays - Solution Explanation

## Problem Summary

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

## Algorithmic Approach

The problem asks for the median of a conceptual combined sorted array without actually merging them. This can be efficiently solved using a binary search approach on the partitions of the arrays. The core idea is to find a partition in both arrays such that all elements to the left of the partition points form the lower half of the combined sorted array.

The algorithm specifically aims to find partition indices `partition1` (in `nums1`) and `partition2` (in `nums2`) such that:

1.  The total number of elements in the left partitions equals `(m + n + 1) // 2` (this handles both odd and even total lengths correctly).
2.  The maximum element in the left partition of `nums1` is less than or equal to the minimum element in the right partition of `nums2` (`max_left1 <= min_right2`).
3.  The maximum element in the left partition of `nums2` is less than or equal to the minimum element in the right partition of `nums1` (`max_left2 <= min_right1`).

We perform binary search on the possible partition indices of the *smaller* array to achieve O(log(min(m, n))) complexity.

## Logic Explanation

1.  **Preprocessing:**
    *   Get lengths `m` and `n`.
    *   Ensure `nums1` is the shorter array by swapping if `m > n`. This optimizes the binary search range.
    *   Calculate `total_length = m + n` and `half_len = (total_length + 1) // 2`. `half_len` is the target count of elements for the combined left partition.
2.  **Binary Search on Partition:**
    *   Initialize `low = 0` and `high = m` (the possible range for `partition1`).
    *   Loop while `low <= high`:
        *   Calculate `partition1 = (low + high) // 2`.
        *   Calculate the corresponding `partition2 = half_len - partition1`.
        *   **Identify Boundary Elements:** Determine the four critical elements around the partitions:
            *   `max_left1`: Largest element in `nums1`'s left partition (`nums1[partition1 - 1]`). Handle `partition1 == 0` with `-math.inf`.
            *   `min_right1`: Smallest element in `nums1`'s right partition (`nums1[partition1]`). Handle `partition1 == m` with `math.inf`.
            *   `max_left2`: Largest element in `nums2`'s left partition (`nums2[partition2 - 1]`). Handle `partition2 == 0` with `-math.inf`.
            *   `min_right2`: Smallest element in `nums2`'s right partition (`nums2[partition2]`). Handle `partition2 == n` with `math.inf`.
        *   **Check Partition Correctness:**
            *   If `max_left1 <= min_right2` AND `max_left2 <= min_right1`: The partition is correct. Proceed to calculate the median.
            *   If `max_left1 > min_right2`: `partition1` is too large (too many elements from `nums1` are in the left partition). Adjust the search range: `high = partition1 - 1`.
            *   If `max_left2 > min_right1`: `partition1` is too small. Adjust the search range: `low = partition1 + 1`.
3.  **Median Calculation (Once Correct Partition is Found):**
    *   Identify the overall maximum element of the combined left partition: `max_left = max(max_left1, max_left2)`.
    *   If `total_length` is odd: The median is simply `float(max_left)`.
    *   If `total_length` is even: The median requires the smallest element of the combined right partition. Identify `min_right = min(min_right1, min_right2)`. The median is `(max_left + min_right) / 2.0`.

## Knowledge Base References

*   **Binary Search for k-th Element/Partition:** The core logic directly implements the binary search on partitions strategy for finding the median (a specific k-th element problem) in two sorted arrays. This algorithm is detailed in `document/algorithms/searching/binary_search_kth_element.md`, including the partition check logic and boundary handling.
*   **Constraint Handling:** While the provided solution doesn't explicitly check for `m+n=0`, being aware of behavior outside constraints (as mentioned in `document/common_mistakes/constraint_violation_handling.md`) is good practice, although not strictly required by the problem's constraints.

## Complexity Analysis

*   **Time Complexity:** O(log(min(M, N))). The binary search is performed on the smaller of the two arrays.
*   **Space Complexity:** O(1). The algorithm uses a constant amount of extra space. 