import math
from typing import List


class Solution:
    """
    Solves LeetCode 3463: Check If Digits Are Equal in String After Operations II.

    The problem involves repeatedly applying an operation on a string of digits:
    replace the string with the sums of adjacent digits modulo 10. This continues
    until the string has length 2. We need to check if the final two digits are equal.

    A direct simulation is O(n^2), which is too slow given n <= 10^5.
    The final digits can be expressed as a linear combination of the initial digits
    with coefficients being binomial coefficients modulo 10.
    Let k = n - 2. The final two digits d0 and d1 are:
    d0 = sum_{i=0}^{k} C(k, i) * s_i mod 10
    d1 = sum_{i=0}^{k} C(k, i) * s_{i+1} mod 10
    We need to check if d0 == d1.

    This requires calculating C(k, i) % 10 efficiently. We use Lucas's Theorem
    for prime factors (2 and 5) and the Chinese Remainder Theorem (CRT) to combine them.
    The overall time complexity is O(n log n) due to calculating n binomial coefficients.
    """

    def __init__(self):
        # Precompute C(n, k) % 5 for 0 <= k <= n <= 4
        self._C_mod5: List[List[int]] = [
            [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 2, 1, 0, 0],
            [1, 3, 3, 1, 0], [1, 4, 1, 4, 1]
        ]
        # Precompute CRT table: result = crt_table[mod2][mod5]
        self._crt_table: List[List[int]] = [
            [0, 6, 2, 8, 4],  # mod2 = 0
            [5, 1, 7, 3, 9]   # mod2 = 1
        ]

    def _nCr_mod5(self, n: int, r: int) -> int:
        """Calculates C(n, r) % 5 using Lucas's Theorem."""
        if r < 0 or r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n // 2:  # Optimization: C(n, r) = C(n, n-r)
            r = n - r

        res = 1
        temp_n, temp_r = n, r
        while temp_n > 0 or temp_r > 0:
            ni = temp_n % 5
            ri = temp_r % 5
            if ri > ni:
                return 0
            # Use precomputed C(ni, ri) % 5
            res = (res * self._C_mod5[ni][ri]) % 5
            if res == 0:  # Optimization
                return 0
            temp_n //= 5
            temp_r //= 5
        return res

    def _nCr_mod2(self, n: int, r: int) -> int:
        """Calculates C(n, r) % 2."""
        if r < 0 or r > n:
            return 0
        # C(n, r) is odd iff r is a submask of n in binary representation
        return 1 if (n & r) == r else 0

    def _nCr_mod10(self, n: int, r: int) -> int:
        """Calculates C(n, r) % 10 using CRT based on mod 2 and mod 5."""
        if r < 0 or r > n:
            return 0
        if r > n // 2:  # Optimization C(n, r) = C(n, n-r)
            r = n - r

        mod2 = self._nCr_mod2(n, r)
        # Optimization: if mod2 is 0, result must be even (0, 2, 4, 6, 8)
        # If C(n,r)%2 is 0, no need to calculate mod5 if we only need parity later?
        # No, we need the exact value mod 10.

        mod5 = self._nCr_mod5(n, r)
        # Optimization: if mod5 is 0, result must be 0 or 5.
        # Combined with mod2: mod5=0, mod2=0 -> 0; mod5=0, mod2=1 -> 5.
        if mod5 == 0:
            return 0 if mod2 == 0 else 5

        # Combine using precomputed CRT table
        return self._crt_table[mod2][mod5]

    def hasSameDigits(self, s: str) -> bool:
        """Checks if the final two digits after operations are the same."""
        n = len(s)
        # Constraints state 3 <= n <= 10^5, so no need to check n < 3 explicitly

        digits = [int(d) for d in s]
        k = n - 2  # Number of operations = degree of binomial coefficients

        d0 = 0
        d1 = 0

        # Calculate d0 = sum(C(k, i) * digits[i]) % 10
        # Calculate d1 = sum(C(k, i) * digits[i+1]) % 10
        for i in range(k + 1):  # i from 0 to k
            coeff = self._nCr_mod10(k, i)
            if coeff == 0:  # Optimization: skip if coefficient is 0
                continue

            # Accumulate contribution to d0
            d0 = (d0 + coeff * digits[i]) % 10

            # Accumulate contribution to d1
            # digits has length n = k+2. Max index needed is k+1.
            d1 = (d1 + coeff * digits[i+1]) % 10

        return d0 == d1
