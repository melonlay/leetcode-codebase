import collections
from typing import List, Set
from collections import defaultdict, deque


class Solution:
    """Solves the Word Ladder problem using Breadth-First Search
    with pattern-based preprocessing for faster neighbor finding."""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Finds the length of the shortest transformation sequence.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: A list of valid words for transformation.

        Returns:
            The number of words in the shortest sequence, or 0 if none exists.
        """
        # Use a set for efficient lookup and include beginWord
        wordSet: Set[str] = set(wordList)
        if endWord not in wordSet:
            return 0
        # Add beginWord to the set for pattern generation, if not already present
        wordSet.add(beginWord)  # Ensure beginWord is part of the processing

        # Preprocessing: Create patterns to find neighbors efficiently
        patterns = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        # BFS Initialization
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord}

        # BFS Loop
        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            # Find neighbors using precomputed patterns
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                # Optimization: Once neighbors for a pattern are processed,
                # we can potentially clear that pattern entry if memory is a concern,
                # but it might complicate revisiting scenarios if graph isn't strictly layered.
                # For simplicity, we don't clear it here.

        return 0  # No path found
