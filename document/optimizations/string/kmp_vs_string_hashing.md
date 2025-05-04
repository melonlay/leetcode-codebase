# Optimization Comparison: KMP vs. String Hashing for Pattern Matching

**Related:** [[../../algorithms/string/kmp.md]], [[../../techniques/string/string_hashing.md]]

## 1. Problem Context

When faced with the task of finding occurrences of a pattern string `P` (length `M`) within a text string `T` (length `N`), two common and efficient approaches are the Knuth-Morris-Pratt (KMP) algorithm and String Hashing (often used within the Rabin-Karp algorithm).

This document compares their trade-offs.

## 2. Comparison

| Feature                 | KMP Algorithm                                  | String Hashing (Polynomial Rolling Hash)          |
| :---------------------- | :--------------------------------------------- | :----------------------------------------------- |
| **Time Complexity**     | **O(N + M)** (Deterministic Worst-Case)        | **O(N + M)** (Expected / Average Case)            |
|                         |                                                | O(N * M) worst-case (highly unlikely w/ good hash) |
| **Space Complexity**    | **O(M)** (For LPS array)                       | **O(N)** (For text prefix hashes & base powers)   |
| **Correctness**         | **Deterministic** (Always correct)             | **Probabilistic** (Risk of hash collisions)       |
| **Implementation**    | Moderately Complex (LPS array logic)           | Generally Simpler (Hash formula, precomputation) |
| **Online Processing**   | Yes (Can process text as it arrives)           | Yes (Can process text as it arrives)           |
| **Multiple Patterns**   | Less direct (Need separate runs or Aho-Corasick) | Easier (Precompute text hash once, compare many pattern hashes) |
| **Substring Operations**| Focused only on full pattern match             | Easily adapted for various substring comparisons (equality, palindromes) |

## 3. Detailed Trade-offs

*   **Correctness Guarantee:** KMP's primary advantage is its deterministic guarantee. It *will* find all occurrences and have no false positives. String Hashing relies on the low probability of collisions; for competitive programming or scenarios where absolute correctness is paramount, KMP or String Hashing with verification/double hashing is preferred.
*   **Performance in Practice:** String Hashing can often be slightly faster in typical competitive programming scenarios due to simpler constant factors in its O(N) loop compared to KMP's potentially more complex inner loop logic, *despite* KMP having a better worst-case guarantee. However, performance depends heavily on implementation and specific data.
*   **Space:** String Hashing requires O(N) space for the precomputed hashes of the *text*, while KMP only needs O(M) space for the LPS array of the *pattern*. This can be significant if the text is very large and memory is constrained.
*   **Ease of Implementation:** Many find the core logic of polynomial hashing and its O(1) substring retrieval easier to implement correctly than the LPS array construction for KMP.
*   **Flexibility:** String Hashing provides O(1) lookup for *any* substring's hash after precomputation, making it useful for a wider range of substring-related problems beyond just finding a single pattern.
*   **Collision Risk (Hashing):** This is the main drawback. While collisions are rare with large prime BASE/MOD pairs (especially 64-bit hashes or double hashing), they *can* happen. Test cases can sometimes be designed to exploit common BASE/MOD choices.

## 4. When to Choose Which

*   **Choose KMP when:**
    *   Absolute correctness is required without relying on probability.
    *   Memory usage for the text (O(N)) is a major concern.
    *   You only need to find occurrences of a specific, fixed pattern.
*   **Choose String Hashing when:**
    *   A small probability of collision is acceptable, or mitigation (like double hashing) is used.
    *   Implementation simplicity or potentially slightly faster average-case performance is desired.
    *   You need to compare many different substrings efficiently (not just search for one pattern).
    *   You need to search for multiple patterns in the same text (precompute text hash once).
    *   Memory usage for O(N) precomputation is acceptable.

## 5. Example Application

*   LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings - Both KMP and String Hashing are viable approaches, demonstrating the trade-offs. KMP guarantees correctness, while String Hashing offers a simpler implementation path if collision risks are accepted/mitigated. 