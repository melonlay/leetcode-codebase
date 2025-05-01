from typing import List, Dict


class Solution:
    # String-based implementation mirroring the fast provided code
    def _get_all_max_subsequences_str(self, s: str, k: int) -> Dict[int, str]:
        """
        Calculates the lexicographically largest subsequence strings for 
        relevant lengths based on the input string and global k.
        Mirrors the logic of the provided get_strs function.
        Returns Dict[length, subsequence_string].
        """
        n = len(s)
        res: Dict[int, str] = {0: ""}
        if n == 0:
            return res
        if n < k:  # Optimization: if string shorter than k, it cant affect result > k
            k = n  # Effectively, only calculate subsequences up to length n

        # Part 1: Equivalent to first loop and k_string generation
        # Note: Uses list of chars for stack efficiency, joins later
        stack = [s[0]]
        i = 1
        while i < n and len(stack) + n - i > k:
            while len(stack) + n - i > k and stack and s[i] > stack[-1]:
                stack.pop()
            stack.append(s[i])
            i += 1

        k_string = "".join(stack) + s[i:]
        n_k = len(k_string)
        if n_k >= 0:
            res[n_k] = k_string

        # Part 2 & 3: Equivalent to second and third loops
        if not k_string:  # Handle empty k_string
            return res

        i = n_k - 1  # Target length index (for res dictionary)
        j = 1  # Pointer into k_string
        stack = [k_string[0]]  # Stack used to build shorter sequences

        while i > 0 and j < n_k:
            while stack and stack[-1] < k_string[j]:
                stack.pop()
                # Combine stack prefix + k_string suffix for length 'i'
                current_res_str = "".join(stack) + k_string[j:]
                if i >= 0:  # Check target length index validity
                    # Store only the required length prefix if too long
                    # (Unlikely here due to logic, but safe)
                    res[i] = current_res_str[:i]
                i -= 1
            # Check prevents adding beyond original k_string length implicitly
            if len(stack) < n_k:
                stack.append(k_string[j])
            j += 1

        # Cleanup loop (if stack still has elements)
        if stack:
            stack.pop()  # Equivalent to line 34
            while stack and i > 0:
                res[i] = "".join(stack[:i])  # Prefix of stack is the result
                stack.pop()  # Equivalent to line 37
                i -= 1

        # Ensure length 0 result
        if 0 not in res:
            res[0] = ""

        return res

    # String-based merge
    def _merge_str(self, s1: str, s2: str) -> str:
        """
        Merges two subsequence strings lexicographically.
        String slicing comparison can still be O(k^2) in worst case.
        """
        merged = []  # Build using list.append then join for efficiency
        p1, p2 = 0, 0
        n1, n2 = len(s1), len(s2)

        while p1 < n1 or p2 < n2:
            if p1 >= n1:
                merged.append(s2[p2:])
                break
            if p2 >= n2:
                merged.append(s1[p1:])
                break

            # Compare remaining string suffixes
            if s1[p1:] > s2[p2:]:
                merged.append(s1[p1])
                p1 += 1
            else:
                merged.append(s2[p2])
                p2 += 1
        return "".join(merged)

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        Creates the maximum number of length k using string-based optimization.
        Complexity: O(m+n + k^3) due to O(k^2) merge comparison.
        With O(k) merge: O(m+n + k^2).
        """
        m, n = len(nums1), len(nums2)

        # Initial conversion to strings
        s_num1 = ''.join(map(str, nums1))
        s_num2 = ''.join(map(str, nums2))

        # Pre-calculate all potentially needed max subsequences as strings
        all_subs1_str = self._get_all_max_subsequences_str(s_num1, k)
        all_subs2_str = self._get_all_max_subsequences_str(s_num2, k)

        max_merged_str = ""

        # Iterate through all possible numbers of digits i from nums1
        for i in range(max(0, k - n), min(k, m) + 1):
            len1 = i
            len2 = k - i

            # Retrieve subsequence strings
            sub1_str = all_subs1_str.get(len1)
            sub2_str = all_subs2_str.get(len2)

            if sub1_str is not None and sub2_str is not None:
                merged_str = self._merge_str(sub1_str, sub2_str)

                # Update max_merged_str if the current merge is better
                if merged_str > max_merged_str:
                    max_merged_str = merged_str

        # Final conversion back to List[int]
        return [int(digit) for digit in max_merged_str]
