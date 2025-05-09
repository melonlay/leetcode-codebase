# Achievable Range of XOR Sums with Basis Elements

**Concept Type:** Mathematical Property (Combinatorics, Bit Manipulation)

**Description:**
Given a set of numbers $P = \{v_1, v_2, \ldots, v_m\}$. If $P$ contains a basis set $B = \{1, 2, 4, \ldots, 2^{k-1}\}$ that can generate all integers up to $2^k-1$ via XOR sums, then it is often possible to form all integers in the range $[0, 2^k-1]$ as an XOR sum of a fixed number of elements (e.g., three elements) chosen from $P$.

**Specific Application (XOR Triplet Problem - LC3513):**
If we need to find the number of unique values for $x \oplus y \oplus z$, where $x, y, z$ are chosen from the set $P_n = \{1, 2, \ldots, n\}$.

*   For $n \ge 3$: Let $k = n.bit\_length()$. This implies $2^{k-1} \le n < 2^k$.
    The set $P_n$ contains all powers of two: $1, 2, 4, \ldots, 2^{k-1}$. These form a basis for the integers in the range $[0, 2^k-1]$.
    It can be shown that any integer $X$ in the range $[0, 2^k-1]$ can be formed as $v_1 \oplus v_2 \oplus v_3$, where $v_1, v_2, v_3 \in P_n$.
    Furthermore, since each $v_i < 2^k$, their XOR sum $v_1 \oplus v_2 \oplus v_3$ will also be less than $2^k$.
    Therefore, the set of all unique XOR triplet values is exactly $\{0, 1, \ldots, 2^k-1\}$.
    The count of such unique values is $2^k = 1 \ll k = 1 \ll n.bit\_length()$.

**Proof Sketch / Justification for $n \ge 3$:**
1.  **Value 0:** $1 \oplus 2 \oplus 3 = 0$. Since $n \ge 3$, $1,2,3 \in P_n$.
2.  **Values $X \in [1, n]$:** $X = X \oplus 1 \oplus 1$. Since $n \ge 3$, $1 \in P_n$. If $X \in P_n$, this is valid.
3.  **General Values $X \in [0, 2^k-1]$:** (This is the less trivial part requiring a more detailed combinatorial argument, often cited as a known result in competitive programming for such problems).
    A common way to argue is: pick $v_3 = 1$ (since $1 \in P_n$). We need to show $X \oplus 1$ can be formed by $v_1 \oplus v_2$. Any number $Y < 2^k$ can be formed by XORing two numbers from $P_n$ if $P_n$ is sufficiently dense (contains the basis). For example, $Y = (Y \oplus v) \oplus v$. If we can choose $v$ and $Y \oplus v$ to be in $P_n$, it works.
    More formally, the property relies on the fact that with the basis $\{1, 2, \dots, 2^{k-1}\}$ available within $P_n$, one can construct any target XOR sum $X \in [0, 2^k-1]$ by carefully selecting three elements. For example, one could be $X$ itself (if $X \in P_n$, then $X \oplus 1 \oplus 1$), or combinations of basis elements.

**Key Conditions for Applicability:**
*   The set of available numbers ($P_n$) must contain the necessary basis elements ($1, 2, \ldots, 2^{k-1}$).
*   The elements chosen for the XOR sum must be drawn from this set $P_n$.
*   The problem asks for a fixed number of elements in the XOR sum (e.g., three).

**Implications:**
This mathematical property allows for an $O(1)$ solution (after determining $n.bit\_length()$) instead of brute-force enumeration or incorrect pattern matching for problems asking for the count of unique XOR sums under these conditions.

**Related Concepts:**
*   Bit Manipulation
*   Basis (Linear Algebra over GF(2))
*   [[../../techniques/bit_manipulation/bitmask_state_tracking.md]] (Related as it uses bitwise properties)
 