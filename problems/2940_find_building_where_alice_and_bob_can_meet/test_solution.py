import unittest
import time
import random

from .solution import Solution

class TestSolution(unittest.TestCase):

    def solve_reference(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        ans = [-1] * len(queries)
        for i, query_pair in enumerate(queries):
            qa, qb = query_pair[0], query_pair[1]
            if qa == qb:
                ans[i] = qa
                continue
            
            found_m_for_query = -1
            # Iterate m from max(qa, qb) up to n-1
            for m_idx in range(max(qa, qb), n):
                alice_can_reach_m = (qa == m_idx) or \
                                  (qa < m_idx and heights[qa] < heights[m_idx])
                bob_can_reach_m = (qb == m_idx) or \
                                (qb < m_idx and heights[qb] < heights[m_idx])
                
                if alice_can_reach_m and bob_can_reach_m:
                    found_m_for_query = m_idx
                    break 
            ans[i] = found_m_for_query
        return ans

    # Category 1: Problem Examples
    def test_problem_examples(self):
        sol = Solution()
        # Example 1
        heights1 = [6,4,8,5,2,7,1]
        queries1 = [[0,1],[0,3],[2,4],[3,4],[2,2]]
        expected1 = [2,5,-1,5,2]
        self.assertEqual(sol.leftmostBuildingQueries(heights1, queries1), expected1, "Failed Example 1")
        self.assertEqual(self.solve_reference(heights1, queries1), expected1, "Failed Example 1 (Reference)")
        
        # Example 2
        heights2 = [5,3,8,2,6,1,4,6]
        queries2 = [[0,7],[3,5],[5,2],[3,0],[1,6]]
        expected2 = [7,6,-1,4,6]
        self.assertEqual(sol.leftmostBuildingQueries(heights2, queries2), expected2, "Failed Example 2")
        self.assertEqual(self.solve_reference(heights2, queries2), expected2, "Failed Example 2 (Reference)")

    # Category 2: Custom Edge Cases
    def test_custom_edge_cases(self):
        sol = Solution()
        # N_MAX_FOR_REFERENCE can be set based on typical local execution limits for O(N*Q)
        # For N, Q up to 100, N*Q = 10^4, feasible.
        # For N, Q up to 500, N*Q = 2.5*10^5, also feasible.

        test_cases = [
            ("n=1", [10], [[0,0]]), 
            ("All heights same", [5,5,5,5], [[0,1],[0,3],[1,2]]), 
            ("Strictly increasing", [1,2,3,4,5], [[0,1],[0,2],[2,4]]), 
            ("Strictly decreasing", [5,4,3,2,1], [[0,1],[0,2],[2,4]]), 
            ("Query a=b", [1,5,2,6], [[1,1]]), 
            ("No solution complex", [10,1,2,12,3], [[0,1]]), # (0,1) -> h0=10,h1=1. m0=1 no. m>1: th=10. h[3]=12. ans=3
            ("No solution simple", [10,1,2], [[0,1]]), # ans=-1
            ("max(a,b) is solution", [1,10,2,3], [[0,1]]), # qa=0,qb=1. m0=1. h0=1<h1=10. ans=1
            ("Solution > max(a,b)", [1,2,10,3,12], [[0,1]]), # qa=0,qb=1. m0=1(h1=2) no. m>1: th=max(1,2)=2. h[2]=10>2. ans=2
            ("Empty heights and queries", [], []), # Should handle gracefully
            ("Empty queries", [1,2,3], []),
            ("a or b at ends", [1,2,3,4,5], [[0,4],[4,0],[2,2],[0,0],[4,4]])
        ]

        for name, heights, queries in test_cases:
            if not heights and not queries: # Handle empty case separately if needed by main sol
                expected = []
            elif not queries: # Empty queries, empty result
                expected = [] 
            else:
                 expected = self.solve_reference(heights, queries)
            
            # print(f"Test: {name}, Heights: {heights}, Queries: {queries}, Expected: {expected}")
            actual = sol.leftmostBuildingQueries(heights, queries)
            # print(f"Actual: {actual}")
            self.assertEqual(actual, expected, f"Failed custom case: {name}")

    # Category 3: Performance Stress Tests
    def test_performance(self):
        sol = Solution()
        N = 1000 # Reduced for quicker local test, problem max is 5*10^4
        Q = 1000 # Reduced for quicker local test, problem max is 5*10^4
        
        heights = [random.randint(1, 10**9) for _ in range(N)]
        queries = []
        for _ in range(Q):
            a = random.randint(0, N-1)
            b = random.randint(0, N-1)
            queries.append([a,b])

        start_time = time.time()
        _ = sol.leftmostBuildingQueries(heights, queries)
        end_time = time.time()
        duration = end_time - start_time
        # print(f"Performance test (N={N}, Q={Q}) took {duration:.4f} seconds.")
        self.assertTrue(duration < 5.0, f"Performance test took too long: {duration:.4f}s (Limit 5s for N,Q={N})") 
        # For full constraints (5e4), a typical limit might be 2-5 seconds on judge systems

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 