import collections
from typing import List


class Solution:
    """Solves LeetCode 3528: Unit Conversion I using a single BFS pass.

    Leverages the problem guarantee that conversions define a unique path
    from root 0 without reverse conversions, implying the input format
    [source, target, factor] inherently defines the directed edges away from root 0.
    """

    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        """Calculates the conversion factor from unit 0 to all other units.

        Args:
            conversions: A list of conversions [source, target, factor],
                         defining directed edges away from root 0.

        Returns:
            A list where the i-th element is the factor to convert 1 unit of type 0
            to units of type i, modulo 10^9 + 7.
        """
        n = len(conversions) + 1
        MOD = 10**9 + 7

        # Build directed adjacency list based on the problem guarantee
        adj = collections.defaultdict(list)
        for u, v, factor in conversions:
            # Assuming [u, v, factor] means u is parent, v is child relative to root 0
            if 0 <= u < n and 0 <= v < n:
                adj[u].append((v, factor))
            # else: handle potential out-of-bounds, though constraints likely prevent this

        # Initialize baseUnitConversion array
        # -1 indicates not yet calculated/visited from root 0
        baseUnitConversion = [-1] * n
        if n == 0:
            return []
        baseUnitConversion[0] = 1  # Unit 0 converts to itself with factor 1

        # Single BFS pass to calculate factors
        q = collections.deque([0])

        while q:
            u = q.popleft()
            current_factor_u = baseUnitConversion[u]

            for v, factor_uv in adj.get(u, []):  # Use .get for safety
                # Process node v only if it hasn't been reached/calculated yet
                # and ensure it's within bounds
                if 0 <= v < n and baseUnitConversion[v] == -1:
                    new_factor_v = (current_factor_u * factor_uv) % MOD
                    baseUnitConversion[v] = new_factor_v
                    q.append(v)

        # Problem guarantees all nodes are reachable from 0
        # Replace any remaining -1 with 0? Or assume they are filled.
        # LeetCode likely expects all nodes 0 to n-1 to have a valid factor.
        # If any node remained -1, it would indicate an issue with input/guarantee.
        # Let's assume the guarantee holds and all will be filled.

        return baseUnitConversion
