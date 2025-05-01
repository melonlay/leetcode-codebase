# Technique: Bitmask State Tracking

## Description

Bitmasking is a technique used to represent and manipulate sets or states compactly using the individual bits of an integer (or a sequence of integers). Each bit in the mask typically corresponds to an element or a flag, where `1` indicates presence/true and `0` indicates absence/false.

This is particularly useful in problems involving subsets, permutations, or states where the number of distinct elements/flags is relatively small (e.g., up to 20-30 for a single 32-bit integer, or up to 60-64 for a 64-bit integer), allowing efficient state representation and manipulation using bitwise operations.

## Core Concepts & Operations

Assume `n` elements, indexed 0 to `n-1`.
A bitmask `mask` is an integer where the `i`-th bit represents the state of element `i`.

*   **Checking if the `i`-th element is set (present/true):**
    ```python
    is_set = (mask >> i) & 1
    # or
    is_set = mask & (1 << i)
    ```
    Result is non-zero (specifically `1 << i`) if set, zero otherwise.

*   **Setting the `i`-th element (mark present/true):**
    ```python
    mask = mask | (1 << i)
    ```

*   **Unsetting the `i`-th element (mark absent/false):**
    ```python
    mask = mask & ~(1 << i)
    ```
    Requires the bitwise NOT operator `~`.

*   **Toggling the `i`-th element:**
    ```python
    mask = mask ^ (1 << i)
    ```

*   **Representing the empty set:** `mask = 0`

*   **Representing the full set (all `n` elements present):** `mask = (1 << n) - 1`

*   **Counting the number of set bits (population count):**
    ```python
    count = bin(mask).count('1') # Simple Python way
    # Or use built-in methods if available/needed for performance
    # e.g., int.bit_count() in Python 3.10+
    ```

*   **Iterating through all subsets (masks from 0 to 2^n - 1):**
    ```python
    for mask in range(1 << n):
        # Process subset represented by mask
    ```

*   **Iterating through all submasks of a given mask:**
    ```python
    submask = mask
    while submask > 0:
        # process submask
        submask = (submask - 1) & mask
    # process empty submask (0)
    ```

## Applications

1.  **Dynamic Programming with Subset States (DP on Subsets):**
    *   Often used when the DP state depends on which elements from a small set have been used or visited.
    *   `dp[mask]` could represent the optimal value/result considering only the elements present in the `mask`.
    *   Transitions involve iterating through elements `i` in the `mask` and relating `dp[mask]` to `dp[mask without i]` (i.e., `dp[mask ^ (1 << i)]`).
    *   **Example:** Traveling Salesperson Problem (TSP) with bitmask DP, problems involving matching or partitioning elements.

2.  **Backtracking / Recursion with Visited States:**
    *   Pass a bitmask representing visited nodes/elements instead of a set or boolean array, especially if `n` is small.
    *   Efficiently check if a node has been visited and update the visited state.
    *   **Example:** Finding Hamiltonian paths, permutations with constraints.

3.  **Representing Set Operations:** Bitwise AND (`&`), OR (`|`), XOR (`^`) correspond to set intersection, union, and symmetric difference.

4.  **Graph Algorithms:** Representing subsets of nodes visited or included in a path/solution.

## When to Use

*   The number of elements/flags `n` is small (typically <= 20-25 for competitive programming, up to 64 if using 64-bit integers).
*   Problems involving subsets, permutations, or state combinations.
*   Need for efficient representation and manipulation (checking, setting, unsetting) of set-like states.
*   Dynamic programming where the state depends on subsets of items used.

## Tradeoffs

*   **Efficiency:** Bitwise operations are extremely fast.
*   **Space:** Very compact state representation (one integer per state).
*   **Scalability:** Limited by the number of bits in standard integer types. Does not scale well for large `n`.
*   **Readability:** Can be less readable than using explicit sets or boolean arrays if not familiar with bitwise operations.

## Related Concepts

*   Bitwise Operations (AND, OR, XOR, NOT, Shifts)
*   Dynamic Programming (DP on Subsets)
*   Backtracking
*   Sets
*   Graph Theory 