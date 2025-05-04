# Technique: Memoization (Top-Down Dynamic Programming)

## Description

Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It is a core component of the **Top-Down Dynamic Programming** approach.

## Core Idea

1.  **Recursive Structure:** Start with a plain recursive function that reflects the natural recursive structure of the problem.
2.  **Cache/Memo:** Use a data structure (typically a hash map/dictionary or an array) to store the results of function calls. The key is usually derived from the function's input parameters that define the subproblem.
3.  **Lookup Before Compute:** Before computing the result for a given set of inputs, check if the result is already present in the cache. If yes, return the cached value directly.
4.  **Compute and Store:** If the result is not in the cache, compute it recursively, store the computed result in the cache, and then return it.

## Python Implementation

Python provides convenient ways to implement memoization:

1.  **`functools.cache` (or `functools.lru_cache(maxsize=None)`):** (Python 3.9+ for `@cache`)
    *   A decorator that automatically wraps a function to cache its results.
    *   Handles cache management internally using a dictionary.
    *   Arguments to the decorated function must be hashable.

    ```python
    import functools

    @functools.cache
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    ```

2.  **Manual Dictionary Cache:**
    *   Explicitly manage a dictionary (`memo`) passed to or accessed by the recursive function.

    ```python
    memo = {}
    def fibonacci_manual(n):
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        result = fibonacci_manual(n-1) + fibonacci_manual(n-2)
        memo[n] = result
        return result
    ```

## When to Use

*   Implementing Top-Down Dynamic Programming solutions.
*   Optimizing recursive functions that exhibit overlapping subproblems (i.e., the same subproblems are solved multiple times).
*   When the recursive structure is more natural or easier to derive than an iterative (bottom-up) DP formulation.

## Relation to Bottom-Up DP

*   Both solve the same subproblems.
*   **Memoization (Top-Down):** Solves subproblems as needed, driven by the initial call. Might not compute all possible subproblems if some branches of the recursion are never reached.
*   **Tabulation (Bottom-Up):** Solves all subproblems iteratively, typically starting from base cases. Ensures prerequisites are met before computing a state.

## Complexity

*   **Time:** Number of distinct states (subproblems) * Time per state transition (excluding recursive calls that hit the cache).
*   **Space:** Number of distinct states stored in the cache + recursion stack depth.

## Pitfalls

*   Ensuring function arguments used as cache keys are hashable (for dictionary-based caches like `@cache`).
*   Potential for exceeding recursion depth limits in Python for very deep recursions (though `@cache` helps by avoiding re-computation).
*   Forgetting to store the result before returning in manual implementations.

## Related Concepts

*   [[../algorithms/dynamic_programming/dynamic_programming.md]]
*   [[../data_structures/hash_table_dict.md]]
*   [[../algorithms/recursion/backtracking.md]] (Backtracking often doesn't use memoization unless optimizing specific state visits). 