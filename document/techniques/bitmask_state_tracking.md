# Pattern: Bitmask State Tracking

## 1. Abstract Definition

Bitmask State Tracking is a technique that uses the individual bits of an integer (a "bitmask") to represent the state of a collection of boolean flags, presence/absence in a set, or other state information, where each item or condition corresponds to a specific bit position. Bitwise operations are then used to efficiently query and manipulate this state.

This pattern is particularly effective when the number of items or conditions to track is relatively small (typically fitting within the bits of a standard integer type, e.g., <= 32 or <= 64).

## 2. Advantages

*   **Speed:** Bitwise operations (AND `&`, OR `|`, XOR `^`, NOT `~`, shifts `<<`, `>>`) are often executed very quickly by the CPU, usually in a single clock cycle. This can be significantly faster than operations on other data structures like sets or dictionaries for state checking and updates.
*   **Space Efficiency:** A single integer can store the state of multiple boolean conditions compactly (e.g., a 64-bit integer can track 64 distinct flags).

## 3. Common Bitwise Operations

Let `mask` be the integer representing the state, and `k` be the 0-indexed bit position corresponding to an item.

*   **Set k-th bit (Mark item `k` as present/true):**
    ```python
    mask |= (1 << k)
    ```
*   **Clear k-th bit (Mark item `k` as absent/false):**
    ```python
    mask &= ~(1 << k)
    ```
*   **Check k-th bit (Is item `k` present/true?):**
    ```python
    is_set = (mask >> k) & 1
    # or alternatively:
    is_set = mask & (1 << k) # Result is non-zero if set, 0 otherwise
    ```
*   **Toggle k-th bit:**
    ```python
    mask ^= (1 << k)
    ```
*   **Get Least Significant Bit (LSB) Mask:** Finds the smallest power of 2 present in the mask (useful for iterating).
    ```python
    lsb_mask = mask & (-mask) # Uses two's complement property
    ```
*   **Remove Least Significant Bit (LSB):**
    ```python
    mask -= lsb_mask
    # or alternatively (often faster):
    mask &= (mask - 1)
    ```
*   **Create a mask with the lower `n` bits set:**
    ```python
    full_mask = (1 << n) - 1
    ```
*   **Check if mask is empty (no bits set):**
    ```python
    is_empty = (mask == 0)
    ```

## 4. Iterating Through Set Bits

A common requirement is to iterate through all items represented by set bits in the mask. The LSB trick is efficient for this:

```python
temp_mask = mask
while temp_mask:
    # 1. Get the LSB mask (e.g., 001000)
    lsb_mask = temp_mask & (-temp_mask)

    # 2. (Optional) Get the index 'k' of the LSB
    # k = lsb_mask.bit_length() - 1 # Python 3.10+ or use math.log2

    # 3. Process the item represented by lsb_mask (or k)
    #    print(f"Processing bit at index: {k}")

    # 4. Remove the LSB from the mask to find the next one
    temp_mask &= (temp_mask - 1)
```

## 5. Use Cases & Examples

*   **Representing Subsets:** Often used in dynamic programming or combinatorial problems involving subsets of items.
*   **Constraint Satisfaction:** Tracking constraints efficiently (e.g., N-Queens, Sudoku).
*   **Graph Algorithms:** Tracking visited nodes in algorithms like DFS/BFS when the number of nodes is small.
*   **State Compression:** Compressing multiple boolean states into a single integer for memoization or DP state keys.

**Example: N-Queens (Problem 52)**
In the N-Queens problem, bitmasks can track:
*   Occupied columns.
*   Occupied positive diagonals (`row + col`).
*   Occupied negative diagonals (`row - col`).

By combining these masks with bitwise OR (`|`) and NOT (`~`), we can quickly find available positions in the current row. Updates for recursive calls involve setting the appropriate bits and shifting the diagonal masks. See `problems/0052_n_queens_ii/solution.md` for a detailed application.

## 6. Limitations

*   The primary limitation is the number of distinct items or states that can be tracked, constrained by the number of bits in standard integer types (e.g., 32 or 64). For larger state spaces, other structures (sets, hash maps, boolean arrays) are necessary. 