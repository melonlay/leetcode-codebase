import collections


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        # Use integers as bitmasks: bit i represents number i+1
        rows = [0] * n
        cols = [0] * n
        boxes = [0] * n

        empty_cells = []

        # Initialize bitmasks and find empty cells
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    d = int(board[r][c])
                    mask = 1 << (d - 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask
                else:
                    empty_cells.append((r, c))

        def count_set_bits(num):
            count = 0
            while num > 0:
                num &= (num - 1)  # Clears the least significant set bit
                count += 1
            return count

        def get_possible_values(r, c):
            box_idx = (r // 3) * 3 + (c // 3)
            used_mask = rows[r] | cols[c] | boxes[box_idx]
            # 0x1FF is mask for 1-9 (binary 111111111)
            possible_mask = (~used_mask) & 0x1FF
            return possible_mask

        def find_best_empty_cell():
            min_possibilities = 10  # More than max possible (9)
            best_cell_info = None  # Store (r, c, index)

            for i, (r, c) in enumerate(empty_cells):
                possible_mask = get_possible_values(r, c)
                num_possibilities = count_set_bits(possible_mask)

                if num_possibilities == 0:  # Found a cell with no possibilities
                    return None, -1  # Indicates immediate failure, return invalid index

                if num_possibilities < min_possibilities:
                    min_possibilities = num_possibilities
                    best_cell_info = (r, c, i)
                    if min_possibilities == 1:  # Optimization: Found cell with only 1 possibility
                        break

            return best_cell_info, min_possibilities

        def backtrack():
            if not empty_cells:
                return True

            # MRV Heuristic: Find the cell with the fewest possibilities
            best_cell_info, num_possibilities = find_best_empty_cell()

            if best_cell_info is None:
                # If num_possibilities was -1, it means conflict found
                # If best_cell_info is None but num_possibilities > 0, something is wrong, but treat as failure.
                # Should be True if None means solved, False if conflict
                return False if num_possibilities == -1 else True

            r, c, idx = best_cell_info
            box_idx = (r // 3) * 3 + (c // 3)
            possible_mask = get_possible_values(r, c)

            # Temporarily remove the cell for recursive calls
            cell_to_process = empty_cells.pop(idx)

            # Try placing possible numbers
            for d in range(1, 10):
                mask = 1 << (d - 1)
                if possible_mask & mask:  # Check if d is possible using bitwise AND
                    num_str = str(d)

                    # Place number and update masks
                    board[r][c] = num_str
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

                    if backtrack():
                        # Found solution, must put cell back before returning True
                        # Otherwise the list remains modified for the caller
                        empty_cells.insert(idx, cell_to_process)
                        return True

                    # Backtrack: Remove number and clear mask bits
                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[box_idx] &= ~mask

            # If no number worked, put the cell back before returning False
            empty_cells.insert(idx, cell_to_process)
            return False

        backtrack()
