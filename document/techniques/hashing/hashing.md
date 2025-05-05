# Technique: Hashing

**Category:** Techniques (`techniques/hashing/`)

## 1. General Concept

Hashing is a fundamental technique used to map data of arbitrary size (keys or elements) to fixed-size values (hash codes or hashes) using a hash function. These hash codes are then typically used as indices into an array (often called a hash table or bucket array) to enable efficient data storage and retrieval.

The primary goal of hashing in data structures is to achieve average constant-time complexity (O(1)) for operations like insertion, deletion, and search/lookup.

## 2. Key Components

*   **Hash Function:** A function `h(key)` that takes a key as input and computes an integer hash code. A good hash function should:
    *   Be deterministic (same key always produces the same hash).
    *   Be fast to compute.
    *   Distribute keys uniformly across the possible hash codes to minimize collisions.
*   **Hash Table / Bucket Array:** An array where elements are stored. The hash code, typically modulo the array size (`h(key) % array_size`), determines the index (bucket) where the key (or data associated with the key) should be placed.
*   **Collision Resolution Strategy:** Since different keys might map to the same hash code (a collision), a strategy is needed to handle this:
    *   **Separate Chaining:** Each bucket in the hash table points to a secondary data structure (commonly a linked list, sometimes a balanced tree) containing all elements that hashed to that bucket. Operations involve hashing to find the bucket and then searching/inserting within the secondary structure.
    *   **Open Addressing:** If a collision occurs at index `i`, probe for the next available slot in the hash table according to a specific sequence (e.g., linear probing `i+1, i+2,...`, quadratic probing `i+1^2, i+2^2,...`, double hashing). All elements are stored directly within the table.

## 3. Why Hashing Enables O(1) Average Time

With a good hash function distributing keys uniformly and an appropriate collision resolution strategy, the average number of elements per bucket (or the average probe sequence length) remains small and bounded by a constant (related to the load factor - the ratio of elements to table size). Therefore, finding the correct bucket and performing the operation within that bucket (or finding an empty slot) takes O(1) time *on average*.

However, the *worst-case* time complexity can degrade to O(N) if many keys collide into the same bucket or probe sequence.

## 4. Applications in Data Structures

Hashing is the core technique behind several essential data structures:

*   **Hash Tables / Dictionaries:** Store key-value pairs. Hashing is applied to the key to determine storage location. [[../../data_structures/hash_table_dict.md]]
*   **Hash Sets:** Store unique elements. Hashing is applied to the element itself to determine storage location and check for duplicates. [[../../data_structures/hash_set.md]]

## 5. Considerations

*   **Hashable Keys/Elements:** Objects used as keys in hash tables or elements in hash sets must be hashable (i.e., their hash value should not change over their lifetime). In Python, this generally means they must be immutable (e.g., numbers, strings, tuples containing only immutables).
*   **Load Factor:** The ratio of stored elements to the size of the hash table. If the load factor gets too high, collisions increase, and performance degrades. Good implementations resize the hash table automatically when the load factor exceeds a threshold.
*   **Choice of Hash Function:** Crucial for performance. Poor hash functions lead to many collisions.

Understanding the principles of hashing helps in appreciating the performance characteristics and limitations of hash-based data structures like dictionaries and sets. 