# Common Mistake: Index Mismatch in Hash Map Lookups

## Context

When using a hash map (dictionary in Python) to find pairs of elements that satisfy a certain condition (e.g., summing to a target, like in the Two Sum problem), a frequent error involves returning incorrect indices, especially in larger test cases or cases with duplicate numbers.

The standard hash map approach for finding pairs often involves:
1. Iterating through the collection (`nums`).
2. For each element `num` at index `i`, calculating a required `complement` based on the target condition.
3. Checking if the `complement` exists as a key in the hash map.
4. If it exists, returning the index stored for the `complement` and the current index `i`.
5. If not, adding the current `num` and its index `i` to the hash map for future lookups.

## Example Error Scenario (from Two Sum)

Consider a test case where the solution incorrectly identifies the pair summing to the target.

**Traceback:**

```
Traceback (most recent call last):
  File "D:\workspace\python\cursor\leet_code\problems\0001_two_sum\test_solution.py", line 71, in test_large_array
    self.assertEqual(sorted(result), sorted(expected))
AssertionError: Lists differ: [1499, 1501] != [9998, 9999]

First differing element 0:
1499
9998

- [1499, 1501]
+ [9998, 9999]
```

**Analysis:**

The error `AssertionError: Lists differ: [1499, 1501] != [9998, 9999]` clearly shows that the function returned `[1499, 1501]` as the indices, while the correct expected indices were `[9998, 9999]`.

## Potential Causes and Fixes

1.  **Handling Duplicates:** If the input collection contains duplicate elements, ensure the hash map logic correctly stores indices. A common mistake is overwriting the index of an element if it appears multiple times *before* its complement/pair is found. Ensure you store the first occurrence's index needed or handle the lookup correctly based on the specific problem requirements (e.g., not using the same element twice if disallowed).
2.  **Lookup Timing:** Ensure you add the *current* element and its index to the map *after* checking for its complement/pair. If you add it before checking, you might incorrectly match an element with itself if the pairing condition allows it (e.g., finding `num` where `target = 2 * num` in Two Sum).
3.  **Index vs. Value:** Double-check that you are storing indices in the map (`{value: index}`) and returning the stored index (`map[complement]`) and the current index (`i`).

Carefully reviewing the hash map insertion and lookup logic against these points usually reveals the source of such index errors when finding pairs or complements. 