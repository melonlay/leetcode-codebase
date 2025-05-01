from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverses nodes of a linked list k at a time.

        Args:
            head: The head of the linked list.
            k: The size of the group to reverse.

        Returns:
            The head of the modified linked list.
        """
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        current_node = head

        while True:
            # 1. Find the k-th node
            kth_node = current_node
            count = 0
            while kth_node and count < k:
                kth_node = kth_node.next
                count += 1

            # 2. Check if k nodes exist
            if count == k:
                # 3. Reverse the k nodes
                # Start reversing from current_node up to (but not including) kth_node
                prev = kth_node  # The node after the group becomes the initial 'prev'
                curr = current_node
                group_head = current_node  # Store the original head of this group

                for _ in range(k):
                    next_temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_temp

                # 4. Reconnect the list
                # prev is now the new head of the reversed group
                # group_head is now the tail of the reversed group
                prev_group_tail.next = prev
                group_head.next = kth_node  # Connect tail of reversed group to next group's head

                # 5. Move pointers for the next iteration
                # The tail of the *just reversed* group is the prev_tail for the next
                prev_group_tail = group_head
                current_node = kth_node  # Start next group check from the node after the reversed group
            else:
                # Not enough nodes left, break the loop
                break

        return dummy.next
