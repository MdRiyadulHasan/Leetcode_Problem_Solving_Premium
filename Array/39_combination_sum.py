class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidates, path, target):
            if target==0:
                result.append(path)
                return 
            for i in range(len(candidates)):
                if target-candidates[i]<0:
                    continue
                dfs(candidates[i:], path+[candidates[i]], target-candidates[i])
            
        dfs(candidates, [], target)
        return result
        
