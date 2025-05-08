import unittest
import time
import collections
from .solution import Solution # Assuming solution.py is in the same directory

class TestShortestPathInWeightedTree(unittest.TestCase):

    def _reference_solution(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        current_edge_weights = {}
        # Initial population of edge weights (0-indexed nodes)
        for u, v, w in edges:
            u0, v0 = u - 1, v - 1
            current_edge_weights[tuple(sorted((u0, v0)))] = w

        results = []

        for query in queries:
            if query[0] == 1: # Update query
                _, u_q, v_q, new_w = query
                u0, v0 = u_q - 1, v_q - 1
                current_edge_weights[tuple(sorted((u0, v0)))] = new_w
            else: # Path query
                _, x_q = query
                target_node_0_idx = x_q - 1
                
                if n == 0:
                    # Should not happen based on constraints, but for safety
                    results.append(-1) # Or raise error, depends on expected behavior for impossible query
                    continue
                if target_node_0_idx < 0 or target_node_0_idx >= n:
                    results.append(-1) # Invalid target
                    continue

                if target_node_0_idx == 0: # Distance from root (node 0) to itself is 0
                    results.append(0)
                    continue

                # Build adjacency list for current BFS
                adj_bfs = [[] for _ in range(n)]
                for (n1, n2), weight in current_edge_weights.items():
                    adj_bfs[n1].append((n2, weight))
                    adj_bfs[n2].append((n1, weight))
                
                q_bfs = collections.deque([(0, 0)]) # (node_0_idx, distance)
                visited_bfs = {0}
                dist_found = -1 # Should find a path in a tree

                path_found_for_target = False
                while q_bfs:
                    curr, d = q_bfs.popleft()
                    if curr == target_node_0_idx:
                        dist_found = d
                        path_found_for_target = True
                        break
                    
                    for neighbor, weight in adj_bfs[curr]:
                        if neighbor not in visited_bfs:
                            visited_bfs.add(neighbor)
                            q_bfs.append((neighbor, d + weight))
                
                results.append(dist_found if path_found_for_target else -1) # -1 if not reachable (not for tree)
        return results

    # Category 1: Provided Examples Verification
    def test_example_1(self):
        n = 2
        edges = [[1,2,7]]
        queries = [[2,2], [1,1,2,4], [2,2]]
        expected_output = [7,4]
        sol = Solution()
        self.assertEqual(sol.treeQueries(n, edges, queries), expected_output)
        self.assertEqual(self._reference_solution(n, edges, queries), expected_output)

    def test_example_2(self):
        n = 3
        edges = [[1,2,2],[1,3,4]]
        queries = [[2,1],[2,3],[1,1,3,7],[2,2],[2,3]]
        expected_output = [0,4,2,7]
        sol = Solution()
        self.assertEqual(sol.treeQueries(n, edges, queries), expected_output)
        self.assertEqual(self._reference_solution(n, edges, queries), expected_output)

    def test_example_3(self):
        n = 4
        edges = [[1,2,2],[2,3,1],[3,4,5]]
        queries = [[2,4],[2,3],[1,2,3,3],[2,2],[2,3]]
        expected_output = [8,3,2,5]
        sol = Solution()
        self.assertEqual(sol.treeQueries(n, edges, queries), expected_output)
        self.assertEqual(self._reference_solution(n, edges, queries), expected_output)

    # Category 2: Custom Small/Edge Case Validation
    def test_single_node(self):
        n = 1
        edges = []
        queries = [[2,1], [2,1]]
        sol = Solution()
        expected = self._reference_solution(n, edges, queries)
        self.assertEqual(sol.treeQueries(n, edges, queries), expected)
        self.assertEqual(expected, [0,0]) # Manual check for reference behavior

    def test_linear_tree_updates(self):
        n = 3
        edges = [[1,2,10], [2,3,20]]
        queries = [
            [2,3],      # 10 + 20 = 30
            [1,1,2,5],  # edge (1,2) to 5
            [2,3],      # 5 + 20 = 25
            [1,2,3,15], # edge (2,3) to 15
            [2,3],      # 5 + 15 = 20
            [2,2]       # 5
        ]
        sol = Solution()
        expected = self._reference_solution(n, edges, queries)
        self.assertEqual(sol.treeQueries(n, edges, queries), expected)
        # Manually derived expected values for self-check: [30, 25, 20, 5]
        self.assertEqual(expected, [30, 25, 20, 5])

    def test_star_graph(self):
        n = 4
        edges = [[1,2,1], [1,3,2], [1,4,3]]
        queries = [
            [2,2], # 1
            [2,3], # 2
            [2,4], # 3
            [1,1,3,10], # edge (1,3) to 10
            [2,3], # 10
            [2,1]  # 0
        ]
        sol = Solution()
        expected = self._reference_solution(n, edges, queries)
        self.assertEqual(sol.treeQueries(n, edges, queries), expected)
        self.assertEqual(expected, [1,2,3,10,0])

    # Category 3: Large Constraint Stress Test (Performance)
    def test_large_linear_tree(self):
        n = 10**5
        edges = [[i, i + 1, 1] for i in range(1, n)]
        queries = []
        # Mix of updates and queries
        for i in range(1, min(n, 10**3) + 1):
            queries.append([2, i]) # Query path to node i
            if i < n -1 :
                 queries.append([1, i, i+1, 2]) # Update edge (i, i+1)
                 queries.append([2,i+1])

        # Add some queries for distant nodes
        if n > 10:
            for i in range(n - 10, n + 1):
                 queries.append([2,i])
        
        if not queries and n==1: # if n=1, edges is empty, loop above won't run
             queries.append([2,1])
        elif not queries and n > 1:
            queries.append([2,n]) # ensure at least one query for larger n if loops are too small

        sol = Solution()
        start_time = time.time()
        result = sol.treeQueries(n, edges, queries)
        end_time = time.time()
        print(f"Large Linear Tree ({n} nodes, {len(queries)} queries) Execution Time: {end_time - start_time:.6f} seconds")
        # Basic validation: check if result length matches number of type 2 queries
        num_type2_queries = sum(1 for q in queries if q[0] == 2)
        self.assertEqual(len(result), num_type2_queries)
        # Check for non-negative distances if applicable (all weights are positive)
        for dist in result:
            self.assertTrue(dist >= 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 