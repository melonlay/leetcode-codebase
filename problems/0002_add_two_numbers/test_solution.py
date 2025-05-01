import unittest
from typing import List, Optional

from .solution import Solution, ListNode

# Helper function to convert a list to a linked list


def list_to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a linked list to a list


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    items = []
    while node:
        items.append(node.val)
        node = node.next
    return items


class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example1(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        expected_output = [7, 0, 8]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_example2(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        expected_output = [0]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_example3(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_different_lengths_l1_longer(self):
        l1 = list_to_linked_list([1, 2, 3, 4])
        l2 = list_to_linked_list([5, 6])
        expected_output = [6, 8, 3, 4]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_different_lengths_l2_longer(self):
        l1 = list_to_linked_list([5, 6])
        l2 = list_to_linked_list([1, 2, 3, 4])
        expected_output = [6, 8, 3, 4]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_carry_over(self):
        l1 = list_to_linked_list([9])
        l2 = list_to_linked_list([1])
        expected_output = [0, 1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_max_length_all_nines(self):
        l1 = list_to_linked_list([9] * 100)
        l2 = list_to_linked_list([9] * 100)
        # 99...9 (100 times) + 99...9 (100 times) = 199...98 (1 followed by 99 nines and an 8)
        # In reverse order: [8, 9, 9, ..., 9, 1] (101 nodes)
        expected_output = [8] + [9] * 99 + [1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_max_length_one_short(self):
        l1 = list_to_linked_list([9] * 100)
        l2 = list_to_linked_list([1])
        # 99...9 (100 times) + 1 = 100...0 (1 followed by 100 zeros)
        # In reverse order: [0, 0, ..., 0, 1] (101 nodes)
        expected_output = [0] * 100 + [1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_carry_propagation_multiple(self):
        l1 = list_to_linked_list([1])
        l2 = list_to_linked_list([9, 9])  # 99 + 1 = 100
        expected_output = [0, 0, 1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_single_digit_no_carry(self):
        l1 = list_to_linked_list([1])
        l2 = list_to_linked_list([2])
        expected_output = [3]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_empty_inputs(self):
        # Test None + None -> None (or empty list)
        l1_none = None
        l2_none = None
        expected_output_none = []
        result_node_none = self.solution.addTwoNumbers(l1_none, l2_none)
        self.assertEqual(linked_list_to_list(
            result_node_none), expected_output_none)

        # Test List + None -> List
        l1_some = list_to_linked_list([1, 2, 3])
        l2_none = None
        expected_output_some1 = [1, 2, 3]
        result_node_some1 = self.solution.addTwoNumbers(l1_some, l2_none)
        self.assertEqual(linked_list_to_list(
            result_node_some1), expected_output_some1)

        # Test None + List -> List
        l1_none = None
        l2_some = list_to_linked_list([4, 5, 6])
        expected_output_some2 = [4, 5, 6]
        result_node_some2 = self.solution.addTwoNumbers(l1_none, l2_some)
        self.assertEqual(linked_list_to_list(
            result_node_some2), expected_output_some2)

    def test_long_carry_propagation_from_short_list(self):
        l1 = list_to_linked_list([1])
        l2 = list_to_linked_list([9, 9, 9])  # 999 + 1 = 1000
        expected_output = [0, 0, 0, 1]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_add_number_to_zero_list(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([1, 2, 3])  # 321 + 0 = 321
        expected_output = [1, 2, 3]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_add_zero_list_to_number(self):
        l1 = list_to_linked_list([1, 2, 3])  # 321 + 0 = 321
        l2 = list_to_linked_list([0])
        expected_output = [1, 2, 3]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)

    def test_carry_into_longer_list(self):
        l1 = list_to_linked_list([8, 9])  # 98
        l2 = list_to_linked_list([3, 2, 1])  # 123
        # 98 + 123 = 221
        expected_output = [1, 2, 2]
        result_node = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result_node), expected_output)


if __name__ == '__main__':
    unittest.main()
