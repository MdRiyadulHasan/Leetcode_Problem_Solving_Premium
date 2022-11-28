class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h = len(word1)+1
        w = len(word2)+1
        dp = [[0]*w for i in range(h)]

        for i in range(h):
            dp[i][0] = i
        for j in range(w):
            dp[0][j]=j
        for row in range(1,h):
            for col in range(1,w):
                i = row-1
                j = col-1
                if word1[i]==word2[j]:
                    dp[row][col]=dp[row-1][col-1]
                else:
                    dp[row][col] = min(dp[row-1][col-1],dp[row-1][col],dp[row][col-1])+1
        return dp[-1][-1]
if __name__ =='__main__':
    word1 = "horse"
    word2 = 'ros'
    ob = Solution()
    ans = ob.minDistance(word1,word2)
    print(ans)