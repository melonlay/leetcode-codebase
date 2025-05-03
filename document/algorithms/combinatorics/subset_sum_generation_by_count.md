# Algorithm: Subset Sum Generation (Grouped by Count)

**Related Problems:** Subset Sum, Knapsack variations, Meet-in-the-Middle

## Description

This algorithm generates all possible subset sums from a given set of numbers (`arr`) and organizes these sums based on the number of elements (`k`) used to form each sum. This is particularly useful as a sub-routine in algorithms like Meet-in-the-Middle (e.g., Problem 2035) where constraints apply not only to the sum but also to the size of the subset.

## Core Idea

Iteratively build up the possible sums. Start with the base case (sum 0 using 0 elements). Then, for each number `x` in the input array, update the existing sums by adding `x` to them. The key is to track both the sum and the number of elements used to achieve it.

## Algorithm Steps (Iterative DP-like approach)

There are two common iterative ways to implement this:

### Method 1: Using a Temporary Dictionary

1.  **Initialization:** `sums_by_count = defaultdict(set)`, `sums_by_count[0] = {0}`.
2.  **Iteration:** For each element `x` in `arr`:
    *   Create `new_sums_this_step = defaultdict(set)`.
    *   Iterate counts `k` from `0` upwards.
    *   If `sums_by_count[k]` exists, for each `s` in it, add `s + x` to `new_sums_this_step[k + 1]`.
    *   After iterating through all `k`, merge `new_sums_this_step` into `sums_by_count`.
3.  **Result:** `sums_by_count`.

### Method 2: In-Place Update with Downward Iteration (Often Faster)

1.  **Initialization:** `sums_by_count = defaultdict(set)`, `sums_by_count[0] = {0}`.
2.  **Iteration:** For each element `x` in `arr`:
    *   Iterate counts `k` **downwards** (e.g., from `len(arr)-1` down to `0`).
    *   If `sums_by_count[k]` exists:
        *   Use `sums_by_count[k+1].update({s + x for s in sums_by_count[k]})`.
        *   The downward iteration ensures that `sums_by_count[k]` contains sums from the state *before* processing `x` when calculating the sums for `k+1` in the current step.
3.  **Result:** `sums_by_count`.

**Recommendation:** Method 2 generally avoids the overhead of creating and merging temporary dictionaries in each iteration and may perform better in practice.

## Implementation (Python Example - Method 2)

```python
from collections import defaultdict
from typing import List, Dict, Set

def get_subset_sums_by_count(arr: List[int]) -> Dict[int, Set[int]]:
    sums_by_count = defaultdict(set)
    sums_by_count[0].add(0)
    n_half = len(arr)

    for x in arr:
        for k in range(n_half - 1, -1, -1):
            if sums_by_count[k]:
                sums_by_count[k + 1].update({s + x for s in sums_by_count[k]})

    return sums_by_count
```

## Complexity

Let `N = len(arr)`.

*   **Time Complexity:** O(N * 2^N). In the worst case, the number of distinct subset sums for each count can grow up to `C(N, k)`. The outer loop runs `N` times. The inner loops iterate through existing counts and sums. The total number of sum entries across all counts is `2^N`. Updating the sets takes roughly constant time on average. Therefore, the complexity is dominated by generating and storing the `2^N` possible sums.
*   **Space Complexity:** O(2^N). Storing all possible subset sums requires space proportional to the total number of subsets.

## When to Use

*   As a preprocessing step for Meet-in-the-Middle algorithms where the number of elements in the chosen subsets matters.
*   When you need to know all achievable sums for subsets of *specific sizes*.

## Related Concepts

*   Subset Sum Problem
*   Dynamic Programming (can be viewed as a DP state transition)
*   Meet-in-the-Middle Pattern [[../../patterns/divide_and_conquer/meet_in_the_middle.md]] 