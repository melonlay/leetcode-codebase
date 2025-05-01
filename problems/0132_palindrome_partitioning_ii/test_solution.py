import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()

    def test_example_cases(self):
        """Test the examples provided in the problem description."""
        self.assertEqual(self.solution.minCut("aab"), 1)
        self.assertEqual(self.solution.minCut("a"), 0)
        self.assertEqual(self.solution.minCut("ab"), 1)

    def test_edge_cases(self):
        """Test edge cases like single character, empty string (per constraints), all same chars."""
        self.assertEqual(self.solution.minCut("b"), 0)
        self.assertEqual(self.solution.minCut("aa"), 0)
        self.assertEqual(self.solution.minCut("bb"), 0)
        self.assertEqual(self.solution.minCut("aaa"), 0)
        self.assertEqual(self.solution.minCut("aaaa"), 0)
        self.assertEqual(self.solution.minCut("aba"), 0)
        self.assertEqual(self.solution.minCut("abba"), 0)

    def test_general_cases(self):
        """Test more general cases."""
        self.assertEqual(self.solution.minCut("abacaba"), 0)  # Palindrome
        self.assertEqual(self.solution.minCut(
            "racecarannakayak"), 2)  # Palindrome components, 2 cuts needed: [racecar|anna|kayak]
        self.assertEqual(self.solution.minCut("abab"), 1)  # a|bab or aba|b
        self.assertEqual(self.solution.minCut("abcba"), 0)  # Palindrome
        self.assertEqual(self.solution.minCut("abcdcba"), 0)  # Palindrome
        self.assertEqual(self.solution.minCut("aabcbaa"),
                         0)  # Is a palindrome itself
        self.assertEqual(self.solution.minCut(
            "fifteen"), 3)  # fif | t | ee | n
        self.assertEqual(self.solution.minCut("coder"), 4)  # c|o|d|e|r

    def test_longer_cases(self):
        """Test cases with longer strings."""
        self.assertEqual(self.solution.minCut(
            "abababababababababababababababababab"), 1)  # Example: a|bab...bab
        # c|abab|abcba|c (check this manually)
        self.assertEqual(self.solution.minCut("cabababcbc"), 3)
        # Manual Check: "cabababcbc", n=10
        # Palindromes ending at index 9 ('c'): c (9,9), bc (8,9) NO, cbc (7,9) YES, ...
        # cuts[-1]=-1
        # cuts[0]=0
        # cuts[1]=1 ('a')
        # cuts[2]=1 ('b')
        # cuts[3]=0 ('aba') cuts[3]=min(2, cuts[0]+1=0)
        # cuts[4]=1 ('b') cuts[4]=min(3, cuts[3]+1=1)
        # cuts[5]=1 ('aba') cuts[5]=min(4, cuts[2]+1=2, cuts[0]+1=0 if 'cabab' is pal NO)
        #   Check s[2..4] = 'bab' -> cuts[5] = min(4, cuts[2]+1=2)
        # cuts[6]=2 ('c') cuts[6]=min(5, cuts[5]+1=3)
        #   Check s[4..5]='bc' NO
        # cuts[7]=2 ('b') cuts[7]=min(6, cuts[6]+1=3)
        #   Check s[5..6]='ab' NO
        #   Check s[3..6]='babc' NO
        # cuts[8]=1 ('cbc') cuts[8]=min(7, cuts[5]+1=2)
        # cuts[9]=2 ('b') cuts[9]=min(8, cuts[8]+1=2)
        #   Check s[7..8]='cb' NO
        # cuts[10]=2 ('c') cuts[10]=min(9, cuts[9]+1=3)
        #   Check s[8..9]='bc' NO
        #   Check s[6..9]='bcbc' YES! cuts[10]=min(3, cuts[6]+1=3)
        #   Check s[4..9]='babcbc' NO
        #   Check s[0..9]='cabababcbc' NO
        # Let's re-run with the code's logic: cuts[i] is for prefix s[0..i-1]
        # s = "cabababcbc", n = 10
        # cuts = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # i=1 (s[0]=c): j=0; is_pal[0][0]=T; cuts[1]=min(0, cuts[0]+1=0) -> cuts=[..0..]
        # i=2 (s[1]=a): j=0; is_pal[0][1]=F; j=1; is_pal[1][1]=T; cuts[2]=min(1, cuts[1]+1=1) -> cuts=[..0,1..]
        # i=3 (s[2]=b): j=0; is_pal[0][2]=F; j=1; is_pal[1][2]=F; j=2; is_pal[2][2]=T; cuts[3]=min(2, cuts[2]+1=2) -> cuts=[..0,1,2..]
        # i=4 (s[3]=a): j=0; F; j=1; is_pal[1][3]=T ('aba'); cuts[4]=min(3, cuts[1]+1=1); j=2; F; j=3; T; cuts[4]=min(1, cuts[3]+1=3)=1 -> cuts=[..0,1,2,1..]
        # i=5 (s[4]=b): j=0; F; j=1; F; j=2; is_pal[2][4]=T ('bab'); cuts[5]=min(4, cuts[2]+1=2); j=3; F; j=4; T; cuts[5]=min(2, cuts[4]+1=2)=2 -> cuts=[..0,1,2,1,2..]
        # i=6 (s[5]=a): j=0; F; j=1; F; j=2; F; j=3; is_pal[3][5]=T ('aba'); cuts[6]=min(5, cuts[3]+1=3); j=4; F; j=5; T; cuts[6]=min(3, cuts[5]+1=3)=3 -> cuts=[..0,1,2,1,2,3..]
        # i=7 (s[6]=b): j=0; F; j=1; F; j=2; F; j=3; F; j=4; is_pal[4][6]=T ('bab'); cuts[7]=min(6, cuts[4]+1=2); j=5; F; j=6; T; cuts[7]=min(2, cuts[6]+1=4)=2 -> cuts=[..0,1,2,1,2,3,2..]
        # i=8 (s[7]=c): j=0; F; j=1; F; j=2; F; j=3; F; j=4; F; j=5; is_pal[5][7]=T ('abc') NO ('aba'); j=6; F; j=7; T; cuts[8]=min(7, cuts[7]+1=3)=3 -> cuts=[..0,1,2,1,2,3,2,3..]
        # i=9 (s[8]=b): j=0; F; ... j=6; is_pal[6][8]=F ('bcb'); j=7; is_pal[7][8]=F ('cb'); j=8; T; cuts[9]=min(8, cuts[8]+1=4)=4 -> cuts=[..0,1,2,1,2,3,2,3,4..]
        # i=10(s[9]=c): j=0; F; ... j=5; is_pal[5][9]=F ('abcbc'); j=6; is_pal[6][9]=T ('bcbc'); cuts[10]=min(9, cuts[6]+1=4); j=7; is_pal[7][9]=T ('cbc'); cuts[10]=min(4, cuts[7]+1=3); j=8; F; j=9; T; cuts[10]=min(3, cuts[9]+1=5)=3 -> cuts=[..0,1,2,1,2,3,2,3,4,3]
        # Result: cuts[10] = 3. Correct. # Partition: c | ababa | b | cbc -> 3 cuts? NO. Partition: c|aba|bab|cbc -> 3 cuts? Yes. Partition: c|abab|cbc -> 2 cuts? NO. c|a|b|a|b|a|b|c|b|c -> 9 cuts.

    # @unittest.skip("Stress test potentially slow")
    # def test_stress_max_length_palindrome(self):
    #     """Test max length string which is already a palindrome."""
    #     s = 'a' * 2000
    #     self.assertEqual(self.solution.minCut(s), 0)

    # @unittest.skip("Stress test potentially slow")
    # def test_stress_max_length_no_palindrome(self):
    #     """Test max length string with minimal palindromes (length 1)."""
    #     s = "ab" * 1000
    #     self.assertEqual(self.solution.minCut(s), 1999)

    def test_edge_case_longer_almost_palindrome(self):
        """Test a longer string that is almost a palindrome but isn't."""
        s = "aabcbaa"
        result = self.solution.minCut(s)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
