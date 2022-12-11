class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(candidates,target,path):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                backtrack(candidates[i:],target-candidates[i],path+[candidates[i]])
        backtrack(candidates,target,[])
        return res        
if __name__ == '__main__':
    ob = Solution()
    candidates = [2,3,6,7] 
    target = 7
    ans = ob.combinationSum(candidates,target)
    print(ans)