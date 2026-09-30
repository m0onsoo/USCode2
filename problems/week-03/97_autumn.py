class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1) # characters used from s1
        n = len(s2) # characters used from s2

        # if len is diff, impossible immediately
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)] # 0 to (m, n)
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue

                target_index = i + j - 1

                take_s1 = (
                    i > 0
                    and dp[i - 1][j]
                    and s1[i - 1] == s3[target_index]
                )

                take_s2 = (
                    j > 0
                    and dp[i][j - 1]
                    and s2[j - 1] == s3[target_index]
                )

                dp[i][j] = take_s1 or take_s2

        return dp[m][n]