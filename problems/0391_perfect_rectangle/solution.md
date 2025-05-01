# Solution Explanation: 391. Perfect Rectangle

## Problem Summary

Given a list of axis-aligned rectangles, determine if they perfectly tile a larger rectangular area without any gaps or overlaps. Each rectangle is defined by its bottom-left `(x1, y1)` and top-right `(a1, b1)` coordinates.

## Algorithmic Approach (Optimized)

This solution uses the most efficient strategy for this problem, relying on area summation and corner point cancellation.

1.  **Area Conservation:** The sum of the areas of the smaller rectangles must equal the area of the overall bounding box.
2.  **Corner Point Cancellation:** In a perfect tiling, interior corners are shared by an even number of rectangles, while the four bounding box corners are shared by exactly one.

These conditions are checked efficiently and implicitly:

*   See the general pattern document: [`../../document/patterns/geometry/perfect_tiling_check.md`](../../document/patterns/geometry/perfect_tiling_check.md)
*   See the optimization discussion: [`../../document/optimizations/bounding_box_calculation_timing.md`](../../document/optimizations/bounding_box_calculation_timing.md)

### Implementation Details

1.  **Initialization:**
    *   Initialize `total_area = 0`.
    *   Initialize an empty set `corners`.

2.  **Iteration (O(N)):**
    *   Loop through each rectangle `[x1, y1, a1, b1]`.
    *   Add the rectangle's area `(a1 - x1) * (b1 - y1)` to `total_area`.
    *   Process the four corners using set symmetric difference update (`^=`): `corners ^= {(x1, y1), (x1, b1), (a1, y1), (a1, b1)}`.
        *   This efficiently implements the **Set-Based Counting** technique ([`../../document/techniques/set_based_counting.md`](../../document/techniques/set_based_counting.md)), cancelling points that appear an even number of times.

3.  **Verification (O(1)):**
    *   **Corner Count Check:** If `len(corners) != 4`, return `False`. Gaps or overlaps would result in a different number of points remaining.
    *   **Derive Bounding Box Corners:** If exactly 4 points remain, derive the bottom-left `(bl_x, bl_y)` and top-right `(tr_a, tr_b)` corners from this set using `min`/`max` with a key based on the sum of coordinates.
    *   **Area Check:** Calculate the `expected_area` of the bounding box derived from these corners: `(tr_a - bl_x) * (tr_b - bl_y)`. Return `True` if `total_area == expected_area`.

### Correctness & Optimization Rationale

This approach is correct because the combination of the final two checks is sufficient:
1.  If `len(corners) == 4`, it means all internal points cancelled correctly, suggesting no overlaps or gaps *within* the area defined by the outer boundary points.
2.  If, *in addition*, `total_area == expected_area` (where `expected_area` is calculated *from those 4 remaining points*), it confirms that:
    *   There were no unaccounted-for gaps (which would make `total_area` too small).
    *   There were no overlaps (which would make `total_area` too large OR would likely have prevented `len(corners)` from being exactly 4).
    *   The 4 points remaining *must* therefore be the correct bounding box corners of a perfectly tiled rectangle whose area matches the sum of its parts.

This avoids the overhead of tracking min/max coordinates during the loop and the extra post-loop verification step present in slightly safer but slower alternative implementations, making it the most performant correct solution for this problem.

## Complexity Analysis

*   **Time Complexity:** O(N), dominated by the single loop through rectangles. Set operations and post-loop checks are O(1) on average.
*   **Space Complexity:** O(N), for the `corners` set in the worst case.

## Knowledge Base Relevance

*   **Pattern:** `Perfect Tiling Check` ([`../../document/patterns/geometry/perfect_tiling_check.md`](../../document/patterns/geometry/perfect_tiling_check.md))
*   **Technique:** `Set-Based Counting` ([`../../document/techniques/set_based_counting.md`](../../document/techniques/set_based_counting.md))
*   **Optimization:** Leverages the principle that for this specific problem, post-loop bounding box derivation combined with area and corner count checks is sufficient, avoiding less performant in-loop tracking or redundant verification. ([`../../document/optimizations/bounding_box_calculation_timing.md`](../../document/optimizations/bounding_box_calculation_timing.md))
*   **Data Structure:** `set` (using `^=`)
*   **Python:** `lambda` functions for `min`/`max` keys.