# 3266. Final Array State After K Multiplication Operations II

## Problem Summary

Given an array `nums`, an integer `k`, and a `multiplier`, perform `k` operations. In each operation, find the smallest element (first occurrence if ties) and replace it with `element * multiplier`. Finally, apply modulo `10^9 + 7` to all elements.

## Approach: Phased Simulation (Round-Robin Detection)

The core challenge is the potentially massive value of `k` (up to `10^9`), which makes direct simulation `k` times (`O(k log n)`) infeasible due to Time Limit Exceeded (TLE).

Observing the process, we can identify two distinct phases:

1.  **Phase 1: Initial Operations & Order Establishment:**
    *   **Goal:** Simulate the operations step-by-step *only* until every element in the original `nums` array has been selected and multiplied at least once, OR until `k` operations are fully consumed.
    *   **Why?** The crucial insight is that once every element has been operated on, the system likely enters a stable state where operations cycle through the `n` elements in a predictable round-robin fashion based on their relative values.
The primary purpose of this phase is to determine the **final relative order** of elements when this stability is potentially reached.
    *   **Implementation:**
        *   Use a min-heap `heap` storing `(value, index)` tuples. Python's large integers handle potentially large values.
        *   Use a set `unseen` (or `operated_once`) to track indices that have *not* yet been popped and multiplied.
        *   In a loop `while k > 0 and unseen:`:
            *   Get the minimum element `(current_val, idx)` using `heap[0]`.
            *   Use `heapq.heappushpop(heap, (current_val * multiplier, idx))` to efficiently simulate one operation (multiply the minimum, push it back, and pop the overall smallest).
            *   Decrement `k`.
            *   Remove `idx` from `unseen`.
    *   **End State:** This loop terminates when `k` reaches 0 or `unseen` becomes empty. The `heap` now contains the values corresponding to the state *after* this initial phase, and `k` holds the number of *remaining* operations.

2.  **Phase 2: Bulk Calculation for Remaining Operations:**
    *   **Goal:** Calculate the effect of the remaining `k` operations without further step-by-step simulation.
    *   **Logic:** Since we assume a stable round-robin state after Phase 1, the remaining `k` operations will consist of `num_cycles = k // n` full cycles (where every element is multiplied) and `final_few_ops = k % n` individual operations hitting the smallest elements *as they were ordered at the end of Phase 1*.
    *   **Implementation:**
        *   Iterate `n` times, popping elements `(val_p1, idx)` from the `heap` (which holds the Phase 1 end state). The order of popping (`i` from 0 to `n-1`) determines the rank.
        *   For each popped element `(val_p1, idx)` with rank `i`:
            *   Calculate the exponent representing the operations applied *during Phase 2*: `exponent_p2 = num_cycles + (i < final_few_ops)`.
The `(i < k % n)` part adds 1 to the exponent only for the first `k % n` smallest elements popped.
            *   Calculate the final value: `final_val = (val_p1 * pow(multiplier, exponent_p2, mod)) % mod`.
            *   Store this `final_val` in the result array at the correct `idx`.

## Why this Approach Works & Avoids Pitfalls:

*   **Handles Large `k`:** Avoids `O(k log n)` simulation. Phase 1 is bounded (stops when `unseen` is empty or `k=0`). Phase 2 is `O(n log n)` (due to heap pops) + `O(n)` calculation.
*   **Avoids Float Precision Issues:** Uses only exact integer arithmetic.
*   **Avoids Large `pow()` in Loops:** Calculates `pow()` only once per element at the very end, using modular exponentiation.
*   **Correctness:** It correctly captures the effect of Phase 1 operations in the `val_p1` base value and calculates the additional exponent needed for Phase 2 operations based on the established relative order.

## Complexity Analysis:

*   **Time Complexity:** `O(P1_Ops * log n + n log n)`, where `P1_Ops` is the number of operations in Phase 1 (at most `k`, but typically much smaller, related to `n` and value distribution). The `n log n` comes from the `n` heap pops in Phase 2. If Phase 1 dominates (e.g., `k` is small), it's closer to `O(k log n)`. If Phase 2 dominates (large `k`), it's closer to `O(n log n)` assuming Phase 1 finishes reasonably quickly.
*   **Space Complexity:** `O(n)` for storing the heap and the result array.

## Knowledge Base Links:

*   **Pattern:** [[../../document/patterns/simulation/phased_simulation_large_k.md]]
*   **Optimization Comparison:** [[../../document/optimizations/simulation/large_k_simulation_strategies.md]]
*   **Common Mistakes Avoided:**
    *   [[../../document/common_mistakes/float_precision_in_comparisons.md]]
    *   [[../../document/common_mistakes/large_exponent_performance.md]]

## Implementation Details

*   We use `heapq`