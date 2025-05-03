# Solution Explanation: LeetCode 218 - The Skyline Problem

## Problem Summary

Given a list of rectangular buildings defined by their left x-coordinate, right x-coordinate, and height, determine the skyline silhouette formed by these buildings when viewed from a distance. The skyline should be represented as a list of key points `[x, y]`, where the y-coordinate changes, sorted by x-coordinate. Consecutive horizontal segments of the same height should be merged.

## Approach: Sweep Line with Max-Heap

This problem is a classic application of the sweep-line algorithm.

1.  **Event Representation:**
    *   Each building contributes two events: a "start" event at its left edge and an "end" event at its right edge.
    *   We represent events as tuples `(x, height_info)`. To handle events at the same x-coordinate correctly (process starts before ends, and taller buildings before shorter ones if they start/end at the same x), we store:
        *   Start event: `(left_x, -height)`
        *   End event: `(right_x, height)`
    *   Storing the negative height for start events ensures that when sorted, start events come before end events at the same `x`, and among start events, taller buildings (more negative `-height`) come first. Similarly, among end events, taller buildings (`height`) come first.

2.  **Sorting Events:**
    *   Create a list of all start and end events from the input buildings.
    *   Sort this list primarily by x-coordinate, and secondarily by the `height_info` (which incorporates the negative sign for starts).

3.  **Sweep Line Processing:**
    *   Initialize an empty list `skyline` to store the result key points.
    *   Initialize `prev_max_h = 0` to track the previous maximum height.
    *   Use two data structures to maintain the heights of currently "active" buildings (buildings intersected by the sweep line):
        *   `live_heights`: A **min-heap** storing the negative heights (`-h`) of active buildings. This simulates a max-heap, allowing O(log n) access to the maximum active height (`-heap[0]`). Initialize with `[0]` representing the ground.
        *   `height_counts`: A `defaultdict(int)` to store the frequency count of each active height. This is crucial because multiple buildings can have the same height, and we only want to remove a height from consideration (conceptually, from the heap) when *all* buildings of that height have ended. Initialize with `height_counts[0] = 1`.
    *   Iterate through the sorted `events`:
        *   For each event `(x, h_event)`:
            *   Determine if it's a start (`is_start = h_event < 0`) or end event.
            *   Get the absolute `height = abs(h_event)`.
            *   **If `is_start`:**
                *   Increment `height_counts[height]`. If this is the first time seeing this height (`height_counts[height]` was 0), push `-height` onto the `live_heights` heap.
            *   **Else (it's an end event):**
                *   Decrement `height_counts[height]`.
            *   **Heap Cleaning:** While the top of the heap (`live_heights[0]`) corresponds to a height whose count is zero (`height_counts[-live_heights[0]] == 0`), pop it from the heap. This lazily removes heights whose buildings have ended.
            *   **Determine Current Max Height:** After cleaning, the current maximum active height is `current_max_h = -live_heights[0]`.
            *   **Append Key Point:** If `current_max_h` is different from `prev_max_h`, it signifies a change in the skyline's vertical level. Append the key point `[x, current_max_h]` to the `skyline` list. Update `prev_max_h = current_max_h`.

4.  **Return Result:** Return the `skyline` list.

## Complexity Analysis

*   **Time Complexity:** O(N log N)
    *   Creating events: O(N), where N is the number of buildings.
    *   Sorting events: O(N log N), as there are 2N events.
    *   Processing events: The loop runs 2N times. Inside the loop, heap push/pop operations take O(log N) time (heap size is at most N). The heap cleaning `while` loop, in total across all iterations, processes each height at most once when it's added and once when its count reaches zero. Thus, the processing part is also O(N log N).
    *   Overall: O(N log N).
*   **Space Complexity:** O(N)
    *   Storing events: O(N).
    *   Storing `live_heights` (heap): O(N) in the worst case.
    *   Storing `height_counts`: O(N) in the worst case.
    *   Storing the `skyline` result: O(N) in the worst case.
    *   Overall: O(N).

## Knowledge Base Links

*   Data Structure: Heap/Priority Queue - [[../../data_structures/heap_priority_queue.md]]
*   Data Structure: Hash Table (for `defaultdict`) - [[../../data_structures/hash_table_dict.md]]
*   (Note: While sweep-line is a known pattern, a specific entry for this exact problem/technique variant was not found during the search.) 