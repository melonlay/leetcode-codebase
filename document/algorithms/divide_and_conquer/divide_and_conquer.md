# Algorithm Paradigm: Divide and Conquer (D&C)

**Category:** Algorithm (`algorithms/divide_and_conquer/`)

## 1. General Description

Divide and Conquer is a fundamental algorithm design paradigm based on recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined (merged) to give a solution to the original problem.

## 2. Core Steps

The paradigm typically involves three steps at each level of the recursion:

1.  **Divide:** Break the given problem into subproblems of smaller size. These subproblems are ideally independent and of roughly equal size.
2.  **Conquer:** Solve the subproblems recursively. If the subproblem sizes are small enough (base case), solve them directly.
3.  **Combine:** Combine the solutions of the subproblems into the solution for the original problem.

## 3. Complexity Analysis

The efficiency of D&C algorithms is often analyzed using recurrence relations. A common form is `T(n) = a * T(n/b) + f(n)`, where:
*   `T(n)` is the time for problem size `n`.
*   `a` is the number of subproblems.
*   `n/b` is the size of each subproblem.
*   `f(n)` is the cost of dividing the problem and combining the subproblem solutions.

The Master Theorem can often be used to solve such recurrences, leading to typical complexities like O(N log N) or O(N).

## 4. Common Applications and Examples

*   **Sorting:** Merge Sort, Quick Sort.
*   **Searching:** Binary Search [[../searching/binary_search.md]].
*   **Matrix Multiplication:** Strassen's algorithm.
*   **Computational Geometry:** Closest pair of points.
*   **Large Integer Multiplication:** Karatsuba algorithm.
*   **Specific Problem Patterns:** Meet-in-the-Middle [[../../patterns/divide_and_conquer/meet_in_the_middle.md]] leverages D&C by splitting the input, conquering each half, and then combining results.

## 5. Advantages

*   Can lead to efficient (often logarithmic factor) algorithms.
*   Naturally suited for parallel processing as subproblems are often independent.
*   Can simplify the design of complex algorithms.

## 6. Disadvantages

*   Recursion overhead can be significant for small problem sizes.
*   Can be complex to implement correctly, especially the combine step.
*   May not be suitable if subproblems are not independent or overlap significantly (in which case Dynamic Programming might be better).

## 7. Related Concepts

*   Recursion [[../recursion/backtracking.md]] (D&C is often implemented recursively)
*   Dynamic Programming [[../dynamic_programming/dynamic_programming.md]] (Contrasting approach, often used when subproblems overlap)
*   Master Theorem (for complexity analysis)
*   Specific Patterns: Meet-in-the-Middle [[../../patterns/divide_and_conquer/meet_in_the_middle.md]]
*   Specific Techniques: [[../../techniques/divide_and_conquer/mitm_combine_diff_value_maps.md]] 