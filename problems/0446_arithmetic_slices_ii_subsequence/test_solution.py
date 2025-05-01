import unittest
from .solution import Solution


class TestArithmeticSlicesII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 4, 6, 8, 10]
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 7, "Example 1 Failed")

    def test_example_2(self):
        nums = [7, 7, 7, 7, 7]
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 16, "Example 2 Failed")

    def test_short_input(self):
        nums = [1, 2]
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 0, "Short input failed")
        nums = [1]
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 0, "Single element input failed")
        nums = []
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 0, "Empty input failed")

    def test_no_arithmetic_slice(self):
        nums = [1, 2, 4, 7, 11]
        # The sequence [1, 4, 7] is arithmetic with diff=3
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 1, "Arithmetic slice [1, 4, 7] found, expected 1")

    def test_negative_numbers(self):
        nums = [3, -1, -5, -9]
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 3, "Negative numbers failed")  # [3,-1,-5], [-1,-5,-9], [3,-1,-5,-9]

    def test_mixed_numbers(self):
        nums = [0, 2, 4, 3, 6, 8]
        # Possible: [0,2,4], [0,3,6], [2,4,6], [4,6,8], [0,4,8], [2,4,6,8]
        # Note: [0,2,4,6], [0,2,4,8] invalid. [3,6] len 2. [2,3] diff 1, [4,6] diff 2
        # DP Trace:
        # i=0: dp[0] = {}
        # i=1: j=0, d=2. dp[1]={2:1}. res=0
        # i=2: j=0, d=4. dp[2]={4:1}. j=1, d=2. c=dp[1][2]=1. res+=1. dp[2]={4:1, 2: dp[2][2]+1+1=2}. res=1
        # i=3: j=0, d=3. dp[3]={3:1}. j=1, d=1. dp[3]={3:1, 1:1}. j=2, d=-1. dp[3]={3:1, 1:1, -1:1}. res=1
        # i=4: j=0, d=6. dp[4]={6:1}. j=1, d=4. c=dp[1][4]=0. dp[4]={6:1, 4:1}. j=2, d=2. c=dp[2][2]=2. res+=2. dp[4]={6:1, 4:1, 2: dp[4][2]+2+1=3}. j=3, d=3. c=dp[3][3]=1. res+=1. dp[4]={6:1, 4:1, 2:3, 3: dp[4][3]+1+1=2}. res=1+2+1=4
        # i=5: j=0, d=8. dp[5]={8:1}. j=1, d=6. c=dp[1][6]=0. dp[5]={8:1, 6:1}. j=2, d=4. c=dp[2][4]=1. res+=1. dp[5]={8:1, 6:1, 4: dp[5][4]+1+1=2}. j=3, d=5. dp[5]={8:1, 6:1, 4:2, 5:1}. j=4, d=2. c=dp[4][2]=3. res+=3. dp[5]={8:1, 6:1, 4:2, 5:1, 2: dp[5][2]+3+1=4}. res=4+1+3=8
        # Seems my manual calculation is missing some? Ah [0,4,8] (d=4), [2,4,6,8] (d=2) count=3 + 1=4, [0,3,6] (d=3)
        # Let's recheck example 1 explanation: [2,4,6], [4,6,8], [6,8,10], [2,4,6,8], [4,6,8,10], [2,4,6,8,10], [2,6,10]
        # The code output 7 for Ex1. It seems correct.
        # Let's recheck calculation for [0, 2, 4, 3, 6, 8]
        # i=0: dp[0]={} res=0
        # i=1(2): j=0(0), d=2. dp[1]={2:1}. res=0
        # i=2(4): j=0(0), d=4. dp[2]={4:1}. j=1(2), d=2. c=dp[1][2]=1. res+=1. dp[2]={4:1, 2:2}. res=1 -> [0,2,4]
        # i=3(3): j=0(0), d=3. dp[3]={3:1}. j=1(2), d=1. dp[3]={3:1, 1:1}. j=2(4), d=-1. dp[3]={3:1, 1:1, -1:1}. res=1
        # i=4(6): j=0(0), d=6. dp[4]={6:1}. j=1(2), d=4. c=dp[1][4]=0. dp[4]={6:1, 4:1}. j=2(4), d=2. c=dp[2][2]=2. res+=2. dp[4]={6:1, 4:1, 2:3}. j=3(3), d=3. c=dp[3][3]=1. res+=1. dp[4]={6:1, 4:1, 2:3, 3:2}. res=1+2+1=4 -> [2,4,6], [0,2,4,6], [0,3,6]
        # i=5(8): j=0(0), d=8. dp[5]={8:1}. j=1(2), d=6. c=dp[1][6]=0. dp[5]={8:1, 6:1}. j=2(4), d=4. c=dp[2][4]=1. res+=1. dp[5]={8:1, 6:1, 4:2}. j=3(3), d=5. dp[5]={8:1, 6:1, 4:2, 5:1}. j=4(6), d=2. c=dp[4][2]=3. res+=3. dp[5]={8:1, 6:1, 4:2, 5:1, 2:4}. res=4+1+3=8 -> [0,4,8], [4,6,8], [2,4,6,8], [0,2,4,6,8]
        # Seems the count is 8? Let's list them: [0,2,4], [0,3,6], [2,4,6], [4,6,8], [0,4,8], [2,4,6,8], [0,2,4,6,8], [?]
        # What did I miss? The explanation above looks incomplete.
        # [0,2,4], [2,4,6], [4,6,8] -> d=2. Count = 3
        # [0,3,6] -> d=3. Count = 1
        # [0,4,8] -> d=4. Count = 1
        # Length 4: [2,4,6,8] (d=2), [0,2,4,6] (d=2) - invalid, only [2,4,6,8]
        # Oh, [0,2,4] contributes to [0,2,4,6] which is invalid seq. [2,4,6] contributes to [2,4,6,8].
        # My code logic adds 'count_j_diff' to total. This is correct. It counts sequences of length >= 3.
        # Let's relist based on the code's logic:
        # i=2, j=1, d=2: count_j_diff=dp[1][2]=1. Add 1 to res. (Adds [0,2,4]). res=1
        # i=4, j=2, d=2: count_j_diff=dp[2][2]=2. Add 2 to res. (Adds [0,2,4] extended to [0,2,4,6] - invalid, and [?, ?, 6]? No. Adds [2,4,6] based on [?,2,4] and [2,4] pair. Also adds [0,2,4,6]? No, it adds the count of length >=3 seqs ending at j=2,d=2. So adds [0,2,4] extended = [0,2,4,6] - invalid? NO, the count is just added to the total. It means we found 2 sequences of len>=3 ending at index 4 with diff 2. These are [2,4,6] and [0,2,4,6]?? No, it's just counting. The sequences added are [2,4,6] (from [2,4]) and [0,2,4,6]? No, wait. dp[j][diff] is count of sequences >=2 ending at j. total_count += dp[j][diff] means we are counting sequences of length >= 3.
        # i=4, j=2, d=2: dp[2][2]=2 represents ([0,2,4] and [2,4]). Adding nums[i]=6 forms [0,2,4,6] and [2,4,6]. Both have length >= 3. Add 2 to total. res=1+2=3.
        # i=4, j=3, d=3: dp[3][3]=1 represents ([0,3]). Adding nums[i]=6 forms [0,3,6]. Length >= 3. Add 1 to total. res=3+1=4.
        # i=5, j=2, d=4: dp[2][4]=1 represents ([0,4]). Adding nums[i]=8 forms [0,4,8]. Length >= 3. Add 1 to total. res=4+1=5.
        # i=5, j=4, d=2: dp[4][2]=3 represents ([2,4,6], [0,2,4,6]?, [4,6]). Adding nums[i]=8 forms [2,4,6,8], [0,2,4,6,8]?, [4,6,8]. All length >= 3. Add 3 to total. res=5+3=8.
        # My manual trace matches the code's output. What are the 8?
        # [0,2,4] (i=2,j=1)
        # [2,4,6] (i=4,j=2 from [2,4])
        # [0,2,4,6] (i=4,j=2 from [0,2,4]) - Wait, [0,2,4,6] is NOT a subsequence. nums=[0, 2, 4, 3, 6, 8]. indices (0,1,2,4) -> [0,2,4,6]
        # [0,3,6] (i=4,j=3)
        # [0,4,8] (i=5,j=2)
        # [4,6,8] (i=5,j=4 from [4,6])
        # [2,4,6,8] (i=5,j=4 from [2,4,6])
        # [0,2,4,6,8]? (i=5, j=4 from [0,2,4,6]?) Indices (0,1,2,4) -> [0,2,4,6] diff 2. dp[4][2] += dp[2][2]+1 = 2+1 = 3. Correct. Sequences ending at 4, d=2 are: [4,6], [2,4,6], [0,2,4,6]. That's 3.
        # So at i=5, j=4, d=2, we add dp[4][2]=3. These correspond to extending [4,6] -> [4,6,8], [2,4,6] -> [2,4,6,8], [0,2,4,6] -> [0,2,4,6,8].
        # Total = 1 + 2 + 1 + 1 + 3 = 8. Yes.
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 8, "Mixed numbers failed")

    def test_duplicates(self):
        nums = [1, 1, 2, 2]
        # i=0: {}
        # i=1: j=0, d=0. dp[1]={0:1}. res=0
        # i=2: j=0, d=1. dp[2]={1:1}. j=1, d=1. c=dp[1][1]=0. dp[2]={1:1, 1:1}. res=0
        # i=3: j=0, d=1. c=dp[0][1]=0. dp[3]={1:1}. j=1, d=1. c=dp[1][1]=0. dp[3]={1:2, 0:1}. res=0
        # Expected 0. Code gives 0.
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 0, "Duplicates test 1 failed")
        nums = [1, 1, 1, 2, 2]
        # i=0: {}
        # i=1: j=0, d=0. dp[1]={0:1}. res=0
        # i=2: j=0, d=0. c=0. dp[2]={0:1}. j=1, d=0. c=dp[1][0]=1. res+=1. dp[2]={0: dp[2][0]+1+1 = 1+1+1=3}. res=1 -> [1,1,1] (j=1)
        # i=3: j=0, d=1. dp[3]={1:1}. j=1, d=1. c=0. dp[3]={1:2}. j=2, d=1. c=0. dp[3]={1:3}. res=1
        # i=4: j=0, d=1. c=0. dp[4]={1:1}. j=1, d=1. c=0. dp[4]={1:2}. j=2, d=1. c=0. dp[4]={1:3}. j=3, d=0. c=dp[3][0]=0. dp[4]={1:3, 0:1}. res=1
        # Expected 1 ([1,1,1]). Code gives 1.
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 1, "Duplicates test 2 failed")
        nums = [2, 2, 3, 4]
        # i=0: {}
        # i=1: j=0, d=0. dp[1]={0:1}. res=0
        # i=2: j=0, d=1. dp[2]={1:1}. j=1, d=1. c=0. dp[2]={1:2}. res=0
        # i=3: j=0, d=2. dp[3]={2:1}. j=1, d=2. c=0. dp[3]={2:2}. j=2, d=1. c=dp[2][1]=2. res+=2. dp[3]={2:2, 1: dp[3][1]+2+1 = 3}. res=2 -> [2,3,4] (from [2,3] @ j=2,i=3), [2,3,4] (from [2,3] @ j=1,i=3)
        # Expected 2. Code gives 2.
        self.assertEqual(self.solution.numberOfArithmeticSlices(
            nums), 2, "Duplicates test 3 failed")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
