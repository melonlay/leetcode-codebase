# 42. Trapping Rain Water (Hard)

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Example 1:

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Visual Representation:

      +---+
  3   |   | W W W +---+
      |   | W W W |   | W W +---+
  2 +---+ W W +---+ W W |   | W |   | W +---+
    |   | W |   | W |   | W |   | W |   | W |   |
  1 +---+---+---+---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |   |   |   |
  0 +---+---+---+---+---+---+---+---+---+---+---+---+---+
    0 1 0 2 1 0 1 3 2 1 2 1   (Indices)

'W' represents trapped water units.
Heights:
Index 0: 0
Index 1: 1
Index 2: 0  (Traps 1 unit, limited by left max 1, right max 3 -> min(1,3)-0 = 1)
Index 3: 2
Index 4: 1  (Traps 1 unit, limited by left max 2, right max 3 -> min(2,3)-1 = 1)
Index 5: 0  (Traps 2 units, limited by left max 2, right max 3 -> min(2,3)-0 = 2)
Index 6: 1  (Traps 1 unit, limited by left max 2, right max 3 -> min(2,3)-1 = 1)
Index 7: 3
Index 8: 2  (Traps 1 unit, limited by left max 3, right max 2 -> min(3,2)-2 = 0. Mistake in manual calc, wait. Right max for index 8 is 2. Trapped water = min(left_max=3, right_max=2) - height[8]=2 -> 2-2=0. Let's recheck example. Ah, the blue blocks show the *level* water reaches. Water at index 8 reaches level 2. min(3,2)=2. Water trapped = 2-2=0. Okay.)
Let's re-evaluate water trapped:
Pos 2: min(max(h[0..1]), max(h[3..11])) - h[2] = min(1, 3) - 0 = 1
Pos 4: min(max(h[0..3]), max(h[5..11])) - h[4] = min(2, 3) - 1 = 1
Pos 5: min(max(h[0..4]), max(h[6..11])) - h[5] = min(2, 3) - 0 = 2
Pos 6: min(max(h[0..5]), max(h[7..11])) - h[6] = min(2, 3) - 1 = 1
Pos 8: min(max(h[0..7]), max(h[9..11])) - h[8] = min(3, 2) - 2 = 0  -> Example explanation might be simplified visually? Let's trust the formula.
Pos 9: min(max(h[0..8]), max(h[10..11])) - h[9] = min(3, 2) - 1 = 1
Pos 10: min(max(h[0..9]), max(h[11..11])) - h[10] = min(3, 1) - 2 -> Wait, right max should include index 11. min(3, 1) is wrong. min(max(h[0..9]), max(h[10..11])) = min(3, max(h[10],h[11])) = min(3, max(2,1)) = min(3, 2) = 2. Water = 2 - h[10] = 2-2=0.

Let's re-trace the example explanation logic: Water lies *between* walls.
Between index 1 and 3: wall height min(1, 2) = 1. Water at index 2 = 1 - h[2] = 1 - 0 = 1.
Between index 3 and 7: wall height min(2, 3) = 2.
  Water at index 4 = 2 - h[4] = 2 - 1 = 1.
  Water at index 5 = 2 - h[5] = 2 - 0 = 2.
  Water at index 6 = 2 - h[6] = 2 - 1 = 1.
Between index 7 and 10: wall height min(3, 2) = 2.
  Water at index 8 = 2 - h[8] = 2 - 2 = 0.
  Water at index 9 = 2 - h[9] = 2 - 1 = 1.
Between index 10 and 11? No right boundary.
Total = 1 + 1 + 2 + 1 + 0 + 1 = 6. Okay, the formula `min(max_left, max_right) - height[i]` applied correctly sums to 6.

Total water = 1 + 1 + 2 + 1 + 0 + 1 + 0 = 6.

## Example 2:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```
Visual Representation:

```
      +---+
  5   |   |
      +---+ W +---+
  4   |   | W |   | W +---+
      |   | W |   | W |   |
  3   | W W W +---+ W |   |
      | W W W |   | W |   |
  2 +---+ W W W W W +---+
    |   | W W W W W |   |
  1 |   | W W W W W |   |
    |   | W W W W W |   |
  0 +---+---+---+---+---+---+
    4 2 0 3 2 5   (Indices)

Pos 1: min(max(h[0]), max(h[2..5])) - h[1] = min(4, 5) - 2 = 4 - 2 = 2
Pos 2: min(max(h[0..1]), max(h[3..5])) - h[2] = min(4, 5) - 0 = 4 - 0 = 4
Pos 3: min(max(h[0..2]), max(h[4..5])) - h[3] = min(4, 5) - 3 = 4 - 3 = 1
Pos 4: min(max(h[0..3]), max(h[5..5])) - h[4] = min(4, 5) - 2 = 4 - 2 = 2
Total = 2 + 4 + 1 + 2 = 9.

## Constraints:

*   `n == height.length`
*   `1 <= n <= 2 * 10^4`
*   `0 <= height[i] <= 10^5`

## Topics

*   Array
*   Two Pointers
*   Dynamic Programming
*   Stack

</rewritten_file> 