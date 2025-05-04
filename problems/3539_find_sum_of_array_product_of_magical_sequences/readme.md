# 100652. Find Sum of Array Product of Magical Sequences

You are given two integers, `M` and `K`, and an integer array `nums`.

A sequence of integers `seq` is called **magical** if:
*   `seq` has a size of `M`.
*   `0 <= seq[i] < nums.length`.
*   The binary representation of `2^seq[0] + 2^seq[1] + ... + 2^seq[M-1]` has `K` **set bits**.

The **array product** of this sequence is defined as `prod(seq) = nums[seq[0]] * nums[seq[1]] * ... * nums[seq[M-1]]`.

Return the **sum** of the **array products** for all valid **magical sequences**.

Since the answer may be large, return it modulo `10^9 + 7`.

A **set bit** refers to a bit in the binary representation of a number that has a value of 1.

**Example 1:**

Input: M = 5, K = 5, nums = [1, 10, 100, 10000, 1000000]
Output: 99160007
Explanation:
All permutations of `[0, 1, 2, 3, 4]` are magical sequences, each with an array product of `10^12`.
There are `5! = 120` such sequences.
The sum is `120 * 10^12`. Modulo `10^9 + 7`, this is `99160007`.
(Note: The example explanation seems simplified. `2^0 + 2^1 + 2^2 + 2^3 + 2^4 = 1 + 2 + 4 + 8 + 16 = 31`, which is `11111` in binary, having 5 set bits. The product is `1*10*100*10000*1000000 = 10^12`. There are `5!` permutations.)

**Example 2:**

Input: M = 2, K = 2, nums = [5, 4, 3, 2, 1]
Output: 170
Explanation:
The magical sequences are `[0, 1]`, `[0, 2]`, `[0, 3]`, `[0, 4]`, `[1, 0]`, `[1, 2]`, `[1, 3]`, `[1, 4]`, `[2, 0]`, `[2, 1]`, `[2, 3]`, `[2, 4]`, `[3, 0]`, `[3, 1]`, `[3, 2]`, `[3, 4]`, `[4, 0]`, `[4, 1]`, `[4, 2]`, `[4, 3]`.
For `[0, 1]`: `2^0 + 2^1 = 3` (binary `11`, 2 set bits). Product `nums[0]*nums[1] = 5*4=20`.
For `[0, 2]`: `2^0 + 2^2 = 5` (binary `101`, 2 set bits). Product `nums[0]*nums[2] = 5*3=15`.
... and so on.
The sum of products is 170.

**Example 3:**

Input: M = 1, K = 1, nums = [28]
Output: 28
Explanation:
The only magical sequence is `[0]`.
`2^0 = 1` (binary `1`, 1 set bit). Product `nums[0] = 28`.

**Constraints:**

*   `1 <= K <= M <= 30`
*   `1 <= nums.length <= 50`
*   `1 <= nums[i] <= 10^9`

**Difficulty:** Hard 