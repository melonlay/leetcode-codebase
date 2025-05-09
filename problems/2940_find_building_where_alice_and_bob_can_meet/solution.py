import math
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        num_q = len(queries)
        ans = [-1] * num_q

        if n == 0:
            return ans

        # pending_queries[i] stores list of (h_target, original_query_idx)
        # for queries whose Stage 2 search starts at index i (i.e., m >= i)
        pending_queries = defaultdict(list)

        for q_idx in range(num_q):
            qa, qb = queries[q_idx]

            if qa == qb:
                ans[q_idx] = qa
                continue

            # Stage 1: Check m0 = max(qa, qb)
            m0 = max(qa, qb)
            
            alice_can_reach_m0 = (qa == m0) or (qa < m0 and heights[qa] < heights[m0])
            bob_can_reach_m0 = (qb == m0) or (qb < m0 and heights[qb] < heights[m0])

            if alice_can_reach_m0 and bob_can_reach_m0:
                ans[q_idx] = m0
                continue

            # Stage 2 needed:
            h_target = max(heights[qa], heights[qb])
            # Search for m >= m0 + 1.
            # The sweep processes index `i`. Queries in `pending_queries[i]` are looking for m >= i.
            # So, queries are attached to `m0 + 1`.
            search_start_index = m0 + 1 

            if search_start_index < n:
                pending_queries[search_start_index].append((h_target, q_idx))
        
        # Monotonic stack: stores indices of buildings.
        # When sweeping i from right to left:
        # stack[-1] is the index i (most recent, smallest index on stack).
        # stack[0] is the largest index on stack.
        # Indices in stack are sorted descending: stk[0] > stk[1] > ... > stk[-1].
        # Heights corresponding to these indices are sorted strictly increasing:
        # heights[stk[0]] < heights[stk[1]] < ... < heights[stk[-1]].
        monotonic_stk = []

        for i in range(n - 1, -1, -1): # current building index, sweeping from right to left
            # Maintain monotonic stack property before adding current building i
            # This creates a stack wheremonotonic_stk[-1] is i, and heights are increasing towards stack[-1]
            while monotonic_stk and heights[monotonic_stk[-1]] <= heights[i]:
                monotonic_stk.pop()
            monotonic_stk.append(i)

            # Process queries whose search_start_index is i
            # These queries are looking for a meeting point m >= i
            if i in pending_queries:
                for h_target, q_idx in pending_queries[i]:
                    if ans[q_idx] != -1: # Already solved by Stage 1
                        continue

                    # Search in monotonic_stk for the rightmost index `k_stk` (smallest actual building index)
                    # such that heights[monotonic_stk[k_stk]] > h_target.
                    # The stack has indices s_L > s_{L-1} > ... > s_0 (s_0 = i, stack[-1])
                    # And heights h(s_L) < h(s_{L-1}) < ... < h(s_0). (heights increasing towards stack top)
                    
                    low = 0
                    high = len(monotonic_stk) - 1
                    found_m = -1
                    
                    # Binary search on the monotonic_stk.
                    # Stack elements: monotonic_stk[0] (largest index, smallest height in stack)
                    #                 monotonic_stk[-1] (smallest index (i), largest height in stack)
                    while low <= high:
                        mid_stk_pos = (low + high) // 2
                        actual_building_idx = monotonic_stk[mid_stk_pos] 
                        
                        if heights[actual_building_idx] > h_target:
                            found_m = actual_building_idx # This building works
                            # We want the smallest building index (which is towards stack top / right of array).
                            # So if monotonic_stk[mid] works, try to find something to its right on stack (larger mid_stk_pos)
                            low = mid_stk_pos + 1 
                        else:
                            # This building monotonic_stk[mid_stk_pos] is not tall enough.
                            # Need taller buildings. Taller buildings are further up the stack (smaller mid_stk_pos / towards stack top).
                            high = mid_stk_pos - 1
                    
                    if found_m != -1:
                        ans[q_idx] = found_m
        return ans 