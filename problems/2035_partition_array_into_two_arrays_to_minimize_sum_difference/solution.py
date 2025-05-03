import bisect
from collections import defaultdict
from typing import List, Dict, Set
import math


class Solution:
    def _get_subset_sums(self, arr: List[int]) -> Dict[int, Set[int]]:
        """ Optimized subset sum generation using downward iteration. """
        sums_by_count = defaultdict(set)
        sums_by_count[0] = {0}
        n_half = len(arr)
        for x in arr:
            # Iterate counts downwards using range
            for count in range(n_half - 1, -1, -1):
                if sums_by_count[count]:
                    sums_to_add = {s + x for s in sums_by_count[count]}
                    sums_by_count[count + 1].update(sums_to_add)
        return sums_by_count

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2

        if half == 0:
            return 0  # Handle n=0 case although constraints say n>=1

        full_sum = sum(nums)
        half_sum = full_sum // 2

        # === Early Exit Checks (from user code) ===
        # Calculate initial sums carefully to avoid redundant full sums
        left_initial_sum = sum(nums[:half])
        if left_initial_sum == half_sum:
            # Difference is total_sum - 2 * half_sum = total_sum % 2
            return full_sum - 2 * half_sum

        # Calculate right sum from total and left
        right_initial_sum = full_sum - left_initial_sum
        if right_initial_sum == half_sum:
            return full_sum - 2 * half_sum
        # === End Early Exit Checks ===

        left_sums_map = self._get_subset_sums(nums[:half])
        right_sums_map = self._get_subset_sums(nums[half:])

        # --- Nested calc function mirroring user code structure ---
        def calc(left_map, right_map):

            # === Initialization mirroring user code ===
            initial_res = float('inf')
            # Check if set exists and is not empty
            if half in left_map and left_map[half]:
                initial_res = min(initial_res, min(left_map[half]))
            # Check if set exists and is not empty
            if half in right_map and right_map[half]:
                initial_res = min(initial_res, min(right_map[half]))

            # If initial_res is still inf, need a better fallback (e.g., overall min sum)
            if initial_res == float('inf'):
                min_possible_sum = float('inf')
                for k_init in range(half + 1):
                    j_init = half - k_init
                    if k_init in left_map and j_init in right_map:
                        left_set = left_map[k_init]
                        right_set = right_map[j_init]
                        if left_set and right_set:
                            min_possible_sum = min(
                                min_possible_sum, min(left_set) + min(right_set))
                initial_res = min_possible_sum if min_possible_sum != float(
                    'inf') else 0  # Default to 0 if no sums found?

            result = initial_res  # This is the equivalent of max_sum_le_half
            # === End Initialization ===

            for left_cnt, left_sums_set in left_map.items():
                right_cnt = half - left_cnt
                if right_cnt not in right_map:
                    continue  # Skip if no corresponding right count

                right_sums_set = right_map[right_cnt]
                if not left_sums_set or not right_sums_set:
                    continue  # Skip if either set is empty

                # --- Sort lists INSIDE the loop (as per user code) ---
                a = sorted(list(left_sums_set))
                b = sorted(list(right_sums_set))
                # --- End Sorting Inside ---

                m = len(a)
                l = len(b)
                i = 0
                j = l - 1

                # --- Two pointer search (same logic as user code) ---
                while i < m and j >= 0:
                    current = a[i] + b[j]
                    if current == half_sum:
                        # Found exact half sum, return minimal difference
                        return full_sum - 2 * current
                    if current > half_sum:
                        j -= 1  # Sum too large, try smaller sum from right
                    else:  # current < half_sum
                        # Update the max sum found that is <= half_sum
                        result = max(result, current)
                        i += 1  # Try larger sum from left

            # Return difference based on the max sum found <= half_sum
            return full_sum - 2 * result
        # --- End Nested calc function ---

        return calc(left_sums_map, right_sums_map)
