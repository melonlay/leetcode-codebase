# Technique: Handle Sign Separately

## Description

When dealing with numerical problems that involve manipulating the digits or structure of a number (like reversing digits, checking for palindromes, summing digits), and the core logic operates independently of the number's sign, it's often cleaner and less error-prone to:

1.  Determine and store the original sign of the number (positive, negative, or zero).
2.  Perform the main logic on the *absolute value* of the number.
3.  Re-apply the original sign to the final result.

This avoids complicating the core manipulation logic with checks for negative signs during intermediate steps (e.g., during modulo or division operations).

## Algorithm Outline

1.  Check if the input number `x` is zero. If so, return 0.
2.  Store the sign: `sign = 1 if x > 0 else -1`.
3.  Work with the absolute value: `x_abs = abs(x)`.
4.  Perform the primary calculation/manipulation on `x_abs` to get an intermediate `result_abs`.
5.  Apply the sign to the final result: `final_result = sign * result_abs`.
6.  (If applicable) Check if `final_result` adheres to any constraints (like integer limits) before returning.

## Example: LeetCode 7 - Reverse Integer

In reversing an integer like `-123`, the reversal logic (extracting digits 3, 2, 1 and combining them to 321) is the same as for `123`.

```python
class Solution:
    def reverse(self, x: int) -> int:
        # Step 1 & 2: Handle zero and store sign
        if x == 0:
            return 0
        INT_MAX = 2**31 - 1
        sign = 1 if x > 0 else -1

        # Step 3: Work with absolute value
        x_abs = abs(x)

        # Step 4: Perform main logic on absolute value
        reversed_abs = 0
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            # (Overflow check on reversed_abs omitted for brevity)
            if reversed_abs > INT_MAX // 10 or (reversed_abs == INT_MAX // 10 and digit > 7):
                 return 0 # Overflow
            reversed_abs = reversed_abs * 10 + digit

        # Step 5: Re-apply sign
        final_result = sign * reversed_abs

        # Step 6: (Overflow already checked)
        return final_result
```

## Benefits

*   **Simplicity:** Keeps the core digit/number manipulation logic cleaner.
*   **Readability:** Easier to understand the main transformation without interleaved sign checks.
*   **Reduced Errors:** Less chance of making mistakes with modulo/division on negative numbers (whose behavior can sometimes vary by language or be less intuitive).

## Applicability

This technique is useful for problems like:
*   Reversing integers.
*   Checking if a number is a palindrome.
*   Summing digits of a number.
*   Converting numbers to different bases (where the absolute value is converted first). 