# Edmonds-Karp Time Complexity Proof Strategy

**Category:** Optimizations
**Sub-Category:** Graph (Max Flow Complexity Analysis)

## Overview

This document outlines the proof strategy used to show that the [[../../algorithms/graph/max_flow_edmonds_karp.md]] algorithm runs in `O(V * E^2)` time. The core idea is to bound the total number of augmentations performed.

The proof relies on analyzing the properties of the shortest path distances from the source `s` in the [[../../techniques/graph/residual_graph.md]] (`Gf`) as the algorithm progresses.

## Key Lemmas and Arguments

Let `d_f(u, v)` denote the shortest path distance (number of edges) from `u` to `v` in the residual graph `Gf` corresponding to flow `f`.

### Lemma 1: Shortest Path Distances are Non-Decreasing

**Statement:** During the execution of Edmonds-Karp, for any vertex `v`, the shortest path distance `d_f(s, v)` from the source `s` in the residual graph `Gf` never decreases.

**Proof Sketch (by Contradiction):**
*   Assume an augmentation using path `p` changes the flow from `f` to `f'`, and for some vertex `v`, `d_{f'}(s, v) < d_f(s, v)`. Let `v` be the vertex with the *smallest* such distance `d_{f'}(s, v)` after the augmentation.
*   Consider the shortest path `s -> ... -> u -> v` in `Gf'`. The edge `(u, v)` must exist in `Gf'`.
*   Since `u` precedes `v` on this shortest path, `d_{f'}(s, u) = d_{f'}(s, v) - 1`.
*   Because `v` had the minimum distance that decreased, `u`'s distance cannot have decreased: `d_{f'}(s, u) >= d_f(s, u)`.
*   Therefore, `d_f(s, u) <= d_{f'}(s, u) = d_{f'}(s, v) - 1 < d_f(s, v) - 1`.
*   Now, consider the edge `(u, v)` in `Gf'`. If `(u, v)` also existed in `Gf`, then `d_f(s, v) <= d_f(s, u) + 1`. Combining with the previous inequality gives `d_f(s, u) < d_f(s, u)`, a contradiction.
*   If `(u, v)` did *not* exist in `Gf`, it means `(u, v)` must be a backward edge corresponding to an original edge `(v, u)` that was *part of the augmenting path `p`* used to go from `f` to `f'`. Since `p` was a *shortest* path found by BFS in `Gf`, we must have had `d_f(s, u) = d_f(s, v) + 1`.
*   Substituting this into `d_f(s, u) <= d_{f'}(s, u)` gives `d_f(s, v) + 1 <= d_{f'}(s, u) = d_{f'}(s, v) - 1`. This implies `d_f(s, v) <= d_{f'}(s, v) - 2`, which contradicts the initial assumption that `d_{f'}(s, v) < d_f(s, v)`.
*   Thus, the assumption fails, and distances `d_f(s, v)` are non-decreasing.

### Lemma 2: Edge Saturation Requires Distance Increase

**Statement:** If an edge `(u, v)` is saturated (becomes the bottleneck edge) by an augmenting path `p` found by BFS at some point, then the next time `(u, v)` appears on a *shortest* augmenting path found by BFS, the distance `d(s, u)` must have increased by at least 2 compared to its value when `(u, v)` was first saturated.

**Proof Sketch:**
*   When `(u, v)` is saturated by path `p`, `p` is a shortest path, so `d_f(s, v) = d_f(s, u) + 1`.
*   After saturation, `(u, v)` disappears from the residual graph `Gf'`. It cannot reappear until flow is pushed back along the reverse edge `(v, u)`.
*   Let `f''` be the flow when `(v, u)` is first used in a *shortest* augmenting path `p'` found by BFS. By definition of shortest path, `d_{f''}(s, u) = d_{f''}(s, v) + 1`.
*   By Lemma 1 (distance non-decreasing), `d_{f''}(s, v) >= d_f(s, v)`.
*   Combining these: `d_{f''}(s, u) = d_{f''}(s, v) + 1 >= d_f(s, v) + 1 = (d_f(s, u) + 1) + 1 = d_f(s, u) + 2`.
*   Therefore, the distance `d(s, u)` must increase by at least 2 between consecutive times `(u, v)` is used as a critical edge on a shortest augmenting path.

## Bounding Augmentations

1.  The shortest path distance `d_f(s, v)` for any `v` is always less than `|V|` (number of vertices).
2.  By Lemma 1, distances `d_f(s, v)` never decrease.
3.  By Lemma 2, each time an edge `(u, v)` becomes saturated, `d(s, u)` must increase by at least 2 before `(u, v)` can become saturated again.
4.  Since `d(s, u)` is bounded by `|V|-1`, any specific edge `(u, v)` can become saturated at most `O(V)` times (specifically, `~ |V| / 2` times).
5.  Each augmentation saturates at least one edge.
6.  There are `O(E)` possible edges in the original graph that could become saturated.
7.  Therefore, the total number of augmentations is bounded by `O(V * E)`.

## Overall Complexity

*   Number of augmentations: `O(V * E)`
*   Time per augmentation (BFS): `O(E)`
*   Total Time: `O(V * E) * O(E) = O(V * E^2)`

## Related Concepts

*   [[../../algorithms/graph/max_flow_edmonds_karp.md]]
*   [[../../algorithms/graph/max_flow_ford_fulkerson.md]]
*   [[../../techniques/graph/residual_graph.md]]
*   [[../../techniques/graph/augmenting_path.md]]
*   [[../../algorithms/graph_search/bfs.md]]
*   Proof by Contradiction (Mathematical Technique) 