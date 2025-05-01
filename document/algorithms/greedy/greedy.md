# Greedy Algorithms

## Paradigm Description

Greedy algorithms build up a solution piece by piece, always choosing the option that offers the most obvious and immediate benefit at the current step, without regard for the overall future consequences of that choice.

**Core Principle:** Make the locally optimal choice at each stage with the hope of finding a global optimum.

**Characteristics:**
*   **Simplicity:** Often easier to conceptualize and implement than other paradigms like Dynamic Programming.
*   **Efficiency:** Typically faster, as they usually involve fewer subproblems or states to consider.
*   **Correctness Challenge:** The main difficulty lies in proving that the series of locally optimal choices consistently leads to a globally optimal solution for the specific problem. This is not always the case, and greedy algorithms only work for problems exhibiting specific properties (like the greedy choice property and optimal substructure).

**Common Applications:**
*   Minimum Spanning Trees (Prim's, Kruskal's)
*   Shortest Path (Dijkstra's - uses a greedy approach with priority queue)
*   Change-making problem (for certain coin systems)
*   Activity Selection Problem
*   Huffman Coding

**When to Consider:**
*   When a problem can be broken down into stages.
*   When making the locally best choice seems intuitively like it should lead to the best overall result.
*   **Crucially:** When you can *prove* that the greedy choice at each step does not prevent reaching the global optimum.

**Contrast with Dynamic Programming:**
*   DP explores multiple options at each stage and remembers results of subproblems to ensure the global optimum.
*   Greedy makes one choice and moves on, never reconsidering past choices. 