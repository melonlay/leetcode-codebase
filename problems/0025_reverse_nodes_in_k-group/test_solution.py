import unittest
from typing import List, Optional

# Relative import of the solution
from .solution import Solution, ListNode

# Helper function to convert a Python list to a ListNode


def list_to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a ListNode back to a Python list


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items

# Helper function to generate the expected list after k-group reversal


def generate_expected(input_list: List[int], k: int) -> List[int]:
    n = len(input_list)
    if k <= 1 or n == 0:
        return input_list[:]  # Return a copy

    output_list = []
    for i in range(0, n, k):
        chunk = input_list[i: min(i + k, n)]
        if len(chunk) == k:
            output_list.extend(chunk[::-1])  # Reverse full chunks
        else:
            output_list.extend(chunk)  # Append remainder as is
    return output_list


class TestReverseKGroup(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        head_list = [1, 2, 3, 4, 5]
        k = 2
        expected_list = [2, 1, 4, 3, 5]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_example2(self):
        head_list = [1, 2, 3, 4, 5]
        k = 3
        expected_list = [3, 2, 1, 4, 5]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_k_equals_1(self):
        head_list = [1, 2, 3, 4, 5]
        k = 1
        expected_list = [1, 2, 3, 4, 5]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_k_equals_n(self):
        head_list = [1, 2, 3, 4, 5]
        k = 5
        expected_list = [5, 4, 3, 2, 1]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_n_multiple_of_k(self):
        head_list = [1, 2, 3, 4, 5, 6]
        k = 3
        expected_list = [3, 2, 1, 6, 5, 4]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_empty_list(self):
        head_list = []
        k = 2
        expected_list = []
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_single_node(self):
        head_list = [1]
        k = 1
        expected_list = [1]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_single_node_k_gt_n(self):
        head_list = [1]
        k = 2
        expected_list = [1]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_k_larger_than_n(self):
        head_list = [1, 2, 3]
        k = 4
        expected_list = [1, 2, 3]
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # Note: A true stress test with n=5000 might be slow in some environments.
    # This test uses a smaller N but checks the logic for large k.
    def test_stress_k_equals_n_large(self):
        n = 100
        k = 100
        head_list = list(range(1, n + 1))
        expected_list = list(range(n, 0, -1))
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_stress_large_n_small_k(self):
        n = 100
        k = 2
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)  # Use helper
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # --- Start of New Test Cases ---

    # @unittest.skip("Skipping potentially slow stress test (n=5000)")
    def test_stress_max_n_max_k(self):
        """Tests max n and max k (reverses entire list). Might be slow."""
        n = 5000
        k = 5000
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        # For very large lists, comparing length and end elements might be faster
        # than full list comparison if performance is critical during testing.
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # @unittest.skip("Skipping potentially slow stress test (n=5000)")
    def test_stress_max_n_small_k(self):
        """Tests max n with small k (many reversals). Might be slow."""
        n = 5000
        k = 2
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # @unittest.skip("Skipping potentially slow stress test (n=5000)")
    def test_stress_max_n_medium_k(self):
        """Tests max n with medium k. Might be slow."""
        n = 5000
        k = 70  # Approx sqrt(5000)
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # @unittest.skip("Skipping potentially slow stress test (n=5000)")
    def test_stress_max_n_large_k_remainder(self):
        """Tests max n with large k leaving a small remainder. Might be slow."""
        n = 5000
        k = 4999  # One group reversed, one node left
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_large_n_k_small_remainder(self):
        """Tests large n where k leaves a small remainder."""
        n = 101  # Example size
        k = 10  # 10 groups of 10, remainder 1
        head_list = list(range(1, n + 1))
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_node_max_value(self):
        """Tests with node values at the constraint maximum."""
        head_list = [1000, 999, 1000, 0, 500, 1000]
        k = 3
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    def test_repeating_values(self):
        """Tests with repeating node values."""
        head_list = [1, 1, 2, 2, 1, 1, 3, 3]
        k = 2
        expected_list = generate_expected(head_list, k)
        head = list_to_linked_list(head_list)
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result_head), expected_list)

    # --- End of New Test Cases ---


if __name__ == '__main__':
    unittest.main()
