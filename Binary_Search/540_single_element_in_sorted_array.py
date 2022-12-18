class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        if nums[l]!=nums[l+1]:
            return nums[l]
        if nums[r]!=nums[r-1]:
            return nums[r]
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid]==nums[mid-1]:
                if mid%2==1:
                    l = mid+1
                else:
                    r = mid-1
            if nums[mid]==nums[mid+1]:
                if mid%2==1:
                    r=mid-1
                else:
                    l = mid+1
        return nums[l]
if __name__ == '__main__':
    nums = [1,1,2,3,3,4,4,8,8]
    ob = Solution()
    ans = ob.singleNonDuplicate(nums)
    print(ans)