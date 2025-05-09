# DP Optimization: State Packing with Bit Manipulation

**Category:** Optimizations (`optimizations/dynamic_programming/`)

## 1. Concept

This technique optimizes Dynamic Programming implementations where the state involves a small, fixed number (`k`) of counters or values that need to be updated simultaneously during transitions. Instead of using an array or dictionary of size `k` to store these counters, they are "packed" into different bit blocks within a single large integer. Transitions are then performed using efficient bitwise operations (shifts and masks).

This is particularly effective when `k` is small (e.g., up to ~60, depending on the required counter size) and the DP involves iterating through a large sequence (`n`), making the constant factor overhead of the DP state update significant.

## 2. Mechanism

1.  **Choose Block Size (`b`):** Determine the maximum possible value any single counter can reach during the computation. Choose a number of bits `b` such that `2^b - 1` is greater than or equal to this maximum value. `b` must be large enough to prevent overflow within a block.
2.  **State Representation (`t`):** A single large integer `t` represents the entire DP state. The state corresponding to remainder `i` (or the `i`-th counter) is stored in the bits from `i*b` to `(i+1)*b - 1`.
3.  **Mask (`m`):** Define a mask `m = (1 << b) - 1`. This mask isolates the lowest `b` bits.
4.  **Extracting State `i`:** To get the value of the counter for state `i`, right-shift `t` by `i*b` bits and apply the mask: `count_i = (t >> (i * b)) & m`.
5.  **Placing State `i`:** To place a value `v` into the block for state `i`, left-shift `v` by `i*b` bits: `v << (i * b)`.

## 3. DP Transition Example (Subarray Product Modulo k)

Consider the problem of finding counts of subarrays ending at index `j` whose product modulo `k` is `r`, for `r` from `0` to `k-1`. (LC 3524)

*   Let `t` store the packed counts for subarrays ending at `j-1`. The `i`-th block (`(t >> (i*b)) & m`) holds the count for remainder `i`.
*   Let `x = nums[j]`. We want to compute `next_t` for subarrays ending at `j`.
*   Iterate through previous remainders `i` from `0` to `k-1`:
    *   Extract the count for remainder `i`: `count_i = (t >> (i * b)) & m`.
    *   Calculate the new remainder if extended by `x`: `new_r = (i * x) % k`.
    *   Shift `count_i` to the block corresponding to `new_r`: `shifted_count = count_i << (b * new_r)`.
*   Sum all `shifted_count` values for `i=0..k-1`. This represents the contribution from extending previous subarrays.
*   Calculate the contribution from the single-element subarray `[x]`. Its remainder is `x % k`. The count is 1. Represent this as `1 << (b * (x % k))`.
*   `next_t = sum(shifted_counts) + (1 << (b * (x % k)))`.

**Code Example (Python, k=5, b=33):**

```python
# nums: input array
# k: modulus (e.g., 5)
# b: bit block size (e.g., 33)
# m: mask ((1 << b) - 1)

t = 0 # Stores packed counts for subarrays ending at j-1
r = 0 # Stores packed *total* counts across all j

for x_val in nums:
    x_mod_k = x_val % k
    
    # Calculate contribution from extending previous subarrays
    sum_shifted_counts = 0
    for i in range(k):
        # Extract count for previous remainder i
        count_i = (t >> (b * i)) & m
        if count_i > 0:
            # Calculate new remainder
            new_r = (i * x_mod_k) % k
            # Shift count to the new remainder's block
            sum_shifted_counts += (count_i << (b * new_r))
            
    # Calculate contribution from the single element subarray [x_val]
    single_element_term = (1 << (b * x_mod_k))
    
    # Update t for the current position j
    t = sum_shifted_counts + single_element_term
    
    # Accumulate total counts
    r += t

# Extract final results for each remainder i
final_counts = [(r >> (i * b)) & m for i in range(k)]
# return final_counts
```

## 4. Benefits and Limitations

*   **Benefit:** Can provide a significant constant factor speedup compared to standard DP using arrays/maps, especially when `n` is large and `k` is small. Bitwise operations are generally faster than array indexing and arithmetic in loops within interpreted languages like Python.
*   **Benefit:** Can reduce space complexity to O(1) (excluding input/output) if only the single integer state is needed.
*   **Limitation:** Only practical when the number of states to pack (`k`) is relatively small (fits within standard integer types, e.g., 64-bit).
*   **Limitation:** The maximum value for each counter must be known or bounded to choose an adequate block size `b`. The total number of bits `k * b` must not exceed the limits of the integer type used.
*   **Limitation:** Can make the code less immediately readable than a straightforward array-based DP state.

## 5. Comparison to Standard DP

The standard approach uses an array `dp = [0] * k`. The transition involves a loop:

```python
new_dp = [0] * k
for r_prev in range(k):
    if dp[r_prev] > 0:
        new_r = (r_prev * x_mod_k) % k
        new_dp[new_r] += dp[r_prev]
new_dp[x_mod_k] += 1
dp = new_dp
# result[r] += new_dp[r] for r in range(k)
```

Both approaches have a time complexity of O(n * k). The state packing method replaces the O(k) array operations in the inner loop with O(k) bitwise operations, often resulting in better performance.

## 6. Related Concepts

*   [[../../algorithms/dynamic_programming/dynamic_programming.md]]
*   Bit Manipulation Techniques 