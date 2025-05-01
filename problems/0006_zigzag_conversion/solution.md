# LeetCode 6: Zigzag Conversion - Solution Explanation

## Problem Summary

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows. We need to read the string line by line and return the result.

Example (numRows = 3):
```
P   A   H   N
A P L S I I G
Y   I   R
```
Result: "PAHNAPLSIIGYIR"

## Algorithmic Approach

This problem can be solved by simulating the traversal path of the zigzag pattern. We can maintain a list of strings (or list of lists of characters), where each inner list represents a row. We then iterate through the input string, placing each character into the correct row based on the current position and direction of movement (down or up) in the zigzag pattern.

## Logic Explanation

1.  **Edge Cases:**
    *   If `numRows` is 1 or if `numRows` is greater than or equal to the length of the string `s`, the zigzag pattern doesn't change the string order. Return `s` directly.
2.  **Initialization:**
    *   Create a list `rows` containing `numRows` empty strings (e.g., `[''] * numRows`). Each string will store the characters belonging to that row.
    *   Initialize `current_row = 0` to track the index of the row we are currently adding characters to.
    *   Initialize `direction = 1`. This variable indicates the direction of vertical movement: `1` means moving down, `-1` means moving up.
3.  **Traversal and Character Placement:**
    *   Iterate through each `char` in the input string `s`.
    *   Append the current `char` to the string at `rows[current_row]`.
    *   **Direction Change Logic:** Check if the traversal has reached the top or bottom row:
        *   If `current_row` is 0 (top row), change `direction` to `1` (start moving down).
        *   If `current_row` is `numRows - 1` (bottom row), change `direction` to `-1` (start moving up).
    *   **Update Current Row:** Update `current_row` by adding `direction` (`current_row += direction`).
4.  **Combine Rows:** After iterating through all characters, the `rows` list contains the characters arranged by row. Join the strings in the `rows` list together in order (`"".join(rows)`) to form the final output string.

## Knowledge Base References

*   **Oscillating Traversal Pattern:** The core logic of moving up and down through rows, controlled by a direction variable that flips at the boundaries, is described by the Oscillating Traversal pattern. See `document/patterns/oscillating_traversal.md`.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string once.
*   **Space Complexity:** O(N). We store all characters of the string `s` in the `rows` list before joining them. 