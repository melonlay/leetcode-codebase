# Algorithm: Constructing the k-th Permutation

## Abstract Definition

This algorithm constructs the k-th lexicographical permutation of a set of `n` distinct, sortable elements given a rank `k` (usually 1-based). It implements the **unranking** process based on the mapping between integers and permutations provided by the **Factorial Number System**.

## Knowledge Base Reference

*   The mathematical foundation for this algorithm is the **Factorial Number System** (Factoradic) and its bijective mapping to permutations via the Lehmer code. See:
    *   `document/mathematical_concepts/combinatorics/factorial_number_system.md`

## Algorithmic Steps (Unranking)

Given a set of `n` distinct, sortable elements and a 1-based rank `k`:

1.  **Preprocessing:**
    *   Ensure the elements are sorted (e.g., `[1, 2, ..., n]` or `['a', 'b', 'c']`). Maintain this set as `availableElements`.
    *   Pre-calculate factorials up to `(n-1)!`.
    *   Convert `k` to be 0-based: `k = k - 1`. This `k` now represents the 0-based index in the lexicographical ordering, which directly corresponds to an integer in the range `[0, n!-1]` suitable for factoradic conversion.

2.  **Iterative Construction:** Iterate `n` times, for `i` from `n-1` down to `0` (corresponding to the factoradic place values `i!`):
    *   Calculate the factorial for the current place value: `fact = i!` (or retrieve from precomputed values).
    *   Determine the factoradic digit (Lehmer code value) for this position: `index = k // fact`.
    *   This `index` tells us which element to select from the *currently sorted* `availableElements`. The element is `selectedElement = availableElements[index]`.
    *   Append `selectedElement` to the result permutation.
    *   Remove `selectedElement` from `availableElements`.
    *   Update `k` for the next lower place value: `k = k % fact`.

3.  **Termination:** After `n` iterations, the result contains the k-th permutation.

## Complexity Analysis

*   **Time:** O(n^2) if using a standard list for `availableElements` (due to O(n) removal/pop). Can be improved to O(n log n) or potentially O(n) with more advanced data structures (like a Fenwick tree or order statistic tree) to handle the selection and removal from `availableElements` more efficiently. Factorial pre-calculation is O(n).
*   **Space:** O(n) for storing factorials, the `availableElements` list/structure, and the result permutation.

## Use Cases

*   Implementing solutions for problems like LeetCode 60 "Permutation Sequence".
*   Generating specific permutations efficiently when the full list isn't needed.

## Example Application

*   **LeetCode 60: Permutation Sequence** - [[https://leetcode.com/problems/permutation-sequence/|LeetCode 60]]

## Implementation (Python Example - LeetCode 60 Style)

```python
import math

def get_kth_permutation(n: int, k: int) -> str:
    """Constructs the k-th permutation of numbers 1 to n."""
    if k < 1 or k > math.factorial(n):
        raise ValueError("k is out of range")

    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i

    # Using list of strings for direct join later
    available_digits = [str(i) for i in range(1, n + 1)] 
    result = []
    
    k -= 1 # Convert k to 0-based index (0 to n!-1)

    for i in range(n, 0, -1):
        # i represents remaining digits, index corresponds to (i-1)! place
        fact = factorials[i - 1]
        index = k // fact
        
        result.append(available_digits.pop(index))
        
        k %= fact

    return "".join(result)

# Example Usage:
print(get_kth_permutation(4, 9)) # Output: "2314"
print(get_kth_permutation(3, 3)) # Output: "213"
```

## Potential Pitfalls

*   **Off-by-one errors:** Correctly handling the 1-based vs 0-based `k` is crucial. Converting `k` to `k-1` at the start aligns it with the 0-based nature of the Factorial Number System / Lehmer code.
*   **Element Removal Efficiency:** `list.pop(index)` has O(n) complexity. This is often acceptable for small `n` (like in LeetCode 60), but for larger `n`, consider data structures optimized for indexed removal/selection.
*   **Integer Overflow:** Factorials grow quickly. Calculations involving `k` and factorials must handle potentially large numbers (though usually constrained in competitive programming).

## Implementation (Python Example)

```python
import math

def get_kth_permutation(elements: list, k: int) -> list:
    """Finds the k-th lexicographical permutation of the given elements."""
    n = len(elements)
    if k < 1 or k > math.factorial(n):
        raise ValueError("k is out of range")

    elements.sort() # Ensure elements are sorted

    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i

    result = []
    k -= 1 # Convert k to 0-based index

    # Create a copy to avoid modifying the original list
    available_elements = list(elements) 

    for i in range(n, 0, -1):
        fact = factorials[i - 1]
        index = k // fact
        result.append(available_elements.pop(index))
        k %= fact

    return result

# Example Usage:
numbers = [1, 2, 3, 4]
k = 9
# Pass a copy if the original list shouldn't be modified
permutation = get_kth_permutation(list(numbers), k) 
print(f"The {k}-th permutation is: {permutation}") # Output: [2, 3, 1, 4]
```

## Related Concepts

*   **Factorial Number System** - A system where each integer can be represented as a sum of powers of factorials.
*   **Lehmer Code** - A representation of a permutation as a sequence of factorial numbers.
*   **Unranking** - The process of finding the k-th permutation in a sequence of permutations. 