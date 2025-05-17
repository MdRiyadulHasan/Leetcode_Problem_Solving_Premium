def searchRange(nums, target):
    def firstPosition(nums):
        l = 0
        r = len(nums)-1
        res = -1
        while l<=r:
            m = (l+r)//2
            if target==nums[m]:
                res=m
                r=m-1
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        return res
    def lastPosition(nums):
        l = 0
        r = len(nums)-1
        res = -1
        while l<=r:
            m = (l+r)//2
            if target==nums[m]:
                res=m
                l = m+1
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        return res
        
    first = firstPosition(nums)
    last = lastPosition(nums)
    return [first, last]
    
nums = [5,7,8,8,8,8,8,10]
target =8
print(searchRange(nums, target))