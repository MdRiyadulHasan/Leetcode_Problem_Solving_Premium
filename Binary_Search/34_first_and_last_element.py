class Solution:
    def searchRange(self, nums, target: int):
        left = self.binary_search(nums,target,True)
        right = self.binary_search(nums,target,False)
        return [left,right]
        
    def binary_search(self, nums,target,leftBias):
        i=-1
        l=0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r = m-1
            else:
                i = m
                if leftBias:
                    r = m-1
                else:
                    l=m+1
        return i