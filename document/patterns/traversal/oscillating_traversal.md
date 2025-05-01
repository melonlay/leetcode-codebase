# Pattern: Oscillating / Zigzag / Spiral Traversal

## Description

This pattern refers to traversing a data structure, typically a 2D matrix (grid) or a tree (like a Binary Tree), in a manner that changes direction at each level or step, creating a back-and-forth or spiral movement.

## Common Variants

1.  **Zigzag Level Order Traversal (Binary Tree):**
    *   **Goal:** Traverse a binary tree level by level, but alternate the direction of traversal for each level (left-to-right, then right-to-left, then left-to-right, etc.).
    *   **Implementation:** Often uses Breadth-First Search (BFS) with a queue. A level counter or flag determines the direction for adding children to the queue or for processing/appending nodes to the result for the current level.
        *   One common method uses a single queue and reverses the sublist for odd/even levels before adding it to the final result.
        *   Another method uses two stacks, processing one stack (left-to-right) and adding children to the second stack (right-to-left), then swapping stacks for the next level.
        *   A deque (double-ended queue) can also efficiently simulate the alternating push/pop directions.
    *   **Example:** LeetCode 103: Binary Tree Zigzag Level Order Traversal.

2.  **Spiral Matrix Traversal:**
    *   **Goal:** Traverse an `m x n` matrix in a clockwise (or counter-clockwise) spiral pattern, starting from the top-left corner and moving inwards.
    *   **Implementation:** Typically uses four boundary pointers: `top`, `bottom`, `left`, `right`.
        1. Traverse right along the `top` row (from `left` to `right`). Increment `top`.
        2. Traverse down along the `right` column (from `top` to `bottom`). Decrement `right`.
        3. Traverse left along the `bottom` row (from `right` to `left`). Decrement `bottom`.
        4. Traverse up along the `left` column (from `bottom` to `top`). Increment `left`.
        5. Repeat steps 1-4, adjusting boundaries until `left > right` or `top > bottom`.
        *   Care must be taken with boundary conditions, especially for non-square matrices or single rows/columns, to avoid duplicate traversal.
    *   **Example:** LeetCode 54: Spiral Matrix, LeetCode 59: Spiral Matrix II (Generating).

3.  **Diagonal Traversal (Zigzag - Matrix):**
    *   **Goal:** Traverse a matrix along diagonals, often alternating direction (up-right then down-left).
    *   **Implementation:** Can be complex. One way involves grouping elements by the sum of their indices (`r + c`). Iterate through diagonal sums (`d` from 0 to `m+n-2`). For each `d`, determine the starting cell and direction. Traverse the diagonal. Even-summed diagonals might go up-right, odd-summed diagonals down-left (or vice-versa).
    *   **Example:** LeetCode 498: Diagonal Traverse.

## When to Use

*   Problems explicitly asking for zigzag, spiral, or diagonal traversal patterns.
*   When the processing logic requires visiting elements in these specific non-linear orders.

## Characteristics

*   **Traversal Order:** The defining feature is the non-standard, direction-changing traversal order.
*   **Implementation:** Often involves managing boundary pointers (matrix spiral) or using queues/stacks/deques with level-based direction logic (tree zigzag).
*   **Complexity:** Typically O(N) where N is the total number of elements (nodes in tree, cells in matrix), as each element is visited once. Space complexity depends on the structure and method (O(width) for BFS queue/stack in trees, O(1) auxiliary for matrix spiral pointers, O(N) if storing result).

## Key Considerations

*   **Boundary Conditions:** Crucial for matrix traversals (spiral, diagonal) to handle edges, single rows/columns, and prevent infinite loops or missed elements.
*   **Direction Logic:** Implementing the direction changes correctly (level flags, swapping stacks, pointer updates) is key.
*   **Data Structure Choice:** Queues, stacks, or deques can simplify tree zigzag traversals.

## Related Concepts

*   Breadth-First Search (BFS)
*   Depth-First Search (DFS) (Less common for level-based zigzag)
*   Matrix/Grid Traversal
*   Binary Tree Traversal
*   [Data Structure: Queue](../../data_structures/queue.md)
*   [Data Structure: Stack](../../data_structures/stack.md)
*   [Data Structure: Deque] (*Assumed link*) 