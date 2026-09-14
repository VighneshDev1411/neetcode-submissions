class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        def func(ind, amount):
            if ind == 0:
                return 1 if amount % coins[0] == 0 else 0 
            
            if dp[ind][amount] != -1:
                return dp[ind][amount]
            
            not_take = func(ind - 1, amount)
            take = 0
            if coins[ind] <= amount:
                take = func(ind, amount - coins[ind])

            dp[ind][amount] = take + not_take
            return dp[ind][amount]

        return func(n - 1, amount)