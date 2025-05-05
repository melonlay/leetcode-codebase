# Data Structures - Overview

**Category:** Data Structures (`data_structures/`)

## 1. General Concept

Data structures are fundamental tools in computer science and algorithmic problem-solving. They provide systematic ways to organize, manage, and store data to enable efficient access and modification.

Choosing the right data structure is often critical for designing efficient algorithms. The choice depends on the specific operations required (e.g., searching, insertion, deletion, finding min/max, range queries) and the performance constraints (time and space complexity).

## 2. Abstract Data Types (ADTs) vs. Implementations

*   **ADT:** Defines a logical description of a data type, focusing on the operations it supports and their expected behavior (e.g., a Stack supports Push, Pop, Peek). ADTs hide implementation details.
*   **Concrete Implementation:** Provides the actual mechanism for storing data and implementing the ADT's operations (e.g., a Stack can be implemented using an array or a linked list).

Understanding both the abstract properties and the trade-offs of different implementations is key.

## 3. Common Data Structures in LeetCode

Below are links to specific data structure documents available in this KB. This list covers structures frequently encountered in LeetCode problems.

*   **Linear Structures:**
    *   Arrays / Lists (Built-in Python `list`)
    *   Linked Lists: [[./linked_list.md]]
    *   Stacks (LIFO): [[./stack.md]] (Often implemented using lists)
    *   Queues (FIFO): [[./queue.md]] (Often implemented using `collections.deque`)
*   **Associative Structures:**
    *   Hash Tables / Dictionaries: [[./hash_table_dict.md]] (Built-in Python `dict`)
    *   Sets (Built-in Python `set`)
*   **Hierarchical Structures / Trees:**
    *   Binary Trees, Binary Search Trees (BSTs)
    *   Heaps / Priority Queues: [[./heap_priority_queue.md]] (Python `heapq` module)
    *   Segment Trees: [[./segment_tree.md]] (Efficient range queries/updates)
    *   *(Other tree types like Tries, Fenwick Trees/BITs may appear)*
*   **Set Structures:**
    *   Disjoint Set Union (DSU) / Union-Find: [[./disjoint_set_union.md]] (Efficiently manages partitions of a set)
*   **Advanced Structures:**
    *   Fibonacci Heaps: [[./fibonacci_heap.md]] (Specific heap variant with good amortized complexities, less common in standard problems)

## 4. Choosing a Data Structure

Consider:
*   **Operations Needed:** What are the primary actions you need to perform on the data?
*   **Frequency of Operations:** Are reads more common than writes? Are range queries needed?
*   **Time Complexity:** What are the required time limits for each operation?
*   **Space Complexity:** How much memory can the structure consume?
*   **Data Characteristics:** Is the data ordered? Are there duplicates?

For example:
*   Need fast lookups by key? -> Hash Table (`dict`).
*   Need fast min/max extraction? -> Heap (`heapq`).
*   Need efficient range sums/updates? -> Segment Tree or Fenwick Tree.
*   Need to manage connected components? -> DSU.
*   Need ordered elements with fast insertion/deletion? -> Balanced BST (less common to implement from scratch) or potentially SortedList (requires external library usually).

Refer to the individual data structure documents for detailed operational complexities and use cases. 