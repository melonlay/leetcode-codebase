# Monotonic Queue Technique

## Description

A Monotonic Queue (often implemented using a `deque` - double-ended queue) is a data structure where the elements are maintained in a specific monotonic order (either strictly increasing or strictly decreasing) from front to back.

This technique is particularly useful for problems involving sliding windows where you need to efficiently find the minimum or maximum element within the current window. It allows O(1) query time for the min/max element within the window and achieves an overall O(N) time complexity for processing N elements, as each element is added and removed from the deque at most once.

## Core Idea (Monotonic Decreasing Queue for Maximum)

To find the maximum in a sliding window:

1.  **Maintain Indices:** The deque stores *indices* of elements from the input array, not the elements themselves.
2.  **Monotonic Decreasing Order:** The elements in the input array corresponding to the indices in the deque are kept in strictly decreasing order. `nums[deque[0]] > nums[deque[1]] > ...`
3.  **Adding Element `nums[i]`:**
    *   **Remove Out-of-Window Indices:** Before considering `nums[i]`, remove indices from the *front* of the deque that fall outside the current window's left boundary (e.g., `deque[0] <= i - k` for a window of size `k` ending at `i`).
    *   **Maintain Monotonicity:** Remove indices `j` from the *back* of the deque as long as `nums[j] <= nums[i]`. Any element smaller than or equal to the current element `nums[i]` and appearing *before* it cannot be the maximum in any future window that includes `nums[i]`.
    *   **Append Current Index:** Add the current index `i` to the back of the deque.
4.  **Querying Maximum:** The maximum element in the current window is always `nums[deque[0]]`, as the deque maintains the potential maximums in decreasing order, and the front element is the largest within the current window's bounds.

## Core Idea (Monotonic Increasing Queue for Minimum)

To find the minimum in a sliding window, the logic is analogous:

1.  Maintain indices in the deque.
2.  Keep corresponding element values in strictly *increasing* order (`nums[deque[0]] < nums[deque[1]] < ...`).
3.  When adding `nums[i]`:
    *   Remove out-of-window indices from the front.
    *   Remove indices `j` from the *back* as long as `nums[j] >= nums[i]`.
    *   Append `i` to the back.
4.  The minimum element in the window is `nums[deque[0]]`.

## Implementation

Uses `collections.deque` in Python for efficient O(1) appends and pops from both ends.

## Complexity

*   **Time Complexity:** O(N), where N is the number of elements processed. Each element is pushed onto and popped from the deque at most once.
*   **Space Complexity:** O(K), where K is the maximum size of the window, as the deque stores at most K indices.

## Use Cases

*   Finding maximum/minimum in a fixed-size sliding window (e.g., LeetCode 239. Sliding Window Maximum).
*   Problems where you need the next greater/smaller element within a certain range.
*   Optimizing certain dynamic programming solutions.

## Related Patterns/Structures

*   **Pattern:** [Sliding Window](../../patterns/sliding_window.md) (Monotonic Queue is often an optimization technique *within* this pattern).
*   **Data Structure:** [Queue](../../data_structures/queue.md) (`collections.deque` provides the necessary double-ended operations).

## Implementation Optimizations & Considerations

While the core logic remains the same, certain implementation choices can impact performance due to constant factors, especially in Python.

### 1. Storing Values vs. Indices

*   **Index Storage (Described Above):** The deque stores indices `i`. Comparisons require looking up values in the original array (e.g., `nums[deque[-1]] <= nums[i]`). The maximum is retrieved via `nums[deque[0]]`. This approach is necessary if the original index itself is needed for later calculations or logic beyond just finding the min/max value. Removing elements falling out of the window is done by checking indices (`deque[0] <= i - k`).
*   **Value Storage:** The deque directly stores values `v`. Comparisons are direct (e.g., `q[-1] < v`). The maximum is retrieved directly (`q[0]`). This avoids the overhead of array lookups (`nums[...]`) within the inner loops, which can lead to better practical performance if only the min/max *value* is required.
    *   **Removal Logic with Value Storage:** When storing values, you cannot reliably use index calculations to remove elements sliding out of the window. Instead, you need access to the element that is *actually* leaving the window. A common pattern is:
        ```python
        # Assuming 'l' is the input list, 'i' is the index of the element LEAVING
        # and 'v' is the element ENTERING the window.
        if q and q[0] == l[i]: # Check if the max element IS the one leaving
            q.popleft()
        while q and q[-1] < v: # Maintain monotonicity with the new element
             q.pop()
        q.append(v)
        # The new maximum is q[0]
        ```
        This "lazy removal" only pops the front element if it matches the value leaving the window. This might perform slightly better than the index check in some cases, as it avoids the `i - k` calculation and potentially performs fewer `popleft` operations if the maximum element persists in the window for longer periods.

### 2. Iterator Usage

*   See [Optimization: Using Iterators](../../optimizations/iterator_usage.md) for details on how using iterators can improve performance.

**Trade-offs:** Choose the implementation based on clarity and whether the original index is needed. For pure min/max sliding window value problems, value storage with lazy removal often provides the best performance in Python. 