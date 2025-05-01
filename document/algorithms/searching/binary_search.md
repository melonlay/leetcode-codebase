# Algorithm: Binary Search

## Description

Binary search is an efficient algorithm for finding an item from a **sorted** list (or array) of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

## Core Algorithm (Iterative)

Given a sorted array `arr` and a target value `target`:

1.  **Initialization:** Set `low = 0`, `high = len(arr) - 1`.
2.  **Loop:** While `low <= high`:
    *   Calculate the middle index: `mid = low + (high - low) // 2` (using this form avoids potential integer overflow compared to `(low + high) // 2`).
    *   **Comparison:**
        *   If `arr[mid] == target`: Target found, return `mid`.
        *   If `arr[mid] < target`: Target must be in the right half. Update `low = mid + 1`.
        *   If `arr[mid] > target`: Target must be in the left half. Update `high = mid - 1`.
3.  **Termination:** If the loop finishes without finding the target, it means the target is not in the array. Return `-1` or an appropriate indicator.

## Variations

*   **Finding Insertion Point:** Modify the logic to return `low` when the loop terminates. This index represents where the `target` *would be* inserted to maintain order.
*   **Finding First/Last Occurrence:** Requires slight modifications to the `low`/`high` updates when `arr[mid] == target` to continue searching in the appropriate half for the boundary element.
*   **Recursive Implementation:** Can also be implemented recursively, passing `low` and `high` as parameters.

## Complexity

*   **Time Complexity:** O(log n), where `n` is the number of elements in the array. The search interval is halved in each step.
*   **Space Complexity:**
    *   O(1) for the iterative version.
    *   O(log n) for the recursive version (due to call stack depth).

## Use Cases

*   Searching in large sorted datasets.
*   Finding insertion points.
*   As a subroutine in more complex algorithms (e.g., finding square roots, searching in rotated arrays, the k-th element problem described in `array/kth_two_sorted_arrays.md`).
*   Lower/Upper bound searches.

## Common Pitfalls

*   **Array Not Sorted:** Binary search *requires* the input array to be sorted.
*   **Off-by-One Errors:** Incorrectly updating `low` or `high` (e.g., `high = mid` instead of `high = mid - 1`).
*   **Termination Condition:** Using `low < high` instead of `low <= high` might miss checking the last element.
*   **Integer Overflow:** Calculating `mid = (low + high) // 2` can overflow for very large indices; `mid = low + (high - low) // 2` is safer. 