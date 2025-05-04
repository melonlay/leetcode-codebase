# Technique: Grid Flattening (Row-Major & Column-Major)

**Related:** Matrix Manipulation, Index Conversion, [[../patterns/matrix/dimension_reduction_matrix_to_1d.md]]

## 1. Description

Grid Flattening is a technique used to convert a 2D grid (matrix) into a 1D array or string. This is often done to leverage algorithms designed for 1D sequences (like string searching, prefix sums, difference arrays) on grid-based problems.

The two most common flattening orders are Row-Major and Column-Major.

## 2. Flattening Orders

Consider an `R x C` grid (R rows, C columns), 0-indexed `grid[r][c]` where `0 <= r < R` and `0 <= c < C`.
***Note:** Using generic `R` (Rows) and `C` (Columns) here to avoid confusion with common `m, n` variables which might be swapped between implementations.*

### 2.1. Row-Major Flattening

*   **Concept:** Concatenate rows one after another.
*   **Order:** `grid[0][0], grid[0][1], ..., grid[0][C-1], grid[1][0], grid[1][1], ..., grid[R-1][C-1]`
*   **Implementation (Python string):**
    ```python
    # Assuming grid has R rows and C columns
    text_row_major = "".join("".join(row) for row in grid)
    # Or equivalently:
    # text_row_major = "".join(grid[r][c] for r in range(R) for c in range(C))
    ```
*   **Result Length:** `R * C`

### 2.2. Column-Major Flattening

*   **Concept:** Concatenate columns one after another.
*   **Order:** `grid[0][0], grid[1][0], ..., grid[R-1][0], grid[0][1], grid[1][1], ..., grid[R-1][C-1]`
*   **Implementation (Python string):**
    ```python
    # Assuming grid has R rows and C columns
    text_col_major = "".join(grid[r][c] for c in range(C) for r in range(R))
    ```
*   **Result Length:** `R * C`

## 3. Index Conversion

When working with flattened representations, it's crucial to convert between the 1D index (`idx`) and the original 2D grid coordinates `(r, c)`.

### 3.1. Row-Major Index Conversion

*   **1D Index (`idx_row_major`) to 2D `(r, c)`:**
    *   `r = idx_row_major // C`  (Divide by **Number of Columns**)
    *   `c = idx_row_major % C`   (Modulo by **Number of Columns**)
*   **2D `(r, c)` to 1D Index (`idx_row_major`):**
    *   `idx_row_major = r * C + c` (Multiply row index by **Number of Columns**)

### 3.2. Column-Major Index Conversion

*   **1D Index (`idx_col_major`) to 2D `(r, c)`:**
    *   `r = idx_col_major % R`   (Modulo by **Number of Rows**)
    *   `c = idx_col_major // R`  (Divide by **Number of Rows**)
*   **2D `(r, c)` to 1D Index (`idx_col_major`):**
    *   `idx_col_major = c * R + r` (Multiply column index by **Number of Rows**)

## 4. Use Cases

*   Applying 1D algorithms (KMP, Difference Array, Prefix Sum) to grid problems.
*   Searching for patterns that wrap across row or column boundaries (depending on the flattening order used).
*   Simplifying iteration logic in some grid traversal scenarios.

## 5. Considerations & Pitfalls

*   **Consistency is Key:** The most common source of errors is inconsistency in defining row/column counts (e.g., using `m, n`) and applying the correct variable in the index conversion formulas. **Always double-check which variable holds the number of columns for row-major calculations and which holds the number of rows for column-major calculations.** Using explicit names like `num_rows`, `num_cols` or generic `R`, `C` (as used here) can improve clarity.
*   Choose the flattening order based on the direction of processing required.
*   Be careful with the correct index conversion formulas for the chosen order.
*   Flattening creates a copy of the data, increasing space complexity by O(R*C).

## 6. Example Application

*   LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings (Used row-major for horizontal KMP search, column-major for vertical KMP search, and index conversion for overlap counting) - See `problems/3529_count_cells_in_overlapping_horizontal_and_vertical_substrings/solution.py` 