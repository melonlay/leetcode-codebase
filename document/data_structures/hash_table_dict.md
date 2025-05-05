# Data Structure: Hash Table / Dictionary

## Abstract Definition

A Hash Table, often implemented as a Dictionary or Hash Map in programming languages, is a data structure that maps keys to values.

It uses a hash function to compute an index (or "bucket") into an array of buckets or slots, from which the desired value can be found. The goal is to provide, on average, constant-time O(1) lookups, insertions, and deletions.

## Key Concepts

*   **Hash Function:** Maps keys (e.g., strings, numbers) to array indices (integers). A good hash function distributes keys uniformly across the available indices.
*   **Buckets/Slots:** The array locations where values (or pointers to values/linked lists of values) are stored.
*   **Collisions:** Occur when the hash function generates the same index for two or more different keys. Collision resolution strategies are needed.

## Collision Resolution

1.  **Separate Chaining:** Each bucket stores a pointer to another data structure (commonly a linked list, sometimes a balanced tree) that holds all key-value pairs hashing to that bucket. Lookups involve hashing to find the bucket and then searching the secondary structure.
2.  **Open Addressing:** All key-value pairs are stored directly within the bucket array itself. When a collision occurs, the algorithm probes for the next available slot according to a defined sequence (e.g., linear probing, quadratic probing, double hashing).

## Key Operations & Complexity (Average Case)

*   **`insert(key, value)` / `map[key] = value`:** O(1)
*   **`search(key)` / `map[key]` / `key in map`:** O(1)
*   **`delete(key)` / `del map[key]`:** O(1)

**Worst Case Complexity:** O(n) - Can occur with very poor hash functions or extreme collisions, degrading performance to that of searching a linked list.

## Python's `dict`

Python's built-in `dict` type is a highly optimized hash table implementation. It uses a combination of techniques, including open addressing with pseudo-random probing. Since Python 3.7 (and CPython 3.6), dictionaries also preserve insertion order.

## Common Use Cases in Algorithms

*   **Frequency Counting:** Storing counts of elements in an array or string. `key = element`, `value = count`.
*   **Two Sum Problem:** Store `(number, index)` pairs. For each `num`, check if `target - num` exists in the map.
*   **Caching/Memoization:** Store results of expensive computations (`key = function arguments`, `value = result`) to avoid redundant calculations, particularly in dynamic programming or recursion.
*   **Finding Duplicates:** Insert elements into a hash set (a hash map where only keys matter). If insertion fails or element is already present, it's a duplicate.
*   **Grouping/Categorization:** Grouping elements based on some property (e.g., grouping anagrams where `key = sorted string`, `value = list of anagrams`).
*   **Graph Representation:** Adjacency List: `key = node`, `value = list of neighbors`.
*   **Fast Lookups:** Replacing linear searches (O(n)) with hash table lookups (average O(1)) when checking for presence or retrieving associated data.

## Tradeoffs

*   **Time:** Excellent average-case performance.
*   **Space:** O(k) where k is the number of stored keys. Can require significant memory.
*   **Order:** Not guaranteed in general hash tables (though Python `dict` maintains it since 3.7).
*   **Key Type:** Keys must be hashable (immutable).
*   **Worst Case:** Performance can degrade with bad hashing/collisions.

## Related Concepts

*   Hashing Technique: [[../techniques/hashing/hashing.md]]
*   Key-Value Stores
*   Associative Arrays
*   Hash Sets: [[../data_structures/hash_set.md]] (Uses similar principles)
*   Load Factor & Resizing

## Usage Context

Hash tables (dictionaries) are ideal when:

*   You need fast average-time lookups, insertions, and deletions based on a key.
*   You want to map unique keys to associated values.
*   You need to count frequencies of items.
*   Implementing caches (memoization).

## Python Implementation (`dict`)

*   Keys must be hashable (immutable types like numbers, strings, tuples containing only hashable types).
*   Order: As of Python 3.7+, dictionaries preserve insertion order. Before that, they were unordered.
*   `collections.Counter` is a subclass of `dict` specifically designed for counting hashable objects.

## Patterns Utilizing This

*   [[../techniques/lookup/hash_map_complement_lookup.md]] (e.g., Two Sum problem)
*   [[../patterns/sliding_window.md]] (often used for tracking window contents/frequencies) 