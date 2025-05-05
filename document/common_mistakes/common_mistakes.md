# Common Mistakes - Overview

**Category:** Common Mistakes (`common_mistakes/`)

## 1. General Concept

Recognizing common pitfalls and sources of error is crucial for efficient debugging and developing robust solutions. This section documents frequently encountered mistakes in algorithmic problem-solving, ranging from logical errors to subtle implementation issues.

Being aware of these common mistakes can help anticipate potential problems during development and speed up the debugging process when tests fail.

## 2. Categories of Common Mistakes

Mistakes can often be categorized based on their nature:

### a. Logic Errors
*   **Concept:** Flaws in the core algorithm design or reasoning.
*   **Examples:**
    *   Incorrect assumption about problem properties (e.g., greedy choice property doesn't hold).
    *   Insufficient DP state (doesn't capture all needed information).
    *   Incorrect base cases or transition logic in DP/recursion.
    *   Misunderstanding problem statement constraints or edge cases.
    *   Rigidly applying a standard algorithm where a modification is needed: [[./logic/rigid_algorithm_application.md]]
    *   Incorrect assumption on derived structures (e.g., shortest paths): [[./graph/incorrect_shortest_path_assumption_on_derived_tree.md]]

### b. Implementation Errors
*   **Concept:** Bugs introduced during the coding process, even if the high-level logic is sound.
*   **Examples:**
    *   Off-by-one errors in loops or indexing.
    *   Incorrect variable updates.
    *   Mismatched indices or keys in data structures: [[./hash_map_index_mismatch.md]]
    *   Integer overflow/underflow: [[./integer_overflow_check.md]]
    *   Floating-point precision issues in comparisons: [[./float_precision_in_comparisons.md]]
    *   Incorrect handling of visited states in traversals (infinite loops).
    *   Errors in specific edge cases like zero: [[./dp_product_limit_zero_interaction.md]]

### c. Performance Issues
*   **Concept:** Solutions that are logically correct but exceed time or memory limits.
*   **Examples:**
    *   Choosing an algorithm with inappropriate time complexity (e.g., O(N^2) when O(N log N) is needed).
    *   Inefficient operations within loops (e.g., list slicing, slow string concatenation).
    *   Unexpectedly high space complexity (e.g., storing large intermediate results): [[./performance/space_complexity_overlooked.md]]
    *   Performance bottlenecks with specific operations (e.g., large exponentiation): [[./large_exponent_performance.md]]

### d. Constraint Handling Errors
*   **Concept:** Failing to properly handle the input constraints defined in the problem.
*   **Examples:**
    *   Not considering minimum/maximum input values.
    *   Ignoring constraints on element values or ranges.
    *   Errors in handling violation checks: [[./constraint_violation_handling.md]]

### e. Testing and Verification Errors
*   **Concept:** Mistakes made during the process of testing the solution.
*   **Examples:**
    *   Incorrect calculation of expected outputs for test cases: [[./test_case_logic_errors.md]]
    *   Insufficient test coverage (missing edge cases).
    *   Incorrect test setup (e.g., environment issues, import errors): [[./unittest_import_error.md]]

## 3. Debugging Strategy

When encountering errors:
1.  Reproduce the failure with a specific test case.
2.  Trace the execution flow for that test case.
3.  Verify assumptions made in the algorithm design.
4.  Check for common mistake patterns listed above.
5.  Simplify the problem or test case if possible.

Explore the linked documents for details on specific mistakes. 