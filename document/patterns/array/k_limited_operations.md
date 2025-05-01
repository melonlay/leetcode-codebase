# Pattern: K-Limited Operations on Arrays

## Concept

This pattern applies to problems involving arrays (or sequences) where you can perform a specific operation (like selecting an element, modifying a value, making a transaction) up to a maximum of `k` times. The goal is often to maximize or minimize some value subject to this constraint.

## Characteristics

- **Input:** Typically an array `nums` and an integer `k`.
- **Operation:** A defined action that can be applied to elements or affects the state.
- **Constraint:** The operation can be performed at most `k` times.
- **Goal:** Optimize a target value (e.g., maximum sum, minimum cost, final state).

## Common Examples

- Selecting at most `k` elements to maximize a sum under certain conditions.
- Performing at most `k` stock transactions (buy/sell pairs) to maximize profit.
- Modifying at most `k` elements to achieve a target state or minimize differences.

## Potential Approaches & Related Algorithms

The choice of algorithm often depends on the specific constraints and the nature of the operation:

1.  **Dynamic Programming:** Suitable when the state can be defined by the current position `i` in the array and the number of operations `j` used so far (e.g., `dp[i][j]`).
    *   See: [[../../algorithms/dynamic_programming/array/k_limited_operations_dp.md|DP Approach for K-Limited Operations]]
2.  **Greedy (often with Heaps/Priority Queues):** Applicable when local optimal choices (e.g., picking the largest/smallest elements, considering the best immediate gains) can lead to a global optimum, especially when needing to efficiently manage the `k` best choices made so far.
    *   See: [[../../algorithms/greedy/array/k_limited_operations_heap.md|Greedy/Heap Approach for K-Limited Operations]]
3.  **Sliding Window / Other Techniques:** Might be applicable depending on the specific problem structure.

## Key Considerations

- **State Definition (DP):** Clearly define the DP state. Does it need to track just `k` operations, or also other factors (e.g., holding/not holding a stock)?
- **Greedy Choice Property:** Does a greedy approach hold? Prove or disprove if necessary.
- **Efficiency:** Ensure the chosen approach meets time/space complexity requirements (e.g., O(n*k) for DP, O(n log k) for Heap). 