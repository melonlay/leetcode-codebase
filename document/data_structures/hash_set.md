# Data Structure: Hash Set

## Abstract Definition

A Hash Set is a data structure that stores a collection of unique elements, using a hash table internally for efficient operations.

It uses a hash function to determine where to store each element, allowing for average constant-time complexity for adding elements, removing elements, and checking for membership.

## Key Concepts

*   **Uniqueness:** Sets only store unique elements. Adding a duplicate element has no effect.
*   **Hashing:** Similar to hash tables/dictionaries, elements must be hashable (immutable).
*   **No Ordering (Typically):** Standard hash sets do not guarantee any specific order of elements (though Python's `set` implementation details might have ordering effects in some versions, it shouldn't be relied upon algorithmically).

## Key Operations & Complexity (Average Case)

*   **`add(element)`:** O(1)
*   **`remove(element)`:** O(1)
*   **`element in set` (Membership Check):** O(1)
*   **`len(set)` (Size):** O(1)

**Worst Case Complexity:** O(N) - Can occur with poor hash functions or extreme collisions.

## Python's `set`

Python's built-in `set` type is an optimized hash set implementation.

## Common Use Cases in Algorithms

*   **Checking for Duplicates:** Quickly determine if an element has been seen before.
*   **Removing Duplicates:** Convert a list to a set and back to a list to get unique elements.
*   **Membership Testing:** Efficiently checking if an item belongs to a collection.
*   **Sliding Window:** Tracking unique elements within the current window (e.g., Longest Substring Without Repeating Characters).
*   **Set Operations:** Performing efficient union, intersection, difference, and symmetric difference between collections.

## Tradeoffs

*   **Time:** Excellent average-case performance for add, remove, contains.
*   **Space:** O(N) where N is the number of unique elements stored.
*   **Order:** Unordered.
*   **Element Type:** Elements must be hashable.

## Related Concepts

*   Hashing Technique: [[../techniques/hashing/hashing.md]]
*   Hash Tables / Dictionaries: [[../data_structures/hash_table_dict.md]]
*   Sets (Mathematical Concept)
*   Collision Resolution 