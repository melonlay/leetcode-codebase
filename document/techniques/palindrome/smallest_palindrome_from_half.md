# Technique: Construct Smallest Palindrome From First Half

## Description

This technique applies the general pattern of [[../../patterns/construction/optimized_construction_via_input_guarantees.md]] to efficiently construct the lexicographically smallest palindromic permutation of a string `s`, specifically when `s` is **guaranteed** to be a palindrome itself.

It avoids processing the entire input string by leveraging the symmetry inherent in the guaranteed palindromic input.

## Technique Steps

Given an input string `s` of length `n` (guaranteed to be a palindrome):

1.  **Handle Base Case:** If `n <= 1`, return `s` directly.
2.  **Count First Half:** Calculate character frequencies using `collections.Counter` on *only* the first half of the input string: `s[:n//2]`.
3.  **Build Result's First Half (List):**
    *   Initialize an empty list `result_first_half_list`.
    *   Iterate through characters `c` from 'a' to 'z'.
    *   For each `c` found in the first-half counts, append `c` to the list `count[c]` times.
4.  **Determine Middle Character:**
    *   If `n` is odd, the middle character is `s[n//2]`.
    *   If `n` is even, there is no middle character (`""`).
5.  **Construct Final String:**
    *   Join the `result_first_half_list` to form `first_half_str`.
    *   Join the `reversed()` iterator of `result_first_half_list` to form `second_half_str`.
    *   Return the concatenation: `first_half_str + middle_char + second_half_str`.

## Python Implementation Example

```python
from collections import Counter

def construct_smallest_palindrome_from_half(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    # 1. Count frequencies ONLY in the first half
    first_half_counts = Counter(s[:n//2])

    # 2. Build the result's first half efficiently using a list buffer
    result_first_half_list = []
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        count_in_half = first_half_counts.get(char, 0)
        if count_in_half > 0:
             # Append char by char for efficiency
             for _ in range(count_in_half):
                 result_first_half_list.append(char)

    # 3. Join the first half list
    result_first_half_str = "".join(result_first_half_list)

    # 4. Get original middle char directly if needed
    middle_char = s[n//2] if n % 2 else ""

    # 5. Construct final palindrome efficiently using reversed() iterator
    result_second_half_str = "".join(reversed(result_first_half_list))

    return result_first_half_str + middle_char + result_second_half_str

```

## Prerequisites

*   The input string `s` **must** be guaranteed to be a palindrome.

## Related Concepts

*   [[../../patterns/construction/optimized_construction_via_input_guarantees.md]] (General Pattern)
*   [[../../data_structures/hash_table_dict.md]] (Counters)
*   [[../../optimizations/string/string_concatenation.md]] (String joining)
*   Python `reversed()` iterator.
*   Palindrome definition. 