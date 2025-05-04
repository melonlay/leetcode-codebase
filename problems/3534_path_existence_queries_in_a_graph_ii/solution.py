# Correct Solution: Sort + Binary Lifting on Farthest Reachable Indices
# Based on the structure provided by the user in the second attempt.

from typing import List
import bisect
import math  # For bit_length


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Special case: no edges except self or duplicates if maxDiff == 0
        # Check bounds for nums access
        if maxDiff < 0:  # Handle negative maxDiff
            return [(0 if u == v else -1) for u, v in queries]
        if maxDiff == 0:
            # Nodes with identical values are directly connected
            # Check bounds for nums access inside list comprehension
            return [0 if u == v else (1 if 0 <= u < n and 0 <= v < n and nums[u] == nums[v] else -1) for u, v in queries]

        # Sort values and track original indices
        idx = list(range(n))
        try:
            idx.sort(key=lambda i: nums[i])
            sorted_vals = [nums[i] for i in idx]
        # Handles cases where n might mismatch len(nums) or indices are bad
        except IndexError:
            return [-1] * len(queries)

        # Map original index to sorted position
        pos = [0] * n  # Initialize with 0, assuming valid indices
        for sorted_pos, orig_idx in enumerate(idx):
            # Assuming orig_idx is always valid (0 to n-1)
            pos[orig_idx] = sorted_pos

        # Build component ids for connectivity check
        # CORRECTED INITIALIZATION to match user's code:
        comp = [0] * n  # Initialize with 0
        cid = 0
        # Assuming n > 0 based on constraints for comp[0] access
        if n > 0:
            comp[0] = 0
            for i in range(1, n):
                # Assuming sorted_vals has at least n elements
                if sorted_vals[i] - sorted_vals[i-1] <= maxDiff:
                    comp[i] = cid
                else:
                    cid += 1
                    comp[i] = cid
        # Map components back to original indices
        # Assuming pos[i] is valid index for comp access
        comp_orig = [comp[pos[i]] for i in range(n)]

        # Special case: complete graph clique
        # Check n>0 before accessing sorted_vals
        is_clique = False
        if n > 0:
            try:
                # Use the EXACT condition provided by the user
                if maxDiff >= sorted_vals[-1] - sorted_vals[0]:
                    is_clique = True
            except IndexError:  # Should not happen if n > 0, but for safety
                is_clique = False

        if is_clique:
            res = []
            for u, v in queries:
                # Use the EXACT logic provided by the user
                if u == v:
                    res.append(0)
                # Check bounds implicitly via comp_orig access validity
                # Assuming u,v are expected to be valid based on constraints
                # if they aren't, IndexError will likely occur here or earlier.
                elif 0 <= u < n and 0 <= v < n and comp_orig[u] == comp_orig[v]:
                    # If the outer condition holds, comp_orig check is technically
                    # redundant IF u,v are valid indices, as all will be in comp 0.
                    # But we follow the user's code structure exactly.
                    res.append(1)
                # Handles u==v, components differ (shouldn't happen if clique), or invalid u/v indices implicitly
                else:
                    # Return -1 for invalid query indices or if somehow components differed
                    res.append(-1)
            return res

        # Precompute farthest reachable in one jump to the right (fr) and left (fl)
        fr = [0] * n
        fl = [0] * n
        for i in range(n):
            # farthest right j where sorted_vals[j] - sorted_vals[i] <= maxDiff
            # Assuming sorted_vals[i] exists
            j = bisect.bisect_right(sorted_vals, sorted_vals[i] + maxDiff) - 1
            # Use EXACT logic from user's provided code
            fr[i] = j

            # farthest left j where sorted_vals[i] - sorted_vals[j] <= maxDiff
            # Assuming sorted_vals[i] exists
            j2 = bisect.bisect_left(sorted_vals, sorted_vals[i] - maxDiff)
            # Use EXACT logic from user's provided code
            fl[i] = j2

        # Build binary lifting tables for jumps
        LOG = (n).bit_length()
        # Initialize tables based on provided code (no modification)
        nxt = [fr]  # Start with base case fr
        prv = [fl]  # Start with base case fl
        for k in range(1, LOG):
            prev_n = nxt[k-1]
            prev_p = prv[k-1]
            # Initialize current level's jump arrays
            cur_n = [0] * n
            cur_p = [0] * n
            for i in range(n):
                # Calculate 2^k jump by chaining two 2^(k-1) jumps
                # Assuming indices from prev_n/prev_p are valid
                intermediate_nxt = prev_n[i]
                # Check bounds before indexing prev_n again
                if 0 <= intermediate_nxt < n:
                    cur_n[i] = prev_n[intermediate_nxt]
                # If intermediate jump leads out of bounds, result is invalid (or stay?)
                else:
                    # Propagate potential out-of-bounds index
                    cur_n[i] = intermediate_nxt

                intermediate_prv = prev_p[i]
                if 0 <= intermediate_prv < n:  # Check bounds
                    cur_p[i] = prev_p[intermediate_prv]
                else:
                    # Propagate potential out-of-bounds index
                    cur_p[i] = intermediate_prv

            nxt.append(cur_n)
            prv.append(cur_p)

        # Helper functions to compute minimum jumps
        def jumps_forward(s: int, t: int) -> int:
            # Assumes s,t are valid sorted indices 0 <= s,t < n
            if s >= t:
                return 0
            cnt = 0
            cur = s
            for k in range(LOG-1, -1, -1):
                # Check bounds before table access
                if 0 <= k < LOG and 0 <= cur < n:
                    ni = nxt[k][cur]
                    # If jump is valid and stays below target
                    # Crucially check if ni is a valid index before comparing
                    if 0 <= ni < n and ni < t:
                        cnt += 1 << k
                        cur = ni  # Take the jump
                    # else if ni >= n or ni < 0, invalid jump result, stop? Or continue with smaller k?
                    # The original code structure implies continuing.
                # else: Skip jump if k or cur invalid

            # Check final jump (k=0)
            # Check bounds before table access
            if 0 <= cur < n and LOG > 0 and 0 <= nxt[0][cur] < n and nxt[0][cur] >= t:
                return cnt + 1
            else:
                # If final jump doesn't reach, return infinity (unreachable)
                return float('inf')

        def jumps_backward(s: int, t: int) -> int:
            # Assumes s,t are valid sorted indices 0 <= s,t < n
            if s <= t:
                return 0
            cnt = 0
            cur = s
            for k in range(LOG-1, -1, -1):
                if 0 <= k < LOG and 0 <= cur < n:
                    pi = prv[k][cur]
                    # If jump is valid and stays above target
                    if 0 <= pi < n and pi > t:
                        cnt += 1 << k
                        cur = pi  # Take the jump
                # else: Skip jump

            # Check final jump (k=0)
            if 0 <= cur < n and LOG > 0 and 0 <= prv[0][cur] < n and prv[0][cur] <= t:
                return cnt + 1
            else:
                # Unreachable
                return float('inf')

        # Answer each query
        ans = []
        for u, v in queries:
            # Assume u,v are valid indices 0 <= u,v < n based on constraints
            if u == v:
                ans.append(0)
                continue

            # Check connectivity via components
            # Assume comp_orig[u/v] are valid component IDs if indices are valid
            if comp_orig[u] != comp_orig[v]:
                ans.append(-1)
                continue

            # Get sorted positions
            # Assume pos[u/v] are valid sorted indices
            pu, pv = pos[u], pos[v]

            # Calculate jumps
            distance = -1
            if pu <= pv:
                distance = jumps_forward(pu, pv)
            else:
                distance = jumps_backward(pu, pv)

            # Convert infinity to -1
            ans.append(distance if distance != float('inf') else -1)

        return ans
