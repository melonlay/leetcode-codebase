# Pattern: In-Place Array Hashing (Cyclic Sort Variant)

## Description

This pattern leverages the input array itself to store information about the presence or properties of elements, typically when constrained to O(1) auxiliary space. It's often used for problems involving numbers in a specific range, usually `[1, n]` or `[0, n-1]`, where `n` is the array length.

The core idea is to treat the array indices as hash keys and the values (or their signs) at those indices as indicators (hash values/presence flags).

## Common Use Cases

*   Finding the first missing positive integer (LeetCode 41).
*   Finding duplicate numbers in an array where numbers are in the range `[1, n]` (LeetCode 287, LeetCode 442).
*   Finding all numbers disappeared in an array (LeetCode 448).
*   Finding the set mismatch (duplicate and missing number) (LeetCode 645).

## Technique: Placing Numbers in Correct Positions

This variant, often called **Cyclic Sort**, aims to place each number `k` (within the target range, e.g., `[1, n]`) at index `k-1`.

### Algorithm Steps

1.  **Iterate and Swap:** Traverse the array (let length be `n`). For each index `i`:
    *   Check if the element `nums[i]` is within the target range (e.g., `1 <= nums[i] <= n`).
    *   Check if `nums[i]` is **not** already in its correct position (`nums[nums[i] - 1] != nums[i]`).
    *   If both conditions are true, swap `nums[i]` with `nums[nums[i] - 1]`.
    *   **Crucially:** Use a `while` loop for these checks and the swap. After a swap, the element newly placed at `nums[i]` might also need moving, so the `while` loop re-evaluates the conditions for the *new* `nums[i]` before moving to the next index `i` in the outer `for` loop. The `nums[nums[i] - 1] != nums[i]` condition prevents infinite loops with duplicates.
2.  **Verification/Result Extraction:** After the rearrangement phase, iterate through the modified array. The information needed (missing number, duplicate, etc.) can usually be found by checking where `nums[i]` does not match the expected value for that index (e.g., `i+1`).

### Example (Finding First Missing Positive - LeetCode 41)

```python
# Example taken from LeetCode 41 solution
# Assumes nums is List[int]
n = len(nums)
# Phase 1: Place numbers in correct positions
for i in range(n):
    # Use while loop for cyclic swaps
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        target_index = nums[i] - 1
        nums[i], nums[target_index] = nums[target_index], nums[i]

# Phase 2: Find first mismatch
for i in range(n):
    if nums[i] != i + 1:
        # return i + 1 # Smallest missing positive
        pass # Placeholder for specific problem's return

# return n + 1 # If all 1 to n are present
```

## Complexity

*   **Time:** O(n). Although there's a nested `while` loop, each number is swapped at most once *into* its correct final position. The total number of swaps is O(n). The subsequent verification scan is O(n).
*   **Space:** O(1). Modifications happen in-place.

## Pitfalls

*   **Off-by-One Errors:** Be careful with index mapping (`k` maps to `k-1`). See `document/common_mistakes/off_by_one_errors.md`.
*   **Loop Conditions:** The `while` loop condition must correctly handle the target range and the duplicate check (`nums[target_index] != nums[i]` or `nums[nums[i] - 1] != nums[i]`) to prevent infinite loops.
*   **Out-of-Range Numbers:** Numbers outside the target range (negative, zero, or > n) should typically be ignored during the placement phase, as their correct position is outside the array bounds. 