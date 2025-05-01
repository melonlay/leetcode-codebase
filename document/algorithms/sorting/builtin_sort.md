# Algorithm: Built-in Sorting (Python)

## Description

Sorting involves arranging elements of a sequence (like a list) in a specific order (e.g., ascending or descending).

Python provides highly optimized, built-in mechanisms for sorting:

1.  **`list.sort()` method:** Sorts a list *in-place*. It modifies the original list and returns `None`.
2.  **`sorted()` function:** Returns a *new* sorted list, leaving the original sequence unchanged. It can accept any iterable (list, tuple, string, etc.) as input.

## Algorithm & Complexity (Timsort)

Python's built-in sort uses **Timsort**, an adaptive, hybrid sorting algorithm derived from merge sort and insertion sort.

*   **Time Complexity:**
    *   **Best Case:** O(n) (when the input is already partially or fully sorted).
    *   **Average Case:** O(n log n).
    *   **Worst Case:** O(n log n).
*   **Space Complexity:** O(n) in the worst case (for `sorted()`, as it creates a new list) or O(k) (where k is the size of temporary runs, often much smaller than n for `list.sort()` due to its adaptive nature, but can be O(n) in some cases).
*   **Stability:** Timsort is a **stable sort**. This means that if two elements have equal sort keys, their relative order in the input sequence is preserved in the sorted output.

## Usage Context

Use built-in sorting whenever you need to order elements, unless specific algorithmic constraints require implementing a different sorting algorithm (which is rare in typical LeetCode scenarios).

*   Use `list.sort()` when you want to modify the original list directly and don't need the original order preserved elsewhere.
*   Use `sorted()` when you need to keep the original sequence intact or when sorting an iterable that isn't a list.

## Customization

Both `list.sort()` and `sorted()` accept optional arguments:

*   `key`: A function that takes an element and returns a value to be used for comparison (e.g., `key=lambda x: x[1]` to sort by the second item of tuples).
*   `reverse`: Set to `True` for descending order (`reverse=False` is the default for ascending).

## Examples

```python
my_list = [3, 1, 4, 1, 5, 9, 2]

# In-place sort
my_list.sort()
# my_list is now [1, 1, 2, 3, 4, 5, 9]

my_tuple = (3, 1, 4, 1, 5, 9, 2)

# Create a new sorted list
new_list = sorted(my_tuple)
# new_list is [1, 1, 2, 3, 4, 5, 9]
# my_tuple remains unchanged

# Sort by length of strings
words = ["apple", "banana", "kiwi", "fig"]
words.sort(key=len)
# words is now ["kiwi", "fig", "apple", "banana"]

# Sort descending
numbers = [5, 2, 8]
sorted_numbers_desc = sorted(numbers, reverse=True)
# sorted_numbers_desc is [8, 5, 2]
```

## Patterns Utilizing This

*   Many patterns implicitly require or benefit from sorted input (e.g., some two-pointer approaches, certain greedy algorithms).
*   `document/patterns/in_place_array_hashing.md` (while not direct sorting, deals with placing elements based on value, a related concept). 