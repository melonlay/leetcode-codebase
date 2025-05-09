# Technique: Applying Constraints to Prefix Sum Differences

## 1. Technique Overview

This technique addresses problems involving finding or counting elements or contiguous subarrays in a sequence whose cumulative values (prefix sums) satisfy certain constraints based on their *differences*. It leverages prefix sums combined with an efficient data structure (typically a sorted set/list or a hash map) to query previously computed prefix sums.

The core idea is that a property related to a range `[i, j]` (like subarray sum `sum(arr[i:j+1])`) can often be expressed using the difference between the prefix sum at `j` and the prefix sum at `i-1`: `current_prefix_sum[j] - previous_prefix_sum[i-1]` (where `prefix_sum[-1] = 0`). The problem constraint (e.g., subarray sum `<= k`) is translated into a condition on the required `previous_prefix_sum` relative to the `current_prefix_sum` and the constraint value(s).

## 2. Core Algorithm Steps

1.  **Initialization:**
    *   Initialize `current_prefix_sum = 0`.
    *   Initialize a data structure `seen_sums` to store encountered prefix sums. For range/inequality constraints, this is typically a sorted structure (like a list for `bisect` or a Balanced BST) initialized with `0`. For equality constraints, a hash map (dictionary) storing frequencies is usually more efficient.
    *   Initialize result variables (e.g., `max_val`, `min_val`, `count`).
2.  **Iteration:** Iterate through the input sequence `arr` (let the current element be `x`):
    *   Update `current_prefix_sum += x`.
    *   **Derive Target Condition on Previous Sum:** Based on the specific problem constraint involving the difference (e.g., `current_prefix_sum - previous_prefix_sum <= k`), determine the condition that a `previous_prefix_sum` must satisfy relative to `current_prefix_sum` and the constraint value(s) `k` (or `k1, k2`).
    *   **Query `seen_sums`:** Search `seen_sums` for `previous_prefix_sum` values that satisfy the derived condition. The type of query (lower bound, upper bound, exact match, range count) depends on the constraint.
    *   **Update Result:** Based on the `previous_prefix_sum`(s) found, update the result (e.g., update `max_val` based on `current_prefix_sum - previous_prefix_sum`, increment `count`).
    *   **Update `seen_sums`:** Insert/update `current_prefix_sum` in the `seen_sums` data structure.

## 3. Common Constraint Variations & Queries

Let `current_ps` be the `current_prefix_sum`, and `prev_ps` be a `previous_prefix_sum` from `seen_sums`.

### a) Constraint: `current_ps - prev_ps <= k` (e.g., Max Subarray Sum <= k)
*   **Condition on `prev_ps`:** Need `prev_ps >= current_ps - k`.
*   **Query:** Find the *smallest* `prev_ps` in `seen_sums` such that `prev_ps >= current_ps - k`. Use lower bound search (e.g., `bisect.bisect_left`).
*   **Result Update:** If `prev_ps` is found, `diff = current_ps - prev_ps`. Update result (e.g., `max_sum = max(max_sum, diff)`).
*   **Structure:** Sorted Set/List (initialized with `0`).

### b) Constraint: `current_ps - prev_ps >= k` (e.g., Min Subarray Sum >= k)
*   **Condition on `prev_ps`:** Need `prev_ps <= current_ps - k`.
*   **Query:** Find the *largest* `prev_ps` in `seen_sums` such that `prev_ps <= current_ps - k`. Use upper bound search (e.g., `bisect.bisect_right`, check index `-1`).
*   **Result Update:** If `prev_ps` is found, `diff = current_ps - prev_ps`. Update result (e.g., `min_sum = min(min_sum, diff)`).
*   **Structure:** Sorted Set/List (initialized with `0`).

### c) Constraint: `current_ps - prev_ps == k` (e.g., Count Subarrays with Sum == k)
*   **Condition on `prev_ps`:** Need `prev_ps == current_ps - k`.
*   **Query:** Check if `target = current_ps - k` exists as a key in `seen_sums`. If yes, retrieve its frequency.
*   **Result Update:** `count += seen_sums.get(target, 0)`.
*   **Structure:** Hash Map / Dictionary mapping `prefix_sum` to frequency (e.g., `collections.defaultdict(int)`), initialized with `{0: 1}`.
*   **Update:** `seen_sums[current_ps] += 1`.

### d) Constraint: `k1 <= current_ps - prev_ps <= k2` (e.g., Count Subarrays with Sum in Range [k1, k2])
*   **Condition on `prev_ps`:** Need `current_ps - k2 <= prev_ps <= current_ps - k1`.
*   **Query:** Find the number of `prev_ps` values in `seen_sums` that fall within the range `[current_ps - k2, current_ps - k1]`. Use two binary searches (lower bound for `current_ps - k2`, upper bound for `current_ps - k1`).
*   **Result Update:** `count += (index_upper - index_lower)`.
*   **Structure:** Sorted Set/List (initialized with `0`).

## 4. Implementation Options and Complexity

Let `M` be the length of the sequence `arr`.

*   **Sorted List + `bisect` (Python):** (Applies to variations a, b, d)
    *   Search: O(log M)
    *   Insert (`bisect.insort`): O(M)
    *   **Overall Time Complexity:** O(M^2)
    *   **Space Complexity:** O(M)
*   **Balanced BST / SortedList:** (Applies to variations a, b, d)
    *   Search (lower/upper bound, range count): O(log M)
    *   Insert: O(log M)
    *   **Overall Time Complexity:** O(M log M)
    *   **Space Complexity:** O(M)
*   **Hash Map (Dictionary):** (Applies to variation c)
    *   Search (`get`): O(1) average
    *   Insert/Update (`[]=`): O(1) average
    *   **Overall Time Complexity:** O(M) average
    *   **Space Complexity:** O(M)

**Trade-offs:** For inequality/range constraints, BST/SortedList offers better asymptotic time complexity than `bisect` on a list. For equality constraints, a hash map is typically the most efficient.

## 5. Related Concepts

*   [[./prefix_suffix_aggregates.md]]: This technique is foundational.
*   [[../../patterns/matrix/dimension_reduction_matrix_to_1d.md]]: Problems using this pattern often reduce to a 1D subproblem solvable by this technique.
*   [[../../data_structures/hash_table_dict.md]]: Relevant for the `== k` variation.
*   [[../../data_structures/heap_priority_queue.md]]: BSTs are related data structures.
*   [[../../optimizations/python_builtin_modules.md]]: Highlights the use of standard library modules like `bisect` and `collections`. 