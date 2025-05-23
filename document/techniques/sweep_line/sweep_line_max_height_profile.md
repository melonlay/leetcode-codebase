# Technique: Sweep Line with Max-Heap for Vertical Profile

## 1. Description

This technique applies the sweep-line paradigm to problems involving finding the upper envelope or maximum vertical profile generated by a set of overlapping intervals, each associated with a value (e.g., height). The canonical example is the Skyline Problem (LeetCode 218).

It efficiently processes critical points (interval starts and ends) along an axis (typically the x-axis) while maintaining the maximum active height at the sweep line's current position using a max-heap combined with lazy deletion.

## 2. Core Algorithm Steps

1.  **Event Representation:**
    *   Transform each interval `[left, right, height]` into two events:
        *   Start Event: `(left, -height)`
        *   End Event: `(right, height)`
    *   Using negative height for start events ensures correct sorting: at the same x-coordinate, starts are processed before ends, and taller intervals starting are processed before shorter ones.
2.  **Sort Events:**
    *   Collect all events.
    *   Sort events primarily by x-coordinate, and secondarily by the height representation (negative for starts).
3.  **Sweep Line Processing:**
    *   Initialize `result` list (e.g., `skyline`).
    *   Initialize `prev_max_height = 0`.
    *   Use a **max-heap** (simulated using a min-heap `live_heights` storing negative heights `-h`) to track currently active heights. Initialize with `[0]` (ground level).
    *   Use a **frequency counter** (`height_counts: defaultdict(int)`) to track the number of active intervals for each height. Initialize with `height_counts[0] = 1`.
    *   Iterate through sorted `events` at position `x` with height info `h_event`:
        *   Get absolute `height = abs(h_event)`.
        *   **Start Event (`h_event < 0`):**
            *   Increment `height_counts[height]`.
            *   If `height_counts[height]` becomes 1 (first active interval of this height), push `-height` onto `live_heights` heap.
        *   **End Event (`h_event > 0`):**
            *   Decrement `height_counts[height]`.
        *   **Lazy Deletion (Heap Cleaning):** While the top of the heap (`-live_heights[0]`) corresponds to a height whose count is zero (`height_counts[-live_heights[0]] == 0`), pop from `live_heights`.
        *   **Get Current Max Height:** `current_max_height = -live_heights[0]`.
        *   **Append to Result:** If `current_max_height != prev_max_height`:
            *   Append `[x, current_max_height]` to `result`.
            *   Update `prev_max_height = current_max_height`.
4.  **Return `result`.**

## 3. Complexity

Let N be the number of input intervals.
*   **Time Complexity:** O(N log N) - Dominated by sorting the 2N events and the N heap operations within the sweep.
*   **Space Complexity:** O(N) - To store events, the heap, the frequency map, and the result.

## 4. Key Concepts & Data Structures

*   **Sweep Line Algorithm:** Processing events along an ordered axis.
*   **Event Point Sorting:** Crucial for handling starts/ends and height priorities correctly.
*   **Max-Heap (Min-Heap Simulation):** Efficiently querying the current maximum active height (O(log N)).
*   **Frequency Counter (Hash Map/Dictionary):** Enables efficient lazy deletion from the heap (O(1) updates/lookups).

## 5. Example Applications

*   **LeetCode 218: The Skyline Problem:** The primary example where building heights form the vertical profile.
*   Calculating the maximum overlap or intensity profile from time intervals with associated values.

## 6. Related Concepts

*   [[../../data_structures/heap_priority_queue.md]]
*   [[../../data_structures/hash_table_dict.md]]
*   Potentially related to Segment Trees for more complex range queries, but the heap approach is often sufficient for max-height profiles.

## 7. Alternative Implementation: Storing Right Boundary in Heap

An alternative implementation avoids the separate frequency counter (`height_counts`) by storing the right boundary (`R`) of each interval directly within the heap.

*   **Heap Element:** Store tuples `(negative_height, right_boundary)` in the min-heap (simulating a max-heap based on height).
*   **Event Representation:** Can use `(L, -H, R)` for starts and `(R, 0, None)` for ends (or similar).
*   **Initialization:** Initialize heap with a ground level sentinel, e.g., `[(0, float('inf'))]`.
*   **Heap Pruning:** *Before* processing the current event at `x`, proactively remove elements from the heap top whose `right_boundary` is less than or equal to `x`.
    ```python
    # Inside the loop processing event (x, neg_h, R_start):
    while x >= max_heap[0][1]: # Check if top element's R is <= current x
        heapq.heappop(max_heap)
    
    if neg_h != 0: # If it's a start event
        heapq.heappush(max_heap, (neg_h, R_start))
    
    current_max_height = -max_heap[0][0]
    # ... rest of the logic ...
    ```
*   **Trade-offs:**
    *   **Pros:** Avoids the need for the separate `height_counts` dictionary, potentially simplifying state management slightly.
    *   **Cons:** Stores slightly more data per heap element. Heap pruning logic is shifted to occur before processing the event's height addition.
    *   **Complexity:** Asymptotic time and space complexity remain O(N log N) and O(N), respectively.

Both the frequency count/lazy deletion method and the store-right-boundary/proactive pruning method are valid ways to implement the core sweep-line + heap technique for this type of problem. 