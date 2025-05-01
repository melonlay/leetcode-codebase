## Problem 60: Permutation Sequence

**Summary:** Given integers `n` and `k`, find the `k`-th lexicographical permutation of the sequence `[1, 2, ..., n]`.

## Algorithmic Approach

The problem asks for the specific `k`-th permutation without needing to generate all `n!` permutations. We can construct the permutation string digit by digit from left to right.

1.  **Initialization:**
    *   Calculate factorials from `0!` to `n!`. We store these, as `(n-i)!` will be needed repeatedly.
    *   Create a list of available digits, initially `[1, 2, ..., n]`.
    *   Adjust `k` to be 0-indexed (`k = k - 1`) because it's easier to work with 0-based indices for calculations involving division and modulo.

2.  **Digit Selection Loop:** Iterate from `i = n` down to `1` (representing the number of digits remaining to be placed).
    *   In each step, we determine which digit should be placed at the current position.
    *   There are `(i-1)!` permutations possible with the remaining `i` digits.
    *   The available digits are sorted lexicographically. The permutations are grouped into blocks of size `(i-1)!`, where each block starts with one of the available digits.
    *   The index of the correct digit to pick from the *current* list of available digits is `index = k // (i-1)!`.
    *   Append the digit `digits[index]` to our result string.
    *   Remove the chosen digit from the `digits` list (`digits.pop(index)`).
    *   Update `k` to be the index within the *next* smaller block of permutations: `k = k % (i-1)!`.

3.  **Result:** Join the selected digits to form the final permutation string.

**Example Trace (n=4, k=9):**

*   Factorials: `0!=1, 1!=1, 2!=2, 3!=6`
*   Digits: `[1, 2, 3, 4]`
*   `k = 9 - 1 = 8` (0-indexed)
*   **i=4:** `fact=(4-1)!=6`. `index = 8 // 6 = 1`. Pick `digits[1] = '2'`. `result = "2"`. `digits = [1, 3, 4]`. `k = 8 % 6 = 2`.
*   **i=3:** `fact=(3-1)!=2`. `index = 2 // 2 = 1`. Pick `digits[1] = '3'`. `result = "23"`. `digits = [1, 4]`. `k = 2 % 2 = 0`.
*   **i=2:** `fact=(2-1)!=1`. `index = 0 // 1 = 0`. Pick `digits[0] = '1'`. `result = "231"`. `digits = [4]`. `k = 0 % 1 = 0`.
*   **i=1:** `fact=(1-1)!=1`. `index = 0 // 1 = 0`. Pick `digits[0] = '4'`. `result = "2314"`. `digits = []`. `k = 0 % 1 = 0`.
*   Final: `"2314"`

## Knowledge Base References

*   The core logic relies on mathematical properties of factorials and permutations.
*   The adjustment `k = k - 1` is crucial for correct 0-based indexing, avoiding potential pitfalls related to `document/common_mistakes/off_by_one_errors.md` (though this file wasn't found in the current KB search).
*   This specific method could be documented as a reusable technique, perhaps under `document/techniques/kth_permutation_factorial.md`.

## Complexity Analysis

*   **Time Complexity:** O(n^2). Calculating factorials takes O(n). The main loop runs `n` times. Inside the loop, calculating `index` and `k` is O(1). However, `digits.pop(index)` on a standard list takes O(n) time in the worst case. Therefore, the total time is dominated by the list removals, resulting in O(n^2).
*   **Space Complexity:** O(n). We store factorials up to `n` (O(n)) and the list of available digits (O(n)). The result string also takes O(n) space. 