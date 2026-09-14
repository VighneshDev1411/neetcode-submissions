class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        # dp = [[-1 for j in range(n)] for i in range(m)]

        def recursion(i, j, dp):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = recursion(i-1, j, dp)
            left = recursion(i, j - 1, dp)

            dp[i][j] = up + left

            return dp[i][j]

        return recursion(m - 1, n - 1, dp)

        