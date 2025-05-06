# Residual Graph

**Category:** Techniques
**Sub-Category:** Graph (Max Flow)

## Description

The Residual Graph (`Gf`) is a fundamental concept used in maximum flow algorithms like Ford-Fulkerson and its variants (Edmonds-Karp, Dinic). Given a flow network `G = (V, E)` with capacities `c(u, v)` and a current flow `f(u, v)`, the residual graph represents the *remaining capacity* for pushing additional flow.

## Construction

For a given flow `f`, the residual graph `Gf = (V, Ef)` has the same vertex set `V` as the original graph `G`. The edges `Ef` and their *residual capacities* `cf(u, v)` are defined as follows:

1.  **Forward Edges:** For each edge `(u, v)` in the original graph `E`:
    *   If `f(u, v) < c(u, v)`, include a forward edge `(u, v)` in `Ef` with residual capacity `cf(u, v) = c(u, v) - f(u, v)`. This represents the additional flow that can be pushed directly from `u` to `v`.

2.  **Backward Edges (Reverse Edges):** For each edge `(u, v)` in the original graph `E`:
    *   If `f(u, v) > 0`, include a backward edge `(v, u)` in `Ef` with residual capacity `cf(v, u) = f(u, v)`. This represents the flow that can be "pushed back" or "canceled" from `v` to `u`, effectively decreasing the flow on the original edge `(u, v)`.

**Note:** An edge `(u, v)` in the original graph `G` can result in *both* a forward edge `(u, v)` and a backward edge `(v, u)` appearing in `Gf` if `0 < f(u, v) < c(u, v)`.

**Number of Edges:** The number of edges in `Gf` can be up to twice the number of edges in `G` (at most `2 * |E|`).

## Purpose in Max Flow

The residual graph is crucial because:

1.  **Finding Augmenting Paths:** An [[augmenting_path.md]] in the *residual graph* `Gf` corresponds to a path along which additional flow can be pushed in the original graph `G`. A path from source `s` to sink `t` in `Gf` with all edges having `cf(u, v) > 0` indicates that more flow can be sent from `s` to `t`.
2.  **Calculating Augmentation Amount:** The bottleneck capacity of an augmenting path found in `Gf` (the minimum `cf(u, v)` along the path) determines the maximum amount of additional flow that can be pushed along that corresponding path/cycle in `G`.
3.  **Updating Flow:** Pushing flow `fp` along an augmenting path in `Gf` updates the flow `f` in `G` and subsequently modifies the residual graph `Gf` for the next iteration.
    *   For each forward edge `(u, v)` on the path in `Gf`, increase `f(u, v)` by `fp`. This decreases `cf(u, v)` and increases `cf(v, u)` in the next `Gf`.
    *   For each backward edge `(v, u)` on the path in `Gf`, decrease `f(u, v)` by `fp`. This increases `cf(u, v)` and decreases `cf(v, u)` in the next `Gf`.

## Related Concepts

*   [[augmenting_path.md]]
*   [[../../algorithms/graph/max_flow_ford_fulkerson.md]]
*   [[../../algorithms/graph/max_flow_edmonds_karp.md]]
*   [[../../algorithms/graph/max_flow_dinic.md]] 