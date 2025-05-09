# Iterative Set Construction for Unique XOR Triplets

**Concept Type:** Optimization / Algorithmic Technique

**Applies to:** Problems requiring the set of unique XOR sums of k-tuples (e.g., triplets) from an array, especially with ordered index constraints like \(i \le j \le k\).

**Core Idea:**
Instead of pre-calculating all possible pairs and then combining with a third element (which might involve iterating over a large theoretical maximum range of XOR values), this technique iteratively builds up sets of achievable XOR sums. It dynamically uses the size of currently found XOR sums, which can be much smaller than the theoretical maximum, leading to significant practical speedups, especially in languages like Python where iteration overhead matters.

**Problem Context Example (LC3514 - Number of Unique XOR Triplets II):**
Given `nums`, find the number of unique values for `nums[i] ^ nums[j] ^ nums[k]` where `i <= j <= k`.

**Optimized Algorithm Steps:**

1.  **Initialization:**
    *   `xorPairs = {0}`: This set will store unique XOR sums of two elements \(nums[a] \oplus nums[b]\) where \(a < b\) from the prefix of `nums` processed so far. The initial `0` is crucial for handling cases involving repeated elements (e.g., to help form \(X \oplus Y \oplus Y = X\) when processing \(X\)).
    *   `xorTriplets = set(nums)`: This set will store the final unique triplet XOR sums. It's initialized with `nums` because any element `x` in `nums` can be formed as a triplet \(x \oplus x \oplus x = x\). This also covers cases like \(x \oplus y \oplus y = x\).
    *   `limit = 1 << max(nums).bit_length()` (or `1 << max(xorTriplets).bit_length()` if `nums` can be empty/all zero):
        This is an early exit condition. If the numbers in `nums` (and their combinations) can generate all \(2^k\) possible XOR sums (where \(k\) is the bit length of the maximum value in `nums`), then `limit` is the maximum possible number of unique XOR sums. Any XOR sum involving these numbers will be less than this `limit`.

2.  **Iteration:**
    Iterate through `nums` with index `idx` and current element `num = nums[idx]`:
    *   **(a) Form Triplets:** `xorTriplets.update(map(num.__xor__, xorPairs))`
        At the beginning of iteration `idx` (processing `num = nums[idx]`):
        *   `xorPairs` contains `0`.
        *   `xorPairs` also contains all unique values of `nums[a] ^ nums[b]` such that `a < b < idx` (from previous iterations).
        This step effectively does:
        *   `num \oplus 0 = num`: Added to `xorTriplets`. This correctly handles cases like `nums[idx] \oplus nums[x] \oplus nums[x] = nums[idx]` for any `x \le idx` (satisfying `i=x, j=x, k=idx` or `i=idx, j=idx, k=idx`).
        *   `num \oplus (nums[a] \oplus nums[b])`: Added to `xorTriplets`. This forms `nums[a] \oplus nums[b] \oplus nums[idx]` where `a < b < idx`. This satisfies the `i \le j \le k` constraint.
    *   **(b) Update Pair XORs for Next Iterations:** `xorPairs.update(map(num.__xor__, islice(nums, 0, idx)))`
        This adds all values `num \oplus nums[j]` (where `j < idx`) to `xorPairs`. After this, `xorPairs` will contain `0` and all unique `nums[a] \oplus nums[b]` where `a < b \le idx`, making them available for the *next* element `nums[idx+1]` to form triplets.
    *   **(c) Early Exit:** `if len(xorTriplets) >= limit: return limit`
        If the number of unique triplet XORs found reaches the theoretical maximum possible for the given range of numbers, no more unique values can be found, so we can stop.

3.  **Result:** `return len(xorTriplets)`

**Why it Correctly Handles \(i \le j \le k\) for Unique Values:**
The process ensures that when `nums[k]` (the element `num` at outer loop index `k`) is considered:
*   Triplets of the form `nums[k] \oplus nums[k] \oplus nums[k]` (i.e., `num`) are covered by the initialization of `xorTriplets` or by `num \oplus 0`.
*   Triplets like `nums[i] \oplus nums[i] \oplus nums[k]` (for `i < k`) and `nums[i] \oplus nums[k] \oplus nums[k]` (for `i < k`) result in `nums[k]` and `nums[i]` respectively. These are covered by `xorTriplets` initialization or `num \oplus 0` for `nums[k]`, and `nums[i]` is already in `xorTriplets`.
*   Triplets `nums[i] \oplus nums[j] \oplus nums[k]` with `i < j < k`: The pair `nums[i] \oplus nums[j]` would have been added to `xorPairs` when `nums[j]` was processed. So, when `nums[k]` is processed, this pair XOR sum is in `xorPairs`, and `nums[k] \oplus (nums[i] \oplus nums[j])` is computed and added.

The key is that the iteration and set updates ensure that combinations are formed respecting the non-decreasing order of indices for generating the *set of unique values*. The exact combination of indices might differ, but the resulting value is what matters for the set.

**Performance Benefits:**
*   **Dynamic Iteration:** The step `xorTriplets.update(map(num.__xor__, xorPairs))` iterates over `len(xorPairs)` elements, not a fixed `MAX_XOR_VAL`. If the number of distinct pair XORs is sparse, this is much faster.
*   **Early Exit:** The `limit` condition can terminate the process very quickly if numbers in `nums` have good bit coverage.
*   **Python Optimizations:** Uses efficient set operations and `map`.

**Complexity Analysis:**
*   **Time:** The outer loop runs \(N\) times.
    *   `xorTriplets.update(...)`: In iteration `idx`, `len(xorPairs)` can be up to \(O(idx^2)\) in theory but capped by `MAX_XOR_VAL` (e.g., 2048). So this part is effectively \(O(N \cdot \min(idx^2, MAX\_XOR\_VAL))\) in total, roughly \(O(N \cdot MAX\_XOR\_VAL)\) in the worst-case sum over all iterations.
    *   `xorPairs.update(...)`: This loop iterates `idx` times. Summing from `idx=0` to `N-1` gives \(O(N^2)\) for this part across all outer loops.
    *   Worst-case asymptotic complexity is still \(O(N^2 + N \cdot MAX\_XOR\_VAL)\).
    *   However, the average-case performance is often much better due to the size of `xorPairs` potentially being small and the early exit.
*   **Space:** \(O(MAX\_XOR\_VAL)\) for `xorPairs` and `xorTriplets` in the worst case.

**Comparison to Static Precomputation:**
This iterative approach contrasts with methods that first compute all \(N^2\) pair XORs and their minimum second indices, and then iterate \(N \cdot MAX\_XOR\_VAL\) times. The dynamic nature and early exit give this method a significant edge in practice for Python.

**KB Location Suggestion:** `document/optimizations/combinatorics/iterative_set_construction_xor_triplets.md` 