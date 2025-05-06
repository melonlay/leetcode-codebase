# Methodology: Algorithm Discovery via Knowledge Base

**Category:** Methodology

## Goal

This document outlines a systematic process for leveraging the knowledge base (KB) to identify and select suitable algorithms or patterns for solving a problem, especially when the optimal approach is not immediately apparent.

This process adheres to the principles outlined in the `python-leetcode` ruleset, particularly Rule 2 (Algorithmic Strategy, Critical Validation, & Knowledge Base Interaction).

## Process Steps

This process typically occurs after initial problem deconstruction and brainstorming (Rule 2a) and triggers the mandatory KB consultation (Rule 2b).

1.  **Problem Formulation & Initial Keywords:**
    *   Translate the problem's core mechanics, constraints, and objectives into abstract concepts (e.g., "find shortest path," "maximize flow through network," "assign limited resources," "find pattern in sequence," "process overlapping intervals").
    *   Identify potential graph structures, data types (sequences, matrices, trees), or mathematical properties involved.

2.  **Mandatory KB Index Check:**
    *   Always start by reading `document/kb_index.md` to get an overview of available categories and potentially relevant high-level concepts.

3.  **Initial Targeted Search (`codebase_search`):**
    *   Use the abstract keywords and concepts identified in Step 1 to perform initial searches.
    *   Focus on patterns, algorithms, or techniques related to the *type* of problem or *structure* identified (e.g., `query="maximum flow graph capacity"`, `query="sliding window pattern array"`, `query="dynamic programming sequence subsequence"`).
    *   Prioritize searching `document/patterns/` and `document/algorithms/`.

4.  **Analyze Search Results & Follow Links (`read_file`):**
    *   Examine the search results for promising leads.
    *   **Crucially, use `read_file` to read the *full content* of any potentially relevant KB entry.** Do not rely solely on snippets or filenames.
    *   Pay close attention to the "Related Concepts" sections within KB files and follow relevant `[[links]]` to explore connected ideas.
    *   Read foundational technique files (e.g., `[[../techniques/graph/residual_graph.md]]`) linked from algorithms or patterns to understand the underlying mechanics.

5.  **Verify Applicability & Complexity:**
    *   Critically evaluate whether the concepts read from the KB truly apply to the specific problem constraints and requirements.
    *   Check the documented time/space complexity against the problem's constraints. Use linked complexity proof files (e.g., `[[../../optimizations/graph/max_flow_ek_complexity_proof.md]]`) if necessary.
    *   If the complexity seems too high, look for alternative algorithms mentioned or search specifically for optimizations (e.g., `codebase_search query="maximum flow optimization dinic"`). Check `document/optimizations/` for comparisons.

6.  **Broaden Search if Necessary (`list_dir` & Exploration):**
    *   If initial searches are unsuccessful or the path is unclear, use `list_dir` to explore relevant directories directly (e.g., `document/algorithms/graph/`, `document/patterns/sequence/`, `document/techniques/`).
    *   Read the contents (`read_file`) of any files whose names suggest relevance based on the abstract problem structure.
    *   Consider searching for high-level optimization comparisons in `document/optimizations/` (e.g., `codebase_search query="greedy vs dynamic programming interval scheduling"`).

7.  **Iterative Refinement:**
    *   The process may be iterative. Reading one KB entry might refine your understanding and lead to better search keywords or exploration targets.
    *   If you identify a specific bottleneck in a potential approach (e.g., performance of a sub-step), search the KB specifically for techniques or optimizations related to that bottleneck.

8.  **Strategy Selection & Justification (Rule 2c):**
    *   Once a suitable algorithm/pattern is identified and verified, select it as the strategy.
    *   Explicitly justify the choice based on the KB findings, referencing the specific files read (e.g., "Using Edmonds-Karp `[[../../algorithms/graph/max_flow_edmonds_karp.md]]` as identified via KB search...").

## Example Scenario (Max Flow Discovery)

Imagine a problem solvable by Max Flow, but not explicitly stated:

1.  **Formulation:** Problem involves routing items through a network with capacities. Goal is to maximize items reaching a destination. Keywords: "network flow," "capacity limits," "maximize throughput," "graph routing bottleneck."
2.  **Index Check:** `kb_index.md` points to Graph Algorithms / Max Flow.
3.  **Search:** `codebase_search query="maximum flow graph capacity"` yields `max_flow_ford_fulkerson.md`.
4.  **Read & Follow:** `read_file` on Ford-Fulkerson -> learn about residual graphs, augmenting paths -> `read_file` on `residual_graph.md`, `augmenting_path.md`. Ford-Fulkerson mentions Edmonds-Karp.
5.  **Read & Verify:** `read_file` on `max_flow_edmonds_karp.md`. Check description and complexity (`O(V*E^2)`). Verify against constraints.
6.  **(Optional Broaden):** If stuck, `list_dir document/algorithms/graph/` might reveal `max_flow_dinic.md` as a faster alternative if needed.
7.  **Select:** Choose Edmonds-Karp (or Dinic if complexity requires) based on KB exploration and verification.

By systematically using `codebase_search`, `list_dir`, and critically evaluating content via `read_file`, the KB becomes a powerful tool for discovering and applying appropriate algorithms. 