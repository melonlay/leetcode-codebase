## 188. Best Time to Buy and Sell Stock IV

### Problem Summary

Given an array `prices` where `prices[i]` is the stock price on day `i`, and an integer `k`, find the maximum profit achievable by completing at most `k` transactions. A transaction consists of buying and then selling a stock. You cannot hold multiple stocks simultaneously.

### Algorithmic Approach (Heap-based)

This solution uses a greedy approach combined with a min-heap to efficiently find the `k` most profitable transactions.

The core idea is to iteratively find the best possible action (either taking a direct profit or enabling a future merge by identifying a loss) and repeat this `k` times.

**1. `max_inc` Helper Function:**
   - This function searches within a given price interval (`start` to `end`).
   - If `direction=1`, it finds the single transaction (buy low, sell high) that yields the maximum profit within that interval.
   - If `direction=-1`, it finds the transaction (buy high, sell low) that represents the *maximum loss* (or the smallest dip) within the interval. It returns the *magnitude* of this loss (a positive value).

**2. Heap Structure:**
   - A min-heap (`heapq`) is used to store potential actions, prioritized by their profit potential.
   - Each item in the heap is a tuple: `(-profit_or_loss_magnitude, interval_start, trade_start, trade_end, interval_end, direction)`.
   - We store the negative profit or loss magnitude so that the min-heap effectively acts as a max-heap, always giving us the action associated with the largest profit (or smallest loss to cancel).

**3. Algorithm Steps:**
   - **Initialization:** Find the single most profitable trade (`direction=1`) in the entire price array (`0` to `n-1`). If profit exists, push its details (with negative profit) onto the heap.
   - **Iteration (up to `k` times):**
     - While `transactions_done < k` and the heap is not empty:
       - Pop the best action (highest profit or smallest loss) from the heap.
       - **If `direction == 1` (Profitable Trade):**
         - Add the profit (`-neg_profit_or_loss`) to `total_max_profit`.
         - Increment `transactions_done`.
         - **Split and Search:** Since we've "consumed" the trade from `current_trade_start` to `current_trade_end`, we need to find the next best actions in the surrounding and internal intervals:
           - Search for the best *loss* (`direction=-1`) *within* the consumed trade interval (`current_trade_start + 1` to `current_trade_end - 1`). Push `(-loss_magnitude, ...)` if found. This represents the potential gain from merging later.
           - Search for the best *profit* (`direction=1`) *before* the consumed trade (`interval_start` to `current_trade_start - 1`). Push `(-profit, ...)` if found.
           - Search for the best *profit* (`direction=1`) *after* the consumed trade (`current_trade_end + 1` to `interval_end`). Push `(-profit, ...)` if found.
       - **If `direction == -1` (Loss Cancellation / Merge):**
         - This action signifies that cancelling out this specific loss allows merging two previously distinct profitable segments into a single, larger potential trade.
         - We don't increment `transactions_done` here because the original trades surrounding this loss were already counted.
         - Search for the best *profit* (`direction=1`) within the *entire interval* spanned by the cancelled loss (`interval_start` to `interval_end`). Push `(-profit, ...)` if found. This represents the new best single trade within the now-merged segment.

**4. Large `k` Optimization:**
   - Similar to the DP approach, if `k >= n / 2`, the problem simplifies to finding the sum of all positive price differences between consecutive days (infinite transactions).

**5. Final Result:**
   - The `total_max_profit` accumulated after the loop is the maximum profit achievable with at most `k` transactions.

### Knowledge Base References

*   **Algorithm Paradigm:** This solution employs a **Greedy Strategy** aided by a priority queue (heap). See potentially `document/algorithms/greedy/greedy.md`.
*   **Specific Algorithm:** This specific heap-based technique for problems with k limited operations is documented in `document/algorithms/greedy/array/k_limited_operations/k_operations_heap.md`.
*   **Data Structure:** Uses a **Min-Heap (Priority Queue)**. See potentially `document/data_structures/heap_priority_queue.md`.
*   **Related Algorithm:** The standard **Dynamic Programming** approach for k limited operations is documented in `document/algorithms/dynamic_programming/array/k_limited_operations/k_operations_dp.md`.

### Complexity Analysis

*   **Time Complexity:** While a strict proof is complex, this approach often performs significantly better than O(N*k) DP, especially for larger `k`. Each `max_inc` scan takes O(interval length). In the worst case, we might push/pop O(N) items from the heap, and heap operations take O(log HeapSize). The heap size can be up to O(N). A reasonable estimate is often O(N log N) or potentially O(N log k) or O(k log N) depending on the price patterns and `k`.
*   **Space Complexity:** O(N) in the worst case for storing potential trades/losses in the heap.

### Algorithmic Approach

The problem asks for the maximum profit with a limit on the number of transactions, which suggests a Dynamic Programming approach. We need to keep track of the day, the number of transactions used, and whether we are currently holding a stock.

**1. State Definition:**

We can define `dp[i][t][0]` as the maximum profit after day `i-1` (considering prices up to `prices[i-1]`) having completed at most `t` transactions, and *not* holding a stock at the end of day `i-1`.

Similarly, `dp[i][t][1]` is the maximum profit after day `i-1` having completed at most `t` transactions, and *holding* a stock at the end of day `i-1`.

**2. Base Cases:**

*   `dp[0][t][0] = 0` for all `t`: No profit before any days.
*   `dp[0][t][1] = -infinity` for all `t`: Cannot hold a stock before day 0.
*   `dp[i][0][0] = 0` for all `i`: No profit with 0 transactions.
*   `dp[i][0][1] = -infinity` for all `i`: Cannot hold a stock with 0 transactions.

**3. Transitions:**

For each day `i` (from 1 to `n`) and transaction count `t` (from 1 to `k`):

*   `dp[i][t][0] = max(dp[i-1][t][0], dp[i-1][t][1] + prices[i-1])`
    *   Max of: (Not holding yesterday) vs (Holding yesterday and selling today at `prices[i-1]`)
*   `dp[i][t][1] = max(dp[i-1][t][1], dp[i-1][t-1][0] - prices[i-1])`
    *   Max of: (Holding yesterday) vs (Not holding yesterday after `t-1` transactions and buying today at `prices[i-1]`. Buying starts the `t`-th transaction).

**4. Space Optimization:**

Notice that the transitions for day `i` only depend on the results from day `i-1`. We can optimize the space complexity from O(n*k) to O(k) by only storing the DP state for the current day being processed. We use two arrays (or a 2D array `dp[k+1][2]`) to represent the states for the current price.

Let `dp[t][0]` be the max profit with `t` transactions, not holding, *after considering the current price*.
Let `dp[t][1]` be the max profit with `t` transactions, holding, *after considering the current price*.

When iterating through prices, we update these states. The transitions become:

```python
for price in prices:
    # Iterate backwards to avoid using updated values within the same price iteration
    for t in range(k, 0, -1):
        # Update dp[t][0] (not holding): max(didn't sell today, sold today)
        dp[t][0] = max(dp[t][0], dp[t][1] + price)
        # Update dp[t][1] (holding): max(didn't buy today, bought today)
        # Buying uses profit from previous transaction (t-1) without holding
        dp[t][1] = max(dp[t][1], dp[t - 1][0] - price)
```

The initialization becomes `dp = [[0, -float('inf')] for _ in range(k + 1)]`.

**5. Large `k` Optimization:**

If `k` is greater than or equal to `n // 2`, where `n` is the number of prices, we can perform as many transactions as we want (buy whenever the price increases). This is because the maximum number of profitable transactions (buy low, sell high immediately) is `n // 2`. In this scenario, the problem reduces to the "Best Time to Buy and Sell Stock II" problem.

We calculate the profit by summing up all positive price differences between consecutive days:

```python
if k >= n // 2:
    max_profit_inf = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            max_profit_inf += prices[i] - prices[i - 1]
    return max_profit_inf
```

**6. Final Result:**

The final answer is `dp[k][0]`, representing the maximum profit after processing all prices, using at most `k` transactions, and not holding a stock.

### Knowledge Base References

*   **Algorithm Paradigm:** This solution uses **Dynamic Programming**. A general description can potentially be found in `document/algorithms/dynamic_programming/dynamic_programming.md`.
*   **Specific Problem Type:** This falls under the category of stock trading problems solvable with DP, potentially documented in `document/algorithms/dynamic_programming/array/k_limited_operations/k_operations_dp.md`.
*   **Optimization Technique:** The reduction of space complexity from O(n*k) to O(k) is a **DP Space Optimization** technique, potentially found in `document/techniques/dp_space_optimization.md`.
*   **Related Pattern:** The large `k` optimization transforms the problem into the **Infinite Stock Transactions** pattern, potentially described in `document/patterns/stock_trading_infinite_transactions.md`.

### Complexity Analysis

*   **Time Complexity:** O(n * k), where `n` is the number of prices. We iterate through each price (n) and for each price, we iterate through the possible transaction counts (k).
*   **Space Complexity:** O(k), due to the space optimization storing the DP states for `k` transactions. 