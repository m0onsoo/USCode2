class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return

        # bellman-ford inspired
        
        # initialize
        results = triangle[-1]

        # solution: O(N)
        for _ in range(len(triangle) - 2, -1, -1):
            for i, num in enumerate(triangle[_]):
                results[i] = min(results[i], results[i + 1]) + num

        return results[0]

        
        