# 2872. Maximum Number of K-Divisible Components

**Hard**

There is an undirected tree with `n` nodes labeled from `0` to `n-1`. You are given the integer `n` and a 2D integer array `edges` of length `n-1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between `a_i` and `b_i` in the tree.

You are also given a 0-indexed integer array `values` of length `n`, where `values[i]` is the value associated with the `i^th` node, and an integer `k`.

A **valid split** of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by `k`, where the **value of a connected component** is the sum of the values of its nodes.

Return the *maximum number of components* in any valid split.

## Example 1:

**Input:** `n = 5`, `edges = [[0,2],[1,2],[1,3],[2,4]]`, `values = [1,8,1,4,4]`, `k = 6`
**Output:** `2`
**Explanation:**
The problem describes a tree structure.
Original tree:
- Node 1 is connected to Node 2 and Node 3.
- Node 2 is connected to Node 1, Node 0, and Node 4.
(Implicitly, Node 0 is connected to Node 2, Node 3 is connected to Node 1, Node 4 is connected to Node 2).

The tree is split by removing the edge between Node 1 and Node 2.
Resulting components:
- Component 1: Consists of Node 1 and Node 3.
- Component 2: Consists of Node 0, Node 2, and Node 4.

We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is `values[1] + values[3] = 8 + 4 = 12`. (12 is divisible by 6)
- The value of the component containing nodes 0, 2, and 4 is `values[0] + values[2] + values[4] = 1 + 1 + 4 = 6`. (6 is divisible by 6)
It can be shown that no other valid split has more than 2 connected components.

## Example 2:

**Input:** `n = 7`, `edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]`, `values = [3,0,6,1,5,2,1]`, `k = 3`
**Output:** `3`
**Explanation:**
Original tree:
- Node 0 is connected to Node 1 and Node 2.
- Node 1 is connected to Node 0, Node 3, and Node 4.
- Node 2 is connected to Node 0, Node 5, and Node 6.
(Implicitly, Node 3 connected to 1, Node 4 to 1, Node 5 to 2, Node 6 to 2).

The tree is split by removing the edge between Node 0 and Node 1, and the edge between Node 0 and Node 2.
Resulting components:
- Component 1: Consists of Node 0.
- Component 2: Consists of Node 1, Node 3, and Node 4.
- Component 3: Consists of Node 2, Node 5, and Node 6.

We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
- The value of the component containing node 0 is `values[0] = 3`. (3 is divisible by 3)
- The value of the component containing nodes 1, 3, and 4 is `values[1] + values[3] + values[4] = 0 + 1 + 5 = 6`. (6 is divisible by 3)
- The value of the component containing nodes 2, 5, and 6 is `values[2] + values[5] + values[6] = 6 + 2 + 1 = 9`. (9 is divisible by 3)
It can be shown that no other valid split has more than 3 connected components.

## Constraints:
*   `1 <= n <= 3 * 10^4`
*   `edges.length == n - 1`
*   `edges[i].length == 2`
*   `0 <= a_i, b_i < n`
*   `values.length == n`
*   `0 <= values[i] <= 10^5`
*   `1 <= k <= 10^9`
*   Sum of `values` is divisible by `k`.
*   The input is generated such that `edges` represents a valid tree. 