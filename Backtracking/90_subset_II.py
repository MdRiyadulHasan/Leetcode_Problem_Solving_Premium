class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def backtrack(nums,path):
            res.append(path)
            for i in range(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[i+1:],path+[nums[i]])
        backtrack(nums,[])
        return res
if __name__ == '__main__':
    nums = [1,2,2]
    ob = Solution()
    ans = ob.subsetsWithDup(nums)
    print(ans)