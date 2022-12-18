class Solution:
    def triangularSum(self, nums) -> int:
        n = len(nums)
        while n>0:
            for i in range(n-1):
                nums[i]=(nums[i]+nums[i+1])%10
            n-=1
        return nums[0]
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    ob = Solution()
    ans = ob.triangularSum(nums)
    print(ans)