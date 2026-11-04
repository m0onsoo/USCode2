class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # edge case
        if len(s1) + len(s2) != len(s3):
            return False

        def helper(l1: int, l2: int) -> bool:
            if l1 == l2 == -1:
                return True
            
            if dp[l1 + 1][l2 + 1] is not None:
                return dp[l1 + 1][l2 + 1]

            idx = l1 + l2 + 1
            res = False
            if l1 >= 0 and s3[idx] == s1[l1]:
                res = res or helper(l1 - 1, l2)
            if l2 >= 0 and s3[idx] == s2[l2]:
                res = res or helper(l1, l2 - 1)
            
            dp[l1 + 1][l2 + 1] = res
            return res

        l1, l2 = len(s1), len(s2)
        
        # None: not visited, False: can't make s3 with l1 and l2, True: can make s3 with l1 and l2
        dp = [[None for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        return helper(l1 - 1, l2 - 1)