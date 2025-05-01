# Technique: Prefix/Suffix Aggregates (Sum, Max, Min, etc.)

## Description

Prefix and Suffix Aggregate techniques involve precomputing cumulative values (like sum, maximum, minimum, product, counts based on properties) from the beginning (prefix) or end (suffix) of a sequence (array, list, string).

This precomputation allows for efficient O(1) querying of the aggregate value over any prefix or suffix, and often enables O(1) calculation of aggregates over arbitrary *ranges* (subarrays/substrings).

## Core Idea & Common Aggregates

Given an input sequence `A` of size `n`.

1.  **Prefix Sum (`prefix_sum`):**
    *   `prefix_sum[i]` stores the sum of elements `A[0...i-1]` (or `A[0...i]`, definition varies).
    *   If `prefix_sum[i] = sum(A[0...i-1])`, then `prefix_sum[0] = 0`.
    *   Computed in O(n): `prefix_sum[i] = prefix_sum[i-1] + A[i-1]`
    *   **Range Sum `sum(A[j...k])`:** `prefix_sum[k+1] - prefix_sum[j]` (adjust indices based on definition).
    *   Use Case: Quickly find sum of subarrays.

2.  **Prefix Maximum (`prefix_max`):**
    *   `prefix_max[i]` stores the maximum value in the subsequence `A[0...i]`.
    *   Computed in O(n): `prefix_max[i] = max(prefix_max[i-1], A[i])` (with `prefix_max[0] = A[0]`)
    *   **Range Max `max(A[0...i])`:** `prefix_max[i]`
    *   Use Case: Find max value up to a point (e.g., Trapping Rain Water DP).

3.  **Suffix Maximum (`suffix_max`):**
    *   `suffix_max[i]` stores the maximum value in the subsequence `A[i...n-1]`.
    *   Computed in O(n) from right-to-left: `suffix_max[i] = max(suffix_max[i+1], A[i])`.
    *   **Range Max `max(A[i...n-1])`:** `suffix_max[i]`
    *   Use Case: Find max value from a point onwards (e.g., Trapping Rain Water DP).

4.  **Prefix/Suffix Minimum:** Analogous to maximum.

5.  **Prefix/Suffix Product:** Similar, but watch out for zeros and potential overflow.

6.  **Prefix XOR Sum:** `prefix_xor[i] = A[0] ^ A[1] ^ ... ^ A[i-1]`. Range XOR `A[j...k]` = `prefix_xor[k+1] ^ prefix_xor[j]`.

7.  **Prefix Counts:** `prefix_count[i]` could store the count of elements satisfying a property in `A[0...i]`. Range count = `prefix_count[k] - prefix_count[j-1]`.

## Implementation

Typically involves creating a new array (or modifying in-place if allowed and careful) of size `n` or `n+1`. A single pass (or two passes for prefix+suffix) computes the aggregate array.

```python
# Example: Prefix Sum (definition: prefix_sum[i] = sum(A[0...i-1]))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + A[i]

# Example: Prefix Max (definition: prefix_max[i] = max(A[0...i]))
prefix_max = [0] * n
if n > 0:
    prefix_max[0] = A[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], A[i])
```

## When to Use

*   Problems requiring frequent calculation of sums, max/mins, or other aggregates over ranges (subarrays/substrings).
*   As a precomputation step in dynamic programming or other algorithms where range aggregates are needed repeatedly.
*   Problems involving differences or relationships between elements at different positions that can be rephrased using prefix aggregates (e.g., finding subarrays with a specific sum `k` using prefix sums and a hash map: `prefix_sum[j] - prefix_sum[i] == k`).
*   Calculating boundary conditions based on values to the left/right (e.g., prefix/suffix max in Trapping Rain Water).

## Complexity

*   **Preprocessing Time:** O(n) to compute the prefix/suffix aggregate array.
*   **Query Time:** O(1) to get the aggregate over any prefix, suffix, or range (for sums, XORs, counts etc.).
*   **Space Complexity:** O(n) to store the aggregate array (can sometimes be O(1) if input modification is allowed and only the previous value is needed during a single pass algorithm).

## Related Concepts

*   Dynamic Programming
*   Sliding Window (Sometimes uses prefix sums)
*   [Pattern: Find Capacity Between Boundaries](../../patterns/array/find_capacity_between_boundaries.md) (Uses prefix/suffix max for DP solution)
*   Difference Arrays

``` 