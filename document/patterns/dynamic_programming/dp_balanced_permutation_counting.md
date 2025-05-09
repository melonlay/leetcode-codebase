# Dynamic Programming for Balanced Permutation Counting

This document outlines two primary dynamic programming approaches for solving problems that require counting distinct permutations of digits (or items) satisfying a "balance" condition, typically related to sums of elements at different types of positions (e.g., even vs. odd indices).

## Problem Type

Given a string of digits (or a list of items), count the number of distinct permutations of these digits such that a specific balance condition is met. A common example is that the sum of digits at even indices equals the sum of digits at odd indices. The result is often required modulo a large prime.

## Approach 1: DP on Sorted Individual Items

This approach involves sorting the input items and then using DP to decide the placement (e.g., into an "even" or "odd" indexed group) for each item one by one.

### State
A typical DP state might be:
`dp(items_of_type1_slots_left, items_of_type2_slots_left, balance_needed_for_type1_slots)`
- `items_of_type1_slots_left`: Number of available slots of the first type (e.g., even-indexed positions).
- `items_of_type2_slots_left`: Number of available slots of the second type (e.g., odd-indexed positions).
- `balance_needed_for_type1_slots`: The remaining sum that items placed into type1 slots must contribute to satisfy the overall balance condition.

The current item being processed is often implicitly determined by `total_items - (items_of_type1_slots_left + items_of_type2_slots_left)`, assuming items are processed from a sorted list.

### Logic
1.  Parse the input string into a list of numbers and sort it (e.g., descending).
2.  Precompute factorials and potentially suffix sums (if useful for base cases).
3.  The DP function explores placing the current item:
    a.  Into a type1 slot: `result_a = dp(type1_left - 1, type2_left, balance_needed - current_item_value) * type1_left`. The multiplication by `type1_left` accounts for choosing one of the available type1 slots.
    b.  Into a type2 slot: `result_b = dp(type1_left, type2_left - 1, balance_needed) * type2_left`. (If the item's value doesn't affect `balance_needed` when placed in type2).
4.  The total for the current state is `(result_a + result_b) % MOD`.

### Base Cases
-   If `balance_needed < 0`: Invalid path, return 0.
-   If `type1_slots_left == 0`: If `balance_needed == 0`, all remaining items must go to type2 slots. The number of ways to arrange them is `factorial(type2_slots_left)`. Otherwise, return 0.
-   If `type2_slots_left == 0`: All remaining items must go to type1 slots. Check if their sum (possibly using precomputed suffix sums) equals `balance_needed`. If so, return `factorial(type1_slots_left)`. Otherwise, return 0.
-   If all items are processed (`current_item_idx == total_items`): Return 1 if all slots are filled and balance is met, else 0. (This case is often covered by the slot exhaustion cases).

### Handling Duplicates in Input
The DP, as described, calculates arrangements as if all items are distinguishable (e.g., by their position in the sorted list). To get the count of *distinct* permutations of the original input items:
- Calculate `raw_dp_result` from the initial DP call.
- Calculate `perm_factor = product(factorial(count_of_each_distinct_item)) % MOD`.
- Final answer: `(raw_dp_result * modInverse(perm_factor, MOD)) % MOD`.

### Complexity
- Time: `O(N_slots1 * N_slots2 * MaxBalance)`, which is typically `O((N/2) * (N/2) * (S/2)) = O(N^2 * S)`, where `N` is the total number of items and `S` is their maximum possible sum (e.g., `N * max_digit_value`).
- Space: Same as time for memoization.

### Pros
-   Potentially better theoretical time complexity compared to some forms of Digit DP if the alphabet size is large.

### Cons
-   Indirectly handles distinct permutations (requires a post-DP adjustment factor).
-   May require careful handling of item indexing and base cases (e.g., using suffix sums).

### Example
An earlier version of the solution for LeetCode problem 3343 (`countBalancedPermutations`) explored this "DP on Sorted Individual Items" pattern before the final solution adopted a Digit DP approach (Approach 2). This pattern remains a valid general strategy for similar problems.

## Approach 2: Digit DP (or Item-Type DP)

This approach iterates through types of items (e.g., digit values 0-9) and, for each type, decides how many occurrences are assigned to type1 slots and how many to type2 slots.

### State
A typical DP state might be:
`dp(current_item_type_idx, items_of_type1_slots_left, items_of_type2_slots_left, balance_needed_for_type1_slots)`
- `current_item_type_idx`: Index or value of the current item type being considered (e.g., digit 9 down to 0).
- `items_of_type1_slots_left`, `items_of_type2_slots_left`: As above.
- `balance_needed_for_type1_slots`: As above.

### Logic
1.  Count frequencies of each item type (e.g., `counts[digit_value]`).
2.  The DP function considers `current_item_type = item_types[current_item_type_idx]`, which has `total_occurrences = counts[current_item_type]`.
3.  Iterate `k` from `0` to `total_occurrences` (number of occurrences of `current_item_type` to place in type1 slots).
    a.  `num_for_type1 = k`.
    b.  `num_for_type2 = total_occurrences - k`.
    c.  If `num_for_type1 <= type1_left` and `num_for_type2 <= type2_left`:
        i.  Ways to choose slots: `C(type1_left, num_for_type1) * C(type2_left, num_for_type2)`.
        ii. Recursive call: `dp_val = dp(current_item_type_idx - 1, type1_left - num_for_type1, type2_left - num_for_type2, balance_needed - current_item_value * num_for_type1)`.
        iii.Add `(ways_to_choose_slots * dp_val) % MOD` to the total for the current state.

### Base Cases
-   If `balance_needed < 0`: Return 0.
-   If `current_item_type_idx < 0` (all item types processed): Return 1 if `type1_left == 0`, `type2_left == 0`, and `balance_needed == 0`. Else return 0.

### Handling Duplicates in Input
This approach naturally handles distinct permutations because the combinations `C(slots_available, num_to_place)` correctly account for placing groups of identical items into distinct available slots. No final adjustment factor is typically needed if the state transitions are defined this way.

### Complexity
- Time: `O(|AlphabetSize| * N_slots1 * N_slots2 * MaxBalance * MaxOccurrencesOfOneItemType)`.
  A tighter analysis might be `O((N + |AlphabetSize|) * N_slots1 * N_slots2 * MaxBalance)`, which is roughly `O((N + |Sigma|) * N^2 * S)`.
- Space: Same as time for memoization.

### Pros
-   Often more concise and directly computes the number of distinct permutations.
-   Considered a standard technique for problems involving constructing sequences/sets from item counts with constraints.

### Cons
-   Theoretical time complexity might be higher than Approach 1 by a factor related to `N` or `|Sigma|`.

### Example
The final, successful solution for LeetCode problem 3343 (`countBalancedPermutations`) in `problems/3343_count_number_of_balanced_permutations/solution.py` implements this Digit DP pattern. A conceptual structure is:
```python
# Example structure for Digit DP (conceptual)
# cnt = Counter(digits)
# @cache
# def dfs(digit_val, odd_slots_rem, even_slots_rem, odd_balance_rem):
#     if digit_val < 0:
#         return 1 if odd_slots_rem == 0 and even_slots_rem == 0 and odd_balance_rem == 0 else 0
#     if odd_slots_rem < 0 or even_slots_rem < 0 or odd_balance_rem < 0:
#         return 0
#
#     res = 0
#     num_occurrences_of_digit = cnt[digit_val]
#     for k_to_odd in range(num_occurrences_of_digit + 1):
#         k_to_even = num_occurrences_of_digit - k_to_odd
#         if k_to_even >= 0 and k_to_odd <= odd_slots_rem and k_to_even <= even_slots_rem:
#             ways_to_choose = comb(odd_slots_rem, k_to_odd) * comb(even_slots_rem, k_to_even)
#             term_res = dfs(digit_val - 1,
#                            odd_slots_rem - k_to_odd,
#                            even_slots_rem - k_to_even,
#                            odd_balance_rem - digit_val * k_to_odd)
#             res = (res + ways_to_choose * term_res) % MOD
#     return res
#
# initial_call = dfs(9, total_odd_slots, total_even_slots, target_odd_sum)
```

## Comparison and Practical Notes

The choice between these DP approaches can be nuanced and may involve an iterative process for complex problems:

-   **Theoretical vs. Practical Speed:** While Approach 1 (DP on sorted items) might appear to have a better theoretical worst-case time complexity in some analyses (e.g., `O(N^2*S)` vs. potentially `O(|Sigma|*N^3*S)` if inner loops in Digit DP are broadly estimated), the actual transition cost in Digit DP (Approach 2) depends on `MaxOccurrencesOfOneItemType` (or `counts[digit_val]`) for each digit type. For problems like LeetCode 3343 (N up to 80), the Digit DP approach proved to be effective and was the chosen final solution. Practical performance in Python is significantly influenced by constant factors, overhead of `math.comb`, `lru_cache` efficiency with different state structures, and specific test case distributions.
-   **Impact of User Guidance and Iteration:** For Problem 3343, initial explorations (including an attempt at Approach 1) faced challenges. User guidance and the provision of a concise Digit DP model were pivotal in shifting to Approach 2, which was ultimately successful. This highlights the value of incorporating external insights and being prepared to iterate on solution strategies.
-   **Elegance and Correctness for Duplicates:** Digit DP (Approach 2) is generally cleaner and more direct for handling distinct permutations due to its inherent use of combinations (`math.comb`). Approach 1 requires a careful post-computation adjustment (modular inverse of permutation factors), which adds a layer of complexity.
-   **Problem Fit:** Digit DP is very natural when the problem involves counts of a fixed alphabet of items (like digits 0-9). DP on sorted items might be considered if the items don't have a small, fixed alphabet or if the specific constraints make its state space demonstrably smaller and transitions simpler.

When choosing an approach, consider the specific constraints, the required clarity of the solution, and whether preliminary performance testing (if possible) indicates an advantage for one over the other for the given platform and language. For complex problems, an iterative approach, potentially trying one method and then refining or switching based on performance, TLEs, or new insights (including user feedback), is often necessary. 