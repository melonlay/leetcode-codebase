import math
from collections import Counter
import string

# Precompute factorials (adjust MAX_L if needed, N <= 10000 -> L <= 5000)
MAX_L = 5001
factorials = [1] * MAX_L
for i in range(2, MAX_L):
    factorials[i] = factorials[i - 1] * i


def count_multiset_permutations(n: int, counts: dict) -> int:
    """
    Calculates the number of distinct permutations of a multiset.
    Uses precomputed factorials.
    Returns numerator // denominator
    """
    if n < 0:
        return 0
    if n >= len(factorials):
        raise ValueError(
            f"n={n} exceeds precomputed factorial limit {len(factorials)}")

    numerator = factorials[n]
    denominator = 1
    for count in counts.values():
        if count < 0:
            return 0
        if count >= len(factorials):
            raise ValueError(
                f"count={count} exceeds precomputed factorial limit {len(factorials)}")
        if count > 1:
            denominator *= factorials[count]
        if denominator == 0:  # Avoid division by zero if possible
            # This case should not happen with valid counts >= 0
            return float('inf')

    if denominator == 0:
        return float('inf')
    return numerator // denominator


def compute_denominator(counts: dict) -> int:
    """ Calculates the product of factorials of counts > 1."""
    denominator = 1
    for count in counts.values():
        # Ensure count is within factorial bounds
        if count >= len(factorials):
            raise ValueError(
                f"count={count} exceeds precomputed factorial limit {len(factorials)}")
        if count > 1:
            denominator *= factorials[count]
        # Allow count 0 or 1, factorial is 1, doesn't change denominator
        elif count < 0:
            raise ValueError(
                "Negative count encountered in denominator calculation")
    # Handle potential zero denominator if logic allows invalid counts, although unlikely
    if denominator == 0:
        raise ValueError("Denominator calculated as zero, check counts")
    return denominator


# Helper function to compute combinations nCr capped at a limit.
# Returns the exact value of nCr(N, k) if it's <= limit, otherwise returns limit + 1.
def nCr_capped(N, k, limit):
    # Standard base cases and symmetry property for combinations
    if k < 0 or k > N:
        return 0
    if k == 0 or k == N:
        return 1
    if k > N // 2:
        k = N - k

    # Optimization for k=1
    if k == 1:
        # C(N, 1) = N. Return N if N <= limit, otherwise limit + 1.
        # Using min ensures we don't return a value > limit + 1.
        # Note: If limit itself is very large, N could exceed it.
        return N if N <= limit else limit + 1

    res = 1
    for i in range(k):
        # Calculate res = res * (N - i) // (i + 1) iteratively.
        # Python's arbitrary precision integers handle large intermediate values.
        # We check if the result exceeds the limit after each step.

        # Direct computation using Python's arbitrary precision integers
        # Check for potential overflow BEFORE multiplication if limit is near maxint
        # In Python 3, integers have arbitrary precision, overflow is less of a concern
        # unless memory runs out or operations become extremely slow.
        # Check if res * (N - i) might realistically exceed limits if 'limit' is huge.
        # For typical limits like 10^6, 10^9, this is fine.

        numerator_product = res * (N - i)
        # Check before division if intermediate product itself exceeds limit in a significant way
        # This check might be overly conservative but prevents massive intermediate numbers if N, k are large
        # if numerator_product // (i + 1) > limit: # Approximate check
        #     return limit + 1

        res = numerator_product // (i + 1)

        # Check if the result exceeds the limit
        if res > limit:
            # Return limit + 1 to signify that the actual value is greater than limit.
            return limit + 1

    # If loop completes without exceeding limit, return the computed result.
    # Final check just in case (should be redundant if check inside loop is correct)
    # return res if res <= limit else limit + 1
    return res


# Helper function to compute multinomial coefficient capped at a limit.
# N! / (n1! * n2! * ... * nk!) where counts = [n1, n2, ..., nk] and sum(counts) == N.
# Returns the exact value if <= limit, otherwise returns limit + 1.
def multinomial_capped(N, counts, limit):
    # Initialize result to 1.
    res = 1
    # Keep track of the remaining N after accounting for counts processed so far.
    current_N = N

    # Filter out zero counts as they don't affect the multinomial coefficient value.
    # Use a copy or generator if counts list/dict is modified elsewhere
    active_counts = [c for c in counts if c > 0]

    # Iterate through each count ni
    for count_val in active_counts:
        # If remaining N is less than current count, something is wrong
        if current_N < count_val:
            raise ValueError(
                "Logic error: current_N became less than count_val")

        # Calculate the binomial coefficient C(current_N, count_val) capped at limit.
        # This represents choosing count_val items from the remaining current_N items.
        # Pass the current 'limit' which acts as the effective cap for intermediate C(n,k)
        binom_val = nCr_capped(current_N, count_val, limit)

        # If binom_val itself exceeded the limit, the total multinomial coeff will also exceed.
        # Note: nCr_capped returns limit + 1 if it exceeds.
        if binom_val > limit:
            return limit + 1

        # Check if multiplying the current result `res` by `binom_val` would exceed the limit.
        # Since binom_val <= limit, we check if res > limit // binom_val to avoid potential overflow
        # This is safer than calculating potential_res directly if limit is huge.
        # However, with Python's arbitrary precision, direct multiplication is usually fine.
        # Let's stick to direct for clarity unless specific overflow is hit.
        potential_res = res * binom_val

        if potential_res > limit:
            # If the potential result exceeds limit, return limit + 1.
            return limit + 1

        # Update the result and decrease current_N.
        res = potential_res
        current_N -= count_val

    # After processing all counts, `res` holds the multinomial coefficient if <= limit.
    # The checks inside the loop ensure `res` doesn't exceed limit.
    # No final check needed as intermediate checks handle it.
    return res


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        """
        Finds the k-th smallest palindromic rearrangement of s.
        """
        N = len(s)
        counts = Counter(s)
        half_counts = Counter()
        mid_char = ""
        found_odd = False

        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            count = counts.get(char, 0)
            if count > 0:
                if count % 2 == 1:
                    if found_odd:
                        # This case implies input s was not a palindrome, handle defensively
                        # Or raise error based on problem constraints guarantee.
                        # Let's assume guarantee holds and this won't be entered.
                        pass
                    mid_char = char
                    found_odd = True
                half_count_val = count // 2
                if half_count_val > 0:
                    half_counts[char] = half_count_val

        m = N // 2

        if m == 0:
            if N == 1:
                return mid_char if k == 1 else ""
            else:
                return ""

        half_counts_list = list(half_counts.values())

        try:
            total_perms = multinomial_capped(m, half_counts_list, k)
        except ValueError as e:
            print(f"Error calculating initial total permutations: {e}")
            return ""

        if total_perms < k:
            return ""

        H = []
        current_counts = half_counts.copy()
        current_m = m

        for i in range(m):
            if current_m <= 0:
                break

            rem_len = current_m - 1

            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)

                if current_counts.get(char, 0) > 0:
                    current_counts[char] -= 1

                    current_hc_list = [
                        count for count in current_counts.values() if count > 0]

                    try:
                        num_perms = multinomial_capped(
                            rem_len, current_hc_list, k)
                    except ValueError as e:
                        print(f"Error calculating num_perms: {e}")
                        current_counts[char] += 1
                        return ""

                    if k <= num_perms:
                        H.append(char)
                        current_m -= 1
                        break
                    else:
                        k -= num_perms
                        current_counts[char] += 1
                else:
                    print("Error: Inner loop completed without finding a character.")
                    return ""

        H_str = "".join(H)

        if N % 2 == 1:
            return H_str + mid_char + H_str[::-1]
        else:
            return H_str + H_str[::-1]
