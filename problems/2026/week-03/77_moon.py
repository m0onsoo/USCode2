from collections import defaultdict

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # res = []
        # stack = [(1, [])]

        # while stack:
        #     # print(stack)
        #     curr_num, path = stack.pop()

        #     if len(path) == k:
        #         res.append(path)

        #     for i in range(curr_num, n + 1):
        #         stack.append((i + 1, path + [i]))
        
        # return res

        def DFS(curr_num, path):
            if len(path) == k:
                res.append(path[:])
                return 
            
            for i in range(curr_num, n + 1):
                path.append(i)
                DFS(i + 1, path)
                path.pop()
            
            return res
        
        res = []
        return DFS(1, [])


