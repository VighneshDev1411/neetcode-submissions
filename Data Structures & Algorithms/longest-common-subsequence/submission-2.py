class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + lcs(i + 1, j + 1)
            
            else:
                dp[i][j] = max(lcs(i+1, j), lcs(i, j + 1))

            return dp[i][j]

        return lcs(0, 0)
        