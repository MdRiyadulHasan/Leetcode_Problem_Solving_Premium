class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp =[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<=dp[j]:
                    dp[i] = 1 + dp[j]
        return max(dp)