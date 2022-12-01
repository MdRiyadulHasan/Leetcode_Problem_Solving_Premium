class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        i=0
        res = 0
        while i<n:
            dp[i][i]=1
            res+=1
            i+=1
        for col in range(1,n):
            for row in range (col):
                if row == col-1 and s[row]==s[col]:
                    dp[row][col] = 1
                    res+=1
                elif dp[row+1][col-1]==1 and s[row] ==s[col]:
                    dp[row][col] = 1
                    res+=1
        return res