from collections import deque, defaultdict

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if not bank:
            return -1
    
        def isMutation(gene1: str, gene2: str) -> bool:
            # logic that checks if the gene1 and gene2 has only 1 difference
            # O(4 x 8 x 8) = Constant
            for idx, char in enumerate(gene1):
                for cand in 'ACGT':
                    changed = gene1[:idx] + cand + gene1[idx+1:]
                    if changed == gene2:
                        # what complexity does it take? O(8)? O(1)?
                        return True
            return False

        # construct a graph and connect node if there is only 1 difference
        graph = defaultdict(list)
        for gene in bank:
            if isMutation(startGene, gene):
                graph[startGene].append(gene)
                graph[gene].append(startGene)
        
        for gene1 in bank:
            for gene2 in bank[1:]:
                if isMutation(gene1, gene2):
                    graph[gene1].append(gene2)
                    graph[gene2].append(gene1)

        queue = deque([startGene]) # 큐 선언할 때 리스트로 감싸야 하는 이유
        visited = set([startGene])

        res = -1
        while queue:
            res += 1
            for _ in range(len(queue)):
                gene = queue.popleft()

                if gene == endGene:
                    return res

                for next_gene in graph[gene]:
                    if next_gene not in visited:
                        queue.append(next_gene)
                        visited.add(next_gene)

        return -1