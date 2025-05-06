# 3519. Count Numbers with Non-Decreasing Digits

(Problem description source: LeetCode)

## Description

You are given two integers, `l` and `r`, represented as strings, and an integer `b`. Return the count of integers in the inclusive range `[l, r]` whose digits are in **non-decreasing** order when represented in base `b`.

An integer is considered to have **non-decreasing digits** if, when read from left to right (from the most significant digit to the least significant digit), each digit is greater than or equal to the previous one.

Since the answer may be too large, return it modulo `10^9 + 7`.

**Example 1:**

Input: `l = "23"`, `r = "28"`, `b = 8`
Output: `3`
Explanation:
The numbers from 23 to 28 in base 8 are: `27` (23_dec), `30` (24_dec), `31` (25_dec), `32` (26_dec), `33` (27_dec), and `34` (28_dec).
Out of these, `27`, `33`, and `34` have non-decreasing digits. Hence, the output is 3.

**Example 2:**

Input: `l = "2"`, `r = "7"`, `b = 2`
Output: `2`
Explanation:
The numbers from 2 to 7 in base 2 are: `10` (2_dec), `11` (3_dec), `100` (4_dec), `101` (5_dec), `110` (6_dec), and `111` (7_dec).
Out of these, `11` and `111` have non-decreasing digits. Hence, the output is 2.

**Constraints:**

*   `1 <= l.length <= r.length <= 100`
*   `2 <= b <= 10`
*   `l` and `r` consist only of digits.
*   The value represented by `l` is less than or equal to the value represented by `r`.
*   `l` and `r` do not contain leading zeros (unless the number itself is 0, although the constraints imply l>=1 based on examples). 