# Technique: Pattern-Based Neighbor Finding via Preprocessing

## 1. Abstract Technique Description

This technique optimizes the process of finding "neighbors" for items in a collection, where neighbors are defined by sharing certain structural similarities or differing in a limited, predefined way. Instead of calculating potential neighbors for each item on-the-fly during a larger algorithm (like graph traversal), it uses a preprocessing step to group items based on intermediate "patterns".

The core mechanism is:

1.  **Pattern Generation:** For each item in the collection, generate a set of intermediate patterns that capture the item's characteristics relevant to the neighborhood definition.
2.  **Pattern Mapping:** Create a map (e.g., a hash map/dictionary) where keys are the generated patterns and values are collections (lists, sets) of the original items that map to that pattern.
3.  **Neighbor Lookup:** During the main algorithm, to find neighbors of a given `current_item`:
    *   Generate the patterns for `current_item`.
    *   For each pattern, look up the collection of items associated with that pattern in the precomputed map.
    *   The union of these collections (excluding `current_item` itself) represents the potential neighbors.

This shifts the computational cost of neighbor identification from the main algorithm's execution phase to an upfront preprocessing phase.

## 2. Applicability

This technique is beneficial when:

*   Finding neighbors on-the-fly is computationally expensive (e.g., involves many checks or transformations).
*   The definition of a "neighbor" can be effectively captured by shared intermediate patterns.
*   An upfront preprocessing cost (time and space) is acceptable to speed up the main algorithm's neighbor-finding steps.
*   The number of distinct patterns is manageable relative to the cost of on-the-fly neighbor generation.

## 3. General Trade-offs

*   **Pros:** Can significantly reduce the time complexity of neighbor finding within the main algorithm loop (e.g., BFS, DFS).
*   **Cons:** Requires preprocessing time and additional space to store the pattern map.

## 4. Implementation Considerations

*   **Pattern Definition:** The effectiveness hinges on defining patterns that accurately capture the neighborhood relationship and are efficient to generate and store.
*   **Map Structure:** Using `defaultdict(list)` or `defaultdict(set)` in Python is common for building the pattern map.
*   **Handling Self-Loops:** Ensure the lookup process correctly excludes the item itself from its list of neighbors if required.

## 5. Specific Application Examples

*   **String Neighbors (Single Character Difference):** See [[string/string_wildcard_neighbors.md]].
*   **(Potential) Tuple/Vector Neighbors:** Neighbors differ in one position.
*   **(Potential) Bitmask Neighbors:** Neighbors differ by a single bit flip.

## 6. Related Concepts

*   Preprocessing
*   Hashing
*   Hash Maps ([../../data_structures/hash_table_dict.md](../../data_structures/hash_table_dict.md))
*   Graph Traversal Algorithms (as a common application context, e.g., [../../algorithms/graph_search/bfs.md](../../algorithms/graph_search/bfs.md)) 