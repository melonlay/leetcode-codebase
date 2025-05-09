# Knowledge Base Index (kb_index.md)

This file serves as the central index for the LeetCode Python Solver knowledge base.

**Goal:** To store generalized, reusable knowledge about algorithms, patterns, techniques, data structures, optimizations, and common mistakes encountered during problem-solving. See [[methodology/algorithm_discovery_via_kb.md]] for guidance on using this KB effectively.

## Main Categories

This file provides a central index to all documents currently in the `./document/` knowledge base.

## Algorithms (`algorithms/`)
*   `combinatorics/`
    *   [[algorithms/combinatorics/kth_permutation_factorial.md]]
    *   [[algorithms/combinatorics/kth_multiset_permutation.md]]
    *   [[algorithms/combinatorics/subset_sum_generation_by_count.md]]
*   `divide_and_conquer/`
    *   [[algorithms/divide_and_conquer/divide_and_conquer.md]]
*   `dynamic_programming/`
    *   [[algorithms/dynamic_programming/dynamic_programming.md]]
    *   `array/`
        *   [[algorithms/dynamic_programming/array/longest_increasing_subsequence.md]] 
        *   [[algorithms/dynamic_programming/array/k_limited_operations_dp.md]]
    *   `sequence/` 
        *   [[algorithms/dynamic_programming/sequence/k_merges_variable_cost_dp.md]]
    *   `string/` (Explore with `list_dir`)
        *   [[algorithms/dynamic_programming/string/palindrome_checking.md]]
        *   [[algorithms/dynamic_programming/string/regex_matching.md]]
        *   [[algorithms/dynamic_programming/string/wildcard_matching.md]]
*   `graph_search/`
    *   [[algorithms/graph_search/bellman_ford.md]]
    *   [[algorithms/graph_search/bfs.md]]
    *   [[algorithms/graph_search/dfs.md]]
    *   [[algorithms/graph_search/dijkstra.md]]
    *   [[algorithms/graph_search/heap_dfs_boundary_fill.md]]
    *   [[algorithms/graph_search/spfa.md]]
*   `greedy/`
    *   [[algorithms/greedy/greedy.md]]
    *   [[algorithms/greedy/kruskal.md]]
    *   [[algorithms/greedy/prims.md]]
    *   `array/`
        *   [[algorithms/greedy/array/k_limited_operations_heap.md]]
*   `linked_list/`
    *   [[algorithms/linked_list/iterative_segment_reversal.md]]
*   `merging/`
    *   [[algorithms/merging/lexicographical_merge.md]]
    *   [[algorithms/merging/k_way_merge_heap.md]]
*   `number_manipulation/`
    *   [[algorithms/number_manipulation/partial_integer_reversal.md]]
*   `recursion/`
    *   [[algorithms/recursion/mrv_heuristic.md]]
    *   [[algorithms/recursion/backtracking.md]]
*   `searching/`
    *   [[algorithms/searching/binary_search.md]]
    *   `array/`
        *   [[algorithms/searching/array/kth_two_sorted_arrays.md]]
*   `sorting/`
    *   [[algorithms/sorting/builtin_sort.md]]
*   `string/`
    *   [[algorithms/string/kmp.md]]

## Patterns (`patterns/`)
*   [[patterns/sweep_line.md]]
*   [[patterns/two_pointers.md]]
*   [[patterns/sliding_window.md]]
*   `array/`
    *   [[patterns/array/find_capacity_between_boundaries.md]]
    *   [[patterns/array/k_limited_operations.md]]
*   `construction/`
    *   [[patterns/construction/optimized_construction_via_input_guarantees.md]]
*   `digit_dp/`
    *   [[patterns/digit_dp/digit_dp.md]]
    *   [[patterns/digit_dp/digit_dp_carry_counts.md]]
*   `dynamic_programming/`
    *   [[patterns/dynamic_programming/dp_on_items_bitwise_sum_constraint.md]]
    *   [[patterns/dynamic_programming/dp_balanced_permutation_counting.md]]
*   `geometry/`
    *   [[patterns/geometry/perfect_tiling_check.md]]
*   `graph/`
    *   [[patterns/graph/graph.md]]
    *   [[patterns/graph/implicit_graph_to_tree_transformation.md]]
    *   [[patterns/graph/minimum_spanning_tree.md]]
*   `grid_tiling/`
    *   [[patterns/grid_tiling/2xn_tiling_dp.md]]
*   `matrix/`
    *   [[patterns/matrix/dimension_reduction_matrix_to_1d.md]]
    *   [[patterns/matrix/dual_path_grid_dp.md]]
*   `sequence/`
    *   [[patterns/sequence/counting_subsequences_by_pairwise_relation.md]]
    *   (LIS is an algorithm: see [[algorithms/dynamic_programming/array/longest_increasing_subsequence.md]])
    *   (K-Merges DP is an algorithm: see [[algorithms/dynamic_programming/sequence/k_merges_variable_cost_dp.md]])
*   `simulation/`
    *   [[patterns/simulation/phased_simulation_large_k.md]]
*   `traversal/`
    *   [[patterns/traversal/oscillating_traversal.md]]

## Data Structures (`data_structures/`)
*   [[data_structures/data_structures.md]]
*   [[data_structures/avl_tree.md]]
*   [[data_structures/binary_search_tree.md]]
*   [[data_structures/deque.md]]
*   [[data_structures/disjoint_set_union.md]]
*   [[data_structures/fenwick_tree_bit.md]]
*   [[data_structures/fibonacci_heap.md]]
*   [[data_structures/hash_set.md]]
*   [[data_structures/hash_table_dict.md]]
*   [[data_structures/heap_priority_queue.md]]
*   [[data_structures/linked_list.md]]
*   [[data_structures/queue.md]]
*   [[data_structures/red_black_tree.md]]
*   [[data_structures/segment_tree.md]]
*   [[data_structures/splay_tree.md]]
*   [[data_structures/stack.md]]
*   (Misplaced sweep_line/polynomial entries removed, they are techniques/optimizations)

## Techniques (`techniques/`)
*   [[techniques/coordinate_compression.md]]
*   [[techniques/set_based_counting.md]]
*   `binary_lifting/`
    *   [[techniques/binary_lifting/binary_lifting.md]]
    *   [[techniques/binary_lifting/binary_lifting_min_steps_precomputed_jumps.md]]
    *   [[techniques/binary_lifting/binary_lifting_sparse_table.md]]
*   `bit_manipulation/`
    *   [[techniques/bit_manipulation/bitmask_state_tracking.md]]
*   `comparison/`
    *   [[techniques/comparison/find_best_by_primary_secondary_criteria.md]]
*   `combinatorics/`
    *   [[techniques/combinatorics/iterative_nCr_modulo.md]]
    *   [[techniques/combinatorics/capped_multinomial.md]]
    *   [[techniques/combinatorics/capped_nCr.md]]
*   `divide_and_conquer/`
    *   [[techniques/divide_and_conquer/mitm_combine_diff_value_maps.md]]
*   `dynamic_programming/`
    *   [[techniques/dynamic_programming/2d_dependency_lis_reduction.md]]
    *   [[techniques/dynamic_programming/dp_lower_bound_constraint.md]]
    *   [[techniques/dynamic_programming/dp_state_subset_difference_max_sum.md]]
    *   [[techniques/dynamic_programming/fixed_window_dp_space_optimization.md]]
    *   [[techniques/dynamic_programming/dp_on_dag_subsets.md]]
    *   [[techniques/dynamic_programming/dp_state_parity_toggle.md]]
*   `graph/`
    *   [[techniques/graph/augmenting_path.md]]
    *   [[techniques/graph/blocking_flow.md]]
    *   [[techniques/graph/level_graph.md]]
    *   [[techniques/graph/residual_graph.md]]
*   `graph_traversal/`
    *   [[techniques/graph_traversal/dfs_derived_tree_path_query.md]]
    *   [[techniques/graph_traversal/edge_relaxation.md]]
*   `grid_processing/`
    *   [[techniques/grid_processing/recursive_quadrant_construction.md]]
*   `hashing/`
    *   [[techniques/hashing/hashing.md]]
*   `interval_management/`
    *   [[techniques/interval_management/height_profile_construction_by_height.md]]
*   `lookup/`
    *   [[techniques/lookup/hash_map_complement_lookup.md]]
*   `matrix/`
    *   [[techniques/matrix/grid_flattening.md]]
*   `number_manipulation/`
    *   [[techniques/number_manipulation/handle_sign_separately.md]]
*   `pattern_based_neighbor_finding/`
    *   [[techniques/pattern_based_neighbor_finding/pattern_based_neighbor_finding.md]]
    *   `string/`
        *   [[techniques/pattern_based_neighbor_finding/string/string_wildcard_neighbors.md]]
*   `polynomial/`
    *   [[techniques/polynomial/elementary_symmetric_polynomial_dp.md]]
    *   [[techniques/polynomial/fast_walsh_hadamard_transform.md]]
*   `recursion/`
    *   [[techniques/recursion/memoization.md]]
*   `sequence/`
    *   [[techniques/sequence/sequence.md]]
    *   [[techniques/sequence/difference_array.md]]
    *   [[techniques/sequence/dp_map_state_for_pairwise_relations.md]]
    *   [[techniques/sequence/find_boundary_pointer_sorted_constraint.md]]
    *   [[techniques/sequence/find_reach_bounds_sorted_constraint.md]]
    *   [[techniques/sequence/in_place_array_hashing.md]]
    *   [[techniques/sequence/monotonic_queue.md]]
    *   [[techniques/sequence/prefix_sum_difference_constraint.md]]
    *   [[techniques/sequence/prefix_suffix_aggregates.md]]
    *   [[techniques/sequence/strict_sequential_parsing.md]]
*   `stack/`
    *   [[techniques/stack/stack_index_tracking_for_subsequences.md]]
*   `string/`
    *   [[techniques/string/string.md]]
    *   [[techniques/string/expand_from_center.md]]
    *   [[techniques/string/string_hashing.md]]
*   `sweep_line/`
    *   [[techniques/sweep_line/sweep_line_max_height_profile.md]]
*   `tree/`
    *   [[techniques/tree/tree_rotations.md]]
    *   [[techniques/tree/greedy_dfs_component_aggregation.md]]
    *   <!-- TODO: [[techniques/tree/tree_traversal.md]] (General tree traversal concepts) -->
*   Subdirectories to explore (ensure all relevant files are linked directly or category is sufficient): `comparison/`, `graph/`, `grid_processing/`, `lookup/`, `polynomial/`, `tree/`.

## Optimizations (`optimizations/`)
*   [[optimizations/optimizations.md]]
*   [[optimizations/bounding_box_calculation_timing.md]]
*   [[optimizations/comprehensions_and_generators.md]]
*   [[optimizations/python_builtin_modules.md]]
*   [[optimizations/iterator_usage.md]]
*   `array/`
    *   [[optimizations/array/offline_processing_monotonic_stack_for_rightward_query.md]]
    *   [[optimizations/array/left_to_right_sweep_heap_for_future_event_resolution.md]]
*   `data_structure_state/`
    *   [[optimizations/data_structure_state/tuple_vs_list_small_fixed_size.md]]
*   `dynamic_programming/`
    *   [[optimizations/dynamic_programming/dp_state_comparison_equal_partition_sums.md]]
    *   [[optimizations/dynamic_programming/digit_dp_carry_counts_topdown_vs_bottomup.md]]
    *   [[optimizations/dynamic_programming/memoization_future_value.md]]
    *   [[optimizations/dynamic_programming/dp_multiset_partition_counting_tle_python.md]]
    *   [[optimizations/dynamic_programming/dp_state_packing_with_bit_manipulation.md]]
    *   [[optimizations/dynamic_programming/stock_problem_k_optimization.md]]
    *   [[optimizations/dynamic_programming/dp_state_space_reduction_product_limit.md]]
*   `graph_shortest_path/`
    *   [[optimizations/graph_shortest_path/path_query_sorted_value_diff_graph.md]]
*   `grid_traversal/`
    *   [[optimizations/grid_traversal/heap_dfs_vs_bfs_boundary_fill.md]]
    *   [[optimizations/grid_traversal/dual_path_dp_topdown_vs_bottomup.md]]
*   `parsing/`
    *   [[optimizations/parsing/recursive_vs_iterative_stack_parsing.md]]
*   `simulation/`
    *   [[optimizations/simulation/large_k_simulation_strategies.md]]
*   `string/`
    *   [[optimizations/string/string_vs_list_manipulation.md]]
    *   [[optimizations/string/string_concatenation.md]]
    *   [[optimizations/string/kmp_vs_string_hashing.md]]
*   `partitioning/`
    *   [[optimizations/partitioning/mitm_vs_linear_dp_max_equal_sum.md]]
*   `pruning/`
    *   [[optimizations/pruning/pruning.md]]
    *   See also: [[algorithms/recursion/mrv_heuristic.md]]
*   `combinatorics/`
    *   [[optimizations/combinatorics/iterative_set_construction_xor_k_tuples.md]]
    *   [[optimizations/combinatorics/iterative_set_construction_xor_triplets.md]]
    *   [[optimizations/combinatorics/kth_permutation_iterative_update.md]]
    *   [[optimizations/combinatorics/nCr_sequence_lucas_vs_iterative.md]]
*   `sequence/`
    *   [[optimizations/sequence/dp_subsequence_state_tradeoffs_property_vs_pair.md]]
*   `searching/`
    *   [[optimizations/searching/mitm_subset_sum_combination_strategies.md]]
    *   [[optimizations/searching/mitm_subset_sum_combine_binary_vs_2ptr.md]]
*   Subdirectories to explore: `combinatorics/`, `sequence/`, `searching/`.

## Mathematical Concepts (`mathematical_concepts/`)
*   [[mathematical_concepts/mathematical_concepts.md]]
*   Subdirectories to explore: `statistics/`, `geometry/`, `combinatorics/`.

## Common Mistakes (`common_mistakes/`)
*   [[common_mistakes/common_mistakes.md]]
*   [[common_mistakes/float_precision_in_comparisons.md]]
*   [[common_mistakes/large_exponent_performance.md]]
*   [[common_mistakes/test_case_logic_errors.md]]
*   [[common_mistakes/integer_overflow_check.md]]
*   [[common_mistakes/unittest_import_error.md]]
*   [[common_mistakes/constraint_violation_handling.md]]
*   [[common_mistakes/hash_map_index_mismatch.md]]
*   `graph/`
    *   [[common_mistakes/graph/incorrect_shortest_path_assumption_on_derived_tree.md]]
*   `logic/`
    *   [[common_mistakes/logic/rigid_algorithm_application.md]]
*   `performance/`
    *   [[common_mistakes/performance/space_complexity_overlooked.md]]

## Heuristics (`heuristics/`)
*   (This category needs to be populated based on existing files, e.g., from `document/heuristics/greedy/`)
*   `greedy/`
    *   [[heuristics/greedy/min_score_terminal_node_heuristic.md]]

*(Note: Some subdirectories may still require `list_dir` if they were missed or added later.)* 