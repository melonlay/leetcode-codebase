# Mathematical Concept: Combinations with Repetition (Stars and Bars)

## Description

Combinations with repetition address the problem of selecting `k` items from a set of `n` distinct types of items, where repetition is allowed and the order of selection does not matter. This is often visualized using the "Stars and Bars" method.

Imagine we have `k` identical items (stars: `*`) to be placed into `n` distinct bins (representing the item types). To separate the items into bins, we need `n-1` dividers (bars: `|`).

For example, selecting `k=3` items from `n=4` types (A, B, C, D) could be represented as:
`* | * * | | ` (1 A, 2 B, 0 C, 0 D)
`| | * * * | ` (0 A, 0 B, 3 C, 0 D)

The problem then becomes arranging `k` stars and `n-1` bars in a sequence. The total number of positions is `k + (n-1)`. We need to choose `k` positions for the stars (or `n-1` positions for the bars).

## Formula

The number of ways to choose `k` items from `n` types with repetition allowed is given by:

\[ CWR(n, k) = \\binom{n+k-1}{k} = \\binom{n+k-1}{n-1} = \\frac{(n+k-1)!}{k!(n-1)!} \]

Where `C(N, K)` or `\\binom{N}{K}` represents the standard binomial coefficient ("N choose K").

## Use Cases

*   Counting solutions to equations like `x_1 + x_2 + ... + x_n = k` where `x_i >= 0` are integers.
*   Counting ways to distribute `k` identical items into `n` distinct boxes.
*   **Counting non-decreasing sequences:** Counting non-decreasing sequences of length `k` using digits from `0` to `m` (inclusive) is equivalent to choosing `k` items from `m+1` types (the digits) with repetition. The count is `CWR(m+1, k) = C(m+1 + k - 1, k) = C(m+k, k)`.
*   **Counting positive non-decreasing sequences:** Counting non-decreasing sequences of length `k` using *positive* digits from `1` to `m` (inclusive) is equivalent to choosing `k` items from `m` types (digits 1 to m) with repetition. The count is `CWR(m, k) = C(m + k - 1, k)`.

## Implementation

Requires an efficient way to calculate binomial coefficients `nCr`, often modulo a large prime.

## Related Concepts

*   [[../../techniques/combinatorics/iterative_nCr_modulo.md]] (For calculating `nCr % M`)
*   Standard Combinations (without repetition) 