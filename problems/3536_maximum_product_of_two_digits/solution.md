# Solution Explanation: 3536. Maximum Product of Two Digits

## Problem Summary

Given a positive integer `n` (where `10 <= n <= 10^9`), find the maximum product that can be obtained by multiplying any two digits present in `n`. Note that the same digit can be used twice if it appears multiple times in `n`.

## Approach and Logic

The goal is to find the two digits in `n` whose product is the largest. Since the digits are single non-negative integers (0-9), the maximum product will come from the two largest digits available in the number `n`.

1.  **Extract Digits:** Convert the integer `n` into its individual digits. A simple way to do this is to convert `n` to a string and then iterate through the characters, converting each back to an integer.
2.  **Identify Two Largest Digits:** To easily find the two largest digits, we can place all extracted digits into a list and sort the list in ascending order.
3.  **Calculate Product:** Once sorted, the two largest digits will be the last two elements in the list (at indices `-1` and `-2`). The maximum product is simply the multiplication of these two digits.

This approach correctly handles cases where the largest digit appears multiple times (e.g., `n=22` -> digits `[2, 2]` -> sorted `[2, 2]` -> product `2*2=4`) and cases where the two largest digits are distinct (e.g., `n=124` -> digits `[1, 2, 4]` -> sorted `[1, 2, 4]` -> product `2*4=8`).

## Implementation Details

The Python implementation uses:
*   `str(n)` to convert the number to a string.
*   A list comprehension `[int(digit) for digit in s]` to create a list of integer digits.
*   `digits.sort()` to sort the list in place.
*   `digits[-1] * digits[-2]` to calculate the product of the two largest digits.

## Complexity Analysis

*   **Time Complexity:** O(D log D), where D is the number of digits in `n`. Converting to a string takes O(D) time. Sorting the digits takes O(D log D) time. Since `n <= 10^9`, D is at most 10. Therefore, the time complexity is very small and effectively constant for practical purposes within the given constraints.
*   **Space Complexity:** O(D) to store the list of digits. Again, since D is at most 10, the space complexity is very small and effectively constant.

## Knowledge Base Links

The core technique relies on basic list manipulation and sorting, which are fundamental operations.
*   Sorting: [[algorithms/sorting/builtin_sort.md]] (Illustrates the use of built-in sorting, which is applied here). 