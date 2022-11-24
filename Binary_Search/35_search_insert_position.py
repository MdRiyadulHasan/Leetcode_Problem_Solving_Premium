class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r = mid-1
        return l
if __name__ == '__main__':
    nums = [2,3,5,7,8]
    target = 1
    ob = Solution()
    ans = ob.searchInsert(nums,target)
    print(ans)