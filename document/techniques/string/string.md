# Techniques for Strings - Overview

**Category:** Techniques (`techniques/string/`)

## 1. General Concept

Strings are sequences of characters, and many algorithmic problems involve processing, matching, searching, or transforming them. This section covers techniques specifically tailored for efficient string manipulation.

## 2. Common String Techniques

Here are categories of common techniques applied to strings, with links to detailed explanations in the KB where available:

### a. Pattern Matching
*   **Concept:** Finding occurrences of a smaller string (pattern) within a larger string (text).
*   **Techniques:**
    *   Knuth-Morris-Pratt (KMP): Efficiently searches for a pattern using a precomputed prefix function (LPS array). [[../../algorithms/string/kmp.md]]
    *   String Hashing (Rabin-Karp): Compares hash values of substrings to quickly identify potential matches. [[./string_hashing.md]]
    *   Naive Brute-Force (Less efficient, O(N*M)).
    *   Specialized Algorithms (e.g., Aho-Corasick for multiple patterns, Suffix Arrays/Trees for advanced searching).

### b. Palindrome Detection/Processing
*   **Concept:** Identifying strings or substrings that read the same forwards and backwards.
*   **Techniques:**
    *   Expand From Center: Efficiently finds all palindromic substrings by expanding outwards from each possible center (single characters and pairs). [[./expand_from_center.md]]
    *   Manacher's Algorithm: Linear time algorithm for finding the longest palindromic substring.

### c. Substring/Subsequence Problems
*   **Concept:** Problems involving properties of contiguous (substring) or non-contiguous (subsequence) parts of a string.
*   **Techniques:** Often involve DP [[../../algorithms/dynamic_programming/dynamic_programming.md]], Sliding Window [[../../patterns/sliding_window.md]], or Two Pointers [[../../patterns/two_pointers.md]]. See also [[../sequence/sequence.md]] for general sequence techniques.

### d. String Comparison & Edit Distance
*   **Concept:** Measuring the similarity or difference between two strings.
*   **Techniques:**
    *   Levenshtein Distance (Edit Distance): Minimum number of single-character edits (insertions, deletions, substitutions) required to change one word into the other. Typically solved with DP.

### e. String Manipulation & Parsing
*   **Concept:** Basic operations like concatenation, splitting, reversing, and parsing structured string formats.
*   **Techniques:** Often rely on built-in language functions, but performance considerations (e.g., concatenation overhead) are important. See [[../../optimizations/string/string_concatenation.md]], [[../../optimizations/string/string_vs_list_manipulation.md]].

## 3. Choosing the Right Technique

Consider:
*   Are you searching for a specific pattern? (KMP, Hashing).
*   Are palindromes involved? (Expand From Center, Manacher's).
*   Does it involve comparing substrings or finding optimal subsequences? (DP, Sliding Window).
*   Are you measuring similarity/difference? (Edit Distance DP).

Explore the linked documents and potentially the `algorithms/string/` and `optimizations/string/` directories for more details. 