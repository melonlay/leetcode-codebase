## Problem: 126. Word Ladder II

Find all shortest transformation sequences from a `beginWord` to an `endWord` using a `wordList`. Each step in the sequence involves changing one letter, and all intermediate words must exist in the `wordList`.

## Approach: BFS + DFS

This problem requires finding *all* shortest paths in an unweighted graph where words are nodes and edges connect words differing by one letter. A combination of Breadth-First Search (BFS) and Depth-First Search (DFS) is suitable.

1.  **Preprocessing (Neighbor Finding):**
    *   To efficiently find neighbors (words differing by one letter), we use a preprocessing step.
    *   Create a `wordSet` from the `wordList` for O(1) lookup.
    *   Check if `endWord` is in `wordSet`. If not, no path is possible, return `[]`.
    *   Build an `adj_map` (adjacency map) using wildcard patterns. For each word (including `beginWord`), generate patterns by replacing one character with `*` (e.g., `hit` -> `*it`, `h*t`, `hi*`). Store a mapping from each pattern to the list of words matching it.
    *   This map allows finding all one-letter-different neighbors of a word quickly by looking up its wildcard patterns in the map. This is potentially more efficient than comparing the word against every other word in the list, especially for larger lists.
    *   This technique can be found documented conceptually in `document/techniques/graph_preprocessing_wildcard.md` (if it existed).

2.  **BFS (Shortest Distance & Parent Tracking):**
    *   Perform a BFS starting from `beginWord` to find the shortest distance to all reachable words.
    *   Use a `distances` dictionary to store the minimum distance found so far from `beginWord` to each word.
    *   Use a `parents` dictionary (`defaultdict(set)`) to store all possible immediate predecessors for each word *on a shortest path*. `parents[word]` contains a set of words from which `word` can be reached via a shortest path.
    *   Use a queue for the BFS. Process the graph level by level to ensure that we prioritize shorter paths.
    *   When exploring neighbors of a `current_word` at `current_dist`:
        *   If a `neighbor` is reached for the first time (`neighbor not in distances`), record its distance (`current_dist + 1`), add `current_word` to its parents (`parents[neighbor].add(current_word)`), and enqueue it.
        *   If a `neighbor` is reached again, but via a path of the *same* shortest length (`distances[neighbor] == current_dist + 1`), it represents an alternative shortest path. Add `current_word` to its parents (`parents[neighbor].add(current_word)`). Do not re-enqueue if it was already processed at this level.
        *   If a `neighbor` is reached via a longer path (`distances[neighbor] < current_dist + 1`), ignore it.
    *   **Crucial Optimization:** To ensure only shortest paths are constructed, once a node is visited and added to the queue at a certain level, remove it from the main `wordSet`. This prevents it from being considered as a neighbor for paths originating from later levels (which would necessarily be longer paths).
    *   Stop the BFS once the level containing the `endWord` has been fully processed.
    *   This modified BFS ensures we build the `parents` map containing only predecessors that contribute to *shortest* paths. The general BFS algorithm details can be found in `document/algorithms/graph/breadth_first_search.md` (if it existed).

3.  **DFS (Path Reconstruction):**
    *   If the `endWord` was never reached (check if `found` flag is true or `endWord` is in `parents`), return `[]`.
    *   Perform a DFS starting from `endWord` and backtracking using the `parents` map.
    *   The DFS function recursively explores parents: `dfs(word, current_path)`.
    *   When the DFS reaches `beginWord`, a complete shortest path has been found. Reverse `current_path` and add it to the `results`.
    *   The combination of BFS for levels/parents and DFS for reconstruction is a common pattern documented conceptually in `document/patterns/bfs_dfs_all_shortest_paths.md` (if it existed).

## Complexity Analysis

Let `N` be the number of words in `wordList` and `L` be the length of the words.

*   **Time Complexity:**
    *   Preprocessing (Adjacency Map): `O(N * L)` - Generating patterns and adding to map.
    *   BFS: `O(N * L)` - In the worst case, each word is visited. Finding neighbors using the map takes `O(L)` for pattern generation and map lookup per word. Total edges considered relates to `N * L`.
    *   DFS: `O(P * L)` where `P` is the number of shortest paths. In the worst case, `P` can be exponential, but given the constraints, it's often manageable. The overall complexity is dominated by the BFS and DFS path reconstruction. Total: Roughly `O(N*L + P*L)`.
*   **Space Complexity:**
    *   `wordSet`: `O(N * L)`
    *   `adj_map`: `O(N * L)`
    *   `distances`: `O(N * L)`
    *   `parents`: `O(N * L)` in the worst case if many words have many parents on shortest paths.
    *   `queue`: `O(N * L)`
    *   DFS recursion stack and `results`: `O(P * L)`
    *   Overall: `O(N * L + P * L)` 