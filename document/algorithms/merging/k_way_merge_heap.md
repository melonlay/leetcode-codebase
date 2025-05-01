# K-Way Merge using Min-Heap

**General Description**

This pattern addresses the problem of merging `k` sorted input sequences (like arrays, lists, or streams) into a single sorted output sequence. It's an extension of the two-way merge used in algorithms like Merge Sort.

**Core Algorithm/Mechanism**

1.  **Data Structure:** A min-heap (priority queue) is used, typically storing elements from the `k` input sequences.
2.  **Initialization:** The first element from each non-empty input sequence is added to the min-heap.
3.  **Iteration:**
    *   Extract the minimum element from the heap. This is the next element in the overall sorted sequence.
    *   Add the extracted element to the result sequence.
    *   If the sequence from which the minimum element came has more elements, add the next element from that sequence into the heap.
4.  **Termination:** Repeat the iteration step until the heap is empty.

**Handling Non-Comparable Items / Stability:**

Python's `heapq` requires elements to be comparable. If storing objects (like custom class instances) or if stable sorting (preserving relative order of equal elements) is needed:
*   Store tuples in the heap: `(primary_key, secondary_key, item)`.
*   `primary_key`: The main value used for sorting (e.g., `node.val`).
*   `secondary_key`: A unique, monotonically increasing counter or index. This acts as a tie-breaker when primary keys are equal, ensuring heap operations don't try to compare the `item` itself.
*   `item`: The actual object or data to be processed.

**Example Application(s)**

*   **LeetCode 23: Merge k Sorted Lists:**
    *   Input: `k` sorted linked lists.
    *   Heap stores: `(node.val, index, node)` for the current node from each list.
    *   When a node is popped, its `next` node is added to the heap.

```python
# Simplified Snippet (LeetCode 23 context)
import heapq

# Assuming ListNode definition exists

def mergeKLists(lists):
    min_heap = []
    counter = 0
    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.val, counter, head))
            counter += 1

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next
```

**Complexity/Benefits/Pitfalls**

*   **Time Complexity:** O(N log k), where N is the total number of elements across all sequences, and k is the number of sequences. Each element is pushed onto and popped from the heap once (O(log k) per operation).
*   **Space Complexity:** O(k) to store at most one element from each sequence in the heap.
*   **Benefits:** Efficient for merging multiple sorted sequences, significantly better than repeatedly merging two lists (which would be O(Nk)).
*   **Pitfalls:** Requires careful handling of heap elements if items are not directly comparable (use the tuple technique). Ensure edge cases like empty input lists or empty sequences are handled. 