# Optimization: Top-Down vs Bottom-Up for Digit DP with Carry/Counts

## Context

This compares implementation styles for the [[../../patterns/digit_dp/digit_dp_carry_counts.md]] pattern, which involves Digit DP with complex carry propagation and tracking multiple constraints (like total count `M` and a property `K`).

## Bottom-Up (Iterative) Approach

*   **Implementation:** Uses nested loops. Outer loop iterates through bit positions `j`. Inner loops iterate through previously calculated valid states `(m, carry, k)` for bit `j-1`. A new DP table (often dictionary) `dp_next` is built for bit `j`.
*   **State:** Typically `dp_j[m][carry][k]` or `dp_j[(m, carry, k)]`, where `m` = count used so far, `k` = property value accumulated so far, `carry` = carry into bit `j`.
*   **Pros:**
    *   Avoids Python recursion depth limits.
    *   Can have slightly lower function call overhead compared to recursion.
    *   State evolution might be easier to trace step-by-step.
    *   Explicit control over DP table management (e.g., only storing necessary layers).
*   **Cons:**
    *   Can be more verbose due to explicit table management and loops.
    *   Might compute states that are ultimately unreachable from the final target state (though often necessary for intermediate calculations).

## Top-Down (Recursive with Memoization) Approach

*   **Implementation:** Uses a recursive function `dp(state...)` memoized with `@lru_cache` or a manual dictionary.
*   **State:** Typically defined by function arguments, e.g., `dp(remaining_m, remaining_k, current_bit_i, carry_value)`. State often uses "remaining" counts.
*   **Pros:**
    *   Significantly more concise code, especially with `@lru_cache`.
    *   Often aligns more closely with a mathematical recurrence relation.
    *   Naturally computes only the states reachable from the initial call (potentially fewer states computed than bottom-up if the state space is sparse).
*   **Cons:**
    *   Subject to Python's recursion depth limit (can be increased with `sys.setrecursionlimit`, but has implications).
    *   Function call overhead can be slightly higher than iteration.
    *   Debugging recursion can sometimes be more complex.
*   **Calculation:** Typically uses the `nCr`-based formulation (Formulation 1) within the recursion.

## State Representation Differences

*   **Counts/Properties:** Iterative usually tracks *used/accumulated* values (e.g., `m` elements used, `k` bits found). Recursive often tracks *remaining* values (e.g., `m` elements left, `k` bits needed).
*   **Carry:** Iterative typically passes the single bit carry *into* the next state calculation. Recursive often passes the full numerical `carry_value` that resulted *from* the previous state, which is then processed (`% Base`, `// Base`) within the function call.

## Pruning / Optimizations

*   Top-down allows for potentially intuitive pruning within the function by checking if the current state can possibly reach the target. Example: `if remaining_m + carry_value.bit_count() < remaining_k: return 0`.
*   Bottom-up implicitly prunes by not generating invalid next states, but similar explicit checks could be added before the innermost loop.

## Conclusion

Both approaches are valid and achieve the same result with similar asymptotic complexity.

*   Choose **Top-Down (Recursive)** for conciseness and potentially faster implementation time, especially if recursion depth is not a concern and the state space reachable from the start is much smaller than the theoretical maximum.
*   Choose **Bottom-Up (Iterative)** for potentially slightly better runtime performance (due to lower overhead), guaranteed avoidance of recursion limits, and potentially easier step-by-step debugging.

Ensure foundational techniques like [[../../techniques/combinatorics/iterative_nCr_modulo.md]] and [[../../techniques/recursion/memoization.md]] (for Top-Down) are understood.

*   **Calculation Variants:** Can compute the summed term using `nCr` within the transition (Formulation 1) or `1/c!` within the transition and multiply by `M!` at the end (Formulation 2). Formulation 2 requires careful handling of the final carry's bit count during aggregation. See [[../../patterns/digit_dp/digit_dp_carry_counts.md]] for details.
    *   **Performance Note:** While asymptotically similar, **Formulation 2 (using `ifac[j]` lookup in the transition)** can be significantly faster in practice than Formulation 1 (calculating `nCr(n, k)` in the transition). This is because the `ifac` lookup is O(1) after precomputation, whereas `nCr` involves several multiplications/lookups within the recursive step. This constant factor improvement can lead to substantial runtime reductions (e.g., observed 2x speedup in some problems). 