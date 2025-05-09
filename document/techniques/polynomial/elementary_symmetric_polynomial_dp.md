# Technique: Elementary Symmetric Polynomial (ESP) Computation via DP

## Description

This technique computes the k-th Elementary Symmetric Polynomial (ESP) for a set of numbers `nums = [a_0, a_1, ..., a_{n-1}]`. The k-th ESP, denoted `e_k(nums)`, is the sum of all products of combinations of `k` distinct elements chosen from `nums`.

`e_k(nums) = Sum_{0 <= i_1 < i_2 < ... < i_k < n} (a_{i_1} * a_{i_2} * ... * a_{i_k})`

Special cases:
*   `e_0(nums) = 1` (empty product)
*   `e_1(nums) = Sum(a_i)`
*   `e_n(nums) = Product(a_i)`

This technique is useful in problems requiring the sum of products of combinations, often modulo some prime.

## Generating Function Approach

The ESPs are the coefficients of the polynomial formed by the product:
`P(x) = Product_{i=0}^{n-1} (1 + a_i * x) = e_0 + e_1*x + e_2*x^2 + ... + e_n*x^n`

## Dynamic Programming Approach

We can compute the coefficients `e_k` (up to a desired `k=M`) iteratively using DP.

Let `dp[k]` be the k-th ESP `e_k` considering numbers from `nums[0]` up to `nums[i-1]`. When we consider the next number `nums[i]`, we can update the coefficients for the polynomial `Product_{j=0}^{i} (1 + a_j * x)`.

The new polynomial is `(Old Polynomial) * (1 + nums[i] * x)`.
The coefficient of `x^k` in the new polynomial (`new_dp[k]`) comes from two terms:
1.  The `x^k` term from the Old Polynomial (multiplied by 1): `dp[k]`
2.  The `x^(k-1)` term from the Old Polynomial multiplied by `nums[i] * x`: `dp[k-1] * nums[i]`

So, the transition is: `new_dp[k] = dp[k] + dp[k-1] * nums[i]`

**Implementation:**

We can compute this in place using a single DP array `dp_poly` of size `M+1`.

```python
dp_poly = [0] * (M + 1)
dp_poly[0] = 1 # e_0 is always 1

for i in range(n): # Consider nums[i]
    num_val = nums[i]
    # Iterate backwards to avoid using the updated dp_poly[j-1] in the same iteration
    for j in range(M, 0, -1):
        # dp_poly[j] represents e_j using nums[0...i-1]
        # dp_poly[j-1] represents e_{j-1} using nums[0...i-1]
        # Update dp_poly[j] to be e_j using nums[0...i]
        dp_poly[j] = (dp_poly[j] + dp_poly[j - 1] * num_val) # Add % MOD if needed
        # dp_poly[0] remains 1
```

After iterating through all `n` numbers, `dp_poly[k]` will hold the value of `e_k(nums)`.

## Complexity

*   **Time:** O(n * M), where `n` is the number of elements in `nums` and `M` is the maximum ESP index needed.
*   **Space:** O(M) for the DP array.

## Use Case Example

Calculating the sum of products of all combinations of size `M` from `nums`, often needed when converting sums over permutations to sums over combinations (e.g., dividing by `M!`). See [[../../patterns/dynamic_programming/dp_on_items_bitwise_sum_constraint.md]] M==K optimization.

## Related Concepts
*   Symmetric Polynomials
*   Generating Functions 