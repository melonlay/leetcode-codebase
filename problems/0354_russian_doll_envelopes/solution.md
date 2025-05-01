# Solution Explanation: LeetCode 354 - Russian Doll Envelopes

## Problem Summary

Given a list of envelopes `[w, h]`, find the maximum number that can be nested (`w1 < w2` and `h1 < h2`).

## Algorithmic Approach: Sorting + LIS

This problem is solvable by reducing the 2D nesting constraint to a 1D Longest Increasing Subsequence (LIS) problem on the heights after a specific sorting procedure.

### Step 1: Sorting Strategy

The goal is to sort the envelopes so that iterating through them allows us to focus only on the height dimension for the LIS calculation. The required order is ascending width (`w`), and for ties in width, descending height (`h`). There are two main ways to achieve this:

1.  **Single-Pass Sort (Compound Key):**
    ```python
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    ```
    - This uses a single sort operation with a tuple key. It's often considered the standard, direct way to express this sorting logic.

2.  **Two-Pass Stable Sort:**
    ```python
    # Requires a stable sort (like Python's Timsort)
    envelopes = sorted(envelopes, key=lambda x: x[1], reverse=True) # Sort height desc
    envelopes = sorted(envelopes, key=lambda x: x[0])                # Stable sort width asc
    ```
    - This relies on the stability of the sort algorithm. The second sort (by width) preserves the relative order of elements with equal widths established by the first sort (height descending).

*Analysis:* Both methods yield the correct logical order. Theoretically, both have an O(n log n) time complexity. However, in practice, the **two-pass stable sort was observed to perform faster** for this specific problem on some platforms. This could be due to factors like the overhead of tuple comparison vs. integer comparison within the sort, or other internal optimizations. The final code uses the two-pass method based on this observation.

### Step 2: Longest Increasing Subsequence (LIS) on Heights

After sorting, the problem reduces to finding the LIS of the heights. Any increasing subsequence of heights corresponds to a valid nesting sequence because the sorting handles the width constraint.

There are subtle variations in implementing the O(n log n) LIS algorithm using binary search:

1.  **Standard LIS (using `tails = []`):**
    ```python
    tails = []
    for _, h in envelopes:
        idx = bisect_left(tails, h)
        if idx == len(tails):
            tails.append(h)
        else:
            tails[idx] = h
    # result = len(tails)
    ```
    - Initializes with an empty list and processes all elements.
    - Always calls `bisect_left` to find the correct position.
    - Handles empty input implicitly.

2.  **Optimized Append Check LIS (using `dp = [h0]`):**
    ```python
    # Assumes non-empty, checked earlier
    dp = [envelopes[0][1]]
    for _, h in envelopes[1:]:
        if dp[-1] < h:
            dp.append(h) # O(1) append
        else:
            i = bisect_left(dp, h) # O(log k) search
            dp[i] = h
    # result = len(dp)
    ```
    - Initializes with the first height.
    - Performs an O(1) check (`dp[-1] < h`). If true, it appends directly, avoiding the O(log k) `bisect_left` cost for that element.
    - Can be slightly faster if appends are frequent.
    - Requires explicit empty list check before initialization.

*Analysis:* The **optimized append check variant was chosen** for the final code (`solution.py`) as it potentially offers a performance edge by skipping some binary searches, aligning with the goal of maximizing speed based on the user's observations.

## Final Implementation Summary

The code in `solution.py` uses the **two-pass stable sort** strategy followed by the **optimized append check LIS** implementation to maximize observed performance.

## Knowledge Base References

*   **Core Algorithm:** [[../../document/algorithms/dynamic_programming/array/longest_increasing_subsequence.md|Algorithm: Longest Increasing Subsequence (LIS)]] - Discusses both O(n^2) and O(n log n) approaches, including the standard and optimized append check O(n log n) variants.
*   **Key Technique:** [[../../document/techniques/array/2d_dependency_lis_reduction.md|Technique: 2D Dependency Reduction via LIS]] - Explains the sorting strategy (including both single-pass and two-pass methods) to reduce this 2D problem to a 1D LIS problem.

## Complexity Analysis

*   **Time Complexity:** O(n log n) - Dominated by sorting and the LIS algorithm.
*   **Space Complexity:** O(n) - For sorting space (depending on implementation) and the `dp`/`tails` array for LIS. 