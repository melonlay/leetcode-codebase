# Data Structure: Hash Table (Python Dictionary)

## Description

A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index (a "bucket") into an array of buckets or slots, from which the desired value can be found.

In Python, the built-in `dict` type is a highly optimized hash table implementation.

## Core Operations & Complexity (Python `dict`)

*   **Insertion `d[key] = value`:** Average: O(1), Worst: O(n) (due to potential resizing or hash collisions)
*   **Deletion `del d[key]`:** Average: O(1), Worst: O(n)
*   **Lookup `d[key]` or `key in d`:** Average: O(1), Worst: O(n)
*   **Iteration `for key in d:`:** O(n), where n is the number of items in the dictionary.

*(Note: The average case assumes a reasonably good hash function and load factor. The O(n) worst case is rare in practice for Python's `dict` but theoretically possible.)*

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

*   `document/patterns/hash_map_lookup.md`
*   `document/patterns/sliding_window.md` (often used for tracking window contents/frequencies) 