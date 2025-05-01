import heapq
from typing import List


class Solution:
    """Solves the Best Time to Buy and Sell Stock IV problem using a heap-based approach."""

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """Calculates the maximum profit with at most k transactions using a heap.

        This approach iteratively finds the most profitable transaction or
        the "most profitable merge" (by finding the smallest loss to remove)
        and adds it to the total profit, up to k times.

        Args:
            k: The maximum number of transactions allowed.
            prices: A list of stock prices for consecutive days.

        Returns:
            The maximum profit achievable.
        """
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # Optimization for k >= n / 2 (same as original DP)
        if k >= n // 2:
            max_profit_inf = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit_inf += prices[i] - prices[i - 1]
            return max_profit_inf

        def max_inc(start: int, end: int, direction: int) -> tuple[int, int, int]:
            """Finds the max increase (direction=1) or max decrease (direction=-1, returned as positive loss)
               within the prices[start...end] interval.

            Args:
                start: Starting index of the interval.
                end: Ending index of the interval.
                direction: 1 for finding max profit, -1 for finding max loss (smallest dip).

            Returns:
                A tuple containing:
                - The maximum profit (if direction=1) or maximum loss magnitude (if direction=-1).
                - The start index of the identified transaction/dip.
                - The end index of the identified transaction/dip.
            """
            max_increase = 0
            result_start = result_end = start
            # Min price if direction=1, Max price if direction=-1
            current_min_max = prices[start]
            current_min_max_idx = start

            for i in range(start + 1, end + 1):
                price = prices[i]
                increase = direction * (price - current_min_max)
                if max_increase < increase:
                    result_start, result_end, max_increase = current_min_max_idx, i, increase
                # If direction=1, find new minimum to buy.
                # If direction=-1, find new maximum to "buy" (start of dip).
                if direction * price < direction * current_min_max:
                    current_min_max, current_min_max_idx = price, i
            return max_increase, result_start, result_end

        total_max_profit = 0
        # Heap stores: (-profit_or_loss_magnitude, interval_start, trade_start, trade_end, interval_end, direction)
        # Use negative profit/loss for min-heap to act as max-heap.
        heap: List[tuple[int, int, int, int, int, int]] = []

        # Find the initial best trade in the whole interval
        initial_profit, trade_start, trade_end = max_inc(0, n - 1, 1)
        if initial_profit > 0:
            heapq.heappush(heap, (-initial_profit, 0,
                           trade_start, trade_end, n - 1, 1))

        transactions_done = 0
        while transactions_done < k and heap:
            # Get the transaction with the highest profit (or the merge with the smallest loss)
            neg_profit_or_loss, interval_start, current_trade_start, current_trade_end, interval_end, direction = heapq.heappop(
                heap)

            # If direction is 1, it's a profitable trade
            if direction == 1:
                total_max_profit -= neg_profit_or_loss  # Add profit
                transactions_done += 1

                # After taking the profit from current_trade_start to current_trade_end:
                # 1. Look for the best *loss* (smallest dip, direction=-1) within this trade's interval.
                #    Pushing this onto the heap represents the potential profit gain if we merge
                #    the segments before and after this dip later.
                loss_profit, loss_start, loss_end = max_inc(
                    current_trade_start + 1, current_trade_end - 1, -1)
                if loss_profit > 0:
                    heapq.heappush(heap, (-loss_profit, current_trade_start + 1,
                                   loss_start, loss_end, current_trade_end - 1, -1))

                # 2. Look for the best *profit* (direction=1) in the interval *before* this trade.
                profit_before, trade_start_before, trade_end_before = max_inc(
                    interval_start, current_trade_start - 1, 1)
                if profit_before > 0:
                    heapq.heappush(heap, (-profit_before, interval_start,
                                   trade_start_before, trade_end_before, current_trade_start - 1, 1))

                # 3. Look for the best *profit* (direction=1) in the interval *after* this trade.
                profit_after, trade_start_after, trade_end_after = max_inc(
                    current_trade_end + 1, interval_end, 1)
                if profit_after > 0:
                    heapq.heappush(heap, (-profit_after, current_trade_end + 1,
                                   trade_start_after, trade_end_after, interval_end, 1))

            # If direction is -1, it represents merging two previously separated profitable segments
            # by "cancelling out" the loss between them.
            else:  # direction == -1
                # This loss cancellation effectively merges two trades, but counts as only ONE transaction overall.
                # The profit associated with cancelling the loss was already added when the surrounding
                # profitable segments were initially pushed. We just need to find the next best profit
                # within the merged interval defined by this loss segment.
                merged_profit, merged_trade_start, merged_trade_end = max_inc(
                    interval_start, interval_end, 1)
                if merged_profit > 0:
                    heapq.heappush(heap, (-merged_profit, interval_start,
                                   merged_trade_start, merged_trade_end, interval_end, 1))

        return total_max_profit
