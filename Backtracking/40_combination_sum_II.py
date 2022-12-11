class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        candidates.sort()
        def backtrack(candidates, target, path):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                if i>=1 and candidates[i]==candidates[i-1]:
                    continue
                backtrack(candidates[i+1:],target-candidates[i],path+[candidates[i]])
        backtrack(candidates,target,[])
        return res
if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    ob = Solution()
    ans = ob.combinationSum2(candidates,target)
    print(ans)