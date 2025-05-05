from typing import List


class Solution:
    """
    Solves LeetCode problem 3522: Calculate Score After Performing Instructions
    using direct simulation.
    """

    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        """
        Simulates the process described by instructions and values.

        Args:
            instructions: A list of strings, either "add" or "jump".
            values: A list of integers corresponding to the instructions.

        Returns:
            The final score after the simulation terminates.
        """
        n = len(instructions)
        current_index = 0
        score = 0
        visited = set()

        while True:
            # Check termination conditions
            if current_index < 0 or current_index >= n:
                break  # Out of bounds
            if current_index in visited:
                break  # Revisited index

            # Mark current index as visited
            visited.add(current_index)

            # Execute instruction
            instruction = instructions[current_index]
            value = values[current_index]

            if instruction == "add":
                score += value
                current_index += 1
            elif instruction == "jump":
                current_index += value
            # else: # Should not happen based on constraints
            #     pass

        return score
