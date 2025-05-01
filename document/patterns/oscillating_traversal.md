# Oscillating Traversal Pattern

## Description

This pattern is used to simulate the traversal of a sequence (like a string) following a repeating up-and-down or zigzag path, often used to reconstruct the sequence based on reading the pattern row by row.

It typically involves maintaining:

1.  An array or list of containers (e.g., strings, lists), one for each "row" of the pattern.
2.  A `current_row` index indicating which container to add the next element to.
3.  A `direction` variable (e.g., +1 for down, -1 for up) controlling the movement between rows.

## Algorithm

1.  Handle edge cases (e.g., if the number of rows is 1 or greater than/equal to the sequence length, the original sequence might be returned directly).
2.  Initialize `numRows` empty containers (e.g., `rows = [''] * numRows`).
3.  Initialize `current_row = 0` and `direction = 1` (assuming starting downwards).
4.  Iterate through the input sequence (e.g., string `s`):
    a.  Append the current element `char` to the container at `rows[current_row]`.
    b.  Check if the boundary rows have been reached:
        i.  If `current_row` is the top row (0), change `direction` to `1` (down).
        ii. If `current_row` is the bottom row (`numRows - 1`), change `direction` to `-1` (up).
    c.  Update `current_row` by adding `direction` (`current_row += direction`).
5.  After iterating through all elements, concatenate the contents of the containers (`rows`) in order to get the final result.

## Complexity

*   **Time Complexity:** O(N), where N is the length of the input sequence, as we iterate through it once.
*   **Space Complexity:** O(N), as we store all characters in the `rows` containers before joining them.

## Illustrative Snippet

This snippet shows the core logic using generic names. Assume `sequence` is the input iterable and `num_levels` is the number of containers/rows.

```python
def zigzag_pattern(sequence, num_levels):
    # Basic length/level check - exact behavior depends on problem
    if num_levels <= 1 or num_levels >= len(sequence):
        # Return based on expected output format for edge cases
        if isinstance(sequence, str):
             return sequence # Common case for string problems
        else:
             return list(sequence)

    levels = [[] for _ in range(num_levels)] # Use lists of lists for generality
    current_level = 0
    direction = 1

    for item in sequence:
        levels[current_level].append(item)
        if current_level == 0:
            direction = 1 # Go down
        elif current_level == num_levels - 1:
            direction = -1 # Go up
        current_level += direction

    # The final step depends on how the levels should be combined.
    # Example: Flattening list of lists:
    # flat_list = [item for sublist in levels for item in sublist]
    # Example: Joining strings if levels contain characters:
    # result = "".join(["".join(map(str, level)) for level in levels])
    # Returning the levels themselves is often useful:
    return levels

```

## Example Use Case: LeetCode 6 - Zigzag Conversion

See `problems/0006_zigzag_conversion/solution.py` for a concrete implementation.

```python
# Simplified snippet from LeetCode 6
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction

        return "".join(rows)
``` 