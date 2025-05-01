# Optimization: Using Built-in Functions and Modules

## Description

Python offers numerous built-in functions (e.g., `sum()`, `max()`, `min()`, `len()`, `map()`, `filter()`) and standard library modules implemented in C (e.g., `collections`, `itertools`, `math`, `array`) that are highly optimized for performance.

## Rationale

These built-in functions and C-implemented modules often execute significantly faster than equivalent logic written in pure Python loops. The C implementations bypass much of the overhead associated with the Python interpreter for each step of the operation.

## Examples

*   **Summing List:** Prefer `total = sum(my_list)` over a manual `for` loop.
*   **Finding Max/Min:** Use `maximum = max(my_list)` instead of iterating and comparing.
*   **Counting Items:** Use `collections.Counter(my_list)` for efficient frequency counting instead of a manual dictionary loop.
*   **Combinations/Permutations:** Use `itertools.combinations()` or `itertools.permutations()` instead of implementing recursive generators manually if performance is critical.
*   **Mathematical Operations:** Use functions from the `math` module (e.g., `math.sqrt()`, `math.log()`) which are typically faster than pure Python equivalents.
*   **Deque Operations:** `collections.deque` provides O(1) append/pop from both ends, crucial for algorithms like BFS or Monotonic Queue.

## When to Use

Always consider using built-in functions and relevant standard library modules (especially `itertools` and `collections` for algorithmic problems) when their functionality matches your needs. This not only improves performance but often leads to more readable and concise code.

## Related Concepts

*   Review specific modules like `collections` ([../data_structures/](../data_structures/)), `itertools` for common, optimized tools. 