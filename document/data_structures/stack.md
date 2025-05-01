# Data Structure: Stack

## Description

A stack is a fundamental linear data structure that follows the **Last-In, First-Out (LIFO)** principle. This means the last element added to the stack is the first element to be removed.

Think of a stack of plates: you add new plates to the top, and you remove plates from the top.

## Core Operations

1.  **Push:** Adds an element to the top of the stack.
    *   Time Complexity: O(1) typically.
2.  **Pop:** Removes and returns the element from the top of the stack. An error or specific value might be returned if the stack is empty.
    *   Time Complexity: O(1) typically.
3.  **Peek (or Top):** Returns the element at the top of the stack without removing it. An error might occur if the stack is empty.
    *   Time Complexity: O(1) typically.
4.  **isEmpty:** Checks if the stack contains any elements.
    *   Time Complexity: O(1) typically.
5.  **Size:** Returns the number of elements currently in the stack.
    *   Time Complexity: O(1) typically.

## Common Implementations

*   **Using Arrays/Lists:** A dynamic array or list can be used. `append` acts as `push`, and `pop` acts as `pop`. Need to handle resizing if using a fixed-size array.
*   **Using Linked Lists:** Each node points to the next node. Push adds a new node at the head, pop removes the head node.

## Use Cases

*   Function call management (call stack).
*   Parsing expressions (e.g., checking balanced parentheses).
*   Undo/Redo functionality.
*   Backtracking algorithms (e.g., DFS).
*   Specific algorithms like finding the next greater element, or as used in the `stack_index_tracking_for_subsequences` pattern.

## Complexity

*   **Access:** O(N) - Only the top element is directly accessible in O(1).
*   **Search:** O(N) - Requires potentially popping elements to find a specific one.
*   **Insertion (Push):** O(1) amortized (for dynamic arrays) or O(1) (for linked lists).
*   **Deletion (Pop):** O(1).
*   **Space:** O(N) - Where N is the maximum number of elements stored.

## Python Implementations

*This section details common ways to implement the Stack ADT using Python built-in types.*

1.  **Using `list`:**
    *   Python's built-in `list` can be used directly as a stack due to its efficient end operations.
    *   `append()` acts as `push` (Amortized O(1)).
    *   `pop()` (without index) acts as `pop` (O(1)).
    *   Accessing the last element `my_list[-1]` acts as `peek` (O(1)).
    *   Checking truthiness (`if my_list:`) checks for non-emptiness (O(1)).
    *   `len(my_list)` provides the size (O(1)).
    *   **Consideration:** While generally efficient for stack operations, `list` is internally a dynamic array. Performance for `push` is amortized O(1) due to potential resizing overhead. It's inefficient (O(n)) for queue operations (insert/delete at the beginning).

2.  **Using `collections.deque` (Double-Ended Queue):**
    *   `deque` is often preferred for pure stack or queue implementations as it guarantees O(1) complexity for appends and pops from *both* ends (implemented as a doubly-linked list).
    *   `append()` acts as `push` (O(1)).
    *   `pop()` acts as `pop` (O(1)).
    *   Accessing the last element `my_deque[-1]` acts as `peek` (O(1)).
    *   Checking truthiness or using `len()` works as with lists (O(1)).
    *   Provides efficient queue operations (`appendleft`, `popleft`) if needed alongside stack operations.

## Patterns Utilizing This

*   `document/patterns/stack_index_tracking_for_subsequences.md`
*   (Implicitly used in iterative DFS algorithms) 