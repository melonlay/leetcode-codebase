## Problem Summary

LeetCode 127: Word Ladder asks for the length (number of words) of the shortest transformation sequence from a `beginWord` to an `endWord`. Each step in the sequence involves changing a single letter, and all intermediate words (and the `endWord`) must exist in a provided `wordList`.

## Algorithmic Approach

This problem is solved by finding the shortest path in an unweighted graph where words are nodes and an edge exists between words differing by one letter. **Breadth-First Search (BFS)** is used for shortest path finding.

To optimize neighbor discovery during BFS, a preprocessing step is employed using wildcard patterns.

**Core Algorithm:** [BFS](../../document/algorithms/graph_search/bfs.md)
**Optimization Technique:** [Wildcard Pattern Preprocessing](../../document/techniques/graph/wildcard_pattern_neighbors.md)

### Implementation Details

1.  **Word Set Creation:** Create a `set` (`wordSet`) from the input `wordList` for efficient lookups. Ensure `beginWord` is also added to this set as it's the starting node and needs to be included in pattern generation.
2.  **Edge Case:** If `endWord` is not in the `wordSet`, return 0 immediately.
3.  **Preprocessing (Pattern Map):**
    *   Initialize a `defaultdict(list)` called `patterns`.
    *   Iterate through each `word` in the `wordSet`.
    *   For each `word`, generate all `L` possible wildcard patterns (e.g., `"h*t"`, `"*ot"`, `"ho*"` for `"hot"`).
    *   Append the `word` to the list associated with each generated `pattern` in the `patterns` map.
4.  **BFS Initialization:**
    *   Initialize a `deque` with `(beginWord, 1)` representing (word, level/path length).
    *   Initialize a `visited` set with `beginWord`.
5.  **BFS Loop:**
    *   While the queue is not empty, dequeue `(current_word, level)`.
    *   If `current_word` is `endWord`, return `level`.
    *   **Neighbor Discovery (Optimized):**
        *   Generate the `L` wildcard patterns for `current_word`.
        *   For each `pattern`, look up the list of potential neighbors in the `patterns` map.
        *   For each `neighbor` word found:
            *   If `neighbor` has not been `visited`, add it to `visited` and enqueue `(neighbor, level + 1)`.
6.  **No Path Found:** If the queue becomes empty, return 0.

## Complexity Analysis

Let `N` be the number of words in the combined set (`wordList` + `beginWord`) and `L` be the length of each word.

*   **Time Complexity:** O(N * L^2)
    *   Preprocessing (Pattern Map Creation): O(N * L^2) - Generating L patterns (O(L) each) for N words.
    *   BFS: In the worst case, visits O(N) nodes. For each node, finding neighbors involves generating L patterns (O(L)) and looking them up. The total work looking up neighbors across all nodes is related to the total number of edges E, which can be up to O(N*L*M) where M is avg pattern size. However, the overall complexity is dominated by the O(N * L^2) preprocessing step.
*   **Space Complexity:** O(N * L)
    *   `wordSet`: O(N * L)
    *   `patterns` map: Stores N words across various pattern lists. Can be up to O(N * L) in the worst case.
    *   `visited` set: O(N * L)
    *   `queue`: O(N * L) in the worst case. 