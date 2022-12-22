class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r=len(s1)
        c=len(s2)
        l=len(s3)
        if r+c!=l:
            return False
        dp = [[False]*(c+1) for i in range (r+1)]
        dp[0][0]=True
        for i in range(1,r+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,c+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,r+1):
            for j in range(1,c+1):
                if s1[i-1]==s3[i+j-1]:
                    dp[i][j]=dp[i-1][j]
                if s2[j-1]==s3[i+j-1]:
                    dp[i][j]=dp[i][j] or dp[i][j-1]
        return dp[-1][-1]