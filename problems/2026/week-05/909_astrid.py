from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        # least number of dice rolls
        # using bfs
        # every level: 6 choices to start
        n = len(board)
        def idx2rc(idx):
            # turn 1-base to 0-base
            idx -= 1
            r = n - 1 - idx // n
            c = idx % n
            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c
            return r, c


    
        # we want: current status(idx), current steps
        # idx: [1, n**2]
        dq = deque()
        dq.append([1, 0])

        vis = set()

        while dq:
            idx, steps = dq.popleft() 
            # roll the dice
            for i in range(1, 7):
                nextidx = idx + i
                # boundary check
                if nextidx > n**2:
                    break
                
                r, c = idx2rc(nextidx)               
                if board[r][c] > 0:
                    # take the ladder/snake
                    nextidx = board[r][c]
                
                if nextidx == n**2:
                    return steps + 1

                if nextidx not in vis:
                    vis.add(nextidx)
                    dq.append([nextidx, steps+1])
        
        return -1

                

            

            
        