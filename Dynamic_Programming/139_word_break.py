class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        len_s = len(s)+1
        dp = [False]*len_s
        dp[0] = True
        for i in range(1,len_s):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[-1]