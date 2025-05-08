import sys

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.fw = [0] * (n + 1) # 1-indexed BIT

    def update(self, i: int, delta: int):
        # i is 1-indexed
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i

    def query(self, i: int) -> int:
        # i is 1-indexed
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def range_add(self, l: int, r: int, delta: int):
        # l and r are 1-indexed (tin values)
        self.update(l, delta)
        if r + 1 <= self.n: # Ensure r + 1 is a valid index for BIT update
            self.update(r + 1, -delta)

class Solution:
    def treeQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        if n == 0:
            return []

        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        tin = [0] * (n + 1)
        tout = [0] * (n + 1) # Will store the max tin value in the subtree
        parent = [0] * (n + 1)
        parent_edge_weight = [0] * (n + 1) # Weight of edge from parent[node] to node
        initial_dist = [0] * (n + 1) # Distance from root (node 1) to node

        dfs_time_counter = 0
        
        # Iterative DFS using (node, parent_of_node, weight_from_parent, state)
        # Root is 1, its parent 0 (dummy), weight from parent 0.
        stack = [(1, 0, 0, 'enter')] 

        while stack:
            node, par, w_edge_from_par, state = stack.pop()

            if state == 'enter':
                dfs_time_counter += 1
                tin[node] = dfs_time_counter
                parent[node] = par
                parent_edge_weight[node] = w_edge_from_par
                
                if node == 1:
                    initial_dist[node] = 0
                else:
                    initial_dist[node] = initial_dist[par] + w_edge_from_par
                
                # Mark for exit processing
                stack.append((node, par, w_edge_from_par, 'exit'))
                
                # Add children to stack - process in reverse to mimic typical recursion order
                # (though for tin/tout ranges, the exact order of sibling subtrees doesn't break it)
                for neighbor, weight_to_neighbor in reversed(graph[node]):
                    if neighbor != par:
                        stack.append((neighbor, node, weight_to_neighbor, 'enter'))
            
            else: # state == 'exit'
                # tout[node] should be the tin of the last node in its subtree,
                # which is the current dfs_time_counter if we consider it as max tin processed so far in this branch.
                # Or, more simply, it's the tin of the node itself if its subtree is just itself and no more children were added.
                # The provided solution sets tout[node] = time (which is current max tin seen).
                # This means tout[node] is the maximum tin value within the subtree rooted at node.
                tout[node] = dfs_time_counter 
        
        bit = Fenwick(n) # Fenwick tree operates on up to n distinct tin values (1 to n)
        answers = []

        for q_item in queries:
            if q_item[0] == 2: # Query distance to x
                x = q_item[1]
                # Distance = initial_dist[x] + sum of deltas affecting nodes up to tin[x]
                # The range_add applies deltas to tin ranges. query(tin[x]) sums these up.
                answers.append(initial_dist[x] + bit.query(tin[x]))
            else: # Update edge weight
                _, u_node, v_node, new_w = q_item
                
                child_node = -1
                if parent[u_node] == v_node:
                    child_node = u_node
                else: # parent[v_node] == u_node (guaranteed tree structure)
                    child_node = v_node
                
                delta = new_w - parent_edge_weight[child_node]
                parent_edge_weight[child_node] = new_w # Update the stored weight
                
                # Apply delta to the entire subtree of child_node
                # The subtree is defined by the range of tin values [tin[child_node], tout[child_node]]
                bit.range_add(tin[child_node], tout[child_node], delta)
                
        return answers 