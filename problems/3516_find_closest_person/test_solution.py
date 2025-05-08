import unittest
import time
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def _reference_solution(self, x: int, y: int, z: int) -> int:
        """A simple, verifiable implementation for comparison."""
        time1 = abs(z - x)
        time2 = abs(z - y)
        if time1 < time2:
            return 1
        elif time2 < time1:
            return 2
        else:
            return 0

    def test_provided_examples(self):
        """Category 1: Tests based on examples in the problem description."""
        # Example 2: x = 2, y = 5, z = 6 -> Output: 2
        x1, y1, z1 = 2, 5, 6
        expected1 = 2
        self.assertEqual(self.solution.solve(x1, y1, z1),
                         expected1, f"Failed on Example 2 ({x1},{y1},{z1})")
        self.assertEqual(self._reference_solution(
            x1, y1, z1), expected1, f"Reference failed on Example 2 ({x1},{y1},{z1})")

        # Example 3: x = 1, y = 5, z = 3 -> Output: 0
        x2, y2, z2 = 1, 5, 3
        expected2 = 0
        self.assertEqual(self.solution.solve(x2, y2, z2),
                         expected2, f"Failed on Example 3 ({x2},{y2},{z2})")
        self.assertEqual(self._reference_solution(
            x2, y2, z2), expected2, f"Reference failed on Example 3 ({x2},{y2},{z2})")

    def test_custom_small_edge_cases(self):
        """Category 2: Custom tests validating against the reference solution."""
        test_cases = [
            (10, 5, 1),    # Person 2 faster
            (3, 8, 1),     # Person 1 faster
            (5, 5, 10),    # Equal time (same start)
            (5, 10, 5),    # Person 1 at target
            (10, 5, 5),    # Person 2 at target
            (1, 1, 1),     # All at same spot
            (1, 2, 100),   # Max z, Person 2 faster
            (99, 100, 1),  # Min z, Person 1 faster
            (1, 100, 50),  # Boundaries, Person 1 faster
            (100, 1, 50),  # Boundaries, Person 2 faster
        ]

        for i, (x, y, z) in enumerate(test_cases):
            with self.subTest(i=i, x=x, y=y, z=z):
                expected = self._reference_solution(x, y, z)
                actual = self.solution.solve(x, y, z)
                self.assertEqual(actual, expected,
                                 f"Mismatch for input ({x}, {y}, {z})")

    def test_large_constraint_stress_test(self):
        """Category 3: Test with maximum constraints (performance check - though trivial for O(1))."""
        x_max, y_max, z_max = 100, 100, 100
        x_min, y_min, z_min = 1, 1, 1

        # Test Case 1: Max values
        start_time = time.time()
        result1 = self.solution.solve(x_max, y_max, z_max)
        end_time = time.time()
        print(
            f"Execution Time (Max Constraints {x_max, y_max, z_max}): {end_time - start_time:.6f} seconds")
        # Optional simple validation (result must be 0, 1, or 2)
        self.assertIn(result1, [0, 1, 2])

        # Test Case 2: Min/Max mix
        x, y, z = x_min, y_max, (x_min + y_max) // 2
        start_time = time.time()
        result2 = self.solution.solve(x, y, z)
        end_time = time.time()
        print(
            f"Execution Time (Min/Max Mix {x, y, z}): {end_time - start_time:.6f} seconds")
        self.assertIn(result2, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
