class Solution:
    def change(self, amount: int, coins) -> int:
        len_coins = len(coins)+1
        amount = amount+1
        dp = [[0]*amount for i in range(len_coins)]
        for i in range(len_coins):
            dp[i][0]=1
        for i in range(1,len_coins):
            for j in range(1,amount):
                if coins[i-1]<=j:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]