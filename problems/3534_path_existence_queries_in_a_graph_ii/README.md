# 3534. Path Existence Queries in a Graph II

**Hard**

**Topics:** Array, Graph, Union Find, Sorting

You are given an integer `n` representing the number of nodes in a graph, labeled from `0` to `n - 1`.

You are also given an integer array `nums` of length `n` and an integer `maxDiff`.

An **undirected** edge exists between nodes `i` and `j` if the **absolute difference** between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each query `[u, v]`, find the **minimum** distance between nodes `u` and `v`. If no path exists between the two nodes, return `-1` for that query.

Return an array `answer`, where `answer[i]` is the result of the `i`th query.

**Note:** The edges between the nodes are unweighted.

**Example 1:**

**Input:** `n = 5`, `nums = [1, 8, 3, 4, 2]`, `maxDiff = 3`, `queries = [[0, 3], [2, 4]]`
**Output:** `[1, 1]`

**Explanation:**
The resulting graph is:
```
   1(8)
   / \
  /   \
0(1)--2(3)--4(2)
 \   /
  \ /
   3(4)
```
(Node values in parentheses)
Edges:
- |1 - 8| = 7 > 3
- |1 - 3| = 2 <= 3 -> Edge (0, 2)
- |1 - 4| = 3 <= 3 -> Edge (0, 3)
- |1 - 2| = 1 <= 3 -> Edge (0, 4)
- |8 - 3| = 5 > 3
- |8 - 4| = 4 > 3
- |8 - 2| = 6 > 3
- |3 - 4| = 1 <= 3 -> Edge (2, 3)
- |3 - 2| = 1 <= 3 -> Edge (2, 4)
- |4 - 2| = 2 <= 3 -> Edge (3, 4)

Graph Edges: (0,2), (0,3), (0,4), (2,3), (2,4), (3,4)

Query [0, 3]: Shortest Path 0 -> 3. Minimum Distance = 1.
Query [2, 4]: Shortest Path 2 -> 4. Minimum Distance = 1.
Thus, the output is `[1, 1]`.

**Example 2:**

**Input:** `n = 5`, `nums = [5, 3, 1, 9, 10]`, `maxDiff = 2`, `queries = [[0, 1], [0, 2], [2, 3], [4, 3]]`
**Output:** `[1, 2, -1, 1]`

**Explanation:**
The resulting graph is:
```
0(5) -- 1(3) -- 2(1)      3(9) -- 4(10)
```
(Node values in parentheses)
Edges:
- |5 - 3| = 2 <= 2 -> Edge (0, 1)
- |5 - 1| = 4 > 2
- |5 - 9| = 4 > 2
- |5 - 10|= 5 > 2
- |3 - 1| = 2 <= 2 -> Edge (1, 2)
- |3 - 9| = 6 > 2
- |3 - 10|= 7 > 2
- |1 - 9| = 8 > 2
- |1 - 10|= 9 > 2
- |9 - 10|= 1 <= 2 -> Edge (3, 4)

Graph Edges: (0,1), (1,2), (3,4)

Query [0, 1]: Shortest Path 0 -> 1. Minimum Distance = 1.
Query [0, 2]: Shortest Path 0 -> 1 -> 2. Minimum Distance = 2.
Query [2, 3]: No path exists. Minimum Distance = -1.
Query [4, 3]: Shortest Path 4 -> 3. Minimum Distance = 1.
Thus, the output is `[1, 2, -1, 1]`.

**Example 3:**

**Input:** `n = 3`, `nums = [3, 6, 1]`, `maxDiff = 1`, `queries = [[0, 0], [0, 1], [1, 2]]`
**Output:** `[0, -1, -1]`

**Explanation:**
There are no edges between any two nodes because:
- Nodes 0 and 1: `|nums[0] - nums[1]| = |3 - 6| = 3 > 1`
- Nodes 0 and 2: `|nums[0] - nums[2]| = |3 - 1| = 2 > 1`
- Nodes 1 and 2: `|nums[1] - nums[2]| = |6 - 1| = 5 > 1`
Thus, no node can reach any other node, and the output is `[0, -1, -1]`. (Query [0,0] distance is 0).

**Constraints:**

*   `1 <= n == nums.length <= 10^5`
*   `0 <= nums[i] <= 10^5`
*   `0 <= maxDiff <= 10^5`
*   `1 <= queries.length <= 10^5`
*   `queries[i] == [ui, vi]`
*   `0 <= ui, vi < n` 