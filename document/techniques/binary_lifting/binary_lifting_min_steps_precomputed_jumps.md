# Technique: Binary Lifting for Minimum Steps via Precomputed Jumps

## 1. Description

This technique utilizes the core concept of [[binary_lifting.md]] to efficiently find the minimum number of "steps" or "jumps" required to travel between two states (e.g., indices `s` and `t` in a sequence, configurations in a state space).

It's applicable when:
1.  A single "step" or "jump" from a state `i` is defined, potentially complexly, leading to a next state `next_state(i)`.
2.  We need to find the minimum number of these complex steps to reach a target state `t` starting from `s`.
3.  The "step" operation is deterministic and can be precomputed.

Instead of simulating jumps one by one (which takes O(k) time), we precompute the state reached after `2^k` jumps using binary lifting tables and then query the minimum steps required in O(log N) or O(log K_max) time.

## 2. Preprocessing (Complexity depends on single-step calculation)

1.  **Calculate Single-Step Result:**
    *   For each state `i`, determine the state `next_state(i)` reached after exactly one step according to the problem's rules. This might involve calculation, lookup, or algorithms like binary search.
    *   **Example (LC3534):** For a sorted array `sorted_vals` and `maxDiff`, the single "forward step" from index `i` reaches the farthest index `j` such that `sorted_vals[j] <= sorted_vals[i] + maxDiff`. This `next_state(i)` (let's call it `fr[i]`) can be found using `bisect_right`. This step is documented in [[../sequence/find_reach_bounds_sorted_constraint.md]]. Similarly, a "backward step" `fl[i]` can be found.
    *   Let the time complexity of calculating the single step for one state be `T_step`. The total time for this phase is O(N * T_step), where N is the number of states.

2.  **Build Binary Lifting Table:**
    *   Create a table `jump[LOG][N]`, where `LOG = ceil(log2(K_max))` (K_max is max possible steps) or `ceil(log2(N))`.
    *   **Base Case (k=0):** `jump[0][i] = next_state(i)`.
    *   **Recursive Step (k > 0):** Compute jumps of `2^k` by composing two `2^(k-1)` jumps: `jump[k][i] = jump[k-1][ jump[k-1][i] ]`.
    *   Handle boundary conditions or invalid states carefully.
    *   This step takes O(N log K_max) or O(N log N).

*Total Preprocessing Time: O(N * T_step + N log K_max)*

## 3. Query (Minimum Steps from `s` to `t`) (O(log K_max))

Assuming we want to reach target `t` from start `s`.

*   **Input:** Start state `s`, target state `t`.
*   **Output:** Minimum steps, or infinity/-1 if unreachable.
*   **Logic:**
    1. Handle base case: If `s` already satisfies the target condition relative to `t`, return 0.
    2. Initialize `count = 0`, `current = s`.
    3. Iterate `k` from `LOG-1` down to `0`:
        *   Retrieve `next_state_k = jump[k][current]` (state after `2^k` steps).
        *   Check validity of `next_state_k`.
        *   If `next_state_k` is valid AND it does *not* reach or exceed the target state `t` (based on the problem's ordering/comparison):
            *   Take the jump: `current = next_state_k`
            *   Add `2^k` to the step count: `count += (1 << k)`
    4. **Final Check:** After the loop, `current` holds the farthest state reached without satisfying the target condition relative to `t`. Check if a single final step from `current` satisfies the condition:
        *   Retrieve `final_jump_state = jump[0][current]`.
        *   Check validity of `final_jump_state`.
        *   If `final_jump_state` is valid AND it satisfies the target condition relative to `t`, return `count + 1`.
    5. If the final check fails, the target is unreachable. Return `float('inf')` or `-1`.

*Note: The exact comparison logic (`< t`, `>= t`) depends on whether the states are ordered (like indices) and whether we are jumping forwards or backwards.*

## 4. Example Use Case (LC3534)

*   **States:** Indices `0..N-1` of the sorted array.
*   **Single Step (Forward):** `fr[i]` = farthest index reachable via `bisect_right`.
*   **Single Step (Backward):** `fl[i]` = farthest index reachable via `bisect_left`.
*   **Tables:** `nxt[k][i]` based on `fr`, `prv[k][i]` based on `fl`.
*   **Query:** Use the logic in Section 3, applying `nxt` for `s <= t` queries and `prv` for `s > t` queries, comparing against the target index `t`.

## 5. Related Concepts

*   [[binary_lifting.md]] (Core concept)
*   [[binary_lifting_sparse_table.md]] (Specific table structure details)
*   Techniques for calculating the single step (e.g., [[../sequence/find_reach_bounds_sorted_constraint.md]], [[../sequence/find_boundary_pointer_sorted_constraint.md]])
*   [[../../algorithms/searching/binary_search.md]] (Often used within single-step calculation) 