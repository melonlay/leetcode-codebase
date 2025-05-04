# LeetCode 188: Best Time to Buy and Sell Stock IV - Solution Explanation

## Problem Summary

Given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`-th day, and an integer `k`, find the maximum profit you can achieve with at most `k` transactions. You must complete a transaction (sell) before starting the next one (buy).

## Algorithmic Approach: Dynamic Programming (Standard)

While the provided Python solution uses a complex heap-based approach, the standard and more generalizable solution for this problem uses Dynamic Programming.

The core idea is to track the maximum profit achievable at day `i` using `j` transactions, considering whether you are holding a stock or not.

**State Definition:**
Let `dp[j][0]` be the maximum profit after day `i` using at most `j` transactions, ending with **no stock** in hand.
Let `dp[j][1]` be the maximum profit after day `i` using at most `j` transactions, ending with **stock** in hand.

We only need to keep track of the states for the current day (`i`) based on the previous day (`i-1`), allowing for space optimization.

**Transitions (Iterating through prices):**
For each price `p = prices[i]`:
Iterate `j` from `1` to `k`:
*   `dp[j][0] = max(dp[j][0], dp[j][1] + p)`
    *   Max profit with no stock: Either rest (previous `dp[j][0]`) or sell the stock held (`dp[j][1] + p`).
*   `dp[j][1] = max(dp[j][1], dp[j-1][0] - p)`
    *   Max profit with stock: Either rest (previous `dp[j][1]`) or buy stock (`dp[j-1][0] - p`). Buying uses up a transaction opportunity, so we look at the profit from `j-1` transactions *before* buying.

**Base Cases:**
*   `dp[j][0] = 0` for all `j` (initially no profit).
*   `dp[j][1] = -infinity` for all `j` (initially cannot hold stock without buying).

**Space Optimization:**
We only need the DP states from the previous day. We can use two arrays (or even update in place carefully) of size `k+1` for `dp[0]` (no stock) and `dp[1]` (stock), reducing space to O(k).

**Result:**
The maximum profit after the last day is `dp[k][0]` (maximum profit using at most `k` transactions, ending with no stock).

## Optimization: `k >= n/2`

If `k` is greater than or equal to `n // 2`, the transaction limit is effectively removed, and the problem becomes equivalent to finding the maximum profit with unlimited transactions (LeetCode 122). This can be solved greedily in O(n) time by summing profits from all consecutive upward price movements.

*   **Reference:** [[../document/optimizations/dynamic_programming/stock_problem_k_optimization.md]]

This check should be performed at the beginning.

## Heap-Based Approach (From `solution.py`)

The provided Python code implements a different, non-standard approach using a min-heap to simulate a max-heap. It iteratively extracts the best current profit or the smallest loss (representing a merge opportunity) and pushes subproblems back onto the heap. While potentially correct, this approach is generally more complex to understand and implement than the standard DP solution.
*   It finds the max profit interval, adds it.
*   Pushes sub-problems: max profit before, max profit after, min loss within.
*   Popping a loss merges intervals.
*   Complexity is less straightforward but potentially faster than O(Nk) if k and the number of price fluctuations are small.

## Knowledge Base References

*   **Standard Approach Pattern:** [[../document/patterns/array/k_limited_operations.md]]
*   **Standard Approach Algorithm:** [[../document/algorithms/dynamic_programming/array/k_limited_operations_dp.md]] (Provides general DP structure).
*   **Standard Approach Optimization:** [[../document/optimizations/dynamic_programming/stock_problem_k_optimization.md]]
*   **(Code's Approach):**
    *   [[../document/data_structures/heap_priority_queue.md]]
    *   [[../document/algorithms/greedy/greedy.md]] (Related concept)

## Complexity Analysis (Standard DP)

*   **Time Complexity:** O(N * k) (where N is the number of prices). O(N) if `k >= n/2` optimization is applied.
*   **Space Complexity:** O(k) (with space optimization). 