# Dinic's Algorithm Time Complexity Proof Strategy

**Category:** Optimizations
**Sub-Category:** Graph (Max Flow Complexity Analysis)

## Overview

This document outlines the proof strategy used to show that [[../../algorithms/graph/max_flow_dinic.md]] (Dinic's algorithm) runs in `O(V^2 * E)` time. The proof involves analyzing the number of phases and the complexity of each phase.

A phase consists of building a [[../../techniques/graph/level_graph.md]] and finding a [[../../techniques/graph/blocking_flow.md]] within it.

## Key Arguments

### 1. Complexity per Phase: `O(V * E)`

*   **Level Graph Construction (BFS):** Takes `O(E)` time.
*   **Finding Blocking Flow (DFS):** This is the more complex part. Using DFS with pointer-based edge exploration (to avoid re-exploring dead ends or fully saturated paths within the phase) can be shown to take `O(V * E)` time. The analysis considers:
    *   Time spent advancing along DFS paths.
    *   Time spent backtracking.
    *   Time spent advancing edge pointers when an edge becomes saturated or a dead end is hit.
    *   Each augmentation found takes O(V) time (path length).
    *   The number of non-augmenting edge traversals/pointer advances is bounded.
    *   Summing these components leads to an `O(V * E)` bound for finding the complete blocking flow within one phase.

### 2. Bounding the Number of Phases: `O(V)`

*   **Core Lemma:** The shortest path distance from source `s` to sink `t`, `d(s, t)`, in the [[../../techniques/graph/residual_graph.md]] `Gf` *strictly increases* after each phase of Dinic's algorithm.
*   **Proof Sketch (by Contradiction):**
    *   Let `d(u, v)` be the shortest distance in `Gf` before a phase, and `d'(u, v)` be the distance after the phase (after finding a blocking flow in the level graph `LG` based on `d`).
    *   Assume `d'(s, t) <= d(s, t)`.
    *   Consider a shortest path `p'` from `s` to `t` in the residual graph *after* the phase (`Gf'`). Let its length be `l = d'(s, t)`.
    *   We know individual distances are non-decreasing (similar to Lemma 1 in [[max_flow_ek_complexity_proof.md]]), so `d'(s, v) >= d(s, v)` for all `v`.
    *   Examine the edges `(u, v)` along path `p'`. Each edge must exist in `Gf'`.
    *   If an edge `(u, v)` existed in the level graph `LG` used during the phase, then `d(s, v) = d(s, u) + 1`. Since `d'(s, v) >= d(s, v)` and `d'(s, u) >= d(s, u)`, we have `d'(s, v) >= d(s, v) = d(s, u) + 1 <= d'(s, u) + 1`.
    *   If an edge `(u, v)` did *not* exist in `LG`, it means either `d(s, v) != d(s, u) + 1` or `(u, v)` was not in `Gf` initially.
    *   The crucial part involves showing that if `d'(s, t) <= d(s, t)`, then *every* edge `(u, v)` on the shortest path `p'` must have satisfied `d(s, v) = d(s, u) + 1`. This implies `p'` only used edges that *could* have been in the level graph `LG`.
    *   Since a *blocking flow* was found in `LG`, *every* path from `s` to `t` within `LG` must contain at least one edge that was saturated during the phase and thus is *not* present in `Gf'` with positive capacity.
    *   This contradicts the existence of path `p'` in `Gf'` consisting only of edges that could have been in `LG`. Therefore, the initial assumption fails, and `d'(s, t) > d(s, t)`.
*   **Conclusion:** Since `d(s, t)` strictly increases in each phase and the maximum possible shortest path length is `V - 1`, there can be at most `V - 1` phases.

## Overall Complexity

*   Number of phases: `O(V)`
*   Time per phase (Level Graph + Blocking Flow): `O(E) + O(VE) = O(VE)`
*   Total Time: `O(V) * O(VE) = O(V^2 * E)`

## Related Concepts

*   [[../../algorithms/graph/max_flow_dinic.md]]
*   [[../../algorithms/graph/max_flow_edmonds_karp.md]] (Comparison)
*   [[../../techniques/graph/level_graph.md]]
*   [[../../techniques/graph/blocking_flow.md]]
*   [[../../techniques/graph/residual_graph.md]]
*   [[max_flow_ek_complexity_proof.md]] (Shares non-decreasing distance idea) 