# Optimization: List vs. Set for Visited Tracking

## Context

When implementing algorithms involving traversal or simulation where detecting previously visited states/nodes/indices is necessary (e.g., graph traversals like BFS/DFS, simulations with cycle detection), a common task is to maintain a collection of visited items.

Two common Python implementations for this are:
1.  Using a boolean `list` (or array) initialized to `False`.
2.  Using a `set`.

This document compares these two approaches.

## Comparison

| Feature             | Boolean List (`visited = [False] * n`) | Set (`visited = set()`)                  |
| :------------------ | :------------------------------------- | :--------------------------------------- |
| **Time - Lookup**   | `O(1)` (Direct Indexing)               | `O(1)` (Average, Hash Lookup)            |
| **Time - Insertion**| `O(1)` (Direct Assignment)             | `O(1)` (Average, Amortized Hash Insert)  |
| **Space Complexity**| `O(N)` (Where N is the max index + 1)  | `O(k)` (Where k is the number visited)   |
| **Memory Overhead** | Potentially lower per element          | Potentially higher per element (hashing) |
| **Initialization**  | Requires knowing max index `N` upfront | Does not require knowing size upfront    |
| **Flexibility**     | Best for dense integer indices 0 to N-1| Handles sparse indices, non-integers     |
| **Bounds Checking** | Requires explicit check *before* access| Implicitly handles non-members           |

## Trade-offs and When to Use

*   **Boolean List:**
    *   **Pros:** Can offer slightly better **constant factor performance** due to direct memory access via indexing, potentially lower memory overhead per element.
    *   **Cons:** Requires knowing the maximum possible index value (`N`) beforehand to pre-allocate the list. Only suitable for tracking non-negative integer indices within a known, dense range `[0, N-1]`. Requires explicit bounds checking before accessing `list[index]` to prevent `IndexError`.
    *   **Use When:** The items being tracked are integers within a known, reasonably sized range `[0, N-1]`, and achieving the absolute best constant factor performance is critical.

*   **Set:**
    *   **Pros:** More flexible – handles any hashable type (not just integers), works well with sparse indices or when the range of indices is unknown or very large. Does not require upfront size allocation. Checking membership (`item in visited_set`) is idiomatic and clean.
    *   **Cons:** May have slightly higher constant factor overhead for lookups/insertions compared to direct list indexing due to hashing. Can have higher memory overhead per element stored.
    *   **Use When:** The items being tracked are not necessarily dense integers (e.g., tuples, strings, sparse large integers), the range is unknown or very large, or the flexibility and cleaner membership checking are preferred.

## Example Scenario (Problem 3522 Simulation)

In LeetCode 3522, we track visited instruction indices `i` where `0 <= i < n`. Both approaches are viable:

*   `visit = [False] * n`: Works well because indices are dense integers in `[0, n-1]`. Requires `while 0 <= i < n and not visit[i]:` or separate checks.
*   `visited = set()`: Also works well. Requires `while True: if i < 0 or i >= n or i in visited: break; visited.add(i) ...`

In this specific case, the list approach *might* provide a marginal constant factor speedup, but the set approach is arguably slightly simpler to implement regarding the combined termination checks inside the loop.

## Related Concepts

*   [[../../data_structures/hash_table_dict.md]] (Underlying concept for Sets) 