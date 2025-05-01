# Lexicographical Merge Technique

## Description

This technique describes how to merge two sequences (often, but not necessarily, sorted or derived from some greedy selection process like finding maximum subsequences) into a single sequence that is lexicographically maximal (or minimal).

It's commonly used as a sub-step in problems where optimal subsequences are generated independently and then need to be combined optimally (e.g., LeetCode 321. Create Maximum Number).

## Core Idea (Maximization)

Given two input sequences, `seq1` and `seq2`, we want to build a merged sequence `merged` by repeatedly choosing the better next element from the remaining parts of `seq1` and `seq2`.

1.  Initialize `merged = []`.
2.  Use pointers `p1 = 0` for `seq1` and `p2 = 0` for `seq2`.
3.  While either `p1 < len(seq1)` or `p2 < len(seq2)`:
    *   **Compare Remaining Suffixes:** Compare `seq1[p1:]` with `seq2[p2:]` lexicographically.
    *   **Append Larger:** If `seq1[p1:] > seq2[p2:]`, append `seq1[p1]` to `merged` and increment `p1`.
    *   Otherwise (if `seq2[p2:] >= seq1[p1:]`), append `seq2[p2]` to `merged` and increment `p2`.

**Why compare suffixes?** Consider `seq1 = [6, 7]` and `seq2 = [6, 0, 4]`. If we only compared `seq1[p1]` and `seq2[p2]`, we'd see `6 == 6`. We wouldn't know whether to take the 6 from `seq1` (leaving `[7]`) or `seq2` (leaving `[0, 4]`). Comparing the suffixes `[6, 7]` vs `[6, 0, 4]` tells us `[6, 7]` is lexicographically larger, so we should take the 6 from `seq1` first.

## Implementation (Python)

```python
def merge_lexicographical_max(seq1, seq2):
    merged = []
    p1, p2 = 0, 0
    n1, n2 = len(seq1), len(seq2)
    
    while p1 < n1 or p2 < n2:
        # Direct comparison of slices/tuples works for lexicographical order
        if seq1[p1:] > seq2[p2:]:
            merged.append(seq1[p1])
            p1 += 1
        else:
            merged.append(seq2[p2])
            p2 += 1
    return merged

# Example from LeetCode 321
sub1 = [6, 5] # max subsequence of length 2 from [3, 4, 6, 5]
sub2 = [9, 8, 3] # max subsequence of length 3 from [9, 1, 2, 5, 8, 3]
result = merge_lexicographical_max(sub1, sub2)
print(result) # Output: [9, 8, 6, 5, 3]
```

## Complexity

*   **Time Complexity:** O(K * (K)), where `K = len(seq1) + len(seq2)`. In each step of the `while` loop (which runs K times), the suffix comparison (`seq1[p1:] > seq2[p2:]`) can take up to O(K) time in the worst case. Therefore, the naive implementation is O(K^2).
    *   **Optimization:** While Python's slice comparison is convenient, a more efficient O(K) implementation is possible by writing a custom comparison function that compares elements one by one only as needed, avoiding repeated full suffix comparisons.
*   **Space Complexity:** O(K) for storing the `merged` list.

## Use Cases

*   Combining optimal subsequences while maintaining lexicographical order (e.g., LeetCode 321).
*   Any scenario requiring merging sequences based on future element potential rather than just the current element.

## Related Concepts

*   **Algorithm:** [Greedy Algorithms](../../algorithms/greedy/greedy.md) (Often used to generate the input sequences `seq1`, `seq2`).
*   **Technique:** [Monotonic Queue](./monotonic_queue.md) (Can be used to generate maximal subsequences). 