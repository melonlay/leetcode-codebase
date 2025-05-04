import math
from typing import List


class Node:
    def __init__(self, pos, time_km=0, idx=0):
        self.pos = pos
        self.time_km = time_km
        self.dist = 0
        self.prev = None
        self.next = None
        self.valid = True
        self.idx = idx


class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:

        if n <= 1:
            return 0

        # Precompute distances D and original times T for segments 0 to n-2
        D = [(position[x+1] - position[x]) for x in range(n - 1)]
        T = time[:n-1]  # Use only times relevant to segments
        num_segments = n - 1

        if k == 0:
            initial_total_time = 0
            for i in range(num_segments):
                initial_total_time += D[i] * T[i]
            return initial_total_time

        if num_segments <= 1:  # Corresponds to n <= 2
            return D[0] * T[0] if num_segments == 1 else 0

        # DP State:
        # f[i][j]: Min time using segments 0..i, j merges among boundaries 1..i, boundary i NOT merged.
        # g[i][j]: Min time using segments 0..i, j merges among boundaries 1..i, boundary i IS merged.
        # i ranges from 0 to num_segments-1 (n-2)
        # j ranges from 0 to k

        f = [[float('inf')] * (k + 1) for _ in range(num_segments)]
        g = [[float('inf')] * (k + 1) for _ in range(num_segments)]

        # Base case: i = 0 (segment 0)
        f[0][0] = D[0] * T[0]
        # g[0][j] remains infinity

        # Iterate through segments i (from 1 to n-2)
        for i in range(1, num_segments):
            # Pre-calculate values for clarity
            dist_i = D[i]
            time_i = T[i]
            dist_prev = D[i-1]  # Exists because i >= 1
            time_prev = T[i-1]
            time_prev_prev = T[i-2] if i >= 2 else 0  # Time for segment i-2
            # Distance of segment i+1
            dist_next = D[i+1] if i + 1 < num_segments else 0

            for j in range(k + 1):  # Number of merges used

                # 1. Calculate f[i][j] (boundary i NOT merged)
                # Cost of segment i depends on whether boundary i-1 was merged
                # If f[i-1][j] is valid, boundary i-1 wasn't merged, add D[i]*T[i]
                time_from_f = f[i-1][j] + dist_i * time_i
                # If g[i-1][j] is valid, boundary i-1 was merged, merge updated T[i], add D[i]*(T[i]+T[i-1])
                time_from_g = g[i-1][j] + dist_i * (time_i + time_prev)
                f[i][j] = min(time_from_f, time_from_g)

                # 2. Calculate g[i][j] (boundary i IS merged) - requires j >= 1
                if j >= 1:
                    # Cost delta if boundary i-1 was NOT merged
                    cost_delta_i = dist_i * \
                        (time_prev - time_i) + dist_next * time_i
                    # Total time = (Time up to i-1) + (Cost of seg i before merge) + (Change from merge i)
                    time_from_f_prev = f[i-1][j-1] + \
                        dist_i * time_i + cost_delta_i

                    # Cost delta if boundary i-1 WAS merged (requires i >= 2)
                    time_from_g_prev = float('inf')
                    if i >= 2:
                        # Effective time of segment i-1 was T[i-2]+T[i-1]
                        cost_delta_merged_i = dist_i * \
                            ((time_prev_prev + time_prev) -
                             time_i) + dist_next * time_i
                        # Total time = (Time up to i-1) + (Cost of seg i before merge, effective T) + (Change from merge i)
                        time_from_g_prev = g[i-1][j-1] + dist_i * \
                            (time_i + time_prev) + cost_delta_merged_i

                    g[i][j] = min(time_from_f_prev, time_from_g_prev)

        # Final answer: min time after considering all n-1 segments (0..n-2), using k merges.
        # Boundary n-1 (after last segment n-2) cannot be merged.
        result = min(f[num_segments - 1][k], g[num_segments - 1][k])

        # Return int result, handle potential infinity if k merges are impossible (shouldn't happen with constraints)
        # Or appropriate handling
        return int(result) if result != float('inf') else -1
