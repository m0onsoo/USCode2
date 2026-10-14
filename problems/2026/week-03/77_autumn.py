class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # the complete combination
            if len(path) == k:
                result.append(path.copy()) # because we need a separate list object
                return

            # try every valid next number
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])

        return result