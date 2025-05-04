# Technique: Recursive Quadrant Construction for Grids

## Concept

This technique applies to problems requiring the construction of a grid (often square and with dimensions that are powers of 2) where the definition or constraints are inherently recursive based on quadrants. The core idea is to fill the grid by recursively filling its four quadrants, often involving a partitioning of the values to be placed based on ordering rules between the quadrants.

## How it Works

1.  **Problem Structure:** Identify if the grid construction follows a recursive pattern based on dividing the grid into four quadrants (Top-Left, Top-Right, Bottom-Left, Bottom-Right). Check if there are ordering constraints on the values *between* these quadrants (e.g., TR < BR < BL < TL).
2.  **Value Partitioning:** Determine how the total range of values to be placed in the grid should be partitioned among the four quadrants to satisfy the ordering constraints. Typically, this involves dividing the range into four equal, contiguous sub-ranges.
3.  **Recursive Function:** Define a recursive function, often taking parameters like:
    *   Current grid dimension/level (`n` for a \(2^n \times 2^n\) grid).
    *   Top-left coordinates (`r`, `c`) of the subgrid to fill (optional, can be handled implicitly).
    *   A base value or offset (`offset`) indicating the start of the value sub-range assigned to this subgrid.
4.  **Base Case:** Define the termination condition for the recursion (e.g., `n=0` for a 1x1 grid). Fill the single cell with the appropriate value (usually `offset`).
5.  **Recursive Step:**
    *   Calculate the size of the next level's sub-quadrants (`sub_size`) and the size of the value partition (`quadrant_value_count`).
    *   Make four recursive calls, one for each conceptual quadrant (e.g., TL, TR, BL, BR), passing `n-1` and the calculated `offset` for that quadrant based on the value partitioning scheme.
    *   Combine the results returned by the recursive calls into the grid for the current level `n`, placing each sub-grid result into its corresponding spatial quadrant.
6.  **Memoization (Optional):** Consider memoizing the results of the recursive function based on its state (e.g., `(n, offset)`) if overlapping subproblems are possible or expected, although the structure might be strictly hierarchical. See [[../../techniques/recursion/memoization.md]].

## Example Application: LeetCode 3537. Fill a Special Grid

In this problem, a \(2^N \times 2^N\) grid needs to be filled with values 0 to \(2^{2N}-1\).
*   Constraints: TR < BR < BL < TL.
*   Value Partitioning: Range \([0, 4^N-1]\) is split into 4 blocks of size \(4^{N-1}\). TR gets Block 0, BR Block 1, BL Block 2, TL Block 3.
*   Recursion: `_fill(n, offset)` calculates the grid.
    *   Base Case: `n=0`, returns `[[offset]]`.
    *   Recursive Step: Calls `_fill(n-1, offset + k * quadrant_count)` for `k=0, 1, 2, 3` corresponding to TR, BR, BL, TL value blocks. Combines the 4 results into the `n`-level grid.

## Related Concepts

*   [[../../patterns/divide_and_conquer/divide_and_conquer.md]]: This technique is a specific application of the Divide and Conquer pattern.
*   Fractals: The resulting grids often exhibit fractal-like properties (e.g., Sierpinski carpet variations, Z-order curve patterns). 