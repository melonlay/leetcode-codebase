# 218. The Skyline Problem

**Difficulty:** Hard

**Topics:** Companies

A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return *the **skyline** formed by these buildings collectively*.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [lefti, righti, heighti]`:

*   `lefti` is the x coordinate of the left edge of the `ith` building.
*   `righti` is the x coordinate of the right edge of the `ith` building.
*   `heighti` is the height of the `ith` building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`.

The **skyline** should be represented as a list of "key points" **sorted by their x-coordinate** in the form `[[x1,y1],[x2,y2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate `0` and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

**Note:** There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...,[2,3],[4,5],[7,5],[11,5],[12,7],...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...,[2,3],[4,5],[12,7],...]`

**Example 1:**

**Input:** `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`
**Output:** `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`
**Explanation:**
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

(Figure A textual representation:
- Building 1: x=2 to x=9, height=10 (Blue)
- Building 2: x=3 to x=7, height=15 (Red on top of Blue)
- Building 3: x=5 to x=12, height=12 (Green next to/overlapping Blue/Red)
- Building 4: x=15 to x=20, height=10 (Purple)
- Building 5: x=19 to x=24, height=8 (Yellow partially overlapping Purple)
)

(Figure B textual representation - Skyline key points marked:
- (2, 10) - Start of first building
- (3, 15) - Start of second, taller building
- (7, 12) - End of second building, reveals third building
- (12, 0) - End of third building, skyline drops to ground
- (15, 10) - Start of fourth building
- (20, 8) - End of fourth building, reveals fifth building
- (24, 0) - End of fifth building, skyline drops to ground
)


**Example 2:**

**Input:** `buildings = [[0,2,3],[2,5,3]]`
**Output:** `[[0,3],[5,0]]`
**Explanation:** Two adjacent buildings of the same height. The output reflects the start of the combined segment and the end where it drops to zero.

**Constraints:**

*   `1 <= buildings.length <= 10^4`
*   `0 <= lefti < righti <= 2^31 - 1`
*   `1 <= heighti <= 2^31 - 1`
*   `buildings` is sorted by `lefti` in non-decreasing order. 