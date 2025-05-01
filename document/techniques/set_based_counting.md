# Technique: Set-Based Counting (Odd Occurrence Finding)

## Concept

This technique leverages the properties of a `set` data structure to efficiently count the occurrences of elements, specifically identifying elements that appear an odd number of times in a collection or stream.

The core idea is that adding an element that already exists in a set has no effect in some implementations, or can be used with logic to remove it. Alternatively, using the symmetric difference operation achieves this directly.

## Implementation Methods

1.  **Add/Remove Logic:**
    *   Iterate through the input elements.
    *   For each element `e`:
        *   If `e` is in the set, `remove(e)`.
        *   If `e` is not in the set, `add(e)`.
    *   After processing all elements, the remaining elements in the set are those that appeared an odd number of times.

2.  **Symmetric Difference (`^=` or `symmetric_difference_update`)**
    *   Initialize an empty set `s`.
    *   Iterate through the input elements.
    *   For each element `e`, update the set using symmetric difference: `s ^= {e}`.
    *   The symmetric difference `A ^ B` contains elements that are in either `A` or `B` but not both. When applied iteratively `s ^= {e}`, if `e` is not in `s`, it's added. If `e` is already in `s`, it's removed.
    *   The final set `s` contains elements that appeared an odd number of times.

## Use Cases

*   **Finding the Single Element:** In an array where every element appears twice except for one, this technique finds the unique element.
*   **Geometric Corner Cancellation:** As seen in the "Perfect Rectangle" problem ([Problem 391](../problems/0391_perfect_rectangle/README.md)), used to verify tiling properties. Each internal corner point of a valid tiling is shared by an even number of rectangles (2 or 4), causing them to be added and removed from the set, cancelling out. The four external bounding box corners are each part of only one rectangle (in the context of corners being added), so they appear once and remain in the set.
    *   See: `../../patterns/geometry/perfect_tiling_check.md`
*   **Verifying Pairings:** Checking if all elements in a stream have a corresponding pair.

## Complexity

*   **Time Complexity:** O(N), where N is the number of elements processed. Each set operation (add, remove, check containment, symmetric difference update) takes O(1) average time.
*   **Space Complexity:** O(k), where k is the number of unique elements that appear an odd number of times. In the worst case, if many elements appear oddly, this could be O(N), but often k is much smaller.

## Advantages

*   Simple implementation.
*   Efficient time complexity.

## Disadvantages

*   Requires extra space for the set.
*   Doesn't preserve the count of occurrences, only the parity (odd/even). 