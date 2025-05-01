# DP Approach for K Limited Operations on Arrays

**Applies Pattern:** [[../../../patterns/array/k_limited_operations.md|Pattern: K-Limited Operations on Arrays]]

**Paradigm:** [[../dynamic_programming.md|Dynamic Programming]]
**Alternative:** [[../greedy/array/k_limited_operations_heap.md|Greedy/Heap Approach]]

## Problem Pattern Context

This dynamic programming approach is applicable to the **K-Limited Operations** pattern, particularly when:
*   The problem involves maximizing (or minimizing) a value over a sequence (array).
*   The process is constrained by performing at most `k` specific state-changing operations.
*   The optimal solution for a subproblem depends on optimal solutions to smaller subproblems (optimal substructure).
*   Overlapping subproblems exist.

## Dynamic Programming Approach

**State:**
The state typically includes:
*   The current index `i` being considered in the sequence.
*   The number of operations `op` already used (up to `k`).
*   Additional state variables required by the specific problem (e.g., holding/not holding a stock, cooldown status).

*   `dp[i][op][state]`: Represents the max/min value after considering index `i-1` (or `i`), having used `op` operations, and ending in `state`.

**Transitions:**
Transitions define how to calculate `dp[i][op][state]` based on states at `i-1`. They are highly dependent on the specific operations allowed by the problem:
*   **No Operation Used:** Transitions representing actions like resting, holding, or skipping the current element without consuming one of the `k` operations. These typically look at `dp[i-1][op][...]`.
*   **Operation Used:** Transitions representing actions like buying, selling, or performing the specific limited action. These typically consume an operation and look at `dp[i-1][op-1][...]`.

**(Example: Stock Trading - Detailed transitions often exist in specific problem documentation, like for LeetCode 123 or 188).**

**Base Cases:**
Initialize the DP table carefully based on the initial conditions at the start of the sequence (e.g., `i=0` or before). Often involves setting impossible states to negative/positive infinity and initial valid states to 0 or their starting values.

**Space Optimization:**
If transitions only depend on the immediately preceding index (`i-1`), the space complexity can often be reduced from O(n * k * num_states) to O(k * num_states) by using only two layers (current and previous) or even a single layer for the DP table, carefully managing updates.

**Problem-Specific Optimizations:**
Analyze the specific problem for edge cases or properties that might allow optimizations. For example, in stock trading problems, if `k` is large enough (`k >= n/2`), the constraint might become non-limiting, simplifying the problem.

## Complexity
*   **Time:** O(n * k * num_states) - Where `num_states` is the number of additional state variables.
*   **Space:** O(k * num_states) (assuming space optimization is applied), otherwise O(n * k * num_states).

## Applicability
Use when:
*   Optimal solution has optimal substructure and overlapping subproblems.
*   There's a strict limit `k` on a specific type of action.
*   The state can be clearly defined, including the operation count and any other necessary status information.
*   O(n * k) or similar time complexity is acceptable. 