# Hash Map Lookup Pattern (for problems like Two Sum)

## Description

This pattern utilizes a hash map (dictionary in Python) to achieve efficient lookups, typically in O(1) average time complexity. It's particularly useful when you need to quickly check for the existence of an element or find a corresponding value (like a 'complement') while iterating through a collection.

## Use Case: Two Sum Problem

In the Two Sum problem, we need to find two numbers in an array `nums` that add up to a `target`. Instead of checking every pair (O(n^2)), we can iterate through the array once (O(n)). For each element `num` at index `i`, we calculate its required `complement = target - num`.

We use a hash map `num_map` to store the numbers encountered so far and their indices (`{number: index}`).

1.  For the current `num`, check if its `complement` exists as a key in `num_map`.
2.  If the `complement` exists, we've found our pair: the number stored at `num_map[complement]` and the current `num`. We return their indices: `[num_map[complement], i]`.
3.  If the `complement` doesn't exist, add the current `num` and its index `i` to the `num_map` for future lookups: `num_map[num] = i`.

## Complexity

*   **Time Complexity:** O(n), as we iterate through the array once, and hash map operations (insertion and lookup) take O(1) on average.
*   **Space Complexity:** O(n), as in the worst case, we might store all elements of the input array in the hash map.

## Python Snippet (Illustrative)

```python
from typing import List

def find_pair_with_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # Hash map: {number: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found the complement
            return [num_map[complement], i]
        # Store current number's index for future checks
        num_map[num] = i
    # Return an indicator if no pair is found (adjust as needed for specific problem)
    return [] 
```

This pattern is fundamental for solving many problems involving finding pairs or checking for specific relationships between elements in a collection efficiently. 