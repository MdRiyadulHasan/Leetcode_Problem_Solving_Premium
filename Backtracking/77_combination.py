class Solution:
    def combine(self, n: int, k: int):
        res = []
        def backtrack(nums,path):
            if len(path)==k:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[i+1:], path+[nums[i]])
        backtrack(list(range(1,n+1)),[])
        return res
if __name__ == '__main__':
    n=4
    k=2
    ob = Solution()
    ans = ob.combine(n,k)
    print(ans)
