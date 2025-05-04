# Common Mistake: Rigid Algorithm Application

## The Mistake

Applying a standard algorithm or technique template rigidly based on recognizing keywords or superficial problem features, without deeply considering if the problem's specific constraints or structure require a non-standard adaptation or a completely different approach.

## Why It's Wrong

*   **Incorrect Results:** The standard template might not be suitable for the specific graph structure, constraints, or objective function, leading to wrong answers (WA).
*   **Inefficiency:** A standard approach might be correct but inefficient (TLE) for the given constraints if a specialized adaptation exists.
*   **Missed Opportunities:** Sticking rigidly to the first recognized pattern can prevent the discovery of simpler, more elegant, or more efficient solutions tailored to the problem.
*   **Getting Stuck:** Trying to force-fit an inappropriate template can lead to complex, buggy code and make debugging difficult.

## Examples

*   **Shortest Path on Special Graphs:** Seeing "shortest path" and immediately implementing standard BFS or Dijkstra without analyzing the graph structure. For graphs implicitly defined by sorted value differences (like LeetCode 3534), specialized techniques like [[../techniques/binary_lifting/binary_lifting_min_steps_on_ranges.md]] or [[../techniques/graph_traversal/dfs_leftmost_pointer_tree_path_query.md]] are needed, as standard BFS is too slow.
*   **Binary Lifting for Non-Tree Structures:** Recognizing the need for `k`-th step calculations and applying standard tree-based Binary Lifting (LCA/k-th ancestor) when the underlying structure isn't a tree or requires lifting on different properties (like reachability ranges).
*   **Greedy Algorithms:** Applying a standard greedy choice (e.g., always take the smallest/largest) without proving its optimality for the specific constraints, potentially failing on edge cases.
*   **DP Transitions:** Using a standard DP state transition without verifying it correctly handles all edge cases or constraints of the current problem.

## How to Avoid

1.  **Deep Problem Understanding:** Fully analyze the inputs, outputs, constraints (especially edge cases and scale), and the exact objective. Don't just match keywords.
2.  **Analyze Structure:** Investigate the specific properties of the data structures or implicit graphs involved. How do constraints affect connectivity or relationships? (e.g., How does sorting + `maxDiff` affect the graph?)
3.  **Question Templates (Rule 2a):** During brainstorming, explicitly ask: "Does this standard algorithm *truly* fit, or does the problem have special properties requiring adaptation?" Consider [[../rules/python-leetcode.mdc#rule-2a-beyond-templates | adaptations]].
4.  **Validate Assumptions (Rule 2f):** If using a standard algorithm, be explicit about the assumptions being made (e.g., "assuming BFS finds shortest paths here because edges are unweighted and this *is* the relevant graph"). If failures occur, re-evaluate these assumptions first.
5.  **Consider Alternatives:** Actively brainstorm multiple approaches, including potentially non-standard ones, before committing.
6.  **KB Search for Patterns/Techniques:** Search the KB not just for standard algorithms (`BFS`, `LCA`) but also for problem *patterns* (`sorted value difference graph`, `implicit graph path query`) or specialized *techniques* that might be relevant.
7.  **Fundamental Rethink (Rule 2f):** If a standard approach fails repeatedly, perform a fundamental rethink, explicitly questioning the suitability of the standard algorithm for the specific problem structure.

## Related Concepts

*   Algorithm Design Paradigms (Greedy, DP, D&C, etc.)
*   Graph Theory
*   Implicit Data Structures
*   [[../rules/python-leetcode.mdc]] (Specifically Rules 2a, 2f, 4d) 