import collections
from typing import List, Set, Dict, DefaultDict, Deque


class Solution:
    """Solves the Word Ladder II problem using BFS and DFS."""

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Finds all shortest transformation sequences from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The ending word.
            wordList: A list of valid intermediate words.

        Returns:
            A list of all shortest transformation sequences, or an empty list if none exist.
        """
        wordSet: Set[str] = set(wordList)
        if endWord not in wordSet:
            return []

        # Preprocessing: Build adjacency map using wildcard patterns
        adj_map: DefaultDict[str, List[str]] = collections.defaultdict(list)
        all_words_for_map = wordSet.union({beginWord})
        L = len(beginWord)
        for word in all_words_for_map:
            for i in range(L):
                pattern = f"{word[:i]}*{word[i+1:]}"
                adj_map[pattern].append(word)

        # BFS to find shortest distances and parents
        distances: Dict[str, int] = {beginWord: 0}
        parents: DefaultDict[str, Set[str]] = collections.defaultdict(set)
        queue: Deque[str] = collections.deque([beginWord])
        found: bool = False

        while queue:
            # Process level by level to ensure shortest paths are prioritized
            level_size = len(queue)
            # Keep track of nodes added at this level
            current_level_nodes: Set[str] = set()

            for _ in range(level_size):
                word = queue.popleft()
                current_dist = distances[word]

                if word == endWord:
                    found = True
                    # Don't break; continue processing this level to find all paths of the same length

                # Optimization: If endWord is found, no need to explore deeper than its level
                # Check if distances[endWord] exists before accessing
                if found and endWord in distances and current_dist >= distances[endWord]:
                    continue

                # Find neighbors
                for i in range(L):
                    pattern = f"{word[:i]}*{word[i+1:]}"
                    if pattern in adj_map:
                        for neighbor in adj_map[pattern]:
                            if neighbor == word:
                                continue

                            # Check if neighbor is reachable and update paths/distances
                            # Only consider words in the original wordList (and endWord) or beginWord
                            # The check `neighbor in wordSet` previously removed might be needed
                            # Let's stick to the version that passed the corrected tests previously
                            # We need to check if neighbor should be processed based on distances

                            # First time reaching neighbor: shortest path found
                            if neighbor not in distances:
                                # Only add neighbors that are in the original word list OR the end word
                                # (beginWord check isn't strictly needed here as it's the start)
                                if neighbor in wordSet or neighbor == endWord:
                                    distances[neighbor] = current_dist + 1
                                    parents[neighbor].add(word)
                                    # Add to queue only if not already processed at this level
                                    # Check distance condition ensures we only add nodes for shortest paths
                                    # and avoid cycles in BFS path finding for this level
                                    if neighbor not in current_level_nodes:
                                        # Avoid adding endWord multiple times if found on this level
                                        if not (found and neighbor == endWord):
                                            queue.append(neighbor)
                                            current_level_nodes.add(neighbor)

                            # Reached neighbor via another path of the same shortest length
                            elif distances[neighbor] == current_dist + 1:
                                # Ensure the word leading to it is valid
                                if neighbor in wordSet or neighbor == endWord:
                                    parents[neighbor].add(word)

            # Optimization: If endWord was found in this level, stop BFS
            # No need to explore further levels as we only want shortest paths.
            if found:
                break

        # DFS to reconstruct paths
        results: List[List[str]] = []
        if not found:
            return []

        def dfs(word: str, path: List[str]):
            # Prepend word to path
            current_path = [word] + path
            if word == beginWord:
                results.append(current_path)
                return
            # Check if the current word has parents recorded from BFS
            if word in parents:
                for parent_word in parents[word]:
                    dfs(parent_word, current_path)

        # Start DFS from endWord with an empty initial path
        dfs(endWord, [])
        return results
