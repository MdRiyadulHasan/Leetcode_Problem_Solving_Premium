class Solution:
    def maxProduct(self, nums) -> int:
        B = nums[::-1]
        for i in range(1,len(nums)):
            if nums[i-1]!= 0:
                nums[i]*=nums[i-1]
            if B[i-1]!= 0:
                B[i]*=B[i-1]
        return max(nums+B)
if __name__ == '__main__':
    nums = [-2, 0, 1]
    ob = Solution()
    ans = ob.maxProduct(nums)
    print(ans)
