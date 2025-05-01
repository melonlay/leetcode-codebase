# Optimization: Timing of Bounding Box Calculation in Geometric Checks

## Context

When solving geometric problems that involve verifying properties against an overall bounding box (e.g., checking if smaller shapes perfectly tile a larger rectangle), a key implementation choice is *when* and *how* to determine the bounding box coordinates (`min_x`, `min_y`, `max_x`, `max_y`).

This often interacts with other checks, such as area summation or point counting.

## Strategies & Trade-offs

Consider a scenario like the [Perfect Tiling Check](../../patterns/geometry/perfect_tiling_check.md), which requires both area conservation and corner point validation.

1.  **Strategy 1: Continuous Tracking & Post-Loop Calculation**
    *   *Implementation:* Track overall min/max coordinates within the main loop.
    *   *Pros:* Robust, bounds definitively known.
    *   *Cons:* Potential performance overhead from O(N) min/max calls within the loop.

2.  **Strategy 2: Post-Loop Derivation Only (Fastest, Conditionally Safe)**
    *   *Implementation:* Do *not* track min/max in the loop. Derive bounding box coordinates *after* the loop solely from other calculated information (e.g., the 4 points remaining in a corner set).
    *   *Pros:* Avoids all min/max overhead in the loop, potentially the fastest.
    *   *Cons:* Relies on the derived information being a correct representation of the bounding box. This assumption might be invalid for some problems (e.g., complex overlaps) but can be **proven sufficient for specific problems like LeetCode 391 (Perfect Rectangle)** where the combination of `len(corners)==4` and `total_area==derived_area` implicitly guarantees correctness.
    *   *Verdict:* Use when correctness can be guaranteed *without* explicit verification against tracked bounds, offering the best performance.

3.  **Strategy 3: Hybrid - Continuous Tracking for Verification, Post-Loop Derivation for Calculation**
    *   *Implementation:* Track min/max in the loop *and* derive coordinates post-loop. Verify derived values against tracked values before using derived values for the final check (e.g., area comparison).
    *   *Pros:* Balances performance (uses derived values for main check) and robustness (explicit verification).
    *   *Cons:* More complex logic; the verification step adds overhead compared to Strategy 2.
    *   *Verdict:* Use when the correctness of Strategy 2 is uncertain or hard to prove, but some performance gain over Strategy 1 is desired.

## Recommendation

*   **Default/Safest:** Strategy 1 (Continuous Tracking).
*   **Highest Performance (If Correctness Proven):** Strategy 2 (Post-Loop Derivation Only). This is the optimal approach for **LeetCode 391: Perfect Rectangle**.
*   **Balanced/Robust Optimization:** Strategy 3 (Hybrid).

Choosing the right strategy requires analyzing the specific problem constraints and determining if the faster Strategy 2 provides sufficient guarantees of correctness, or if the overhead of Strategy 1 or 3 is necessary. 