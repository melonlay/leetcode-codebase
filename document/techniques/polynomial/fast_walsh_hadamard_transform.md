# Fast Walsh-Hadamard Transform (FWHT)

**Concept Type:** Algorithm / Technique (Polynomials, Bit Manipulation)

**Description:**
The Fast Walsh-Hadamard Transform (FWHT) is an algorithm used to efficiently compute the convolution of two sequences, particularly when the convolution is defined by a bitwise operation (like AND, OR, or XOR) on the indices.

For XOR convolution (also known as dyadic convolution), if we have two polynomials (represented by coefficient arrays) \(A(x) = \sum a_i x^i\) and \(B(x) = \sum b_i x^i\), their XOR convolution \(C(x) = A(x) \star B(x)\) is defined as \(C(x) = \sum c_k x^k\) where \(c_k = \sum_{i \oplus j = k} a_i b_j\). (Here \(\oplus\) denotes bitwise XOR).

FWHT provides a way to compute this in \(O(M \log M)\) time, where \(M\) is the size of the arrays (typically a power of 2), similar to how FFT is used for standard polynomial multiplication.

**Algorithm Steps (for XOR convolution):**

1.  **Forward FWHT (\(\hat{A} = FWHT(A)\)):**
    The transform is applied in place.
    ```
    n = len(A) # (must be a power of 2)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = A[j]
                y = A[j+h]
                A[j] = x + y
                A[j+h] = x - y
        h *= 2
    ```

2.  **Element-wise Product:**
    If computing \(A \star B\), then after transforming \(A\) to \(\hat{A}\) and \(B\) to \(\hat{B}\), compute \(\hat{C}[i] = \hat{A}[i] \cdot \hat{B}[i]\) for all \(i\).
    If computing \(A \star A \star A\) (for sum of 3 elements), compute \(\hat{C}[i] = (\hat{A}[i])^3\).

3.  **Inverse FWHT (\(C = FWHT^{-1}(\hat{C})\)):**
    The inverse transform is very similar to the forward transform.
    ```
    n = len(\hat{C}) # (must be a power of 2)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = \hat{C}[j]
                y = \hat{C}[j+h]
                \hat{C}[j] = x + y
                \hat{C}[j+h] = x - y
        h *= 2
    ```
    Finally, divide every element of the resulting array by `n`:
    ```
    for i in range(n): C[i] = \hat{C}[i] // n # (use integer division if dealing with counts)
    ```

**Applications:**
*   Counting pairs/triplets/k-tuples with a specific XOR sum.
*   Problems involving subset XOR sums (related to "Sum over Subsets" DP, for which FWHT for AND/OR convolutions is also used).
*   Finding the number of unique XOR sums achievable by combining elements from a multiset.

**Problem Context Example (LC3514 - Number of Unique XOR Triplets II):**
In this problem, `nums` is an array of integers. We need to find the number of unique values of \(v_1 \oplus v_2 \oplus v_3\), where \(v_1,v_2,v_3\) are chosen from the multiset `nums`.
1. Create a frequency array `counts` where `counts[x]` is the frequency of `x` in `nums`. The size `M` of `counts` must be a power of 2, large enough to hold all possible XOR sums (e.g., 2048 if max element value is 1500).
2. Compute \(\widehat{counts} = FWHT(counts)\).
3. Compute \(\widehat{result}[i] = (\widehat{counts}[i])^3\).
4. Compute \(Result = FWHT^{-1}(\widehat{result})\).
5. The number of unique XOR triplet values is the count of indices `k` for which `Result[k] != 0`.
This approach is \(O(M \log M)\) and significantly faster than \(N^2\) or \(N^3\) solutions if \(M\) is relatively small compared to \(N^2\).

**Important Notes:**
*   The input array length for FWHT must be a power of 2. Pad with zeros if necessary.
*   The butterfly operation `(x+y, x-y)` is specific to XOR convolution. AND and OR convolutions use different butterfly operations.
*   When dealing with counts, ensure integer arithmetic. If working in a finite field (e.g., modulo a prime), modular arithmetic (including modular inverse for division) should be used.

**Complexity:** \(O(M \log M)\) for an array of size \(M\).

**Related Concepts:**
*   Fast Fourier Transform (FFT) for standard polynomial multiplication.
*   Sum over Subsets (SOS) DP.
*   Bit Manipulation.
*   [[../../mathematical_concepts/combinatorics/xor_sum_achievable_range.md]]
 