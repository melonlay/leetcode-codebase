import collections
from typing import List
from itertools import islice  # Import islice


class Solution:
    """
    Solves the Sliding Window Maximum problem using a monotonic decreasing deque.

    This optimized approach stores values directly in the deque and uses iterators
    for potential performance gains. It maintains values in the deque in
    strictly decreasing order, allowing finding the maximum element in the
    current window in O(1) time.
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum value in each sliding window of size k.

        Args:
            nums: The input list of integers.
            k: The size of the sliding window.

        Returns:
            A list containing the maximum value for each window.
        """
        if not nums or k <= 0:
            return []
        if k == 1:
            return nums

        # Deque stores values directly, monotonically decreasing
        q = collections.deque()
        result = []
        it = iter(nums)  # Create iterator

        # Process the initial window of size k
        for v in islice(it, k):  # Use islice for the first k elements
            # Maintain monotonic decreasing property
            while q and q[-1] < v:
                q.pop()
            q.append(v)

        # The maximum of the first window is at the front
        if q:  # Check if deque is not empty (handles cases like k > n)
            result.append(q[0])

        # Process the rest of the elements
        # 'i' is the index of the element LEAVING the window (0-based from start of nums)
        # 'v' is the element ENTERING the window
        for i, v in enumerate(it):  # i starts from 0 corresponding to nums[k]
            # Lazy removal: Remove front element only if it's the element
            # sliding out of the window (nums[i]) and it's the current max (q[0])
            if q and q[0] == nums[i]:
                q.popleft()

            # Maintain monotonic decreasing property with the new element 'v'
            while q and q[-1] < v:
                q.pop()
            q.append(v)

            # The maximum for the current window is at the front
            if q:  # Check if deque is not empty
                result.append(q[0])

        return result
