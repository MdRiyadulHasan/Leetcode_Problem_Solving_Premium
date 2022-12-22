class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        return self.Lcs(text1,text2)
    def Lcs(self,text1,text2):
        row = len(text1)
        col = len(text2)
        dp = [[0]*(col+1) for i in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]