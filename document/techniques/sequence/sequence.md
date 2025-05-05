# Techniques for Sequences - Overview

**Category:** Techniques (`techniques/sequence/`)

## 1. General Concept

Sequences (arrays, lists, sometimes strings) are one of the most common data structures in algorithmic problems. This section covers various techniques specifically designed for efficient processing, querying, and manipulation of sequential data.

These techniques often leverage properties like ordering (if sorted), indexing, or relative positions of elements.

## 2. Common Sequence Techniques

Here are categories of common techniques applied to sequences, with links to detailed explanations in the KB:

### a. Prefix/Suffix Computations
*   **Concept:** Pre-calculating aggregate values (sums, products, counts, etc.) for all prefixes or suffixes of a sequence to answer range queries quickly.
*   **Techniques:**
    *   Prefix Sums / Suffix Sums: [[./prefix_suffix_aggregates.md]]
    *   Applying Constraints to Prefix Sum Differences: [[./prefix_sum_difference_constraint.md]] (Useful for subarray sum problems).
    *   Difference Arrays: [[./difference_array.md]] (Efficiently apply range updates and query point values).

### b. Windowing / Pointer Techniques
*   **Concept:** Using one or more pointers to define and move a "window" or track specific positions within the sequence, often to check conditions or find optimal substructures.
*   **Techniques:**
    *   Sliding Window (See [[../../patterns/sliding_window.md]])
    *   Two Pointers (See [[../../patterns/two_pointers.md]])
    *   Finding Boundaries in Sorted Sequences:
        *   Using Two Pointers: [[./find_boundary_pointer_sorted_constraint.md]]
        *   Using Binary Search: [[./find_reach_bounds_sorted_constraint.md]]

### c. Monotonic Structures
*   **Concept:** Maintaining data structures (stacks, queues) where elements preserve a specific monotonic order (increasing or decreasing). Useful for finding nearest greater/smaller elements, range minimum/maximum queries in sliding windows, etc.
*   **Techniques:**
    *   Monotonic Queue / Deque: [[./monotonic_queue.md]]
    *   Monotonic Stack (Similar principle, often used for Next Greater/Smaller Element)

### d. Hashing / Marking In-Place
*   **Concept:** Using the array indices or values themselves to store information (hashing) or mark elements as visited/processed, often to achieve O(1) space complexity.
*   **Techniques:**
    *   In-Place Array Hashing (Cycle Sort variant / Index Marking): [[./in_place_array_hashing.md]]

### e. Dynamic Programming State Techniques
*   **Concept:** Specific ways to define or manage state when applying Dynamic Programming to sequence problems.
*   **Techniques:**
    *   Using Maps for Pairwise Relations: [[./dp_map_state_for_pairwise_relations.md]]

### f. Parsing / Sequential Processing
*   **Concept:** Techniques focused on processing sequences strictly according to their order, often for validation or specific calculations.
*   **Techniques:**
    *   Strict Sequential Parsing: [[./strict_sequential_parsing.md]]

## 3. Choosing the Right Technique

Consider:
*   Is the sequence sorted? (Enables binary search, two pointers for boundary finding).
*   Are range queries (sum, min/max) needed? (Consider prefix sums, segment trees, monotonic structures).
*   Are range updates needed? (Consider difference arrays, segment trees).
*   Do you need to find properties related to adjacent elements or subarrays/subsequences? (Sliding window, two pointers, DP).
*   Are constraints on space tight? (Consider in-place techniques).

Explore the linked documents for details on specific techniques and their applications. 