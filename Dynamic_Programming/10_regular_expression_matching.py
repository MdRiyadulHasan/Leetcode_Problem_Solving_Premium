class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)+1
        p_len = len(p)+1
        dp = [[False]*p_len for i in range(s_len)]
        dp[0][0] = True
        for i in range(1,p_len):
            if p[i-1]=='*':
                dp[0][i] = dp[0][i-2]
        for row in range(1,s_len):
            for col in range(1,p_len):
                i = row-1
                j = col-1
                if s[i]==p[j] or p[j]=='.':
                    dp[row][col] = dp[row-1][col-1]
                elif p[j] =='*':
                    if dp[row][col-2]==1:
                        dp[row][col]=dp[row][col-2]
                    elif s[i]==p[j-1] or p[j-1]=='.':
                        dp[row][col] = dp[row-1][col]
        return dp[-1][-1]