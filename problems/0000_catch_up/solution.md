# Problem: Catch Up (Placeholder Name)

Determine which of two people, Person 1 starting at position `x` or Person 2 starting at position `y`, will reach a target Person 3 at position `z` first.

- If Person 1 is faster, return 1.
- If Person 2 is faster, return 2.
- If they arrive at the same time, return 0.

The time taken to reach the target is the absolute difference between the starting position and the target position `z`.

Constraints:
*   `1 <= x, y, z <= 100`

## Approach: Direct Calculation and Comparison

Given the small constraints and the simple definition of "time taken", a direct calculation is the most straightforward and efficient approach.

1.  **Calculate Time for Person 1:** Compute the absolute difference between Person 3's position (`z`) and Person 1's position (`x`):
    `time1 = abs(z - x)`

2.  **Calculate Time for Person 2:** Compute the absolute difference between Person 3's position (`z`) and Person 2's position (`y`):
    `time2 = abs(z - y)`

3.  **Compare Times:**
    *   If `time1 < time2`, Person 1 is faster. Return `1`.
    *   If `time2 < time1`, Person 2 is faster. Return `2`.
    *   If `time1 == time2`, they arrive simultaneously. Return `0`.

## Complexity Analysis

*   **Time Complexity:** O(1)
    The solution involves a fixed number of arithmetic operations (subtraction, absolute value) and comparisons, regardless of the input values.

*   **Space Complexity:** O(1)
    The solution uses only a few variables (`time1`, `time2`) to store intermediate results, requiring constant extra space.

## Knowledge Base Interaction

Due to the simplicity of the problem and the direct O(1) calculation method, no specific algorithms, patterns, techniques, or optimizations from the knowledge base were required or applicable. 