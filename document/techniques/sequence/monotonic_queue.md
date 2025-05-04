# Technique: Monotonic Queue / Stack

## Description

A Monotonic Queue or Monotonic Stack is a data structure technique where the elements maintained in the queue (often a Deque for efficient additions/removals from both ends) or stack are always kept in a specific monotonic order (either strictly increasing or strictly decreasing).

This property is used to efficiently process elements in a sequence (like an array) to find relationships like the nearest smaller/larger element, or to maintain candidates for sliding window minimum/maximum problems.

## Core Idea

As you iterate through the input sequence, you maintain the monotonic property of the queue/stack:

*   **Monotonic Increasing Queue/Stack:** Before adding the current element, remove elements from the *end* (tail of queue, top of stack) that are *greater than or equal to* the current element. Then, add the current element.
*   **Monotonic Decreasing Queue/Stack:** Before adding the current element, remove elements from the *end* that are *less than or equal to* the current element. Then, add the current element.

The elements removed are those that can no longer be candidates for certain future comparisons (e.g., if looking for the *next smaller element*, a larger element preceding a smaller one becomes irrelevant).

## Data Structure Choice

*   **Deque (`collections.deque`):** Often preferred, especially for sliding window problems. It allows efficient O(1) addition and removal from *both* ends. See [[../data_structures/deque.md]].
    *   `append()`: Add to the right (tail).
    *   `pop()`: Remove from the right (tail).
    *   `appendleft()`: Add to the left (head).
    *   `popleft()`: Remove from the left (head).
*   **Stack (List):** Sufficient if only additions/removals from one end (the top/end) are needed (e.g., finding next/previous greater/smaller element).
    *   `append()`: Add to the top (end).
    *   `pop()`: Remove from the top (end).

## Common Applications

1.  **Sliding Window Maximum/Minimum (e.g., LeetCode 239):**
    *   **Goal:** Find the maximum (or minimum) element in each sliding window of size `k`.
    *   **Approach (Max):** Use a *monotonic decreasing deque*. 
        *   **Storage:** The deque can store either *indices* or *values* from the input array `nums`.
        *   **Adding Element:** Before adding the current element (or its index `i`), remove elements (or indices `j`) from the *tail* where the corresponding value `nums[j]` is *less than or equal to* the current value `nums[i]`. Then add the current element/index.
        *   **Removing Element (Window Sliding):** When the window slides past an element at `leaving_index`, check if the element/index at the *head* of the deque corresponds to this leaving element. 
            *   **Option A (Index-based):** If storing indices, remove the head index `j` if `j <= leaving_index`.
            *   **Option B (Value-based / Lazy Removal):** If storing values, remove the head value only if `deque[0] == nums[leaving_index]`. This avoids removing elements that are no longer the maximum but are still within the window.
        *   **Result:** The element corresponding to the index/value at the *head* of the deque is the maximum for the current window.

2.  **Next Greater/Smaller Element (e.g., LeetCode 496, 503):**
    *   **Goal:** For each element, find the first element to its right (or left) that is greater/smaller.
    *   **Approach (Next Greater):** Use a *monotonic decreasing stack* storing *indices*. Iterate through the array. While the stack is not empty and the current element `nums[i]` is greater than the element at the stack top `nums[stack[-1]]`, pop the index `top_idx` from the stack. The current element `nums[i]` is the "next greater element" for `nums[top_idx]`. Push the current index `i` onto the stack.

3.  **Previous Greater/Smaller Element:** Similar to above, but iterate backward through the array or adjust logic slightly.

4.  **Largest Rectangle in Histogram (e.g., LeetCode 84):**
    *   **Goal:** Find the largest rectangle area under a histogram.
    *   **Approach:** For each bar `i`, find the nearest bar to its left (`left_i`) and right (`right_i`) that is *strictly smaller*. The width is `right_i - left_i - 1`. Use a *monotonic increasing stack* (storing indices) twice (or once with careful logic) to find these boundaries efficiently.

5.  **Sum of Subarray Minimums/Maximums (e.g., LeetCode 907):**
    *   **Goal:** Calculate the sum of `min(B)` for all contiguous subarrays `B`.
    *   **Approach:** For each element `A[i]`, determine how many subarrays have `A[i]` as their minimum element. This depends on finding the "previous smaller" (`left_boundary`) and "next smaller" (`right_boundary`) elements using a monotonic increasing stack. The number of such subarrays is `(i - left_boundary) * (right_boundary - i)`. Sum `A[i]` times this count for all `i`.

6.  **Shortest Subarray with Sum at Least K (e.g., LeetCode 862):**
    *   **Goal:** Find the shortest subarray whose sum is at least `K`.
    *   **Approach:** Calculate prefix sums `P`. We want the smallest `y - x` such that `P[y] - P[x] >= K`. Use a *monotonic increasing deque* storing indices `x` of the prefix sum array. When considering `P[y]`, remove indices `x` from the *head* where `P[y] - P[x] >= K` (updating the shortest length). Then, remove indices `j` from the *tail* where `P[j] >= P[y]` (to maintain the increasing property for future optimal `x` candidates).

7.  **Lexicographically Largest Subsequence of Length k (e.g., LeetCode 321):**
    *   **Goal:** Find the lexicographically largest subsequence of length `k` from a sequence `nums` of length `n`.
    *   **Approach:** Use a *monotonic decreasing stack*. Iterate through `nums`. For each element `num`:
        *   **Pop Condition:** While the stack is not empty, the top element `stack[-1]` is smaller than `num`, AND removing `stack[-1]` still leaves enough remaining elements in `nums` to potentially form a subsequence of length `k` (`len(stack) - 1 + remaining_elements_in_nums >= k`), pop from the stack.
        *   **Push Condition:** If the stack size is less than `k`, push `num` onto the stack.
        *   If the stack size exceeds `k` after pushing (only possible if the pop condition wasn't met due to length constraints), it implies we kept a smaller element unnecessarily earlier; this specific logic variant needs careful implementation (often the pop condition prevents this).
        *   A simpler approach ensures the pop condition considers `k` correctly: `while stack and stack[-1] < num and (len(stack) + n - 1 - i) > k: stack.pop()`. Then push if `len(stack) < k`. Finally, ensure the stack has exactly `k` elements (it might have fewer if `k` is large).
    *   **Result:** The stack contains the lexicographically largest subsequence.

## Implementation Details

*   **Store Indices:** Often crucial to store indices in the deque/stack, not just values, to calculate distances, check window boundaries, or map results back to the original positions.
*   **Strict vs. Non-Strict:** Decide whether to use `<` or `<=` (`>` or `>=`) in the removal condition based on whether equal values should be kept or removed.
*   **Boundary Conditions:** Handle empty deque/stack cases. Consider adding sentinel values to the input array sometimes to simplify edge case logic.

## Complexity

*   **Time:** Typically O(n), where n is the size of the input sequence. Each element is added to and removed from the deque/stack at most once.
*   **Space:** O(k) or O(n). For sliding window problems, space is O(k) (window size). For next/previous greater/smaller or histogram problems, it can be up to O(n) in the worst case (e.g., a sorted array).

## Related Concepts

*   [[../data_structures/deque.md]]
*   [[../data_structures/stack.md]]
*   [[../patterns/sliding_window.md]]
*   [Technique: Stack for Index/Value Tracking](../stack/stack_index_tracking_for_subsequences.md) 