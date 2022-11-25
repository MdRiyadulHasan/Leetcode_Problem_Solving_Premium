class Solution:
    def findMiddleIndex(self, nums) -> int:
        leftsum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if leftsum == total-nums[i]:
                return i
            leftsum+=nums[i]
            total-=nums[i]
        return -1