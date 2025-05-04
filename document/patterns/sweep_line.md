# Pattern: Sweep Line Algorithm

## Description

The Sweep Line algorithm (or plane sweep algorithm) is a computational geometry pattern and a general algorithmic technique. It solves problems, often involving geometric objects (like points, line segments, rectangles) or intervals, by conceptually sweeping a line (usually vertical or horizontal) across the input space.

The algorithm processes events that occur at specific points along the sweep axis. These events typically correspond to the start or end points of the objects being considered (e.g., x-coordinates of vertical edges of rectangles, start/end times of intervals).

As the sweep line moves, it maintains a data structure (the "status structure") that holds information about the objects currently intersected by the line. When an event point is encountered, the status structure is updated, and calculations relevant to the problem are performed.

## Core Steps

1.  **Define Events:** Determine the critical points along the chosen sweep axis (e.g., x-coordinates) where the status of the system might change. These points become the events. Events often store information like the coordinate, the type (start/end), and associated object data (e.g., height, object ID).
2.  **Sort Events:** Collect all events and sort them according to their coordinates along the sweep axis. Define a clear tie-breaking rule for events at the same coordinate (e.g., process starts before ends, process lower points before higher points).
3.  **Initialize Status Structure:** Choose a data structure that can efficiently maintain the state of objects intersected by the sweep line and support necessary queries/updates (e.g., finding max/min, checking overlaps, maintaining counts).
4.  **Sweep and Process:** Iterate through the sorted events:
    *   Move the conceptual sweep line to the current event's coordinate.
    *   Process the event(s) at this coordinate:
        *   Update the status structure based on the event type (e.g., add an interval, remove an interval, update a value).
        *   Perform calculations or queries relevant to the problem based on the current status (e.g., calculate area, find max height, check for intersections).
5.  **Combine Results:** Aggregate the results obtained during the sweep to get the final answer.

## Key Components

*   **Sweep Line:** The conceptual line moving across the plane.
*   **Events:** Discrete points along the sweep axis where updates/calculations occur.
*   **Status Structure:** Data structure holding information about objects intersecting the sweep line. The choice is crucial for efficiency.

## Common Status Structures

*   **Balanced Binary Search Tree (BST) / Set / Sorted List:** To maintain intervals or points intersected by the sweep line in sorted order, allowing efficient searching, insertion, deletion (often O(log N)).
*   **Heap (Priority Queue):** To efficiently find the maximum or minimum value among active objects (e.g., max height in Skyline problem - see [[../techniques/sweep_line/sweep_line_max_height_profile.md]]). O(log N) updates/queries.
*   **Segment Tree / Fenwick Tree (BIT):** For problems requiring range queries or updates on the status along the axis *perpendicular* to the sweep line (e.g., maintaining counts or sums over y-intervals while sweeping along x). O(log M) or O(log N) per operation, where M is coordinate range or N is number of intervals.
*   **Hash Map / Dictionary:** For simple counting or presence checks.

## Complexity

Let N be the number of objects or intervals, leading to O(N) events.
*   **Time Complexity:** Typically O(N log N), dominated by:
    *   Sorting the events: O(N log N).
    *   Processing each event, involving updates/queries on the status structure: Often O(log N) per event using trees/heaps, leading to O(N log N) total.
*   **Space Complexity:** O(N) or O(M), depending on whether the status structure stores information related to N objects or the coordinate range M.

## Use Cases

*   **Geometric Intersections:** Finding intersections between line segments, rectangles.
*   **Closest Pair of Points:** An efficient O(N log N) algorithm uses sweep line.
*   **Rectangle Union Area:** Calculating the total area covered by a set of possibly overlapping rectangles.
*   **Skyline Problem:** Finding the upper envelope of a set of buildings [[../techniques/sweep_line/sweep_line_max_height_profile.md]].
*   **Maximum Overlap:** Finding the point in time or space with the maximum number of overlapping intervals.
*   **Interval Scheduling Variations:** Problems involving processing intervals based on their start/end times.

## Example: Maximum Overlapping Intervals

1.  **Events:** `(time, +1)` for interval start, `(time, -1)` for interval end.
2.  **Sort Events:** Sort by time, breaking ties (e.g., starts before ends).
3.  **Status Structure:** An integer `current_overlap_count`.
4.  **Sweep:** Iterate through events. Update `current_overlap_count` based on event type (+1 or -1). Keep track of the maximum `current_overlap_count` seen.

## Related Concepts

*   Computational Geometry
*   Interval Problems
*   Sorting Algorithms
*   Data Structures (Heaps, BSTs, Segment Trees) 