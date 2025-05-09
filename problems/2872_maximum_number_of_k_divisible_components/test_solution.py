import unittest
import sys
import os
import collections # Added for reference_solution

# Add the directory of this test file (which contains solution.py) to the Python path
# This allows 'from solution import Solution' to work directly.
# __file__ refers to '.../problems/2872_maximum_number_of_k_divisible_components/test_solution.py'
# os.path.dirname(os.path.abspath(__file__)) gives '.../problems/2872_maximum_number_of_k_divisible_components'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import Solution

# Optional: If you want to clean up sys.path after the import.
# However, for test modules, it's often left as is.
# if sys.path[0] == os.path.dirname(os.path.abspath(__file__)):
#     sys.path.pop(0)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.components_count_ref = 0 # For reference solution state

    def _dfs_reference(self, u: int, parent: int, adj: dict, values: list[int], k: int) -> int:
        current_sum_for_u_component = values[u]
        for v_neighbor in adj[u]:
            if v_neighbor == parent:
                continue
            sum_from_child_component = self._dfs_reference(v_neighbor, u, adj, values, k)
            if sum_from_child_component % k == 0:
                self.components_count_ref += 1
            else:
                current_sum_for_u_component += sum_from_child_component
        return current_sum_for_u_component

    def reference_solution(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        if n == 0:
            return 0

        adj = collections.defaultdict(list)
        for u_node, v_node in edges:
            adj[u_node].append(v_node)
            adj[v_node].append(u_node)

        self.components_count_ref = 0 # Reset for each call
        
        # Local sys.setrecursionlimit for reference if needed, though main solution handles it.
        # original_recursion_limit = sys.getrecursionlimit()
        # try:
        #     sys.setrecursionlimit(max(original_recursion_limit, n + 500))
        # except RecursionError:
        #     pass

        if n > 0:
            self._dfs_reference(0, -1, adj, values, k)
            # try:
            #     sys.setrecursionlimit(original_recursion_limit)
            # except RecursionError:
            #    pass
            return self.components_count_ref + 1
        else:
            # try:
            #    sys.setrecursionlimit(original_recursion_limit)
            # except RecursionError:
            #    pass
            return 0

    def test_example1(self):
        n = 5
        edges = [[0,2],[1,2],[1,3],[2,4]]
        values = [1,8,1,4,4]
        k = 6
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 2)
        self.assertEqual(self.reference_solution(n, edges, values, k), 2) # Verify reference too

    def test_example2(self):
        n = 7
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        values = [3,0,6,1,5,2,1]
        k = 3
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 3)
        self.assertEqual(self.reference_solution(n, edges, values, k), 3) # Verify reference too

    # Category 2: Custom Edge Cases (verified by reference_solution)
    def test_single_node(self):
        n = 1
        edges = []
        values = [6]
        k = 3
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

        n = 1
        edges = []
        values = [3]
        k = 3
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

    def test_k_is_one(self):
        n = 3
        edges = [[0,1],[1,2]]
        values = [10,20,30] # Sum = 60, div by k=1
        k = 1
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

    def test_all_values_zero(self):
        n = 3
        edges = [[0,1],[1,2]]
        values = [0,0,0] # Sum = 0, div by k=5
        k = 5
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

    def test_no_cuts_possible_forms_one_component(self):
        n = 3
        edges = [[0,1],[1,2]]
        values = [1,1,1] # Sum = 3
        k = 3
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

    def test_linear_tree_some_cuts(self):
        n = 4
        edges = [[0,1],[1,2],[2,3]]
        values = [2,2,2,6] # Sum = 12
        k = 4
        expected = self.reference_solution(n, edges, values, k)
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), expected)

    # Category 3: Performance Stress Tests
    # These would typically not have assertions for correctness unless a reference is available
    # or focus on just execution time. For now, placeholders.
    # def test_large_n_path_graph(self):
    #     n = 30000
    #     edges = [[i, i+1] for i in range(n-1)]
    #     values = [1] * n 
    #     k = 1 # Expect n components
    #     # This test might be too slow to run in typical unit test suites locally
    #     # self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), n)
    #     pass

if __name__ == '__main__':
    unittest.main() 