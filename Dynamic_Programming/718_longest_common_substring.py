class Solution:
    def findLength(self, nums1, nums2) -> int:
        if not nums1 or not nums2:
            return 0
        return self.Lcs(nums1,nums2)
    def Lcs(self,nums1,nums2):
        row=len(nums1)
        col = len(nums2)
        dp = [[0]*(col+1) for i in range(row+1)]
        res=0
        for i in range(1,row+1):
            for j in range(1,col+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    res = max(res,dp[i][j])
                else:
                    dp[i][j]=0
        return res