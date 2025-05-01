import unittest
from typing import List, Optional

# Use relative import for testing within the package structure
from .solution import Solution, ListNode

# --- Helper Functions ---


def assertLinkedListEqual(test_case, l1: Optional[ListNode], l2: Optional[ListNode]):
    """Helper function (outside class) to compare two linked lists."""
    while l1 and l2:
        test_case.assertEqual(l1.val, l2.val)
        l1 = l1.next
        l2 = l2.next
    test_case.assertIsNone(l1)
    test_case.assertIsNone(l2)


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    """Helper function (outside class) to convert a Python list to a ListNode chain."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    """Helper function (outside class) to convert a ListNode chain back to a Python list."""
    items = []
    current = node
    while current:
        items.append(current.val)
        current = current.next
    return items

# --- Test Class ---


class TestMergeKLists(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example1(self):
        lists = [
            list_to_linkedlist([1, 4, 5]),
            list_to_linkedlist([1, 3, 4]),
            list_to_linkedlist([2, 6])
        ]
        expected_list = [1, 1, 2, 3, 4, 4, 5, 6]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        # Also check list conversion for easier debugging if needed
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_example2_empty_input(self):
        lists = []
        expected_list = []
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_example3_list_of_empty_list(self):
        lists = [list_to_linkedlist([])]
        expected_list = []
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_list_with_empty_lists_mixed(self):
        lists = [
            list_to_linkedlist([1, 3]),
            list_to_linkedlist([]),
            list_to_linkedlist([2, 4])
        ]
        expected_list = [1, 2, 3, 4]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_single_list(self):
        lists = [list_to_linkedlist([1, 2, 3])]
        expected_list = [1, 2, 3]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_all_empty_lists(self):
        lists = [
            list_to_linkedlist([]),
            list_to_linkedlist([]),
            list_to_linkedlist([])
        ]
        expected_list = []
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_negative_numbers(self):
        lists = [
            list_to_linkedlist([-2, -1, 0]),
            list_to_linkedlist([-3])
        ]
        expected_list = [-3, -2, -1, 0]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_duplicate_numbers_across_lists(self):
        lists = [
            list_to_linkedlist([1, 1]),
            list_to_linkedlist([1, 2])
        ]
        expected_list = [1, 1, 1, 2]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_one_list_is_none(self):
        lists = [None, list_to_linkedlist([1, 2]), None]
        expected_list = [1, 2]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    # --- Constraint and Stress Tests ---

    def test_stress_max_k_max_total_n(self):
        # k = 10000, total N = 10000 (each list has 1 element)
        # Tests O(N log k) with large k
        k = 10000
        lists = [list_to_linkedlist([i]) for i in range(k)]
        expected_list = list(range(k))
        expected_head = list_to_linkedlist(expected_list)
        # Measure time (optional, useful for local profiling)
        # import time
        # start = time.time()
        result_head = self.solution.mergeKLists(lists)
        # end = time.time()
        # print(f"\nMax K test time: {end - start:.4f}s")
        assertLinkedListEqual(self, result_head, expected_head)
        # Avoid converting large list back unless necessary for debugging
        # self.assertEqual(self.linkedlist_to_list(result_head), expected_list)

    def test_stress_max_n_moderate_k(self):
        # k = 20, list_len = 500, total N = 10000
        # Tests O(N log k) with smaller k but larger lists
        k = 20
        list_len = 500
        lists = []
        expected_list = []
        for i in range(k):
            # Create lists like [0, 20, 40...], [1, 21, 41...], etc.
            sub_list = [i + j * k for j in range(list_len)]
            lists.append(list_to_linkedlist(sub_list))
            expected_list.extend(sub_list)

        expected_list.sort()  # The merge result should be sorted
        expected_head = list_to_linkedlist(expected_list)

        # Measure time (optional)
        # import time
        # start = time.time()
        result_head = self.solution.mergeKLists(lists)
        # end = time.time()
        # print(f"\nMax N test time: {end - start:.4f}s")

        # Due to potentially large size, only check first/last few elements or length
        result_as_list = linkedlist_to_list(result_head)
        self.assertEqual(len(result_as_list), len(expected_list))
        self.assertEqual(result_as_list[0], expected_list[0])
        self.assertEqual(result_as_list[-1], expected_list[-1])
        # Full comparison if needed, but might be slow for assertion output
        # self.assertLinkedListEqual(result_head, expected_head)

    def test_min_max_values(self):
        min_val = -10000
        max_val = 10000
        lists = [
            list_to_linkedlist([min_val, 0, max_val]),
            list_to_linkedlist([min_val + 1, 1, max_val - 1]),
            list_to_linkedlist([min_val])
        ]
        expected_list = [min_val, min_val,
                         min_val + 1, 0, 1, max_val - 1, max_val]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_many_empty_and_none_lists(self):
        lists = [None] * 5000 + [list_to_linkedlist([])] * 4998 + [
            list_to_linkedlist([1, 3]),
            list_to_linkedlist([2, 4])
        ]  # Total k = 10000
        expected_list = [1, 2, 3, 4]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    # --- More Critical/Edge Cases ---

    def test_all_lists_start_same_value(self):
        lists = [
            list_to_linkedlist([5, 8, 10]),
            list_to_linkedlist([5, 9]),
            list_to_linkedlist([5, 5, 12])
        ]
        expected_list = [5, 5, 5, 5, 8, 9, 10, 12]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_heavily_interleaved_values(self):
        lists = [
            list_to_linkedlist([1, 10, 20]),
            list_to_linkedlist([2, 11, 21]),
            list_to_linkedlist([3, 12, 22])
        ]
        expected_list = [1, 2, 3, 10, 11, 12, 20, 21, 22]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_one_dominant_long_list(self):
        long_list_data = list(range(0, 498, 2))  # Even numbers up to 496
        lists = [
            list_to_linkedlist(long_list_data),
            list_to_linkedlist([1]),
            list_to_linkedlist([3]),
            list_to_linkedlist([497]),
            list_to_linkedlist([499]),
        ]
        expected_list = sorted(long_list_data + [1, 3, 497, 499])
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        # Check conversion for easier debugging
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_duplicates_within_lists(self):
        lists = [
            list_to_linkedlist([1, 1, 5, 5]),
            list_to_linkedlist([1, 4, 4]),
            list_to_linkedlist([2, 6, 6])
        ]
        expected_list = [1, 1, 1, 2, 4, 4, 5, 5, 6, 6]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_lists_ending_with_same_value(self):
        lists = [
            list_to_linkedlist([1, 5]),
            list_to_linkedlist([2, 5]),
            list_to_linkedlist([3, 5])
        ]
        expected_list = [1, 2, 3, 5, 5, 5]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)

    def test_alternating_empty_none(self):
        lists = [
            list_to_linkedlist([1, 6]),
            None,
            list_to_linkedlist([]),
            list_to_linkedlist([2, 7]),
            None,
            list_to_linkedlist([3, 8])
        ]
        expected_list = [1, 2, 3, 6, 7, 8]
        expected_head = list_to_linkedlist(expected_list)
        result_head = self.solution.mergeKLists(lists)
        assertLinkedListEqual(self, result_head, expected_head)
        self.assertEqual(linkedlist_to_list(result_head), expected_list)


if __name__ == '__main__':
    unittest.main()
