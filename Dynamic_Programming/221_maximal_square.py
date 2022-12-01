class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)+1
        n = len(matrix[0])+1
        dp = [[0]*n for _ in range(m)]
        largest = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = 1+ min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    if dp[i][j]>largest:
                        largest = dp[i][j]
        return largest*largest