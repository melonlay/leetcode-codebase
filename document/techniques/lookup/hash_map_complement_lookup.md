# Technique: Hash Map Complement Lookup

## Problem Addressed

Efficiently finding if two elements in a collection sum up to a specific target value, or more generally, finding if an element `x` exists such that `x + y = target` for a given `y`.

## Core Idea

Utilize a hash map (like Python's `dict`) to store elements encountered so far, allowing for O(1) average time complexity lookups for the required complement.

## Steps

1.  **Initialize:** Create an empty hash map (e.g., `num_map = {}`). This map will typically store `element: associated_data` (e.g., `number: index` for the Two Sum problem).
2.  **Iterate:** Loop through the elements (`y`) of the input collection.
3.  **Calculate Complement:** For each element `y`, calculate the `complement` (`x = target - y`).
4.  **Lookup:** Check if the `complement` (`x`) exists as a key in the hash map.
    *   **If Found:** The pair (`x`, `y`) that sums to the target has been found. Use the current element `y` and the information stored in the map for `x` (e.g., its index).
    *   **If Not Found:** Store the current element `y` and its associated data (e.g., its index) in the hash map: `num_map[y] = index_of_y`. This makes `y` available as a potential complement for future elements.

## Example (Two Sum Variant)

```python
def find_complement_pair(nums: list[int], target: int) -> tuple | None:
    num_map = {} # Stores {number: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found: return the complement and current number
            return (complement, num)
        num_map[num] = i
    return None # No pair found
```

## Complexity

*   **Time:** O(N) on average, where N is the number of elements. Each element is processed once, with O(1) average time for hash map operations.
*   **Space:** O(N) in the worst case to store elements in the hash map.

## Applicability

*   Classic Two Sum problem and its variations.
*   Problems requiring finding pairs with a specific sum or difference.
*   Can be adapted for Three Sum or K Sum problems (often involving sorting first and then using this technique on subproblems).

## Related Concepts

*   [[../../data_structures/hash_table_dict.md]]
*   [[../../patterns/two_pointers.md]] (Alternative for sorted arrays) 