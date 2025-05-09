# Pattern: Perfect Tiling Check (Axis-Aligned Rectangles)

## Problem Structure

Determine if a given collection of axis-aligned rectangles perfectly covers a larger rectangular region without any gaps or overlaps.

## Necessary Conditions

For a set of smaller rectangles to form a perfect tiling of a single larger rectangle, the following conditions must hold:

1.  **Area Conservation:** The sum of the areas of all the smaller rectangles must exactly equal the area of the encompassing bounding box.
2.  **No Gaps:** The union of the smaller rectangles must completely cover the bounding box.
3.  **No Overlaps:** The interiors of any two smaller rectangles must not overlap.

## Verification Strategies

Checking these conditions directly (e.g., complex geometric union and overlap calculations) can be computationally expensive. Common strategies simplify the verification:

### 1. Area + Corner Point Counting (Common for Axis-Aligned)

This is an efficient method particularly suited for axis-aligned rectangles. It relies on checking the Area Conservation principle and a clever way to infer the No Gaps/No Overlaps conditions based on corner point properties:

*   **Area Check:** Calculate the total area of the small rectangles (`total_area`). Find the overall bounding box (`min_x`, `min_y`, `max_a`, `max_b`) and its area (`expected_area`). Check if `total_area == expected_area`. This is necessary but not sufficient.
*   **Corner Point Check:** Use a counting mechanism (like a set) to track the occurrences of the corners of all small rectangles.
    *   Leverage the **Set-Based Counting** technique ([`../../techniques/set_based_counting.md`]) where points appearing an even number of times cancel out.
    *   In a perfect tiling, only the four corners of the overall bounding box should remain in the set (each appearing exactly once).
    *   **Verification:** After processing all corners, check:
        1.  Does the set contain exactly 4 points?
        2.  Are these 4 points precisely the corners of the overall bounding box?
*   **Combined Check:** The tiling is perfect if and only if **both** the area condition (`total_area == expected_area`) and the corner point conditions (exactly 4 bounding box corners remain in the set) are met.
*   **Implementation Note:** The determination and verification of the bounding box relative to the corner point set can be implemented in slightly different ways, trading off performance and robustness. See [[../../optimizations/bounding_box_calculation_timing.md]] for a discussion.
*   **Example Implementation:** See [[../../../problems/0391_perfect_rectangle/solution.md|Problem 391: Perfect Rectangle]].

### 2. Sweep-Line Algorithms

Sweep-line algorithms can also be used, often for more general overlap detection or area calculation problems.

*   Treat vertical edges as events. Sort events by x-coordinate.
*   Sweep a vertical line across the plane.
*   Maintain an active set of y-intervals intersected by the sweep line (e.g., using a Segment Tree or similar structure).
*   At each vertical edge event, update the active y-intervals. Check for overlaps or calculate covered length along the sweep line.
*   Integrate the covered length over the x-dimension.
*   This approach can be more complex to implement but can handle more general cases or provide different kinds of information (like total covered area even with overlaps).

## Applicability

The Area + Corner Point Counting method is highly effective and relatively simple for problems involving **axis-aligned rectangles** where a perfect, non-overlapping, gap-free tiling of a single rectangle is required.

Sweep-line is more general but often more complex. 