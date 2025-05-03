# Optimization: Meet-in-the-Middle Subset Sum Combination - Binary Search vs. Two Pointers

**Context:** This applies to the "Combine / Meet" step of the [[../../patterns/divide_and_conquer/meet_in_the_middle.md]] pattern, specifically for variations of the Subset Sum problem where we have generated two sets of sums (e.g., `sums1` and `sums2`) from the two halves of the input, and need to find pairs `(s1, s2)` such that `s1` is from `sums1`, `s2` is from `sums2`, and `s1 + s2` satisfies a target condition (e.g., equals `T`, is closest to `T`, is `<= T`).

Let `M = |sums1|` and `L = |sums2|`. Both can be up to `O(2^(N/2))` where `N` is the original problem size.
Let `total_sum` be the sum of all original elements, and `target = total_sum / 2` (or `total_sum // 2` for integer math).

## Strategy 1: Binary Search (Find Closest)

*   **Method:**
    1. Generate `sums1`, `sums2` (sets).
    2. Convert `sums2` to `sorted_sums2` (O(L log L)).
    3. Iterate `s1` in `sums1` (M iterations).
    4. Calculate `target_s2 = target - s1`.
    5. Binary search (`bisect_left`) in `sorted_sums2` for `target_s2`.
    6. Check candidate `s2` values at `idx` and `idx-1`.
    7. For each candidate pair `(s1, s2)`, calculate `current_sum = s1 + s2` and update `min_abs_diff = min(min_abs_diff, abs(total_sum - 2 * current_sum))`.
*   **Combination Step Complexity:** O(M * log L) after sorting `sums2`.
*   **Overall Complexity:** O(N * 2^(N/2)).

## Strategy 2: Two Pointers (Track Min Diff Directly)

*   **Method:**
    1. Generate `sums1`, `sums2` (sets).
    2. Convert `sums1` to `sorted_sums1` (O(M log M)).
    3. Convert `sums2` to `sorted_sums2` (O(L log L)).
    4. Init `l_ptr = 0`, `r_ptr = L-1`, `min_abs_diff = inf`.
    5. While `l_ptr < M` and `r_ptr >= 0`:
        * `s1 = sorted_sums1[l_ptr]`, `s2 = sorted_sums2[r_ptr]`
        * `current_sum = s1 + s2`
        * `min_abs_diff = min(min_abs_diff, abs(total_sum - 2 * current_sum))`
        * If `2 * current_sum < total_sum`, increment `l_ptr`.
        * Else, decrement `r_ptr`.
*   **Combination Step Complexity:** O(M + L) after sorting both lists O(M log M + L log L).
*   **Overall Complexity:** O(N * 2^(N/2)).

## Strategy 3: Two Pointers (Find Max Sum <= Target) - Often Fastest

*   **Method:**
    1. Generate `sums1`, `sums2` (sets).
    2. Convert `sums1` to `sorted_sums1` (O(M log M)).
    3. Convert `sums2` to `sorted_sums2` (O(L log L)).
    4. Init `l_ptr = 0`, `r_ptr = L-1`, `max_sum_le_target = -inf` (initialize properly, e.g., with overall min possible sum).
    5. Target `half_sum = total_sum // 2`.
    6. While `l_ptr < M` and `r_ptr >= 0`:
        * `s1 = sorted_sums1[l_ptr]`, `s2 = sorted_sums2[r_ptr]`
        * `current_sum = s1 + s2`
        * If `current_sum == half_sum`, return `total_sum - 2 * half_sum`.
        * If `current_sum < half_sum`:
            * `max_sum_le_target = max(max_sum_le_target, current_sum)`
            * Increment `l_ptr` (try larger sum).
        * Else (`current_sum > half_sum`):
            * Decrement `r_ptr` (try smaller sum).
    7. Return `total_sum - 2 * max_sum_le_target`.
*   **Why it Works:** Due to symmetry, the minimum absolute difference `min|S - (total_sum - S)| = min|2S - total_sum|` corresponds to the achievable sum `S` closest to `target = total_sum / 2`. Finding the largest sum `S <= target` (`max_sum_le_target`) is sufficient because the difference `total_sum - 2 * max_sum_le_target` will be the minimum possible absolute difference.
*   **Combination Step Complexity:** O(M + L) after sorting O(M log M + L log L).
*   **Overall Complexity:** O(N * 2^(N/2)).

## Comparison & Recommendation

| Feature                | Binary Search         | Two Pointers (Min Diff) | Two Pointers (Max <= Target) |
| :--------------------- | :-------------------- | :----------------------- | :----------------------------- |
| **Asymptotic Overall** | O(N * 2^(N/2))        | O(N * 2^(N/2))           | O(N * 2^(N/2))                 |
| **Combination Step**   | O(M log L)            | O(M + L) (after sort)    | O(M + L) (after sort)          |
| **Sorting Required**   | One list (`sums2`)    | Both lists               | Both lists                     |
| **Logic Complexity**   | Moderate              | Moderate                 | Simpler comparison in loop     |

**Recommendation:**

While all three have the same overall asymptotic complexity, the **Two Pointer methods generally outperform Binary Search** in the combination step. Between the two pointer methods:

*   **Strategy 3 (Find Max Sum <= Target)** was observed to be significantly faster in practice for LeetCode 2035. This is likely due to the simpler comparison logic (`current_sum` vs `half_sum`) and potentially fewer state updates (`max_sum_le_target` updated only when `current_sum < half_sum`) compared to Strategy 2 (which updates `min_abs_diff` more frequently).

Therefore, for optimizing Meet-in-the-Middle for subset sum problems aiming for the closest sum to `total_sum / 2`, **Strategy 3 (Two Pointers Finding Max Sum <= Target)** is the recommended approach for best performance. 