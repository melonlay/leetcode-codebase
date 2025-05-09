# Algorithm: Longest Increasing Subsequence (LIS)

## Concept

The Longest Increasing Subsequence (LIS) problem involves finding the length of the longest subsequence within a given sequence such that all elements of the subsequence are sorted in increasing order.

For example, in the sequence `[10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 101]`, and its length is 4.

## Approaches

### 1. Dynamic Programming (O(n^2))

Let `dp[i]` be the length of the LIS ending at index `i`.
To compute `dp[i]`, we look at all `j < i`. If `nums[i] > nums[j]`, it means we can potentially extend the LIS ending at `j` by including `nums[i]`.
So, `dp[i] = 1 + max(dp[j])` for all `0 <= j < i` where `nums[i] > nums[j]`. If no such `j` exists, `dp[i] = 1`.
The final answer is `max(dp)`.

- **Time Complexity:** O(n^2) - Two nested loops.
- **Space Complexity:** O(n) - To store the `dp` array.

### 2. Binary Search / Patience Sorting (O(n log n))

This is a more efficient approach. We maintain an array `tails` (or `piles` in Patience Sorting analogy) where `tails[i]` stores the smallest tail element of all increasing subsequences of length `i+1` found so far.

Iterate through the input `nums`:
- For each `num` in `nums`:
    - Use binary search (`bisect_left` in Python) to find the smallest `tails[i]` such that `tails[i] >= num`.
    - If such an element exists (i.e., `num` is not greater than all elements in `tails`), replace `tails[i]` with `num`. This means we've found a potential LIS of length `i+1` that ends with a smaller number (`num`) than the previous LIS of the same length. This smaller tail gives more possibilities for extension later.
    - If `num` is greater than all elements in `tails`, it means we can extend the longest LIS found so far. Append `num` to `tails`, increasing the LIS length by 1.

The length of the LIS is simply the final length of the `tails` array.

- **Time Complexity:** O(n log n) - We iterate through `n` numbers, and each binary search takes O(log n) time.
- **Space Complexity:** O(n) - In the worst case (a strictly increasing sequence), the `tails` array can grow up to size `n`.

## Python Implementation (O(n log n))

There are two common ways to implement the O(n log n) approach:

### Variant 1: Standard Approach (Empty Initialization)

This version initializes the `tails` list as empty and processes all elements, relying on `bisect_left` to determine insertion or replacement.

```python
import bisect

def lengthOfLIS_standard(nums: list[int]) -> int:
    if not nums: # Handles empty input
        return 0
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
```
- **Pros:** Handles empty lists naturally, arguably slightly cleaner logic flow.
- **Cons:** Always performs a binary search (`bisect_left`) for every element.

### Variant 2: Optimized Append Check

This version initializes the `tails` (often called `dp` in competitive programming contexts) list with the first element and explicitly checks if the current number extends the LIS before resorting to `bisect_left`.

```python
from bisect import bisect_left

def lengthOfLIS_optimized_append(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [nums[0]] # Initialize with first element
    for num in nums[1:]: # Iterate from second element
        if dp[-1] < num:
            dp.append(num) # Append directly if extending
        else:
            # Only binary search if replacing an element
            i = bisect_left(dp, num)
            dp[i] = num
    return len(dp)
```
- **Pros:** Can be slightly faster if the input often involves appending rather than replacing, as it avoids some `bisect_left` calls (O(1) check vs O(log k)).
- **Cons:** Requires explicit handling of the empty list case. Initialization depends on the first element.

## Applications

*   Finding the longest monotonic subsequence in a sequence.
*   As a subroutine in other problems, e.g., [[../../techniques/dynamic_programming/2d_dependency_lis_reduction.md|2D Dependency Reduction via LIS]].
*   Patience Sorting.

## Related Techniques

- [[../../../../techniques/array/2d_dependency_lis_reduction.md|Technique: 2D Dependency Reduction via LIS]] - For applying LIS to problems with 2D constraints.

## Tradeoffs

- The O(n^2) DP approach is simpler to understand conceptually but too slow for large inputs (e.g., n > 5000).
- The O(n log n) binary search approach is significantly faster and necessary for larger constraints, relying on the `bisect` module in Python for efficient implementation. 