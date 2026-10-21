# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        graph = defaultdict(list)
        # for i in range(len(triangle-1)):
        #     for j in range(i+1):
        #         graph[(i,j)].append()

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dist = [[float('inf')] * len(row) for row in triangle]
        dist[0][0] = triangle[0][0]

        for i in range(n - 1):                 # 위상정렬 순서 = 위에서 아래로
            for j in range(i + 1):
                for nj in (j, j + 1):          # 간선 두 개 relax
                    dist[i+1][nj] = min(dist[i+1][nj], dist[i][j] + triangle[i+1][nj])

        return min(dist[-1])