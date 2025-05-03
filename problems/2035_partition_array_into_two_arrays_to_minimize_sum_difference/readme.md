# 2035. Partition Array Into Two Arrays to Minimize Sum Difference

**Hard**

Topics: Companies, Hint

You are given an integer array `nums` of `2 * n` integers. You need to partition `nums` into two arrays of length `n` to **minimize the absolute difference** of the sums of the arrays. To partition `nums`, put each element of `nums` into **one** of the two arrays.

Return *the minimum possible absolute difference*.

**Example 1:**

```
array 1: [3, 9]
nums:    [3, 9, 7, 3]
array 2: [7, 3]
```
**Input:** nums = [3,9,7,3]
**Output:** 2
**Explanation:** One optimal partition is `arr1 = [3,9]` and `arr2 = [7,3]`.
The absolute difference between the sums of the arrays is `abs((3 + 9) - (7 + 3)) = abs(12 - 10) = 2`.

**Example 2:**

**Input:** nums = [-36,36]
**Output:** 72
**Explanation:** One optimal partition is `arr1 = [-36]` and `arr2 = [36]`.
The absolute difference between the sums of the arrays is `abs((-36) - (36)) = abs(-72) = 72`.

**Example 3:**

```
array 1: [2, 4, -9]
nums:    [2, -1, 0, 4, -2, -9]
array 2: [-1, 0, -2]
```
**Input:** nums = [2,-1,0,4,-2,-9]
**Output:** 0
**Explanation:** One optimal partition is `arr1 = [2,4,-9]` and `arr2 = [-1,0,-2]`.
The absolute difference between the sums of the arrays is `abs((2 + 4 + -9) - (-1 + 0 + -2)) = abs(-3 - (-3)) = 0`.

**Constraints:**

*   `1 <= n <= 15`
*   `nums.length == 2 * n`
*   `-10^7 <= nums[i] <= 10^7` 