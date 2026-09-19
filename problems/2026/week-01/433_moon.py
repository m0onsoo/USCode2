from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if not bank:
            return -1

        queue = deque([(startGene, 0)]) 
        visited = {startGene}

        bank_set = set(bank)
        while queue:
            curr, steps = queue.popleft()
            if curr == endGene:
                return steps
            for i in range(len(curr)):
                for ch in 'ACGT':
                    mutated = curr[:i] + ch + curr[i+1:]
                    if mutated in bank_set and mutated not in visited:
                        queue.append((mutated, steps + 1))
                        visited.add(mutated)

        return -1