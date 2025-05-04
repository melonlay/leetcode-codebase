# LeetCode 127: Word Ladder - Solution Explanation

## Problem Summary

Given a `beginWord`, an `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that only one letter can be changed at a time, and each transformed word must exist in the `wordList`. Return 0 if no such sequence exists.

## Algorithmic Approach: BFS with Preprocessed Neighbors

This problem can be modeled as finding the shortest path in an implicit graph where words are nodes and an edge exists between two words if they differ by a single letter. **Breadth-First Search (BFS)** is the standard algorithm for finding shortest paths in unweighted graphs.

To avoid iterating through the entire `wordList` to find neighbors for each word during the BFS (which would be slow), this solution uses a preprocessing step based on wildcard patterns to efficiently find neighbors.

## Logic Explanation

1.  **Preprocessing (Neighbor Finding Optimization):**
    *   Create a `wordSet` from `wordList` for O(1) lookups.
    *   Check if `endWord` is in `wordSet`. If not, return 0.
    *   Add `beginWord` to `wordSet` to include it in pattern generation.
    *   Create a `patterns` map (`defaultdict(list)`).
    *   For each `word` in `wordSet`, generate all `L` possible wildcard patterns (e.g., `h*t`, `*ot`, `ho*` for `hot`).
    *   Store each `word` in the list associated with its generated patterns: `patterns[pattern].append(word)`.
    *   This step is detailed in `[[../document/techniques/pattern_based_neighbor_finding/string/string_wildcard_neighbors.md]]`.
2.  **BFS Initialization:**
    *   Create a `queue` (`collections.deque`) and add the starting state `(beginWord, 1)`, representing (word, sequence length).
    *   Create a `visited` set and add `beginWord`.
3.  **BFS Traversal:**
    *   While the `queue` is not empty:
        *   Dequeue `current_word, level`.
        *   If `current_word == endWord`, return `level` (shortest path found).
        *   **Find Neighbors via Patterns:**
            *   Generate the `L` wildcard patterns for `current_word`.
            *   For each `pattern`, look up the list of potential `neighbor` words in `patterns[pattern]`.
            *   For each `neighbor`:
                *   If `neighbor` has not been `visited`:
                    *   Mark `neighbor` as `visited`.
                    *   Enqueue `(neighbor, level + 1)`.
4.  **No Path:** If the queue becomes empty and `endWord` was not reached, return 0.

## Knowledge Base References

*   **Core Algorithm:** [[../document/algorithms/graph_search/bfs.md]] (Explains the BFS algorithm for shortest paths).
*   **Neighbor Finding Technique:** [[../document/techniques/pattern_based_neighbor_finding/string/string_wildcard_neighbors.md]] (Details the wildcard preprocessing optimization used here).
*   **General Preprocessing Pattern:** [[../document/techniques/pattern_based_neighbor_finding/pattern_based_neighbor_finding.md]]
*   **Data Structures:**
    *   [[../document/data_structures/hash_table_dict.md]] (for `defaultdict` and `set`)
    *   [[../document/data_structures/queue.md]] (conceptual basis for `deque`)
    *   [[../document/data_structures/deque.md]] (for `collections.deque`)

## Complexity Analysis

Let `N` be the number of words in the list and `L` be the length of each word.
*   **Time Complexity:** O(N * L^2). Preprocessing takes O(N * L^2) to generate patterns. BFS visits each word/pattern combination at most once. Finding neighbors involves generating L patterns and iterating through matches, contributing to the overall complexity.
*   **Space Complexity:** O(N * L). Storing the `patterns` map requires O(N * L) space. The `queue` and `visited` set require up to O(N) space. 