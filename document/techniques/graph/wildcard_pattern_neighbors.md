# Wildcard Pattern Preprocessing for Neighbor Finding

**Related Concepts:**
*   [BFS](../../algorithms/graph_search/bfs.md)
*   Graph Traversal
*   Preprocessing

## Technique Description

This technique optimizes finding neighbors in graph problems where nodes are strings (like words) and edges exist between strings differing by a single character (e.g., Word Ladder problem).

Instead of generating all possible single-character transformations for a node during the graph traversal (e.g., BFS), we perform a preprocessing step:

1.  **Pattern Generation:** For each word in the potential node set (e.g., word list + start word), generate all possible "wildcard patterns" by replacing one character at a time with a placeholder (like `*`).
    *   Example: `"hot"` -> `"*ot"`, `"h*t"`, `"ho*"`.
2.  **Pattern Map:** Store these patterns in a hash map (e.g., Python's `defaultdict(list)` or `defaultdict(set)`). The keys are the wildcard patterns, and the values are lists or sets of words that match that pattern.
    *   Example: `patterns["*ot"] = ["hot", "dot", "lot"]`

3.  **Neighbor Lookup During Traversal:** During the graph search (e.g., BFS), when visiting a `current_word`:
    *   Generate the `L` wildcard patterns corresponding to `current_word` (where `L` is the word length).
    *   For each pattern, look up the list/set of matching words in the precomputed `patterns` map.
    *   These retrieved words are the valid neighbors of `current_word`.

## Trade-offs

*   **Pros:** Significantly speeds up neighbor finding during the traversal phase. Instead of O(L*26*L) work per node to generate, create, and check neighbors, it becomes O(L * AvgPatternSize) lookup work.
*   **Cons:** Requires an upfront preprocessing step which has its own time and space cost. Introduces extra space complexity to store the pattern map.

## Complexity

Let `N` be the number of words and `L` be the length of each word.

*   **Preprocessing Time:** O(N * L^2) - Each of the N words requires generating L patterns, and string slicing/hashing takes O(L).
*   **Preprocessing Space:** O(N * L) - In the worst case, each word contributes L pattern entries, and each entry stores the word itself. The total space for the map keys and values is bounded by O(N*L).
*   **Traversal Neighbor Lookup:** O(L * M) per node, where M is the average number of words matching a pattern. This is typically much faster than O(L^2) in practice.

## Use Cases

*   Word Ladder and similar string transformation problems.
*   Any graph problem where edges are defined by small, localized differences between string-based nodes. 