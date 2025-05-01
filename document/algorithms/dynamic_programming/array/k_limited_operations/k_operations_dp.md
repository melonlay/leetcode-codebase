# DP on Arrays with K Limited Operations

See General DP Paradigm: `../../dynamic_programming.md`
Alternative Heap Approach: `../../../greedy/array/k_limited_operations/k_operations_heap.md`

## Problem Pattern Description

This pattern applies to problems involving maximizing (or minimizing) a value over a sequence (array) where the process is constrained by performing at most `k` specific state-changing operations.

## Dynamic Programming Approach

**State:**
The state typically includes:
*   The current index `i` being considered in the sequence.
*   The number of operations `op` already used (up to `k`).
*   Additional state variables required by the problem (e.g., holding/not holding, cooldown status).

*   `dp[i][op][state]`: Max/min value after considering index `i-1`, using `op` operations, ending in `state`.

**Transitions:**
Transitions define how to calculate `dp[i][op][state]` based on states at `i-1`. They depend heavily on the specific operations allowed:
*   Transitions that *don't* consume an operation (e.g., resting, staying in the same secondary state).
*   Transitions that *do* consume an operation (e.g., buying a stock, performing an action). These typically reference a state with `op-1` operations from the previous index `i-1`.

**(Example: Stock Trading - see `k_operations_dp.md` in `stock_trading` for specific transitions)**

**Base Cases:**
Initialize DP table considering initial conditions (e.g., zero value before start, impossible states set to +/- infinity, state at index 0).

**Space Optimization:**
If transitions only depend on `i-1`, space can often be reduced to O(k * num_states) by dropping the `i` dimension.

**Problem-Specific Optimizations:**
Look for characteristics of the specific problem that might allow optimizations (e.g., the `k >= n/2` case in stock trading).

## Complexity
*   Time: O(n * k * num_states)
*   Space: O(k * num_states) (with space optimization)

## Applicability
Use when:
*   Optimal solution depends on choices made at previous indices.
*   There's a strict limit `k` on a specific type of action.
*   The state can be clearly defined including the operation count. 