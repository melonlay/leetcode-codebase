from typing import List, Dict, Set
import sys

# Note: @lru_cache is not used here as the state includes mutable sets.
# Manual memoization using a dictionary is required.

# Increase recursion depth limit needed for deep searches
try:
    # Adjust based on N (max depth is N)
    sys.setrecursionlimit(2500)
except Exception:
    pass  # Might fail in restricted environments


class Solution:
    """Solves LeetCode 3530 using optimized Recursive DP with Future Score Memoization.
       State includes partitioned available node sets and visited mask.
    """

    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        """Calculates the maximum profit using optimized recursive DP.
        """
        # Handle edge case: No edges means nodes can be processed in any order.
        # Optimal strategy is to assign highest scores to highest positions.
        if not edges:
            scores_sorted = sorted(score)
            return sum(s * i for i, s in enumerate(scores_sorted, start=1))

        # --- Graph Representation ---
        is_root = {i: True for i in range(n)}
        children: Dict[int, List[int]] = {i: [] for i in range(n)}
        parents: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            is_root[v] = False
            children[u].append(v)
            parents[v].append(u)

        # --- Initial Available Node Sets ---
        childless_roots: Set[int] = set()
        roots_with_child: Set[int] = set()
        for i in range(n):
            if is_root[i]:
                if not children[i]:  # Check if list is empty
                    childless_roots.add(i)
                else:
                    roots_with_child.add(i)

        # --- Memoization Table ---
        # FUTURE_SCORE[visited_mask] stores the max *additional* profit
        # achievable after the nodes in visited_mask have been placed.
        FUTURE_SCORE: Dict[int, int] = {}

        # --- Recursive Function ---
        def get_best_score(current_profit_so_far: int,
                           next_pos: int,
                           options_with_child: Set[int],
                           childless_options: Set[int],
                           visited_mask: int) -> int:

            # --- Memoization Check ---
            if visited_mask in FUTURE_SCORE:
                # Return current path profit + optimal future profit
                return current_profit_so_far + FUTURE_SCORE[visited_mask]

            # --- Base Case (Implicit): No more options available ---
            # If both sets are empty, the loops below won't run.
            # max_total_score will remain current_profit_so_far.

            # Best total score found from this state
            max_total_score = current_profit_so_far
            is_leaf_path = True  # Assume this is the end unless loops run

            # --- Heuristic: Try placing the MIN score childless node ---
            temp_score_after_childless = -1  # Sentinel value
            if childless_options:
                is_leaf_path = False
                # Find the node with the minimum score among childless options
                min_score_node = -1
                min_s = float('inf')
                for node in childless_options:
                    if score[node] < min_s:
                        min_s = score[node]
                        min_score_node = node

                # Simulate placing this node
                childless_options.remove(min_score_node)
                temp_score_after_childless = get_best_score(
                    current_profit_so_far + next_pos * score[min_score_node],
                    next_pos + 1,
                    options_with_child,  # This set remains the same
                    childless_options,
                    visited_mask | (1 << min_score_node)
                )
                # Backtrack the set modification
                childless_options.add(min_score_node)
                max_total_score = max(
                    max_total_score, temp_score_after_childless)

            # --- Explore placing nodes WITH children ---
            # Iterate over a copy of the set as we modify it
            options_to_try = list(options_with_child)
            if options_to_try:
                is_leaf_path = False

            for node_with_child in options_to_try:
                options_with_child.remove(node_with_child)
                new_visited_mask = visited_mask | (1 << node_with_child)

                # Determine newly available children and modify sets for recursive call
                added_childless: Set[int] = set()
                added_with_child: Set[int] = set()

                for child in children[node_with_child]:
                    # Check if all parents of child are now visited
                    all_parents_visited = True
                    for p in parents[child]:
                        if not ((new_visited_mask >> p) & 1):
                            all_parents_visited = False
                            break

                    if all_parents_visited:
                        if not children[child]:  # Child has no children
                            if child not in childless_options:  # Avoid adding if already there
                                childless_options.add(child)
                                added_childless.add(child)
                        else:  # Child has children
                            if child not in options_with_child:  # Avoid adding if already there
                                options_with_child.add(child)
                                added_with_child.add(child)

                # Recursive call
                score_after_this_node = get_best_score(
                    current_profit_so_far + next_pos * score[node_with_child],
                    next_pos + 1,
                    options_with_child,
                    childless_options,
                    new_visited_mask
                )
                max_total_score = max(max_total_score, score_after_this_node)

                # Backtrack set modifications
                for c in added_childless:
                    childless_options.remove(c)
                for c in added_with_child:
                    options_with_child.remove(c)
                options_with_child.add(node_with_child)  # Add the parent back

            # --- Memoization Update ---
            # Store the calculated maximum *additional* profit from this state
            # Handle the case where this path might be a leaf (no further nodes)
            future_profit = max_total_score - current_profit_so_far
            if is_leaf_path and not childless_options and not options_with_child:
                future_profit = 0  # Base case for profit calculation

            FUTURE_SCORE[visited_mask] = future_profit
            return current_profit_so_far + future_profit  # Return total score for this path

        # --- Initial Call ---
        result = get_best_score(0, 1, roots_with_child, childless_roots, 0)
        return result
