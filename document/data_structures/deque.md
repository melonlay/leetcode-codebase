# Data Structure: Deque (Double-Ended Queue)

## Abstract Definition

A Deque (pronounced "deck"), or Double-Ended Queue, is a linear data structure that supports element insertion and deletion at both ends (head and tail).

It combines the functionalities of both queues (FIFO - First-In, First-Out) and stacks (LIFO - Last-In, First-Out).

## Key Operations & Complexity (Typical Implementation)

Efficient implementations (like Python's `collections.deque`) provide average constant-time complexity for operations at both ends:

*   **`append(item)`:** Add `item` to the right end (tail). O(1).
*   **`appendleft(item)`:** Add `item` to the left end (head). O(1).
*   **`pop()`:** Remove and return the item from the right end (tail). O(1).
*   **`popleft()`:** Remove and return the item from the left end (head). O(1).
*   **`extend(iterable)`:** Extend the right end by appending elements from `iterable`. O(k) where k is iterable length.
*   **`extendleft(iterable)`:** Extend the left end (note: elements are added in reverse order of the iterable). O(k).
*   **`__getitem__(index)`:** Access element by index. O(N) in general for deque, but O(1) for Python's `collections.deque`.
*   **`__len__()`:** Get the number of items. O(1).
*   **`rotate(n)`:** Rotate the deque n steps to the right (or left if n is negative). O(k) where k is abs(n).

## Python's `collections.deque`

Python's `collections.deque` is a highly optimized implementation based on a doubly-linked list of fixed-size blocks. This allows for O(1) appends and pops from both ends.

## Common Use Cases in Algorithms

*   **Monotonic Queues:** Essential for implementing monotonic queues (see `[[../techniques/sequence/monotonic_queue.md]]`) used in sliding window problems, finding nearest smaller/larger elements, etc.
*   **Breadth-First Search (BFS):** Can be used as the queue in BFS (`append` for enqueue, `popleft` for dequeue).
*   **Storing Recent Items:** Maintaining a list of the last N items seen.
*   **Palindrome Check:** Comparing elements from both ends.
*   **Implementing Queues and Stacks:** Can serve as either, although `list` is often simpler for basic stacks.

## Tradeoffs

*   **Time:** O(1) for appends/pops at both ends.
*   **Space:** O(N) for storing N elements.
*   **Indexing:** While Python's `deque` offers O(1) indexed access, general deque implementations might have O(N) access time. Inserting/deleting in the middle is generally O(N).

## Comparison with `list`

*   `collections.deque`: Optimized for appends/pops from ends (O(1)). Mid-list insertions/deletions are O(N).
*   `list`: Appends/pops from the end are amortized O(1). Insertions/deletions at the beginning or middle are O(N) due to shifting elements.

Choose `deque` when frequent additions/removals from both ends are required.

## Related Concepts

*   [[../data_structures/queue.md]]
*   [[../data_structures/stack.md]]
*   [[../data_structures/linked_list.md]] 