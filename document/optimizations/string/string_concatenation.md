# Optimization: String Concatenation Efficiency

## Description

Efficiently concatenating strings is important in Python due to the immutability of strings. Different methods have varying performance characteristics.

## Methods & Performance

1.  **`+` or `+=` Operator:**
    *   `s = s1 + s2` or `s += s3`
    *   **Performance:** In CPython versions prior to ~2.4, this was often O(N*M) or O(N^2) in loops due to creating new strings at each step.
    *   **Modern Python:** CPython has significant optimizations (since ~2.4/2.5) for the `s += other` pattern, often making it closer to O(N) total time when building a string incrementally *by appending*. However, `s = s1 + s2 + s3 + ...` can still involve intermediate string creation.
    *   **Readability:** Often the most readable for simple cases.

2.  **`%` Formatting (Older Style):**
    *   `s = "%s %s" % (val1, val2)`
    *   **Performance:** Generally less efficient than newer methods, involves parsing the format string.
    *   **Readability:** Less readable and flexible than f-strings or `.format()`.

3.  **`str.format()` Method:**
    *   `s = "{} {}".format(val1, val2)`
    *   **Performance:** More efficient than `%` formatting, but generally slightly slower than f-strings for equivalent operations.
    *   **Readability:** Quite readable, more powerful than `%`.

4.  **f-Strings (Formatted String Literals - Python 3.6+):**
    *   `s = f"{val1} {val2}"`
    *   **Performance:** Generally the fastest method for creating strings from variables or expressions due to optimized bytecode generation.
    *   **Readability:** Considered highly readable and concise.

5.  **`str.join(iterable)`:**
    *   `s = "".join([str1, str2, str3])` or `s = "-".join(list_of_strings)`
    *   **Performance:** The **most efficient** way to concatenate multiple strings stored in a list or other iterable. It calculates the total required size once and creates the final string in a single pass (O(N) where N is the total length).
    *   **Readability:** Very clear when combining elements from an iterable.

## Recommendations

*   **Building strings incrementally in loops:** Use `list.append()` and then `" ".join(list)` at the end. ([See String vs. List Manipulation](string_vs_list_manipulation.md))
*   **Combining a few existing strings/variables:** Use **f-strings** (Python 3.6+) for best performance and readability.
*   **Combining many strings from a list/iterable:** Use **`str.join()`**. This is the standard and most efficient way.
*   Avoid `%` formatting in new code.
*   Use `str.format()` if f-strings are not available or if the format string is not known at compile time.

## Related Concepts

*   String Immutability
*   [String vs. List Manipulation](string_vs_list_manipulation.md)
*   f-Strings
*   `str.format()`
*   `str.join()` 