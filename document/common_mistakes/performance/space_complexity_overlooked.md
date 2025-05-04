# Common Mistake: Space Complexity Overlooked

## The Mistake

Focusing solely on optimizing time complexity while neglecting or underestimating the space complexity required by an algorithm or data structure.

## Why It's Wrong

*   **Memory Limit Exceeded (MLE):** Many competitive programming platforms and real-world systems have strict memory limits. An algorithm that is fast but requires excessive memory will fail.
*   **Performance Impact:** Even if not exceeding limits, high memory usage can negatively impact performance due to factors like cache misses and allocation overhead.
*   **Feasibility:** Certain approaches might be theoretically possible time-wise but practically infeasible due to unreasonable memory requirements (e.g., creating a full adjacency matrix for a graph with 10^5 nodes).
*   **Algorithm Choice:** Comparing algorithms often involves a time-space tradeoff. Ignoring space complexity leads to incomplete analysis and potentially choosing a suboptimal approach overall.

## Examples

*   **Binary Lifting vs. Other Structures:** Standard Binary Lifting for LCA or range queries often requires O(N log N) space for the lookup tables. While queries are fast (O(log N) or O(1)), alternative approaches like the DFS-based method in [[../optimizations/graph_shortest_path/path_query_sorted_value_diff_graph.md]] might achieve similar time complexity with only O(N) or O(N+Q) space, making them preferable under memory constraints.
*   **DP State:** Using a DP state like `dp[i][j]` where `j` can be very large might lead to MLE. Techniques like state compression, rolling arrays, or optimizing the state definition might be necessary.
*   **Full Adjacency Matrix:** Storing a dense graph using an O(N^2) adjacency matrix is often infeasible for N > ~2000-5000.
*   **Storing All Subsets/Paths:** Explicitly generating and storing all subsets or paths in exponential problems will quickly exceed memory limits.

## How to Avoid

1.  **Analyze Space Early:** Consider space complexity alongside time complexity during the initial brainstorming (Rule 2a) and strategy selection (Rule 2c).
2.  **Estimate Memory Usage:** Roughly estimate the memory needed based on data structure sizes (e.g., `N * LOG` integers for Binary Lifting tables, `N * M` for a DP table) and variable types (integer size, object overhead).
3.  **Know Data Structure Costs:** Be aware of the typical space complexities of common data structures (Arrays, Lists, Hash Maps, Trees, Graphs, DP tables).
4.  **Look for Tradeoffs:** Explicitly consider time-space tradeoffs when comparing algorithms. Document these in `document/optimizations/`.
5.  **Check Constraints:** Pay attention to memory limits provided by the platform or system.
6.  **Consider Alternatives:** If a chosen approach has high space complexity, actively search for alternative algorithms or data structures with lower memory requirements (e.g., Fenwick Tree vs. Segment Tree for some problems, adjacency list vs. matrix).

## Related Concepts

*   Time Complexity Analysis
*   Space Complexity Analysis
*   Big O Notation
*   Data Structures
*   [[../optimizations/graph_shortest_path/path_query_sorted_value_diff_graph.md]] (Example comparison) 