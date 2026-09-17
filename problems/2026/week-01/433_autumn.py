from collections import deque

class Solution:
    def minMutation(
        self,
        startGene: str,
        endGene: str,
        bank: List[str]
    ) -> int:
        if startGene == endGene:
            return 0

        valid_genes = set(bank)

        if endGene not in valid_genes:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}
        letters = "ACGT"

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for position in range(len(gene)):
                for letter in letters:
                    # no need to consider the same letter
                    if letter == gene[position]:
                        continue

                    next_gene = (
                        gene[:position]
                        + letter
                        + gene[position + 1:]
                    )

                    if (
                        next_gene in valid_genes
                        and next_gene not in visited
                    ):
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))

        return -1