class Solution:
    # 2d dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        # using dp
        # dp[i][j] represents: the (i+j)th character is combined from 
        # the first i ch of s1 and the first j ch of s2
        # if dp[i][j] == True
        # the last ch: s3[i+j-1] should come from s1[i-1](the ith ch) or s2[j-1](the jth ch)

        m, n = len(s1), len(s2)
        dp = [[False]* (n+1) for _ in range(m+1)]
        # base case
        dp[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                # current idx of s3
                k = i + j - 1
                # 来自s1[i-1]
                if i > 0 and s1[i-1] == s3[k] and dp[i-1][j]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                # 来自s2[j-1]   
                elif j > 0 and s2[j-1] == s3[k] and dp[i][j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        
        return dp[m][n]
         
            

        





# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s3) != len(s1) + len(s2):
#             return False
        
#         # pointer to record the current location
#         # 用s3遍历
#         n, m = len(s1), len(s2)
#         p1, p2 = 0, 0
#         fra1, fra2 = 0, 0
#         prev = 0
#         for ch in s3:
#             if p1 < n and ch == s1[p1]:
#                 p1 += 1
#                 if prev != 1:
#                     fra1 += 1
#                     prev = 1
#             elif p2 < m and ch == s2[p2]:
#                 p2 += 1
#                 if prev != 2:
#                     fra2 += 1
#                     prev = 2
#             else:
#                 return False

#         # print((fra1, fra2))
#         if abs(fra1-fra2) <= 1:
#             return True
#         return False

