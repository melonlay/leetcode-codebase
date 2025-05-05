import sys
from typing import List, Tuple

# Increase recursion depth for potentially deep segment trees
# sys.setrecursionlimit(2000) # Might be needed locally if n is large


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Node structure: (product_mod_k, counts_tuple_size_k)
        # counts[rem] = number of prefixes starting at node.start
        #               ending in node.range with product = rem % k
        # Use tuples for potential micro-optimization since k is small
        initial_counts = (0,) * k
        tree_nodes = [(0, initial_counts) for _ in range(4 * n)]

        # Combine results from left and right children
        def combine(left_res: Tuple[int, Tuple[int]], right_res: Tuple[int, Tuple[int]]) -> Tuple[int, Tuple[int]]:
            if left_res is None:
                return right_res
            if right_res is None:
                return left_res

            prod_l, counts_l = left_res
            prod_r, counts_r = right_res

            new_prod = (prod_l * prod_r) % k
            # Convert tuple to list for modification, then back to tuple
            new_counts_list = list(counts_l)

            # Combine counts from the right child, transformed by left product
            for r_rem in range(k):
                if counts_r[r_rem] > 0:
                    final_rem = (prod_l * r_rem) % k
                    new_counts_list[final_rem] += counts_r[r_rem]

            return new_prod, tuple(new_counts_list)

        # Build the segment tree
        def build(v: int, tl: int, tr: int):
            if tl == tr:
                val_mod_k = nums[tl] % k
                counts_list = [0] * k
                counts_list[val_mod_k] = 1
                tree_nodes[v] = (val_mod_k, tuple(counts_list))
            else:
                tm = (tl + tr) // 2
                build(2 * v, tl, tm)
                build(2 * v + 1, tm + 1, tr)
                tree_nodes[v] = combine(
                    tree_nodes[2 * v], tree_nodes[2 * v + 1])

        # Update a value at a specific position
        def update(v: int, tl: int, tr: int, pos: int, new_val: int):
            if tl == tr:
                val_mod_k = new_val % k
                counts_list = [0] * k
                counts_list[val_mod_k] = 1
                tree_nodes[v] = (val_mod_k, tuple(counts_list))
            else:
                tm = (tl + tr) // 2
                if pos <= tm:
                    update(2 * v, tl, tm, pos, new_val)
                else:
                    update(2 * v + 1, tm + 1, tr, pos, new_val)
                tree_nodes[v] = combine(
                    tree_nodes[2 * v], tree_nodes[2 * v + 1])

        # Query the combined result for a range [ql, qr]
        def query(v: int, tl: int, tr: int, ql: int, qr: int) -> Tuple[int, Tuple[int]]:
            # Check for complete non-overlap first to handle edge cases returning None
            if ql > tr or qr < tl:
                return None

            if ql <= tl and tr <= qr:  # Node fully contained in query range
                return tree_nodes[v]

            tm = (tl + tr) // 2
            left_res = query(2 * v, tl, tm, ql, qr)
            right_res = query(2 * v + 1, tm + 1, tr, ql, qr)

            # Combine results from children
            return combine(left_res, right_res)

        # --- Main Logic ---
        if k == 0:  # Avoid modulo by zero, though constraints say k>=1
            return [0] * len(queries)

        # Handle k=1 separately for potential speedup?
        # If k=1, product % k is always 0. counts[0] is just the length.
        # Might add complexity, let's stick to the general k case for now.
        # if k == 1:
        #     # Simplified logic for k=1 if needed
        #     pass

        build(1, 0, n - 1)

        results = []
        for index, value, start, x_target in queries:
            update(1, 0, n - 1, index, value)

            if start >= n:
                results.append(0)
                continue

            query_result = query(1, 0, n - 1, start, n - 1)

            if query_result is None:
                results.append(0)
            else:
                _, counts = query_result
                # Ensure x_target is within bounds for tuple indexing
                if 0 <= x_target < k:
                    results.append(counts[x_target])
                else:  # Should not happen based on constraints, but safe check
                    results.append(0)

        return results
