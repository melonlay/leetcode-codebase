# Queue Data Structure

**Related Concepts:**
*   Abstract Data Type (ADT)
*   FIFO (First-In, First-Out)
*   [Breadth-First Search (BFS)](../algorithms/graph_search/bfs.md)
*   Level Order Traversal

## Abstract Definition

A Queue is a linear data structure that follows the **First-In, First-Out (FIFO)** principle. This means the first element added to the queue will be the first one to be removed.

Think of it like a queue of people waiting in line: the person who arrived first is the first one served.

## Core Operations

*   **Enqueue:** Adds an element to the rear (end) of the queue.
*   **Dequeue:** Removes and returns the element from the front (head) of the queue.
*   **Peek/Front:** Returns the element at the front of the queue without removing it.
*   **IsEmpty:** Checks if the queue contains any elements.
*   **Size:** Returns the number of elements currently in the queue.

## Common Implementations

*   **Using Dynamic Arrays/Lists:** Simple to implement, but dequeue operations can be inefficient (O(n)) if elements need to be shifted after removing the front element. Enqueue (append) is typically O(1) amortized.
*   **Using Linked Lists:** Both enqueue (adding to tail) and dequeue (removing from head) can be O(1).
*   **Using `collections.deque` (Python):** This is the recommended implementation in Python. `deque` (double-ended queue) is implemented as a doubly-linked list, providing efficient O(1) time complexity for both appending (enqueue) and popping from the left (dequeue).

## Complexity (using `collections.deque`)

*   **Enqueue (append):** O(1)
*   **Dequeue (popleft):** O(1)
*   **Peek (access `queue[0]`):** O(1)
*   **Space Complexity:** O(N), where N is the number of elements in the queue.

## Use Cases

*   BFS graph traversal.
*   Level order traversal in trees.
*   Task scheduling (where tasks are processed in the order they arrive).
*   Handling requests in servers.
*   Buffering data (e.g., keyboard buffer). 