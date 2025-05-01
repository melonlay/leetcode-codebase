# String Neighbors via Wildcard Preprocessing

**Applies:** [[../pattern_based_neighbor_finding.md]]

## 1. Problem Context: String Transformations

This technique is commonly applied to problems involving finding paths or relationships between strings (usually words of the same length) where an edge exists between two strings if they differ by exactly one character. A classic example is the Word Ladder problem (LeetCode 127).

## 2. Specific Application of General Technique

This applies the [[../pattern_based_neighbor_finding.md]] technique using single-character wildcards as the intermediate patterns.

1.  **Pattern Generation:** For each word `w` of length `L` in the input word list, generate `L` wildcard patterns by replacing the character at each position `i` (from 0 to `L-1`) with a wildcard character (e.g., `*`).
    *   Example: `w = "hot"` -> Patterns: `"*ot"`, `"h*t"`, `"ho*"`.

2.  **Pattern Mapping:** Store these patterns in a hash map (`pattern_map`). The keys are the wildcard patterns, and the values are lists (or sets) of words from the input list that generate that specific pattern.
    *   `pattern_map["*ot"]` would include `"hot"`, `"dot"`, `"lot"` (if they are in the word list).
    *   `pattern_map["h*t"]` would include `"hot"`, `"hat"`, `"hit"` (if present).

3.  **Neighbor Lookup:** When performing a graph traversal (like BFS starting from `beginWord`) and visiting `current_word`:
    *   Generate the `L` wildcard patterns for `current_word`.
    *   For each pattern, retrieve the list of words from `pattern_map[pattern]`.
    *   These retrieved words are the valid neighbors (words reachable by changing one character).
    *   Care must be taken to handle visited states correctly within the traversal algorithm (e.g., remove words from the map lists once visited or use a separate visited set).

## 3. Complexity

Let `N` be the number of words and `L` be the length of each word.

*   **Preprocessing Time:** O(N * L^2) (Dominated by generating L patterns of length L for N words).
*   **Preprocessing Space:** O(N * L) (To store the `pattern_map`).
*   **Neighbor Lookup (per word during BFS):** O(L * M), where M is the average number of words matching a wildcard pattern. This lookup is typically much faster than generating neighbors on the fly (which would be O(L * AlphabetSize)).

## 4. Example Implementation Notes (Python)

```python
import collections

wordList = ["hot","dot","dog","lot","log","cog"]
L = len(wordList[0])

pattern_map = collections.defaultdict(list)
for word in wordList:
    for i in range(L):
        pattern = word[:i] + "*" + word[i+1:]
        pattern_map[pattern].append(word)

# Example Lookup for neighbors of "hot"
current_word = "hot"
neighbors = []
for i in range(L):
    pattern = current_word[:i] + "*" + current_word[i+1:]
    if pattern in pattern_map:
        for neighbor in pattern_map[pattern]:
            if neighbor != current_word:
                neighbors.append(neighbor)
# Remember to handle visited state in actual BFS
# neighbors might contain duplicates if not using sets
print(f"Neighbors of {current_word}: {list(set(neighbors))}")
# Output: Neighbors of hot: ['dot', 'lot']

```

## 5. Related Concepts

*   [[../pattern_based_neighbor_finding.md]] (General Technique)
*   String Manipulation
*   Word Ladder Problem
*   Breadth-First Search ([../../../algorithms/graph_search/bfs.md](../../../algorithms/graph_search/bfs.md))
*   Hash Maps ([../../../data_structures/hash_table_dict.md](../../../data_structures/hash_table_dict.md)) 