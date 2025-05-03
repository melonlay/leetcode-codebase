# Pattern: Divide and Conquer

## Description

Divide and Conquer (D&C) is a fundamental algorithm design paradigm. It works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined (merged) to give a solution to the original problem.

## Core Steps

1.  **Divide:** Break the given problem into subproblems of smaller size. The subproblems should ideally represent smaller instances of the original problem.
2.  **Conquer:** Solve the subproblems recursively. If the subproblem sizes are small enough (base case), solve them directly.
3.  **Combine:** Combine the solutions of the subproblems into the solution for the original problem.

## Common Examples

*   **Merge Sort:** Divides the array in half, recursively sorts each half, and then merges the two sorted halves.
*   **Quick Sort:** Divides the array based on a pivot, recursively sorts the partitions.
*   **Binary Search:** Divides the search space in half at each step (though often considered a distinct algorithm, it follows the D&C principle).
*   **Closest Pair of Points:** Divides points by a vertical line, recursively finds closest pairs in each half, and combines by checking pairs near the dividing line.
*   **Strassen's Algorithm:** For matrix multiplication.
*   **Karatsuba Algorithm:** For fast multiplication of large numbers.

## Complexity Analysis

The time complexity of Divide and Conquer algorithms is often analyzed using recurrence relations of the form:
`T(n) = a * T(n/b) + f(n)`
where:
*   `T(n)` is the time for problem size `n`.
*   `a` is the number of subproblems.
*   `n/b` is the size of each subproblem.
*   `f(n)` is the cost of dividing the problem and combining the results.

The **Master Theorem** is frequently used to solve such recurrences.

## When to Use

*   Problems that can be naturally broken down into independent or easily combinable smaller instances of themselves.
*   When solving subproblems recursively leads to a more efficient solution than iterative or brute-force approaches.
*   Problems involving sorting, searching, or optimization on recursively structured data.

## Related Concepts

*   Recursion
*   Master Theorem (for analysis)
*   Merge Sort, Quick Sort, Binary Search (specific algorithms)
*   Meet-in-the-Middle [[meet_in_the_middle.md]]: While related (it divides the problem), its combination step is often different and more complex than typical D&C merges, focusing on searching/pairing between the results of the two halves rather than a direct merge. 