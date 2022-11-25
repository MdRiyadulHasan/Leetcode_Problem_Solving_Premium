class Solution:
    def productExceptSelf(self, nums):
        answer = []
        product = 1
        for i in range(len(nums)):
            product*=nums[i]
            answer.append(product)
        product = 1
        for i in range(len(nums)-1, 0, -1):
            answer[i]=answer[i-1]*product
            product*=nums[i]
        answer[0]=product
        return answer 
if __name__ == '__main__':
    nums = [1,2,3,4]
    ob = Solution()
    ans = ob.productExceptSelf(nums)
    print(ans)