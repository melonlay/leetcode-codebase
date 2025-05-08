# Data Structure: Fenwick Tree (Binary Indexed Tree - BIT)

## 1. Description
A Fenwick Tree, also known as a Binary Indexed Tree (BIT), is a data structure that can efficiently update element values and calculate prefix sums in an array. It's particularly effective for problems requiring point updates and range sum queries, or its dual: range updates and point queries.

## 2. Core Concepts
*   **Tree Structure (Implicit):** It's conceptually a tree where each node is responsible for a range of elements. The structure is implicitly defined by bitwise operations on array indices.
*   **Array Representation:** Typically implemented using a 1-indexed array (let's call it `bit_array`) of size `n+1` for an original array of size `n`.
*   `bit_array[idx]` stores the sum of a specific range of elements from the original array. The range depends on `idx` and its least significant bit (LSB).
*   `lsb(idx) = idx & (-idx)` gives the value of the least significant bit of `idx`.

## 3. Common Operations (for Point Update, Prefix Sum Query)

Let `n` be the size of the conceptual 0-indexed array we are operating on. The BIT itself is often 1-indexed of size `n` (or `n+1` if mapping 0-indexed `i` to `i+1`). The size of the internal `bit_array` should be `max_index_accessed + 1`.

*   **`update(idx, delta)`:** Adds `delta` to the element at `original_array[idx]`. 
    *   Convert `idx` to 1-based for BIT: `i = idx + 1`.
    *   Loop: `while i < len(bit_array):`
        *   `bit_array[i] += delta`
        *   `i += lsb(i)` (move to the next responsible node)
    *   Complexity: O(log n)

*   **`query_prefix_sum(idx)`:** Calculates sum `original_array[0...idx]`.
    *   Convert `idx` to 1-based for BIT: `i = idx + 1`.
    *   Initialize `sum_val = 0`.
    *   Loop: `while i > 0:`
        *   `sum_val += bit_array[i]`
        *   `i -= lsb(i)` (move to the next contributing range)
    *   Return `sum_val`.
    *   Complexity: O(log n)

## 4. Technique: Range Add, Point Query

A Fenwick tree can be adapted to support adding a value `delta` to a range `[L, R]` (inclusive, 0-indexed) and querying the value of a single element `original_array[idx]`.

1.  **Initialization:**
    *   Store the initial values of `original_array` separately (e.g., `initial_values[0...n-1]`).
    *   Create a Fenwick tree `bit_for_deltas` to operate on `n` elements (internal array size `n+1` or more if `R+1` can be `n`), initialized to all zeros. This BIT will store the *effect* of range updates.

2.  **`range_add(L, R, delta)`:** (0-indexed L, R on an array of size `n`)
    *   To add `delta` to `original_array[i]` for `i` in `[L, R]`:
        *   `bit_for_deltas.update(L, delta)`  (updates effect from index `L` onwards)
        *   If `R + 1 < n`: (Ensure `R+1` is a valid index for conceptual updates)
            *   `bit_for_deltas.update(R + 1, -delta)` (cancels the effect from index `R+1` onwards)

3.  **`point_query(idx)`:** (0-indexed idx)
    *   The current value of `original_array[idx]` is:
        `initial_values[idx] + bit_for_deltas.query_prefix_sum(idx)`

*   **Complexity:**
    *   `range_add`: Two BIT updates, so O(log n).
    *   `point_query`: One BIT query, so O(log n).
    *   Space: O(n) for `initial_values` and O(n) for `bit_for_deltas`.

## 5. Implementation Notes
*   BITs are often 1-indexed internally. If your problem uses 0-indexed arrays of size `N`, the BIT structure would typically have an internal array of size `N+1` and operations would convert 0-indexed `idx` to `idx+1` before BIT logic.
*   The `update` for `range_add` at `R+1` should handle the case where `R == N-1`. If `R+1 == N`, the update should still proceed if the BIT is sized to handle index `N` (e.g. size `N+1` for 1-based indexing, effectively index `N` is `N-1` for 0-based array).

## 6. Use Cases
*   Dynamic prefix sums.
*   Problems requiring frequent point updates and range sum queries.
*   Problems requiring frequent range updates and point queries (using the adaptation above).
*   Counting inversions (with coordinate compression).

## 7. Comparison with Segment Tree
*   **Pros:**
    *   Simpler to implement than Segment Tree with lazy propagation.
    *   Smaller constant factors, often faster in practice for problems it can solve.
    *   Less space (O(n) vs O(4n) for Segment Tree array).
*   **Cons:**
    *   Less versatile. Standard BIT handles point update/range query. Segment Tree can handle more complex range operations (e.g., range min/max query, range set/multiply update) with lazy propagation.

## 8. Related Concepts
*   [[segment_tree.md]]
*   Prefix Sums 