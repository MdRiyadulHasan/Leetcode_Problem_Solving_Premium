class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            maxarea = max(maxarea, self.largestRectangleArea(dp))
        return maxarea
if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    ob = Solution()
    ans = ob.maximalRectangle(matrix)
    print(ans)