# https://leetcode.com/problems/minimum-genetic-mutation/

# 뭔가 그래프로 생각하면 되지 않을까
# 각각 스트링을 노드로, 엣지는 1개 변형으로 가능한 놈들만 연결하면 될거같다.
# 각 스트링마다 거리를 구하는 함수를 만들어야할듯

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank:
            return -1

        def can_mutate(g1, g2):
            count = 0
            for i in range(8):
                if g1[i] != g2[i]:
                    count += 1
                if count > 1:
                    return False
            if count == 0: # 만약 같은 놈이 있으면 연결 x
                return False
            return True
        
        graph = defaultdict(list)
        
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if can_mutate(bank[i], bank[j]):
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])

        for i in range(len(bank)):
                if can_mutate(startGene, bank[i]):
                    graph[startGene].append(bank[i])


        def dfs(node, visited):
            ans = float('inf')
            if node == endGene:
                return len(visited)
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.append(nxt)
                    mutations = dfs(nxt, visited[:])
                    visited.pop()
                    if mutations != -1:
                        ans = min(ans, mutations)
            return -1 if ans == float('inf') else ans

        return dfs(startGene, [])