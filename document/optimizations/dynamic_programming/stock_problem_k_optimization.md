# Optimization: K-Transactions Stock Problem Constraint (`k >= n/2`)

**Related Problems:** LeetCode 123 (k=2), LeetCode 188 (variable k)
**Related Pattern:** [[../../patterns/array/k_limited_operations.md]]
**Related Algorithm:** [[../../algorithms/dynamic_programming/array/k_limited_operations_dp.md]]

## Context

Stock trading problems often involve maximizing profit with a limit of at most `k` transactions (where one transaction is a buy-sell pair).

Standard Dynamic Programming solutions typically have a time complexity related to O(n * k), where `n` is the number of days (prices).

## Optimization Condition

A key observation arises when `k` is large relative to `n`.

If `k >= n / 2`, the constraint of `k` transactions becomes non-binding. Why?

*   A single transaction (buy-sell) involves at least two days.
*   To maximize profit, we ideally buy low and sell high on every upward price movement.
*   The maximum number of non-overlapping, profitable transactions possible in an array of length `n` is `floor(n / 2)` (e.g., buy day 0, sell day 1; buy day 2, sell day 3; ...).
*   Therefore, if `k` allows at least `n / 2` transactions, we can effectively perform as many transactions as are profitable.

## Simplified Problem: Unlimited Transactions

When `k >= n / 2`, the problem simplifies to finding the maximum profit with *unlimited* transactions (LeetCode 122: Best Time to Buy and Sell Stock II).

This can be solved greedily in O(n) time:

```python
def maxProfitUnlimited(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        # Add profit from every upward price movement
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit
```

## Applying the Optimization

In solutions for problems like LeetCode 188 (Best Time to Buy and Sell Stock IV), check for the condition `k >= n // 2` at the beginning. If true, apply the simple O(n) greedy calculation for unlimited transactions and return the result immediately. This avoids running the potentially more complex O(n * k) DP solution when it's not necessary.

## Complexity Benefit

*   Reduces time complexity from O(n * k) to O(n) when `k` is large.
*   Simplifies the implementation significantly for this specific case. 