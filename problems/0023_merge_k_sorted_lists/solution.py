import heapq
from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper for testing: Create ListNode from list
    @staticmethod
    def from_list(vals: List[int]) -> Optional['ListNode']:
        if not vals:
            return None
        head = ListNode(vals[0])
        current = head
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper for testing: Convert ListNode to list
    def to_list(self) -> List[int]:
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next
        return vals

    # Needed for comparison in tests if nodes are directly compared
    # Although not strictly needed for the heap implementation using tuples
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.val == other.val and self.next == other.next

    def __lt__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        # This is needed for heapq if we didn't use the index tiebreaker
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        # Use a counter for tie-breaking in the heap
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
