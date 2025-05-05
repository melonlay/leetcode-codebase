# Optimization: Calculating Final Sequence Size After Local Reductions

## Context

This describes optimizations applicable when the goal is to determine the final **scalar count** (e.g., number of elements, segments, blocks) of a sequence after it undergoes a series of reduction/merge/consolidation operations based on **local conditions**, where merges replace segments with a single derived value (often the maximum).

Instead of fully simulating the construction of the final sequence, we can sometimes use more direct methods.

## Problem Archetype

*   **Input:** A sequence (e.g., array `nums`).
*   **Operation:** Repeatedly apply a reduction operation based on a local condition between adjacent or nearby elements (e.g., merge `nums[i]` and `nums[i+1]` if `condition(nums[i], nums[i+1])` is true). The merge replaces the involved elements with a single derived value (e.g., `max` or some other function).
*   **Goal:** Find the final **size** (number of elements) of the sequence after the operations stabilize or are applied exhaustively.

## Applicability Conditions for Optimized Counting

Optimized approaches (Strategies 2 & 3) are suitable when:

1.  **Goal is Count Only:** The final sequence content itself is *not* required.
2.  **Local Trigger:** Reduction operations are triggered based on local conditions.
3.  **(For Strategy 2 - Counting Reductions):** The final size = initial size - number of reductions, AND the local effect of reductions can be simulated for subsequent checks.
4.  **(For Strategy 3 - Greedy Scan):** The final count can be built incrementally by tracking the state/value of the *last* element in the conceptual final sequence.

## Strategies Compared

### Strategy 1: Full Simulation (e.g., Stack-Based)

*   **Idea:** Directly simulate the process of applying reductions and building the final sequence.
*   **Implementation:** Often uses a stack/list. Iterate through input, apply merge logic when conditions met, modify the auxiliary structure (e.g., pop and push `max`).
*   **Pros:** Constructs the final sequence. Necessary if sequence content is needed.
*   **Cons:** Overhead from data structure operations (pushes, pops, allocations). O(N) extra space.
*   **Complexity:** Typically O(N) Time, O(N) Space.
*   **Reference:** [[../../data_structures/stack.md]]

### Strategy 2: Counting Reductions

*   **Idea:** Calculate final size as `initial_size - total_necessary_reductions`. Count reduction events.
*   **Implementation:** Iterate through sequence, check local reduction condition. If triggered:
    *   Decrement `final_size` counter.
    *   **Crucially:** Simulate the local effect if it impacts subsequent checks (e.g., update `nums[i+1]` in-place).
*   **Example (LC 3523):** Iterate `i` from 0 to `n-2`. If `nums[i] > nums[i+1]`, decrement `final_size`, set `nums[i+1] = nums[i]`.
*   **Pros:** Avoids auxiliary data structure. Faster constant factors than simulation. O(1) additional space if in-place modification allowed.
*   **Cons:** Only calculates size. Modifies input (or needs copy).
*   **Complexity:** Typically O(N) Time, O(1) Space (if in-place allowed).

### Strategy 3: Greedy Scan (Direct Count Construction) - Often Best

*   **Idea:** Directly count the elements that *will* form the final sequence without explicitly simulating merges or counting reductions.
*   **Implementation:** Iterate through the input sequence, maintaining the state/value of the *last element* added to the conceptual final sequence (`last_val`). If the current element `num` meets the condition to be the *next* element (e.g., `num >= last_val` for non-decreasing), increment the final count and update `last_val`.
*   **Example (LC 3523):** Initialize `count = 0`, `last_max = -infinity` (or 0 if nums >= 1). Iterate `num` in `nums`. If `num >= last_max`, increment `count`, set `last_max = num`.
*   **Pros:** Usually the simplest logic. Often the fastest constant factors (single pass, minimal operations). O(1) additional space. Does not modify input.
*   **Cons:** Only calculates size.
*   **Complexity:** O(N) Time, O(1) Space.

## Performance Comparison

*   **Strategy 3 (Greedy Scan)** is typically the most performant and space-efficient when applicable, as it involves a single pass with minimal state.
*   **Strategy 2 (Counting Reductions)** is generally faster than Strategy 1 but slower than Strategy 3, and requires careful handling of effect propagation (e.g., in-place modification).
*   **Strategy 1 (Full Simulation)** is the most general but often the slowest due to data structure overhead.

## Recommendation

*   **If only the final size/count is needed:**
    1.  **Attempt Strategy 3 (Greedy Scan) first.** Can you formulate a greedy rule based on the last accepted element?
    2.  If Strategy 3 is difficult or seems incorrect, consider **Strategy 2 (Counting Reductions)**. Can you count reduction triggers and simulate local effects?
*   **If the actual final sequence is needed:** Use **Strategy 1 (Full Simulation)**.

## Related Concepts

*   Simulation
*   Greedy Algorithms
*   Sequence Processing
*   In-place Algorithms
*   [[../../data_structures/stack.md]] (Often used in Strategy 1) 