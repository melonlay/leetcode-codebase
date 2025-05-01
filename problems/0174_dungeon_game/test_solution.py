import unittest
import math
from .solution import Solution


class TestDungeonGame(unittest.TestCase):

    def setUp(self):
        """Set up the Solution object for each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example provided by LeetCode."""
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 7)

    def test_example_2(self):
        """Test the second example provided by LeetCode (1x1 grid)."""
        dungeon = [[0]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 1)

    def test_single_cell_negative(self):
        """Test a 1x1 grid with a negative value."""
        dungeon = [[-10]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 11)

    def test_single_cell_positive(self):
        """Test a 1x1 grid with a positive value."""
        dungeon = [[10]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 1)

    def test_all_positive(self):
        """Test a grid where all cells provide health."""
        dungeon = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 1)

    def test_all_negative(self):
        """Test a grid where all cells cause damage."""
        dungeon = [[-1, -1], [-1, -1]]
        # Expected: dp[1][1]=2, dp[0][1]=3, dp[1][0]=3, dp[0][0]=max(1, min(3,3)-(-1))=4
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 4)

    def test_path_choice_matters(self):
        """Test a case where the seemingly better immediate move is worse overall."""
        dungeon = [[-2, 10], [-100, -10]]
        # Path R->D: Need 3 at (0,0) -> 1 at (0,1) -> 11 at (1,1). Initial = 3.
        # Path D->R: Need 103 at (0,0) -> 1 at (1,0) -> 11 at (1,1). Initial = 103.
        # DP: dp[1][1]=11, dp[0][1]=max(1,11-10)=1, dp[1][0]=max(1,11-(-100))=112
        # dp[0][0]=max(1, min(112, 1) - (-2)) = max(1, 1 + 2) = 3
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 3)

    def test_need_high_health_early(self):
        """Test a case where a large negative value early forces high initial health."""
        dungeon = [[-10, 1], [1, -5]]
        # DP: dp[1][1]=6, dp[0][1]=max(1,6-1)=5, dp[1][0]=max(1,6-1)=5
        # dp[0][0]=max(1, min(5, 5) - (-10)) = max(1, 5 + 10) = 15
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 15)

    def test_long_row(self):
        """Test a single row dungeon."""
        dungeon = [[10, -20, 30, -5]]
        # DP: dp[0][3]=6, dp[0][2]=max(1,6-30)=1, dp[0][1]=max(1,1-(-20))=21, dp[0][0]=max(1,21-10)=11
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 11)

    def test_long_column(self):
        """Test a single column dungeon."""
        dungeon = [[10], [-20], [30], [-5]]
        # DP: dp[3][0]=6, dp[2][0]=max(1,6-30)=1, dp[1][0]=max(1,1-(-20))=21, dp[0][0]=max(1,21-10)=11
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 11)

    # @unittest.skip("Stress test potentially slow, enable if needed.")
    def test_stress_large_grid(self):
        """Test a larger grid to check performance and potential edge cases under load."""
        # Create a 50x50 grid with alternating -1 and 1
        size = 50
        dungeon = [[(-1 if (i + j) % 2 == 0 else 1)
                    for j in range(size)] for i in range(size)]
        dungeon[size-1][size-1] = -5  # Ensure last cell requires > 1 health
        # Expected value needs calculation, but the DP should handle it.
        # For a checkerboard pattern ending in -5, the requirement propagates
        # requiring alternating 1 and 2 health, roughly.
        # Let's trace the end:
        # dp[49][49] = max(1, 1 - (-5)) = 6
        # dp[48][49] (val=1): max(1, 6 - 1) = 5
        # dp[49][48] (val=1): max(1, 6 - 1) = 5
        # dp[48][48] (val=-1): max(1, min(5,5) - (-1)) = max(1, 6) = 6
        # dp[47][48] (val=1): max(1, 6 - 1) = 5
        # dp[48][47] (val=1): max(1, 6 - 1) = 5
        # dp[47][47] (val=-1): max(1, min(5,5) - (-1)) = 6
        # It seems the answer should be 6 for this pattern.
        # Let's double check the top left corner (0,0), val=-1
        # Assume dp[1][0]=5, dp[0][1]=5
        # dp[0][0] = max(1, min(5,5) - (-1)) = 6
        self.assertEqual(self.solution.calculateMinimumHP(dungeon), 6)


if __name__ == '__main__':
    unittest.main()
