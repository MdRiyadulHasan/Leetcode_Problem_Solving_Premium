class Solution:
    def generate(self, numRows: int):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                pascal [i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        return pascal
if __name__ =='__main__':
    numRows = 5
    ob = Solution()
    ans = ob.generate(numRows)
    print(ans)