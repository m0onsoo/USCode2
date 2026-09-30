# https://leetcode.com/problems/interleaving-string/
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # condition 1 : the diff of number of substrings <= 1
        # condition 2 : the concat of substrings need to interleave


        # idea : proceed with s1 then s2....
        # I could try using dfs
        # variables should be 
        # indicator if proceeding with s1 or s2
        # counter of substrings for s1, s2
        # index of s1, s2

        n1, n2 = len(s1), len(s2)

        def dfs(indicator, idx_s1, idx_s2, sub_count1, sub_count2):
            idx_s3 = idx_s1 + idx_s2

            if idx_s1 == n1 and idx_s2 == n2 and abs(sub_count1 - sub_count2) <= 1:
                return True

            if indicator == 1:
                if idx_s1 < n1 and s1[idx_s1] == s3[idx_s3]:
                    if dfs(1, idx_s1 + 1, idx_s2, sub_count1, sub_count2):
                        return True
                if idx_s2 < n2 and s2[idx_s2] == s3[idx_s3]:
                    if dfs(2, idx_s2, idx_s2 + 1, sub_count1, sub_count2 + 1):
                        return True
            else: # indicator == 2
                if idx_s2 < n2 and s2[idx_s2] == s3[idx_s3]:
                    if dfs(2, idx_s1, idx_s2 + 1, sub_count1, sub_count2):
                        return True
                if idx_s1 < n1 and s1[idx_s1] == s3[idx_s3]:
                    if dfs(1, idx_s1 + 1, idx_s2, sub_count1 + 1, sub_count2):
                        return True



        if s1 and s1[0] == s3[0]:
            dfs(1, 1, 0, 1, 0)
        if s1 and s1[0] == s3[0]:
            dfs(2, 0, 1, 0, 1)

        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False 

        n1, n2 = len(s1), len(s2)
        memo = {}

        def dfs(idx1, idx2):
            idx3 = idx1 + idx2
            if idx1 == n1 and idx2 == n2:
                return True
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            result = False
            if idx1 < n1 and s1[idx1] == s3[idx3]:
                if dfs(idx1 + 1, idx2):
                    result = True
            if idx2 < n2 and s2[idx2] == s3[idx3]:
                if dfs(idx1, idx2 + 1):
                    result = True

            memo[(idx1, idx2)] = result
            return result

        return dfs(0, 0)
        # return False