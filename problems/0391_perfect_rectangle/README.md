# 391. Perfect Rectangle

**Difficulty:** Hard

**Topics:** Array, Line Sweep

Given an array `rectangles` where `rectangles[i] = [xi, yi, ai, bi]` represents an axis-aligned rectangle. The bottom-left point of the rectangle is `(xi, yi)` and the top-right point of it is `(ai, bi)`.

Return `true` if all the rectangles together form an exact cover of a rectangular region.

**Example 1:**

(Image description: A grid showing 5 rectangles perfectly tiling a larger rectangle bounded by (1,1) and (4,4). The constituent rectangles have corners described by the input.)

Input: rectangles = `[[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4],[2,3,4,4]]`
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region from (1,1) to (4,4).

**Example 2:**

(Image description: Two separate rectangles on a grid, one from (1,1) to (2,3) and another from (3,1) to (4,4). There is a noticeable gap between x=2 and x=3.)

Input: rectangles = `[[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]`
Output: false
Explanation: Because there is a gap between the two rectangular regions.

**Example 3:**

(Image description: Four rectangles on a grid. One large rectangle from (1,1) to (3,3). Another from (3,1) to (4,2). Another from (1,3) to (2,4). A fourth one from (2,2) to (4,4). The area from (2,2) to (3,3) is covered by both the first and fourth rectangles, indicated by hatching.)

Input: rectangles = `[[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]`
Output: false
Explanation: Because two of the rectangles overlap with each other.

**Constraints:**

*   `1 <= rectangles.length <= 2 * 10^4`
*   `rectangles[i].length == 4`
*   `-10^5 <= xi < ai <= 10^5`
*   `-10^5 <= yi < bi <= 10^5` 