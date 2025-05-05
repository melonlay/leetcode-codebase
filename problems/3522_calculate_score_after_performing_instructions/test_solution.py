import unittest
import time
from typing import List

# Make sure solution is imported correctly. Adjust path if necessary.
from .solution import Solution


class TestCalculateScore(unittest.TestCase):
    """
    Unit tests for the calculateScore method.
    """

    def setUp(self):
        """Set up the test fixture."""
        self.solution = Solution()

    # --- Reference Implementation (Identical to main for simplicity here) ---
    def _reference_solution(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        current_index = 0
        score = 0
        visited = set()
        while True:
            if current_index < 0 or current_index >= n:
                break
            if current_index in visited:
                break
            visited.add(current_index)
            instruction = instructions[current_index]
            value = values[current_index]
            if instruction == "add":
                score += value
                current_index += 1
            elif instruction == "jump":
                current_index += value
        return score

    # --- Category 1: Provided Examples Verification ---
    def test_example_1(self):
        """Test Example 1 from LeetCode description."""
        instructions = ["jump", "add", "add", "jump", "add", "jump"]
        values = [2, 1, 3, 1, -2, -3]
        expected_output = 1
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected_output)
        self.assertEqual(self._reference_solution(
            instructions, values), expected_output)

    def test_example_2(self):
        """Test Example 2 from LeetCode description."""
        instructions = ["jump", "add", "add"]
        values = [3, 1, 1]
        expected_output = 0
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected_output)
        self.assertEqual(self._reference_solution(
            instructions, values), expected_output)

    def test_example_3(self):
        """Test Example 3 from LeetCode description."""
        instructions = ["jump"]
        values = [0]
        expected_output = 0
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected_output)
        self.assertEqual(self._reference_solution(
            instructions, values), expected_output)

    # --- Category 2: Custom Small/Edge Case Validation ---
    def test_empty(self):
        """Test with empty input (should not happen per constraints, but good check)."""
        instructions = []
        values = []
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 0

    def test_single_add(self):
        """Test single add instruction leading out of bounds."""
        instructions = ["add"]
        values = [5]
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 5

    def test_single_jump_out(self):
        """Test single jump instruction leading out of bounds."""
        instructions = ["jump"]
        values = [1]
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 0

    def test_single_jump_out_negative(self):
        """Test single jump instruction leading out of bounds (negative index)."""
        instructions = ["jump"]
        values = [-1]
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 0

    def test_simple_cycle(self):
        """Test a simple cycle: jump back to start."""
        instructions = ["add", "jump"]
        values = [10, -1]
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 10

    def test_longer_path_no_cycle(self):
        """Test a path that finishes without cycles."""
        instructions = ["add", "add", "jump", "add"]
        values = [1, 2, -1, 3]  # 0->1(s=1) -> 2(s=3) -> 1(visited)
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect 3

    def test_negative_score(self):
        """Test case resulting in a negative score."""
        instructions = ["add", "add", "add"]
        values = [-5, -2, 10]
        expected = self._reference_solution(instructions, values)
        self.assertEqual(self.solution.calculateScore(
            instructions, values), expected)  # Expect -7

    # --- Category 3: Large Constraint Stress Test (Performance) ---
    def test_large_input_no_cycle(self):
        """Test performance with large input, linear path (all adds)."""
        n = 10**5
        instructions = ["add"] * n
        values = [1] * n
        start_time = time.time()
        # We don't calculate expected for large cases, just check execution
        result = self.solution.calculateScore(instructions, values)
        end_time = time.time()
        print(
            f"\n[Perf Test] Large Input (n={n}, all adds): Time={end_time - start_time:.6f}s, Score={result}")
        self.assertIsInstance(result, int)  # Basic check

    def test_large_input_immediate_cycle(self):
        """Test performance with large input, immediate cycle."""
        n = 10**5
        instructions = ["jump"] + ["add"] * (n - 1)
        values = [0] + [1] * (n - 1)
        start_time = time.time()
        result = self.solution.calculateScore(instructions, values)
        end_time = time.time()
        print(
            f"[Perf Test] Large Input (n={n}, immediate cycle): Time={end_time - start_time:.6f}s, Score={result}")
        self.assertEqual(result, 0)  # Immediate cycle gives score 0


if __name__ == '__main__':
    unittest.main()
