class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        nrows = len(coins)+1
        ncols = amount+1
        dp = [[2**64]*ncols for i in range(nrows)]
        for i in range(nrows):
            dp[i][0]=0
        for i in range(1,nrows):
            for j in range(1,ncols):
                if coins[i-1]<=j:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
                    
        if dp[-1][-1] !=2**64:
            return dp[-1][-1]
        else:
            return -1