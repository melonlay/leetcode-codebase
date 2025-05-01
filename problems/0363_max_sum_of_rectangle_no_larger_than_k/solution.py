import bisect
import math
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the maximum sum of a rectangle in the matrix such that its sum is no larger than k.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        max_sum = -math.inf

        # Iterate over the smaller dimension squared for optimization
        transpose = rows > cols
        if transpose:
            # Conceptually transpose by swapping loops
            m, n = cols, rows  # m is the dimension for the inner 1D array
        else:
            m, n = rows, cols  # m is the dimension for the inner 1D array

        for i in range(n):  # Iterate through the dimension N (outer loop)
            # `sums_in_m` stores the sum of elements for each element in dimension M,
            # accumulated across the range [i, j] in dimension N.
            sums_in_m = [0] * m
            for j in range(i, n):  # Iterate through the dimension N (outer loop)
                # Accumulate sums for the current range [i, j]
                for row_or_col_m in range(m):
                    if transpose:
                        # If transposed, N=rows, M=cols. Iterate rows (i, j), accumulate columns (row_or_col_m)
                        sums_in_m[row_or_col_m] += matrix[j][row_or_col_m]
                    else:
                        # If not transposed, N=cols, M=rows. Iterate columns (i, j), accumulate rows (row_or_col_m)
                        sums_in_m[row_or_col_m] += matrix[row_or_col_m][j]

                # Now solve the 1D problem: Find max subarray sum <= k in sums_in_m
                current_max_1d = self._find_max_subarray_sum_le_k(sums_in_m, k)
                max_sum = max(max_sum, current_max_1d)

                # Optimization: if max_sum hits k, we can't do better.
                if max_sum == k:
                    return k

        # Should not happen based on guarantee
        return int(max_sum) if max_sum != -math.inf else 0

    def _find_max_subarray_sum_le_k(self, arr: List[int], k: int) -> float:
        """
        Finds the maximum subarray sum <= k in a 1D array.
        Uses prefix sums and binary search (via bisect).
        Returns -infinity if no subarray sum is <= k (though problem guarantees one exists).
        Complexity: O(M^2) due to bisect.insort, where M is len(arr).
                    O(M log M) if a balanced BST (like SortedList) was used.
        """
        max_s = -math.inf
        prefix_sum = 0
        # Stores prefix sums encountered so far, including 0 for subarrays starting at index 0
        seen_sums = [0]

        for x in arr:
            prefix_sum += x

            # We want to find a previous prefix_sum `prev_s` such that:
            # current_subarray_sum = prefix_sum - prev_s <= k
            # This means we need prev_s >= prefix_sum - k

            # Find the smallest `prev_s` in `seen_sums` that is >= `prefix_sum - k`
            target = prefix_sum - k
            idx = bisect.bisect_left(seen_sums, target)

            if idx < len(seen_sums):
                # Found a `prev_s = seen_sums[idx]` such that `prev_s >= target`
                current_subarray_sum = prefix_sum - seen_sums[idx]
                # current_subarray_sum is guaranteed to be <= k here
                max_s = max(max_s, current_subarray_sum)

            # Insert the current prefix_sum into the sorted list
            bisect.insort(seen_sums, prefix_sum)

        return max_s
