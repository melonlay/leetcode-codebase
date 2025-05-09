# Technique: Greedy DFS for Component Aggregation/Cutting in Trees

**Category:** `techniques/tree/`
**Related Concepts:** [[../../algorithms/graph_search/dfs.md]], [[../../algorithms/greedy/greedy.md]]

## 1. Description

This technique is employed to solve problems on trees that involve partitioning the tree into multiple connected components by selectively "cutting" edges. The objective is typically to maximize or minimize the number of resulting components, or to optimize a certain property related to these components (e.g., each component's sum of node values must be divisible by a given `k`).

The decision to cut an edge is usually made greedily, based on aggregated information from the subtree on one side of the potential cut.

## 2. Core Idea

The strategy revolves around a Depth-First Search (DFS) traversal, with key decisions made in a post-order fashion (i.e., after all children of a node have been processed).

1.  **DFS Function Signature:** The DFS function, say `dfs(u, parent)`, typically returns a value representing an aggregated property of the component currently rooted at `u` (assuming no cut is made between `u` and `parent`). This could be a sum, count, or a more complex state.

2.  **Node Processing (Post-Order Logic):**
    *   Initialize `current_aggregation_value` with the intrinsic value of node `u` (e.g., `values[u]`).
    *   For each child `v` of node `u` (where `v` is not `parent`):
        *   Recursively call `child_aggregation_value = dfs(v, u)`.
        *   **Greedy Decision Point:** Based on `child_aggregation_value`:
            *   **Condition Met (e.g., `child_aggregation_value % k == 0`):** If the component/subtree led by `v` (which resulted in `child_aggregation_value`) satisfies the criteria for being a standalone valid component:
                *   Increment a global counter for valid components formed by such "cuts".
                *   The `child_aggregation_value` is *not* combined with `u`'s `current_aggregation_value` (as `v`'s component is now separate).
            *   **Condition Not Met:** If `child_aggregation_value` alone doesn't form a valid component, it must be merged with `u`'s component to potentially satisfy the condition at a higher level.
                *   Combine `child_aggregation_value` with `u`'s `current_aggregation_value` (e.g., add it to the sum).
    *   Return `current_aggregation_value` (which now represents the aggregated value for the component `u` leads, to be passed to `u`'s parent).

3.  **Global Counter:** A global variable (or a class member) is used to count the number of successful "cuts" made, which corresponds to the number of valid components separated from their parents.

## 3. Handling the Root Component

Many problems utilizing this technique include a global constraint that ensures the final component (the one containing the root of the initial DFS call, after all optimal cuts in its subtrees) will also satisfy the required property. For instance, if the sum of all node values in the entire tree is guaranteed to be divisible by `k`, and all cut-off components are also k-divisible, then the remaining main component must also be k-divisible.

In such cases, the total number of valid components is `(global_counter_for_cuts) + 1`.

## 4. Why the Greedy Approach Often Works

The greedy choice (making a cut as soon as a subtree forms a valid component) is often optimal because:
*   It maximizes the number of components locally.
*   In a tree, cutting an edge `(u,v)` and isolating the component associated with `v`'s subtree does not prevent other cuts from being made elsewhere in the tree. Decisions are largely independent due to the acyclic nature of trees.
*   A formal proof, if required, typically involves an exchange argument: assume an optimal solution differs from the greedy one, then show that the greedy choices can be substituted into the optimal solution without making it worse, eventually transforming it into the greedy solution.

## 5. Example Problem Types

*   Maximizing the number of k-divisible components in a tree (e.g., LeetCode 2872).
*   Counting subtrees that satisfy a specific sum or size criteria.
*   Problems involving partitioning a tree where component properties must be met.

## 6. Complexity

*   **Time Complexity:** O(N) or O(N+M), where N is the number of nodes and M is the number of edges (M=N-1 for a tree). This is due to the single DFS traversal.
*   **Space Complexity:** O(N) for storing the adjacency list and O(H) for the recursion stack, where H is the height of the tree. In the worst case (a skewed tree), H can be N, leading to O(N) space.

## 7. Key Considerations

*   **Traversal Order:** Post-order traversal (processing children before the parent) is crucial for the aggregation logic.
*   **Aggregation Logic:** The specific way values/states are combined (e.g., sum, max, min, boolean conditions) depends on the problem.
*   **Return Value of DFS:** Clearly define what the DFS function should return to its caller (parent node).
*   **Base Cases:** Leaf nodes in the DFS usually return their own value or a base aggregation state.
*   **Global vs. Local Information:** Distinguish between information passed up the tree (local aggregation) and global counters or states. 