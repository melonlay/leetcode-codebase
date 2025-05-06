import sys

MOD = 10**9 + 7
# MAX_LEN = 101  # Max length of r string + buffer for combinations
# MAX_BASE = 10

# Revised Precomputation Size Calculation
MAX_LEN_INPUT = 100  # Max length of input decimal string r
# Max digits in base b (worst case b=2): floor(MAX_LEN_INPUT * log2(10)) + 1 approx 332 + 1 = 333
MAX_DIGITS_B = 335  # A bit of buffer
MAX_BASE = 10
# Max value needed for n in nCr(n,k) is roughly MAX_DIGITS_B + MAX_BASE
MAX_N_COMB = MAX_DIGITS_B + MAX_BASE  # Around 345, use 350 for safety


# Precompute factorials and modular inverses
# fact = [1] * (MAX_LEN + MAX_BASE)
# inv_fact = [1] * (MAX_LEN + MAX_BASE)
fact = [1] * MAX_N_COMB
inv_fact = [1] * MAX_N_COMB


# for i in range(1, MAX_LEN + MAX_BASE):
for i in range(1, MAX_N_COMB):
    fact[i] = (fact[i - 1] * i) % MOD

# Calculate modular inverse using Fermat's Little Theorem (MOD is prime)
# inv_fact[MAX_LEN + MAX_BASE - 1] = pow(fact[MAX_LEN + MAX_BASE - 1], MOD - 2, MOD)
inv_fact[MAX_N_COMB - 1] = pow(fact[MAX_N_COMB - 1], MOD - 2, MOD)
# for i in range(MAX_LEN + MAX_BASE - 2, -1, -1):
for i in range(MAX_N_COMB - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD


def nCr_mod(n, r):
    """Calculates nCr % MOD using precomputed values"""
    if r < 0 or r > n:
        return 0
    # Check bounds against precomputed array size
    if n >= MAX_N_COMB:
        # This case should ideally not happen with correct MAX_N_COMB calculation
        # Handle error or return 0/appropriate value if it does
        # For now, assume MAX_N_COMB is sufficient
        # print(f"Warning: n={n} exceeds MAX_N_COMB={MAX_N_COMB}")
        pass
    num = fact[n]
    den = (inv_fact[r] * inv_fact[n - r]) % MOD
    return (num * den) % MOD


def combinations_with_repetition(n_items, k_choices):
    """Calculates combinations with repetition C(n+k-1, k)"""
    if n_items == 0 and k_choices > 0:  # Cannot choose from 0 items
        return 0
    if k_choices == 0:  # Only one way to choose 0 items (empty set)
        return 1
    # Need to handle n_items + k_choices - 1 potentially being negative if n_items=0, k_choices=0? No, k_choices==0 returns 1.
    # If n_items=1, k_choices=0 -> C(0,0)=1. Correct.
    # If n_items=0, k_choices=0 -> returns 1. Correct.
    return nCr_mod(n_items + k_choices - 1, k_choices)


class Solution:

    def _to_base_b(self, n: int, b: int) -> list[int]:
        """Converts a non-negative integer n to its list representation (digits) in base b."""
        if n == 0:
            return [0]  # Represent 0 as [0] for consistency
        digits = []
        while n > 0:
            digits.append(n % b)  # Store as int directly
            n //= b
        # If the original number was 0, digits is empty, handle this? No, handled by n==0 case.
        return digits[::-1]  # Return list of ints

    def _count_le(self, num: int, b: int) -> int:
        """Counts non-decreasing numbers x such that 0 <= x <= num in base b using combinations."""
        if num < 0:
            return 0  # No non-negative numbers less than 0

        # Handle num = 0 separately. Base representation is [0].
        # It is non-decreasing. Count is 1 (just the number 0).
        if num == 0:
            return 1

        s_digits = self._to_base_b(num, b)
        n = len(s_digits)
        ans = 0  # This will count numbers in [1, num]

        # 1. Count positive non-decreasing numbers with length < n
        for length in range(1, n):
            # Choose 'length' digits from 'b' options (0 to b-1) with repetition
            # count = combinations_with_repetition(b, length)
            # Subtract the all-zero case (number 0) which is counted by CWR but not positive
            # ans = (ans + count - 1 + MOD) % MOD

            # CORRECTED logic: Count positive non-decreasing numbers.
            # Choose 'length' digits from 'b-1' options (1 to b-1) with repetition
            count = combinations_with_repetition(b - 1, length)
            ans = (ans + count) % MOD

        # 2. Count positive non-decreasing numbers with length n that are <= num
        last_digit = 0
        is_non_decreasing_prefix = True
        for i in range(n):
            limit = s_digits[i]

            # Determine start digit for this position
            start_digit = 1 if i == 0 else last_digit

            for digit in range(start_digit, limit):
                rem_len = n - 1 - i
                num_items = b - digit  # Digits available are 'digit' through 'b-1'

                count = combinations_with_repetition(num_items, rem_len)
                ans = (ans + count) % MOD

            # Check if the prefix s[0...i] is non-decreasing
            # Note: first digit check (i=0) is implicitly handled as last_digit=0 initially
            if limit < last_digit:
                is_non_decreasing_prefix = False
                break

            last_digit = limit

        # 3. If the number `num` itself (represented by s_digits) is non-decreasing, add 1
        if is_non_decreasing_prefix:
            ans = (ans + 1) % MOD

        # `ans` currently holds the count of non-decreasing numbers in [1, num].
        # We need the count in [0, num]. Add 1 for the number 0.
        return (ans + 1) % MOD

    def countNumbers(self, l: str, r: str, b: int) -> int:
        """
        Calculates the count of numbers x in [l, r] (inclusive)
        such that x has non-decreasing digits in base b.
        Uses the combinatorial approach.
        """
        l_int = int(l)
        r_int = int(r)

        # Calculate count of non-decreasing numbers <= r (includes 0)
        count_r = self._count_le(r_int, b)

        # Calculate count of non-decreasing numbers <= l-1 (includes 0)
        count_l_minus_1 = self._count_le(l_int - 1, b)

        # The result is count(<=r) - count(<=l-1)
        ans = (count_r - count_l_minus_1 + MOD) % MOD

        return ans
