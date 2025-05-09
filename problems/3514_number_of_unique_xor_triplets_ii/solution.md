# Solution Explanation for 3514. Number of Unique XOR Triplets II

## Problem Summary

Given an integer array `nums`, we need to find the number of unique values resulting from `nums[i] XOR nums[j] XOR nums[k]` where `i <= j <= k` are indices into the array.
The constraints are `nums.length <= 1500` and `nums[i] <= 1500`.

## Algorithmic Strategy: Optimized Iterative Set Construction

This problem seeks the number of unique values of $N_i \\oplus N_j \\oplus N_k$ subject to $i \\le j \\le k$. While a previous $O(N^2 + N \\cdot \\text{MAX_XOR_VAL})$ approach (precomputing pairs and then combining with a third element) passed, it was close to the time limit. A more optimized iterative Python solution, often significantly faster in practice, is used here. This solution dynamically builds sets of achievable XOR sums and features a powerful early exit condition.

**Core Logic:**

The algorithm iterates through the `nums` array, maintaining two primary sets:
1.  `xorTriplets`: Stores the unique XOR sums of three elements ($N_i \\oplus N_j \\oplus N_k$ with $i \\le j \\le k$) found so far.
2.  `xorPairs`: Stores unique XOR sums of two elements ($N_a \\oplus N_b$ with $a < b$) from the prefix of `nums` processed, plus an essential `0`.

**Detailed Steps:**

1.  **Handle Empty Input:** If `nums` is empty, return 0.

2.  **Initialization:**
    *   `xorPairs = {0}`: This set is crucial. The `0` represents an XOR sum of two identical elements (e.g., $N_x \\oplus N_x = 0$). When `num_current` (from the main loop) is XORed with this `0`, it yields `num_current`. This helps correctly form triplets like $N_k \\oplus N_i \\oplus N_i = N_k$.
    *   `xorTriplets = set(nums)`: This initializes the result set. Any `num` in `nums` can form a triplet $num \\oplus num \\oplus num = num$. This also correctly covers cases like $num \\oplus x \\oplus x = num$.
    *   `limit`: An early exit threshold. This is calculated as $2^k$, where $k$ is the bit length of the maximum value in `nums`. If the numbers in `nums` can generate all $2^k$ possible XOR values within this bit range, then `len(xorTriplets)` will reach this `limit`, and we can stop early. Any XOR sum involving numbers from `nums` cannot exceed $2^k-1$. So, `limit` is the maximum possible *count* of unique values if they span the full bit range of `max(nums)`. (For example, if `max(nums)` is 7 (binary `111`, bit_length 3), `limit` is $2^3=8$. All XOR sums will be $<8$. If `max(nums)` is 9 (binary `1001`, bit_length 4), `limit` is $2^4=16$.)

3.  **Iteration:**
    Iterate through `nums` with index `current_idx` and element `current_num = nums[current_idx]`:
    *   **Form Triplets:** `xorTriplets.update(map(current_num.__xor__, xorPairs))`
        At this step, `xorPairs` contains `0` and all unique values $N_a \\oplus N_b$ where $a < b < current\\_idx$ (formed in previous iterations of the main loop).
        *   When `current_num` is XORed with `0` (from `xorPairs`), `current_num` itself is considered for `xorTriplets`. This handles cases like $N_{current\\_idx} \\oplus N_x \\oplus N_x = N_{current\\_idx}$ for $x \\le current\\_idx$.
        *   When `current_num` is XORed with an existing pair $N_a \\oplus N_b$ (where $a < b < current\\_idx$), it forms $N_a \\oplus N_b \\oplus N_{current\\_idx}$. This satisfies $a < b < current\\_idx$, which is a valid $i \\le j \\le k$ ordering.
    *   **Update Pair XORs:** `xorPairs.update(map(current_num.__xor__, islice(nums, 0, current_idx)))`
        This calculates $current\\_num \\oplus N_j$ for all $j < current\\_idx$. These new pair XOR sums are added to `xorPairs`. Now, `xorPairs` will contain `0` and all unique $N_a \\oplus N_b$ where $a < b \\le current\\_idx$. This prepares `xorPairs` for the *next* iteration of the main loop (when processing `nums[current_idx + 1]`).
    *   **Early Exit:** `if len(xorTriplets) >= limit: return limit`
        If `xorTriplets` has reached the `limit` (the theoretical maximum number of unique XOR sums possible given the bit length of `max(nums)`), then all possible unique XOR sums have been found, and the algorithm can terminate early.

4.  **Result:** `return len(xorTriplets)`

**Correctness for Ordered Indices ($i \\le j \\le k$):**
The algorithm correctly generates all unique triplet XOR sums $N_i \\oplus N_j \\oplus N_k$ with $i \\le j \\le k$ because:
*   **Initialization:** `set(nums)` covers $N_x \oplus N_x \oplus N_x = N_x$.
*   **Iteration Logic (when processing `N_k` as `current_num`):**
    *   $N_k \oplus 0$ (from `xorPairs`) effectively covers $N_k \oplus N_i \oplus N_i = N_k$ (for $i \le k$).
    *   $N_k \oplus (N_i \oplus N_j)$ (where $N_i \oplus N_j$ is from `xorPairs`, meaning $i < j < k$) covers $N_i \oplus N_j \oplus N_k$ for $i < j < k$.
    The use of `islice(nums, 0, current_idx)` ensures that when pairs $N_k \oplus N_j$ are formed, $j < k$, satisfying the ordering for future triplet formations.

**Performance:**
*   **Time Complexity:** While the worst-case asymptotic complexity remains $O(N^2 + N \\cdot \text{MAX_XOR_VAL_Range})$ (where $\text{MAX_XOR_VAL_Range}$ is $\approx 2048$), the practical performance is often much better.
    *   The `map(current_num.__xor__, xorPairs)` step iterates `len(xorPairs)` times, not always up to the theoretical maximum 2048. If `xorPairs` stays small, this is fast.
    *   The `map(current_num.__xor__, islice(nums, 0, current_idx))` step contributes to the $O(N^2)$ part for building `xorPairs`.
    *   The early exit condition (`len(xorTriplets) >= limit`) can provide substantial speedups if the `limit` is reached quickly.
*   **Space Complexity:** $O(\text{MAX_XOR_VAL_Range})$ for `xorPairs` and `xorTriplets` in the worst case.

This iterative, dynamic set-building approach is significantly more efficient in practice for Python than static precomputation methods for this problem, largely due to iterating over smaller, actual set sizes and the powerful early exit condition.

**KB Reference:** [[document/optimizations/combinatorics/iterative_set_construction_xor_k_tuples.md]]