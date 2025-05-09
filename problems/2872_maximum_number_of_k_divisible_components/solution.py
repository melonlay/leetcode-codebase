import collections
import sys

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        # Set recursion limit, especially important for larger N that might form deep trees (e.g., path graph)
        # Add a small buffer to N. Typical LeetCode environments might have higher defaults too.
        # Constraints: 1 <= n <= 3 * 10^4
        # Python's default is often 1000 or 3000. This needs to be higher.
        # Setting it to n + a small buffer like 500 should be safe for tree traversal up to depth N.
        # However, directly setting it this high might be platform dependent or disallowed in some environments.
        # For LeetCode, it's often better to rely on their environment's limits or use iterative DFS if recursion depth is an issue.
        # For now, including it as a conceptual step. If it causes issues on a platform, it can be removed/adjusted.
        # A more robust approach for extreme N would be iterative DFS.
        try:
            sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 500))
        except RecursionError: # Some environments might restrict this.
            pass # Continue if setting limit fails, rely on environment's default.

        if n == 0:
            return 0 # Based on constraints n >= 1, so not strictly needed.

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.components_count = 0
        
        # visited array is not strictly necessary for a tree if parent argument is used correctly in DFS.
        # It's more for general graph traversal to avoid cycles or reprocessing.

        def dfs(u: int, parent: int) -> int:
            """
            Performs DFS from node u.
            Returns the sum of values in the component rooted at u, after potential cuts in its subtrees.
            Updates self.components_count for each k-divisible component cut off.
            """
            current_sum_for_u_component = values[u]
            
            for v_neighbor in adj[u]:
                if v_neighbor == parent:
                    continue
                
                sum_from_child_component = dfs(v_neighbor, u)
                
                if sum_from_child_component % k == 0:
                    # This child's subtree forms a valid k-divisible component.
                    # Cut the edge (u, v_neighbor).
                    self.components_count += 1
                    # Its sum does not contribute to u's component sum.
                else:
                    # This child's component is not k-divisible on its own,
                    # so it must merge with u's component.
                    current_sum_for_u_component += sum_from_child_component
            
            return current_sum_for_u_component

        # Start DFS from node 0. The specific root choice doesn't matter for a tree.
        # The value returned by dfs(0, -1) is the sum of the component containing node 0
        # after all cuts. Due to the problem constraint (total sum of values % k == 0),
        # this root component will also be k-divisible.
        if n > 0: # dfs(0, -1) requires at least one node.
            dfs(0, -1) 
            # The total number of components is the number of cuts + 1 (for the root component).
            return self.components_count + 1
        else:
            return 0 # Should not be reached due to constraints n >= 1 