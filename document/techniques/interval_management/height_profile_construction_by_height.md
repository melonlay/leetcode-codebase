# Technique: Height Profile Construction via Height-Ordered Overwrite

## 1. Description

This technique constructs a vertical profile (like a skyline) from intervals `[left, right, height]` by processing the intervals ordered by increasing height. It explicitly maintains the profile's critical points (x-coordinates) and the height associated with each segment, allowing taller intervals processed later to "overwrite" the profile established by shorter intervals.

## 2. Conceptual Algorithm (Naive List-Based - Inefficient)

This outlines the idea but uses standard lists, leading to poor performance.

1.  **Sort Intervals:** Sort the input intervals `buildings` by height (`h`) in ascending order.
2.  **Initialize Profile:**
    *   `pos = [0]` (Sorted list of critical x-coordinates)
    *   `height = [0]` (List where `height[k]` is the profile height starting at `pos[k]`)
3.  **Process Intervals (by Height):**
    *   For each interval `(left, right, h)`:
        *   Find insertion indices `i` for `left` (`bisect_left`) and `j` for `right` (`bisect_right`) in `pos`.
        *   Update `pos`: Replace elements `pos[i...j-1]` with `left` and `right` -> `pos[i:j] = [left, right]`. This removes internal points and ensures `left`, `right` are critical points.
        *   Update `height`: Replace corresponding heights. Set the height starting at `left` (now `pos[i]`) to `h`. Preserve the height that existed just after the original `pos[j-1]` -> `height[i:j] = [h, height[j-1]]`.
4.  **Extract Result:** Iterate through the final `pos` and `height`. Append `[pos[k], height[k]]` whenever `height[k]` differs from `height[k-1]`.

## 3. Complexity (Naive List-Based)

*   **Time Complexity: O(N^2)** - While sorting and bisects are O(N log N), the list slice assignments `pos[i:j] = ...` and `height[i:j] = ...` take O(K) time each, where K is the length of the lists (up to O(N)). This occurs inside the N-iteration loop, leading to O(N^2) overall.
*   **Space Complexity: O(N)** - To store `pos`, `height`, and the result.

**Warning:** The O(N^2) time complexity makes this list-based implementation impractical for typical competitive programming constraints.

## 4. Optimization: Using a Segment Tree (Recommended)

The correct and efficient way to implement this conceptual approach is using a **Segment Tree** with **Coordinate Compression**.

1.  **Coordinate Compression:** Collect all unique `left` and `right` coordinates from the N buildings. Sort them and create a mapping from these coordinates to compressed indices `0...M-1`, where `M <= 2N`.
2.  **Segment Tree:** Build a segment tree covering the index range `[0, M-1]`. Each node should store the maximum height in its corresponding range. Lazy propagation can be used for efficient range updates.
3.  **Process Intervals (Order Doesn't Matter Here):** For each building `(left, right, h)`:
    *   Map `left` and `right` to their compressed indices `idx_left`, `idx_right`.
    *   Perform a **range update** on the segment tree for the index range `[idx_left, idx_right - 1]`. Update the maximum height in this range to `h` (using `max(current_height, h)` or assignment with lazy propagation).
4.  **Extract Result:** Perform a traversal of the segment tree (e.g., query each leaf interval `[idx, idx+1]`) to find the height at each minimal interval. Construct the final skyline points by appending `[original_coord[idx], height]` whenever the height changes between adjacent minimal intervals.

## 5. Complexity (Segment Tree Implementation)

*   **Time Complexity: O(N log N)** - Coordinate compression takes O(N log N). Segment tree build is O(M) = O(N). Each of the N range updates takes O(log M) = O(log N). Final traversal/query takes O(M) = O(N). Overall O(N log N).
*   **Space Complexity: O(N)** - O(N) for coordinate mapping and O(M) = O(N) for the segment tree.

## 6. Comparison to Sweep Line

*   **Sweep Line + Heap:** Processes x-coordinate events, maintains only *active* heights using a heap. Generally considered the standard approach for Skyline.
*   **Height Overwrite + Segment Tree:** Processes buildings (often by height conceptually, but not required for segment tree correctness), explicitly builds the entire height profile using range updates on a tree structure.

Both optimized approaches achieve O(N log N) time complexity.

## 7. Related Concepts

*   Coordinate Compression
*   Segment Tree (with Range Updates / Lazy Propagation)
*   [[../../data_structures/segment_tree.md]] (Assumed link)
*   [[../../techniques/coordinate_compression.md]] (Assumed link) 