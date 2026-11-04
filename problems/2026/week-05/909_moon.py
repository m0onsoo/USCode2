class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        
        # BFS
        # print(board)
        n = len(board)
        queue = deque([1])
        visited = set([1])
        steps = -1
        while queue:
            steps += 1

            for _ in range(len(queue)):
                curr = queue.popleft()
        
                if curr == n ** 2:
                    return steps
                
                for nxt in range(curr + 1, min(curr + 6, n ** 2) + 1):
                    if ((nxt - 1) // n) % 2 == 0:
                        # even row (left -> right)
                        nr, nc = n - (nxt - 1) // n - 1, nxt % n - 1
                    else:
                        # odd row (right -> left)
                        nr, nc = n - (nxt - 1) // n - 1, n - (nxt - 1) % n - 1

                    if board[nr][nc] != -1:
                        nxt = board[nr][nc]
                    
                    if nxt not in visited:
                        queue.append(nxt)
                        visited.add(nxt)
        
        return -1