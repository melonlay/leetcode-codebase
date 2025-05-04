# Technique: String Hashing (Polynomial Rolling Hash)

**Related:** String Searching, Pattern Matching, Rabin-Karp Algorithm

## 1. Description

String Hashing, specifically Polynomial Rolling Hashing, is a technique used to assign a numerical value (hash) to a string or substring, allowing for fast comparisons. It enables checking if two strings are equal in O(1) expected time (after initial O(N) precomputation) by comparing their hash values.

It's a key component of the Rabin-Karp algorithm for pattern searching and useful in various problems involving substring comparisons, palindrome detection, or finding duplicate strings.

## 2. Core Idea: Polynomial Rolling Hash

The hash of a string `S = s_0 s_1 ... s_{n-1}` is calculated as:

`hash(S) = (s_0 * BASE^{n-1} + s_1 * BASE^{n-2} + ... + s_{n-1} * BASE^0) % MOD`

Where:
*   `s_i`: Typically the integer representation of the character (e.g., `ord(character)`).
*   `BASE`: A chosen base number (a prime number larger than the alphabet size is recommended).
*   `MOD`: A chosen modulus (a large prime number is recommended to reduce collisions).

## 3. Precomputation for Efficient Substring Hashing

To quickly calculate the hash of any substring `S[l...r]`, we precompute:

1.  **Prefix Hashes (`h`):** `h[i]` stores the hash of the prefix `S[0...i-1]`. Size `N+1`.
    `h[0] = 0`
    `h[i] = (h[i-1] * BASE + ord(S[i-1])) % MOD` for `i > 0`.
2.  **Base Powers (`p`):** `p[i]` stores `BASE^i % MOD`. Size `N+1`.
    `p[0] = 1`
    `p[i] = (p[i-1] * BASE) % MOD` for `i > 0`.

*   **Time Complexity:** O(N) where N is the length of the main string.
*   **Space Complexity:** O(N)

## 4. O(1) Substring Hash Calculation (`get_hash(l, r)`)

Using the precomputed `h` and `p` arrays, the hash of the substring `S[l...r]` (inclusive, length `L = r - l + 1`) can be calculated in O(1) time:

`hash(S[l...r]) = (h[r+1] - h[l] * p[L]) % MOD`

*   **Explanation:** `h[r+1]` contains the hash of `S[0...r]`. `h[l]` contains the hash of `S[0...l-1]`. We need to subtract the hash of the prefix `S[0...l-1]` from `h[r+1]`, but adjusted by the correct power of `BASE` to align it. `h[l]` needs to be multiplied by `BASE^L` (which is `p[L]`) because its characters are `L` positions shifted to the left relative to their positions in `h[r+1]`. The modulo operation handles potential negative results correctly in most languages (or requires `+ MOD` before the final `% MOD`).

## 5. BASE and MOD Selection

*   **Goal:** Minimize hash collisions (different strings having the same hash).
*   **`BASE`:** Should be larger than the size of the character set (e.g., > 256 for ASCII). Common choices are primes like 31, 131, 131313.
*   **`MOD`:** Should be a large prime number to distribute hashes widely. Common choices are primes around 10^9+7, 10^9+9, or even larger primes like 10^13+7 (as used in the example code) if the language supports large integers.
*   Using randomly chosen BASE/MOD can sometimes thwart adversarial test cases designed to cause collisions for common primes.

## 6. Collision Risk & Mitigation

*   **Risk:** Hash collisions are always possible, although unlikely with good BASE/MOD choices. Relying solely on hash equality means the algorithm is probabilistic, not deterministic like KMP.
*   **Mitigation:**
    *   **Double Hashing:** Use two different pairs of (BASE, MOD). Two strings are considered equal only if *both* their hashes match. This significantly reduces the collision probability.
    *   **Verification:** If absolute certainty is required, verify actual string equality after a hash match (this negates the O(1) comparison benefit).

## 7. Complexity (Rabin-Karp using Hashing)

*   **Preprocessing:** O(N + M) - O(N) for text prefix hashes, O(M) for pattern hash.
*   **Searching:** O(N) expected time. In the worst case (many collisions or a very specific pattern/text causing repeated partial matches), it can degrade, but this is rare in practice with good hashing parameters.
*   **Space:** O(N) for precomputed arrays.

## 8. Use Cases

*   Rabin-Karp pattern searching.
*   Finding duplicate substrings.
*   Palindrome checking (comparing hash of prefix with hash of reversed suffix).
*   Data structures like hash tables where string keys are used.

## 9. Example Application

*   LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings (Used instead of KMP for pattern finding) - See alternative solution provided by user.
*   Finding the longest duplicate substring in a string. 