# Technique: DP State Parity Toggle

## Description

This technique involves incorporating **parity** (typically odd/even) as part of the state in a Dynamic Programming solution. It is often useful in problems where:

*   The operation performed depends on the index (e.g., add at even indices, subtract at odd indices).
*   The problem involves traversing a sequence or building a subsequence where alternating behavior is key.
*   The state needs to distinguish between subsequences of odd and even lengths.

## State Representation

The DP state typically includes a dimension for parity:

*   `dp[parity][other_state_keys...]`
*   Or, using separate tables: `dp_odd[other_state_keys...]`, `dp_even[other_state_keys...]`

Where:
*   `parity = 0` might represent an even length/index context.
*   `parity = 1` might represent an odd length/index context.

## State Transition

The core idea is that processing an element `num` transitions the state from one parity to the other.

*   **From Odd State (e.g., Parity 1):** When extending a subsequence of odd length, the new element `num` is effectively at an even position relative to the start of the *extended* subsequence. The transition often involves reading from `dp[1]` and writing to `dp[0]`. The operation applied (e.g., addition/subtraction) depends on the problem definition for even indices.
    ```python
    # Example: Alternating Sum (Add even, Subtract odd)
    # Extending an odd-length seq (prev state dp[1]) makes num the next even element (index 1, 3, etc.)
    # In the alternating sum definition, elements at odd indices (1, 3, ...) are subtracted.
    # So, read from dp[1][s_prev], write to dp_next[0][s_prev - num]
    ```
*   **From Even State (e.g., Parity 0):** When extending a subsequence of even length, the new element `num` is effectively at an odd position. The transition reads from `dp[0]` and writes to `dp[1]`. The operation applied depends on the problem definition for odd indices.
    ```python
    # Example: Alternating Sum (Add even, Subtract odd)
    # Extending an even-length seq (prev state dp[0]) makes num the next odd element (index 0, 2, etc.)
    # In the alternating sum definition, elements at even indices (0, 2, ...) are added.
    # So, read from dp[0][s_prev], write to dp_next[1][s_prev + num]
    ```

**Note:** The exact addition/subtraction logic depends heavily on the specific problem's definition (0-based vs 1-based indexing, definition of alternating operation). Carefully map the parity state to the operation required by the problem statement.

## Implementation

Often implemented using two dictionaries or arrays, one for each parity state, and swapping/updating them in each iteration.

## Example Applications

*   LeetCode 3509: Maximum Product of Subsequences With an Alternating Sum Equal to K
*   Problems involving finding subsequences with alternating properties.
*   Grid traversal problems where movement direction alternates.

## Related Concepts
*   General Dynamic Programming
*   [[dp_map_state_for_pairwise_relations.md]] (Can be combined if other relations matter) 