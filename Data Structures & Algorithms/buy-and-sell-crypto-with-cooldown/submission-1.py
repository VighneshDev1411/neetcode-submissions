class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices))]
        def func(ind, buy, prices):
            n = len(prices)
            if ind >= n:
                return 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            if buy:
                dp[ind][buy] =  max(-prices[ind] + func(ind + 1, 0, prices), 0 + func(ind + 1, 1, prices))
            else:
                dp[ind][buy] = max(prices[ind] + func(ind + 2, 1, prices), 0 + func(ind + 1, 0, prices))

            return dp[ind][buy]

        return func(0, 1, prices)
        