# Technique: Binary Lifting / Sparse Table

## 1. Description

Binary Lifting (often implemented using a Sparse Table for range queries) is a technique that allows for efficient querying of information related to powers of two. It preprocesses data to answer certain types of queries in logarithmic or constant time.

Common applications include:
*   Finding the k-th ancestor of a node in a tree (Level Ancestor Problem).
*   Finding the Lowest Common Ancestor (LCA) of two nodes in a tree.
*   Answering range queries (like min, max, sum, gcd) on a static array where the combining operation is associative and ideally idempotent (for O(1) range queries) or just associative (for O(log N) range queries).
*   Solving problems involving repeated application of a function (finding `f^k(x)`).
*   Finding minimum steps/jumps based on precomputed single steps (as seen in [[binary_lifting_min_steps_on_ranges.md]]).

## 2. Core Concept

The fundamental idea is to precompute values for intervals or jumps of sizes that are powers of two (1, 2, 4, 8, ...). A query involving an arbitrary range or jump `k` can then be decomposed into a small number (O(log k)) of these precomputed power-of-two steps.

## 3. Implementation Variants

### a) Ancestor/Function Application (e.g., LCA, k-th Ancestor, Min Steps)

*   **Preprocessing:** Build a table `up[k][i]` (or `nxt[k][i]`, `prv[k][i]`) storing the result of applying the function/jump `2^k` times starting from state/node `i`.
    *   Base case `k=0`: `up[0][i]` stores the result of 1 jump (e.g., the parent of `i`, or `fr[i]`/`fl[i]`).
    *   Recursive step: `up[k][i] = up[k-1][ up[k-1][i] ]`. This computes the `2^k` jump by chaining two `2^(k-1)` jumps.
*   **Table Size:** `LOG x N`, where `LOG` is typically `ceil(log2(N))` or `ceil(log2(max_k))`.
*   **Preprocessing Time:** O(N log N) or O(N log K_max).
*   **Query (e.g., find k-th ancestor/jump):** Iterate through the bits of `k`. If the `j`-th bit is set, jump by `2^j` using the precomputed table: `current_node = up[j][current_node]`.
    *   **Query Time:** O(log K_max) where K_max is the maximum jump distance.
*   **Query (e.g., min steps to reach target):** Iterate `k` from `LOG-1` down to `0`. If taking a jump of `2^k` does *not* reach or overshoot the target, take the jump (`current = up[k][current]`) and add `2^k` to the count. Check the final `up[0][current]` step.
    *   **Query Time:** O(log N) or O(log K_max).

### b) Range Queries (Sparse Table - e.g., RMQ)

*   **Preprocessing:** Build a table `st[k][i]` storing the aggregate value (e.g., min, max) for the range starting at `i` of length `2^k`, i.e., `[i, i + 2^k - 1]`.
    *   Base case `k=0`: `st[0][i]` stores the value of the single element `array[i]`.
    *   Recursive step: `st[k][i] = combine( st[k-1][i], st[k-1][i + (1 << (k-1))] )`. Combines results from the two halves of length `2^(k-1)`.
*   **Table Size:** `LOG x N`.
*   **Preprocessing Time:** O(N log N).
*   **Query (Range `[L, R]`):**
    *   Find the largest `k` such that `2^k <= length = R - L + 1`.
    *   **If `combine` is idempotent (like min, max, gcd):** The answer is `combine(st[k][L], st[k][R - (1 << k) + 1])`. These two ranges of length `2^k` cover the query range `[L, R]`. Query time O(1).
    *   **If `combine` is only associative (like sum):** Decompose the range `[L, R]` into O(log N) disjoint ranges of power-of-two lengths and combine their results. Query time O(log N). (Note: Segment Trees or Fenwick Trees are often preferred for range sum).
*   **Updates:** Standard Sparse Tables do not efficiently support updates. For updates, use [[../../data_structures/segment_tree.md]] or [[../../data_structures/fenwick_tree_bit.md]].

## 4. Complexity Summary

*   **Preprocessing:** O(N log N) or O(N log K_max)
*   **Query:** O(1) (RMQ with idempotent op), O(log N) or O(log K_max) (ancestor, non-idempotent range queries, min steps)
*   **Space:** O(N log N) or O(N log K_max)

## 5. Common Mistakes

*   Off-by-one errors in range calculations or jump logic.
*   Incorrect calculation of `LOG`.
*   Handling boundary conditions (e.g., jumping beyond array bounds or tree root).
*   Using sparse table query logic for non-idempotent operations without proper range decomposition.

## 6. Related Concepts

*   [[../../data_structures/segment_tree.md]]
*   [[../../data_structures/fenwick_tree_bit.md]]
*   Lowest Common Ancestor (LCA)
*   Dynamic Programming
*   Divide and Conquer
*   [[binary_lifting_min_steps_on_ranges.md]] (Specific application) 