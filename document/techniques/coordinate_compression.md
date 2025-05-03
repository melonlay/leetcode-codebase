# Technique: Coordinate Compression

## 1. Description

Coordinate Compression is a technique used primarily in competitive programming and algorithms involving geometric problems or discrete events on a number line. It addresses scenarios where the absolute values of coordinates can be very large (e.g., up to 10^9 or more), but the *number* of distinct coordinates relevant to the problem is relatively small (e.g., up to 10^5).

The goal is to map these sparse, large coordinate values to a smaller range of consecutive integer indices (typically `0` to `M-1`, where `M` is the number of unique coordinates). This allows the use of data structures that depend on index ranges, such as arrays, Fenwick Trees (BIT), or Segment Trees, which would be infeasible to build over the original large coordinate range due to memory or time constraints.

## 2. Core Algorithm Steps

1.  **Collect Coordinates:** Gather all relevant coordinate values from the input (e.g., `left` and `right` endpoints of intervals, x or y coordinates of points).
2.  **Unique & Sort:** Create a sorted list (or array) of the *unique* collected coordinates.
3.  **Create Mapping:** Build a mapping (typically a hash map / dictionary) from each unique original coordinate to its index in the sorted list. The index `i` corresponds to the coordinate `sorted_unique_coords[i]`.
4.  **Replace Coordinates:** Replace the original large coordinate values in the input data or during processing with their corresponding compressed integer indices obtained from the map.
5.  **Apply Algorithm:** Use the compressed indices with index-based data structures (Segment Tree, BIT, etc.).
6.  **(Optional) Map Back:** If the final result needs to be expressed in terms of original coordinates, use the sorted unique coordinate list to map indices back.

## 3. Example Implementation (Python)

```python
# Example Input: list of intervals [(left, right, value), ...]
intervals = [(10, 100, 5), (20, 50, 8), (150, 200, 3)]

# 1. Collect Coordinates
coords = set()
for l, r, _ in intervals:
    coords.add(l)
    coords.add(r)

# 2. Unique & Sort
sorted_unique_coords = sorted(list(coords))

# 3. Create Mapping
coord_to_index = {coord: i for i, coord in enumerate(sorted_unique_coords)}
index_to_coord = {i: coord for i, coord in enumerate(sorted_unique_coords)} # Optional for mapping back

# 4. Replace Coordinates (Example: preparing for Segment Tree)
compressed_intervals = []
for l, r, val in intervals:
    idx_l = coord_to_index[l]
    idx_r = coord_to_index[r]
    # Note: Often use range [idx_l, idx_r - 1] for segment tree updates
    compressed_intervals.append((idx_l, idx_r, val))

# 5. Apply Algorithm (e.g., Build and update Segment Tree using compressed indices)
M = len(sorted_unique_coords)
# seg_tree = build_segment_tree(M)
# for idx_l, idx_r, val in compressed_intervals:
#    update_segment_tree(seg_tree, idx_l, idx_r - 1, val)

# 6. Map Back (Example: result from Segment Tree query at index `res_idx`)
# original_coordinate = index_to_coord[res_idx]
```

## 4. Complexity

Let N be the number of original coordinates collected.
*   **Time Complexity:** O(N log N) - Dominated by the sorting step.
*   **Space Complexity:** O(N) - To store the unique coordinates and the mapping.

## 5. When to Use

*   When coordinate values are large, but the number of distinct coordinates is manageable.
*   Before using index-based data structures like Segment Trees, Fenwick Trees, or even simple arrays/prefix sums where the required size depends on the coordinate range.
*   Problems involving intervals, rectangles, or points on a line or grid where only the relative order or discrete positions matter, not the absolute large values.

## 6. Important Considerations

*   **Interval Representation:** Be careful when compressing intervals `[left, right]`. A common convention for Segment Trees/BITs is to operate on ranges `[idx_left, idx_right - 1]` corresponding to the segments *between* the compressed points.
*   **Point vs. Segment Queries:** Coordinate compression effectively discretizes the space. Queries often relate to the intervals *between* the original coordinates.

## 7. Related Concepts

*   [[../../data_structures/segment_tree.md]] (Assumed link)
*   [[../../data_structures/fenwick_tree_bit.md]] (Assumed link)
*   Discretization 