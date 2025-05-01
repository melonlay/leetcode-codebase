# Mathematical Concept: Factorial Number System (Factoradic)

## Abstract Definition

The **Factorial Number System**, also known as **factoradic**, is a mixed radix numeral system where the place values are successive factorials (0!, 1!, 2!, 3!, ...). Any non-negative integer can be uniquely represented in this system.

## Representation

An integer `k` can be uniquely represented in factoradic form as:

k = d<sub>n</sub> * n! + d<sub>n-1</sub> * (n-1)! + ... + d<sub>2</sub> * 2! + d<sub>1</sub> * 1! + d<sub>0</sub> * 0!

where `d<sub>i</sub>` is the *coefficient* or *digit* for the place value `i!`, and crucially, `0 <= d<sub>i</sub> <= i`. The largest coefficient `d<sub>i</sub>` is constrained by its place value index `i`.

**Example:**

The number 463 (base 10) in factoradic is:

*   4! = 24. 463 // 24 = 19 (too large, need 5!)
*   5! = 120. 463 // 120 = 3. (d<sub>5</sub> = 3). Remainder = 463 % 120 = 103.
*   4! = 24. 103 // 24 = 4. (d<sub>4</sub> = 4). Remainder = 103 % 24 = 7.
*   3! = 6. 7 // 6 = 1. (d<sub>3</sub> = 1). Remainder = 7 % 6 = 1.
*   2! = 2. 1 // 2 = 0. (d<sub>2</sub> = 0). Remainder = 1 % 2 = 1.
*   1! = 1. 1 // 1 = 1. (d<sub>1</sub> = 1). Remainder = 1 % 1 = 0.
*   0! = 1. (d<sub>0</sub> = 0).

So, 463<sub>10</sub> = 341010<sub>!</sub> (factoradic representation).

## Bijective Mapping to Permutations (Lehmer Code)

There exists a direct bijective (one-to-one) mapping between the integers from 0 to `n!-1` and the `n!` unique permutations of `n` distinct items (e.g., `[0, 1, ..., n-1]` or `[1, 2, ..., n]`).

The factoradic representation of an integer `k` (where `0 <= k < n!`) directly corresponds to the **Lehmer code** of the k-th lexicographical permutation (0-indexed).

The Lehmer code `(l<sub>n-1</sub>, l<sub>n-2</sub>, ..., l<sub>1</sub>, l<sub>0</sub>)` for a permutation `p = (p<sub>0</sub>, p<sub>1</sub>, ..., p<sub>n-1</sub>)` is defined such that `l<sub>i</sub>` is the number of elements `p<sub>j</sub>` to the right of `p<sub>i</sub>` (i.e., `j > i`) that are *smaller* than `p<sub>i</sub>`. Equivalently, `l<sub>i</sub>` can be seen as the index of `p<sub>i</sub>` within the set of remaining available elements when constructing the permutation step-by-step.

The factoradic digits `(d<sub>n-1</sub>, d<sub>n-2</sub>, ..., d<sub>1</sub>, d<sub>0</sub>)` of `k` are precisely the Lehmer code `(l<sub>n-1</sub>, l<sub>n-2</sub>, ..., l<sub>1</sub>, l<sub>0</sub>)` of the k-th permutation. That is, `d<sub>i</sub> = l<sub>i</sub>` for `i` from 0 to `n-1`.

This bijection allows us to:

1.  **Rank:** Given a permutation, find its Lehmer code, convert it to base 10 from factoradic to find its 0-based lexicographical rank `k`.
2.  **Unrank:** Given a 0-based rank `k`, convert it to factoradic to get the Lehmer code `(d<sub>n-1</sub>, ..., d<sub>0</sub>)`. Use these digits sequentially to select elements from the available set to reconstruct the k-th permutation.

## Use Cases

*   Theoretical combinatorics for analyzing and indexing permutations.
*   Algorithms for ranking and unranking permutations.
*   Generating specific permutations without iterating through others.

## Related Concepts

*   Mixed radix systems
*   Lehmer code
*   Permutation generation algorithms 