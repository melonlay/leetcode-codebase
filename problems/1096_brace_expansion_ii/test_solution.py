import unittest
from .solution import Solution


class TestBraceExpansionII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        expression = "{a,b}{c,{d,e}}"
        expected = ["ac", "ad", "ae", "bc", "bd", "be"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_example2(self):
        expression = "{{a,z},a{b,c},{ab,z}}"
        expected = ["a", "ab", "ac", "z"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_single_letter(self):
        expression = "a"
        expected = ["a"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_simple_union(self):
        expression = "{a,b,c}"
        expected = ["a", "b", "c"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_simple_concat(self):
        expression = "abc"
        expected = ["abc"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_concat_with_union(self):
        expression = "a{b,c}d"
        expected = ["abd", "acd"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_nested_braces(self):
        expression = "{{a,b}}"
        expected = ["a", "b"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_complex_nesting(self):
        expression = "{a,b}c{d,{e,f}}"
        expected = ["acd", "ace", "acf", "bcd", "bce", "bcf"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_empty_inner_braces(self):
        # According to grammar rules and implementation, R({}) yields {""}.
        # R(a{b,{}}c) = R(a) * (R(b) U R({})) * R(c)
        #             = {'a'} * ({'b'} U {""}) * {'c'}
        #             = {'a'} * {'b', ""} * {'c'}
        #             = {'ab', 'a'} * {'c'} = {'abc', 'ac'}
        expression = "a{b,{}}c"
        expected = ["abc", "ac"]  # Corrected sorted order
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

        # R(c{}) = R(c) * R({}) = {'c'} * {""} = {'c'}
        # R({b,c{}}) = R(b) U R(c{}) = {'b'} U {'c'} = {'b', 'c'}
        # R(a{b,c{}}d) = R(a) * R({b,c{}}) * R(d)
        #              = {'a'} * {'b', 'c'} * {'d'}
        #              = {'ab', 'ac'} * {'d'} = {'abd', 'acd'}
        expression = "a{b,c{}}d"
        expected = ["abd", "acd"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

        # R({a,b}{}) = R({a,b}) * R({}) = {'a', 'b'} * {""} = {'a', 'b'}
        expression = "{a,b}{}"
        expected = ["a", "b"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_adjacent_letters_braces(self):
        expression = "z{a,b}y"
        expected = ["zay", "zby"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

        expression = "{a,b}xy{c,d}"
        expected = ["axyc", "axyd", "bxyc", "bxyd"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)

    def test_no_braces(self):
        expression = "leetcode"
        expected = ["leetcode"]
        self.assertEqual(self.solution.braceExpansionII(expression), expected)


if __name__ == '__main__':
    unittest.main()
