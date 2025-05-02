# 3266. Final Array State After K Multiplication Operations II (Hard)

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:
1. Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first** (has the smallest index).
2. Replace the selected minimum value `x` with `x * multiplier`.

After the `k` operations, apply modulo `10^9 + 7` to every value in `nums`.

Return an integer array denoting the final state of `nums` after performing all `k` operations and then applying the modulo.

**Example 1:**
Input: `nums = [2,1,3,5,6]`, `k = 5`, `multiplier = 2`
Output: `[8,4,6,5,6]`
Explanation:
Operation | Result
------- | --------
Initial | `[2, 1, 3, 5, 6]`
After operation 1 | `[2, 2, 3, 5, 6]` (1 at index 1 replaced by 1*2=2)
After operation 2 | `[4, 2, 3, 5, 6]` (2 at index 0 replaced by 2*2=4)
After operation 3 | `[4, 4, 3, 5, 6]` (2 at index 1 replaced by 2*2=4)
After operation 4 | `[4, 4, 6, 5, 6]` (3 at index 2 replaced by 3*2=6)
After operation 5 | `[8, 4, 6, 5, 6]` (4 at index 0 replaced by 4*2=8)
After applying modulo | `[8, 4, 6, 5, 6]`

**Example 2:**
Input: `nums = [100000, 2000]`, `k = 2`, `multiplier = 1000000`
Output: `[999999307, 999999993]`
Explanation:
Operation | Result
------- | --------
Initial | `[100000, 2000]`
After operation 1 | `[100000, 2000000000]` (2000 at index 1 replaced by 2000*1M = 2*10^9)
After operation 2 | `[100000000000, 2000000000]` (100000 at index 0 replaced by 100000*1M = 10^11)
After applying modulo | `[999999307, 999999993]` (10^11 % (10^9+7) = 999999307, 2*10^9 % (10^9+7) = 999999993)

**Constraints:**
*   `1 <= nums.length <= 10^4`
*   `1 <= nums[i] <= 10^9`
*   `1 <= k <= 10^9`
*   `1 <= multiplier <= 10^6`
*   `mod = 10^9 + 7` 