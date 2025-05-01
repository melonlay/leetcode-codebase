# Technique: Stack for Index/Value Tracking in Subsequences

## Description

This technique involves using a stack not just for its LIFO (Last-In, First-Out) property but specifically to track indices (or index-value pairs) of elements encountered so far in a sequence (like an array or string). This is often used to efficiently find previous or next elements that satisfy a certain condition relative to the current element, such as the "next greater element," "previous smaller element," or to identify boundaries of certain subsequences.

This is closely related to the Monotonic Stack technique, as the conditions for pushing/popping often maintain a monotonic property (increasing or decreasing) within the stack, either by value or by index referencing a value.

## Core Idea

Iterate through the input sequence. Maintain a stack, typically storing indices.

When considering the current element `seq[i]`:

1.  **Comparison with Stack Top:** Compare `seq[i]` with the element(s) referenced by the index/indices at the top of the stack (`seq[stack.top()]`).
2.  **Popping Condition:** While the stack is not empty and `seq[i]` satisfies a specific condition relative to `seq[stack.top()]` (e.g., `seq[i]` is greater for "next greater element", `seq[i]` is smaller for "next smaller element"), pop the index `top_index` from the stack. The popped `top_index` and the current index `i` now form a pair that satisfies the desired relationship (e.g., `seq[i]` is the next greater element for `seq[top_index]`). Process this relationship (e.g., store the result in an answer array `ans[top_index] = seq[i]`).
3.  **Pushing:** After processing all elements on the stack that satisfy the popping condition with `seq[i]`, push the *current index* `i` onto the stack.

**Why Indices?** Storing indices is often crucial because the problem requires associating the result (e.g., the next greater element) back to the *original position* of the element being processed when it was popped.

## Common Applications & Variants

*   **Next Greater/Smaller Element:** Find the next element to the right (or left, by iterating backward) that is strictly greater/smaller.
*   **Previous Greater/Smaller Element:** Find the nearest element to the left that is strictly greater/smaller.
*   **Largest Rectangle in Histogram:** The stack helps find the nearest smaller elements to the left and right for each bar, defining the width of the largest rectangle using that bar as the height.
*   **Trapping Rain Water (1D - Stack approach):** The stack stores indices of bars forming potential walls. When a taller bar is found, it traps water against the previous wall(s) on the stack.
*   **Subarray Minimum/Maximum Sums (e.g., LeetCode 907):** A monotonic stack helps find the contribution of each element `A[i]` as the minimum/maximum within subarrays ending or starting at `i`.

## Implementation Notes

*   Initialize the result array often with a default value (e.g., -1) to indicate no such element was found.
*   Decide whether to store indices or `(value, index)` pairs on the stack based on problem needs.
*   Handle the end condition: Elements remaining on the stack after the loop might not have found a satisfying element to their right (or left, depending on iteration direction).

## Related Concepts

*   [Data Structure: Stack](../../data_structures/stack.md)
*   [Technique: Monotonic Queue/Stack](../monotonic_queue.md) (This is often a specific type of index-tracking stack)
*   Arrays 