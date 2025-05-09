# Solution Explanation: 2872. Maximum Number of K-Divisible Components

## Approach

The problem asks us to find the maximum number of connected components we can form by cutting edges in a tree, such that the sum of node values in each component is divisible by `k`.

This problem can be solved using a greedy approach with a Depth First Search (DFS) traversal. The core idea is to perform a post-order traversal (processing children before the parent). For each node `u`, we calculate the sum of values in the component that `u` would form along with its already processed children (those whose edges were not cut).

Let `dfs(u, parent)` be a function that returns the sum of values of the component rooted at `u` (potentially including its descendants if their connecting edges are not cut).
Inside `dfs(u, parent)`:
1.  Initialize `current_component_sum = values[u]`.
2.  For each neighbor `v` of `u` (excluding `parent`):
    a.  Recursively call `child_component_sum = dfs(v, u)`. This `child_component_sum` is the sum of the component that `v` leads.
    b.  If `child_component_sum % k == 0`:
        i.  This means the component led by `v` is a valid k-divisible component on its own.
        ii. We "cut" the edge `(u,v)` and increment a global counter for the number of valid components found this way.
        iii. `child_component_sum` is *not* added to `u`'s `current_component_sum` because it forms a separate, counted component.
    c.  Else (`child_component_sum % k != 0`):
        i.  The component led by `v` is not yet k-divisible by itself. To potentially become part of a k-divisible component, it must merge with `u`.
        ii. `child_component_sum` is added to `u`'s `current_component_sum`.
3.  The function returns `current_component_sum`.

We initialize a global `components_cut_off_count = 0`. The DFS is started from an arbitrary node (e.g., node 0).

A crucial problem constraint is: "Sum of `values` is divisible by `k`."
This implies that the component containing the root of the DFS traversal (after all possible cuts in its subtrees are made) will also have a sum divisible by `k`. This is because the total sum is k-divisible, and all components that were "cut off" are also k-divisible. Therefore, the sum of the remaining part must also be k-divisible.

The total maximum number of components is `components_cut_off_count + 1` (the "+1" accounts for the component containing the DFS root).

This greedy strategy works because making a cut as soon as a k-divisible component is found maximizes the number of components. Not cutting a valid k-divisible component doesn't help create more components later, as it would merely merge a k-divisible sum with an ancestor, and the ancestor's sum would still need to be k-divisible relative to its own ancestors.

## Complexity Analysis

*   **Time Complexity:** O(N), where N is the number of nodes.
    *   Building the adjacency list takes O(N + M) time, where M is the number of edges. For a tree, M = N-1, so it's O(N).
    *   The DFS visits each node and edge once, performing constant time work per node/edge (arithmetic operations, modulo). So, the DFS traversal is O(N + M) = O(N).
    *   Overall: O(N).

*   **Space Complexity:** O(N).
    *   The adjacency list requires O(N + M) = O(N) space.
    *   The recursion stack for DFS can go up to O(H) in depth, where H is the height of the tree. In the worst-case scenario (a path graph), H can be N. So, the recursion stack can take O(N) space.
    *   Overall: O(N).

## Notes on Implementation
- An adjacency list is used to represent the tree.
- The `sys.setrecursionlimit()` might be needed for deep trees in Python, though the LeetCode environment often has a higher default limit. An iterative DFS could also be used to avoid recursion depth issues for very large N. 