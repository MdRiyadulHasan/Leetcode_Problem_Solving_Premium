class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        candidate1=nums[-1]*nums[-2]*nums[-3]
        candidate2 = nums[0]*nums[1]*nums[-1]
        return max(candidate1,candidate2)