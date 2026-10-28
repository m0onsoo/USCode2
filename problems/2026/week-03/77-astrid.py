from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        arr = [i for i in range(1,n+1)]
        ans = []
        for c in combinations(arr, k):
            ans.append(c)
        return ans