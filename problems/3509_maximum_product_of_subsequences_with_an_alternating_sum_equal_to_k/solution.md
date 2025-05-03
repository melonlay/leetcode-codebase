# Solution for LeetCode 3509: Maximum Product of Subsequences With an Alternating Sum Equal to K

## Problem Summary

Given an array `nums`, an integer `k`, and an integer `limit`, find a non-empty subsequence of `nums` such that:
1.  The alternating sum of the subsequence equals `k`.
2.  The product of its elements is maximized, but does not exceed `limit`.

Return this maximum product, or -1 if no such subsequence exists.
The alternating sum adds elements at even indices and subtracts elements at odd indices (0-based).

## Approach: Set-Based Dynamic Programming

This problem involves finding optimal subsequences based on two criteria (alternating sum and maximum valid product), suggesting a Dynamic Programming approach. The key challenge lies in correctly handling the product limit and the effect of multiplying by zero.

A robust way to handle this is to store **sets** of all achievable valid products for each state.

### State Definition

We use two dictionaries, representing the DP state based on the parity of the subsequence length:

*   `even_sums[sum] = {product1, product2, ...}`: Stores the set of all valid products (`0 <= product <= limit`) for subsequences of **even length** that result in an alternating `sum`.
*   `odd_sums[sum] = {product1, product2, ...}`: Stores the set of all valid products for subsequences of **odd length** that result in an alternating `sum`.

### State Transition

We iterate through each `val` in the input `nums`. In each iteration, we calculate the new states that can be formed by extending the existing subsequences (stored in `odd_sums` and `even_sums` from the *previous* iteration) with the current `val`.

1.  **Temporary Storage:** We use temporary dictionaries (`new_odd_sums`, `new_even_sums`) to store the results calculated *in the current iteration* before merging them.
2.  **Extend Even Length (-> Odd Length):** Iterate through each `(curr_sum, products)` pair in `even_sums`. The new sum will be `target_sum = curr_sum + val`. For each `p` in `products`, calculate `new_prod = p * val`. If `0 <= new_prod <= limit`, add `new_prod` to `new_odd_sums[target_sum]`. Crucially, if `val == 0`, explicitly add `0` to `new_odd_sums[target_sum]`, as multiplying any previous product by 0 results in a valid product of 0.
3.  **Extend Odd Length (-> Even Length):** Iterate through each `(curr_sum, products)` pair in `odd_sums`. The new sum will be `target_sum = curr_sum - val`. For each `p` in `products`, calculate `new_prod = p * val`. If `0 <= new_prod <= limit`, add `new_prod` to `new_even_sums[target_sum]`. If `val == 0`, explicitly add `0` to `new_even_sums[target_sum]`.
4.  **Merge New States:** After calculating all extensions, merge the temporary results into the main DP tables: `odd_sums[i].update(new_odd_sums[i])` and `even_sums[i].update(new_even_sums[i])`.
5.  **Add Base Case:** Consider the subsequence containing only the current `val`. This has odd length (parity 1) and sum `val`. If `0 <= val <= limit`, add `val` to `odd_sums[val]`.

### Final Result

After processing all `val` in `nums`, the final DP tables `odd_sums` and `even_sums` contain all possible valid products for all achievable sums and parities.

To find the answer, we look at the sets associated with the target sum `k` in both tables:
*   `prods0 = even_sums.get(k, set())`
*   `prods1 = odd_sums.get(k, set())`
Combine these sets: `combined_prods = prods0.union(prods1)`.

If `combined_prods` is empty, no valid subsequence exists, return -1.
Otherwise, return `max(combined_prods)`. This works because the sets only ever contain valid products (0 to limit), so the maximum element is the desired answer.

## Complexity Analysis

*   **Time Complexity:** Roughly O(N * S_max * P_max), where N is the length of `nums`, S_max is the maximum number of distinct sums possible at any step, and P_max is the maximum size of the product set for any given state. The range of sums depends on N and `max(abs(nums))`. The size of the product sets can grow, making this potentially slower than the (correctly implemented) two-state optimization in some cases, but it is conceptually simpler and more robust against implementation errors related to zero/limit handling.
*   **Space Complexity:** O(S_max * P_max) to store the DP states (the sets of products).

## Implementation Notes

The final correct implementation uses this set-based approach. Initial attempts using a two-state (actual + capped) optimization failed due to implementation errors, highlighting the complexity of that approach. While potentially faster, the two-state method requires meticulous handling of state merging and zero injection (see [[../document/common_mistakes/dp_state_merge_sentinel_special.md]] and [[../document/optimizations/dynamic_programming/dp_state_space_reduction_product_limit.md]]). 