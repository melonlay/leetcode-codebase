# Optimization: Offline Processing with Monotonic Stack for Rightward Queries

## 1. Problem Type Addressed

This technique is effective for problems where multiple queries ask to find the **leftmost element `m` at or to the right of a query-specific starting index `s`, such that `element[m]` satisfies a certain condition** (e.g., `element[m] > query_threshold`).

A specific example is LeetCode 2940 ("Find Building Where Alice And Bob Can Meet"), where for each query `(a, b)`, we need to find the leftmost building `m >= max(a,b)+1` such that `heights[m] > max(heights[a], heights[b])`.

## 2. Core Idea & Algorithm Steps

The approach combines offline query processing with a right-to-left sweep using a monotonic stack.

1.  **Offline Query Grouping:**
    *   For each query, determine its actual search starting index `s` and the specific condition it needs to meet (e.g., a `threshold_value`).
    *   Group queries by this `s`. A common way is `pending_queries[s] = list_of_query_details_for_s`.
        *   _Example (LeetCode 2940):_ After checking if `m0 = max(qa, qb)` itself is a solution, if not, the search for `m` starts at `s = m0 + 1`. The `threshold_value` is `max(heights[qa], heights[qb])`. The query `(threshold_value, original_query_idx)` is added to `pending_queries[s]`.

2.  **Right-to-Left Sweep with Monotonic Stack:**
    *   Initialize an empty `monotonic_stack`. This stack will store indices of elements encountered so far during the sweep.
    *   Iterate with current index `i` from `n-1` down to `0` (where `n` is the array size).
        *   **Maintain Monotonic Stack:** Before processing queries for `i`, update the `monotonic_stack` with `element[i]`. The stack should maintain indices `s_k, s_{k-1}, ..., s_0` such that:
            *   `s_k > s_{k-1} > ... > s_0` (indices are sorted descending; `s_0` is the most recently added, i.e., `i`).
            *   `element[s_k] < element[s_{k-1}] < ... < element[s_0]` (elements are sorted strictly increasing).
            *   This is achieved by:
                ```python
                # while monotonic_stack and element[monotonic_stack[-1]] <= element[i]:
                #     monotonic_stack.pop()
                # monotonic_stack.append(i)
                ```
        *   **Process Pending Queries for `i`:** For each query `(threshold_value, original_query_idx)` in `pending_queries[i]`:
            *   The query is looking for the leftmost (smallest index) `m >= i` such that `element[m] > threshold_value`.
            *   The current `monotonic_stack` contains indices `j >= i` that form an increasing sequence of element values.
            *   Perform a binary search on `monotonic_stack` to find the "best" `m`. We want the smallest index `m` (which corresponds to the rightmost element in the stack that satisfies the condition).
                *   Let `stack_len = len(monotonic_stack)`.
                *   `low = 0`, `high = stack_len - 1`, `found_m = -1`.
                *   `while low <= high:`
                    *   `mid_stack_pos = (low + high) // 2`
                    *   `actual_building_idx = monotonic_stack[mid_stack_pos]`
                    *   `if element[actual_building_idx] > threshold_value:`
                        *   `found_m = actual_building_idx`  // This is a candidate
                        *   `low = mid_stack_pos + 1`      // Try to find a smaller index (further to the right in stack)
                    *   `else:`
                        *   `high = mid_stack_pos - 1`     // Element not good enough, need larger values (further to the left in stack)
                *   If `found_m != -1`, assign it as the answer for `original_query_idx`.

3.  **Result:** The array storing answers for each original query index.

## 3. Data Structure Details (Monotonic Stack)

*   The stack `monotonic_stack` stores **indices** of the input array.
*   When sweeping `i` from `n-1` down to `0`:
    *   The elements `monotonic_stack[0], monotonic_stack[1], ..., monotonic_stack[top]` represent building indices `idx_0, idx_1, ..., idx_top`.
    *   `idx_0 > idx_1 > ... > idx_top` (indices are descending because `idx_0` was added earliest from the right).
    *   `element[idx_0] < element[idx_1] < ... < element[idx_top]` (values are strictly increasing towards the stack top, which holds `i` after its addition).
*   The binary search aims to find the rightmost element in this stack (smallest index) that satisfies the height condition.

## 4. Complexity

*   **Time Complexity:**
    *   Preprocessing queries: O(Q)
    *   Sweep: N iterations.
        *   Monotonic stack operations: Each element is pushed and popped at most once, so O(N) total.
        *   Processing queries at each step `i`: If `k_i` queries start at `i`, each takes O(log N) for binary search on the stack (stack size at most N). Total for queries: Sum(k_i * log N) = O(Q log N).
    *   Overall: **O(N + Q log N)**.
*   **Space Complexity:** O(N + Q) for `pending_queries` and `monotonic_stack`.

## 5. Advantages

*   Achieves the same asymptotic time complexity as some Segment Tree based solutions for similar problems.
*   Often exhibits better constant factors and practical performance in Python compared to recursive Segment Tree solutions, due to iterative processing and efficient list operations for the stack.
*   Can be more intuitive than complex Segment Tree augmentations for specific query types once the sweep and stack logic is understood.

## 6. When to Consider

*   When multiple queries require finding a "first element to the right meeting criteria."
*   When an O(N log N) or O((N+Q)log N) solution is acceptable.
*   When direct simulation or simpler data structures are too slow.
*   As an alternative to Segment Trees if performance with Segment Trees is suboptimal due to overhead.

## 7. Related Concepts

*   [[../../patterns/sweep_line.md]]
*   [[../../techniques/sequence/monotonic_queue.md]] (general monotonic stack/queue)
*   Offline Query Processing
*   Binary Search 