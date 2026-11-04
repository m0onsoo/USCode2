# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        def dfs(start, count, path):
            if count == k:
                ans.append(path)
                return
            if start > n: 
                return
            for i in range(start, n + 1):
                dfs(i+1, count+1, path + [i])
        dfs(1, 0, [])
        return ans