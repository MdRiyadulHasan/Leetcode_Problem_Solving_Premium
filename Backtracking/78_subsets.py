class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(nums,path):
            res.append(path)
            for i in range(len(nums)):
                backtrack(nums[i+1:],path+[nums[i]])
        backtrack(nums,[])
        return res
if __name__ == '__main__':
    nums = [1,2,3]
    ob = Solution()
    ans = ob.subsets(nums)
    print(ans)