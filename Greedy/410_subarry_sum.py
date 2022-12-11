class Solution:
    def splitArray(self, nums, k: int) -> int:
        def canSplit(nums,mid,k):
            subarrays = 1
            curSum = 0
            for n in nums:
                curSum+=n
                if curSum>mid:
                    subarrays+=1
                    curSum=n
            return subarrays<=k
        l = max(nums)
        h = sum(nums)
        while l<=h:
            mid = (l+h)//2
            if canSplit(nums,mid,k):
                h=mid-1
            else:
                l=mid+1
        return l
if __name__ =='__main__':
    nums = [7,2,5,10,8]
    k=2
    ob = Solution()
    ans = ob.splitArray(nums,k)
    print(ans)