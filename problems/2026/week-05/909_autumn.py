class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)  
        target = n * n  
        squares = [-1]  
        left_to_right = True

        # flatten the table into an 1D list
        for row in range(n - 1, -1, -1): # the board starts from the very bottom-left cell
            if left_to_right:
                row_values = board[row]
            else:
                row_values = board[row][::-1]
            squares.extend(row_values)
            left_to_right = not left_to_right  # switch direction for the next row

        queue = deque([(1, 0)])  # store the starting square and the number of rolls used
        visited = {1}  # a snake and ladder is used only once

        # explore all reachable positions
        while queue:  
            position, rolls = queue.popleft()  # explore the position with the fewest rolls
            if position == target:
                return rolls

            for step in range(1, 7):
                next_position = position + step 
                # if the next position goes beyond the target
                if next_position > target:
                    break

                # check for a snake or ladder (should be visited )
                if squares[next_position] != -1:  
                    next_position = squares[next_position]

                if next_position not in visited:
                    visited.add(next_position)
                    queue.append((next_position, rolls + 1))

        return -1  # non-reachable