# LeetCode 218: The Skyline Problem - Solution Explanation

## Problem Summary

Given a list of rectangular buildings `[left, right, height]`, return the skyline formed by these buildings when viewed from a distance. The skyline should be represented as a list of "key points" `[x, y]`, which are the left endpoints of horizontal line segments. Adjacent horizontal segments of the same height should be merged.

## Algorithmic Approach: Sweep Line with Max-Heap

This problem is a classic application of the **Sweep Line** algorithm combined with a **Max Heap** (or a min-heap storing negative heights) and **Lazy Deletion** using counts.

The core idea is to sweep a vertical line across the x-axis and track the maximum height of the buildings currently intersected by the sweep line. Changes in this maximum height correspond to the key points of the skyline.

## Logic Explanation

The detailed logic follows the steps outlined in the Knowledge Base document for this specific technique:

*   **Reference:** `[[../document/techniques/sweep_line/sweep_line_max_height_profile.md]]`

Here's a summary tailored to the code:

1.  **Event Generation:**
    *   Each building `[L, R, H]` generates two events:
        *   Start: `(L, -H)`
        *   End: `(R, H)`
    *   Storing `-H` for starts ensures correct sorting priorities.
2.  **Event Sorting:**
    *   Sort all events primarily by x-coordinate (`L` or `R`), and secondarily by the height value (`-H` or `H`). This ensures starts are processed before ends at the same `x`, and taller starts/ends are processed first.
3.  **Sweep Line Processing:**
    *   Initialize `skyline = []`, `live_heights = [0]` (min-heap storing negative heights, starting with ground), `height_counts = defaultdict(int)` (with `height_counts[0] = 1`), and `prev_max_h = 0`.
    *   Iterate through sorted `events` at coordinate `x` with height data `h_event`:
        *   Determine `height = abs(h_event)` and if it's a `is_start` event (`h_event < 0`).
        *   **Update Counts & Heap:**
            *   If `is_start`: Increment `height_counts[height]`. If count was 0, `heapq.heappush(live_heights, -height)`.
            *   Else (is end): Decrement `height_counts[height]`.
        *   **Lazy Deletion:** While the height at the top of the heap (`-live_heights[0]`) has a count of 0 in `height_counts`, `heapq.heappop(live_heights)`.
        *   **Get Current Max:** `current_max_h = -live_heights[0]`.
        *   **Check for Change:** If `current_max_h != prev_max_h`:
            *   Add `[x, current_max_h]` to `skyline`.
            *   Update `prev_max_h = current_max_h`.
4.  **Return `skyline`.**

## Knowledge Base References

*   **Core Technique:** `[[../document/techniques/sweep_line/sweep_line_max_height_profile.md]]` (Details the specific algorithm used here, including event representation and lazy heap deletion).
*   **Overall Pattern:** `[[../document/patterns/sweep_line.md]]`
*   **Data Structures:**
    *   `[[../document/data_structures/heap_priority_queue.md]]`
    *   `[[../document/data_structures/hash_table_dict.md]]` (for `defaultdict`)

## Complexity Analysis

*   **Time Complexity:** O(N log N), dominated by sorting events and heap operations (where N is the number of buildings).
*   **Space Complexity:** O(N) for storing events, heap elements, and the counts dictionary. 