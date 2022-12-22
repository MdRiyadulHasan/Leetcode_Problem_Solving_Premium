class Solution(object):
    def longestOnes(self, nums, k):
          
        freq = {0:0,1:0}
        l = 0 
        best = 0
        for r in range(len(nums)):      
            freq[nums[r]]+=1         
            while freq[0] > k:
                freq[nums[l]]-=1
                l+=1       
            best = max(best,r-l+1)
        return best
if __name__ =='__main__':
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    ob =Solution()
    ans = ob.longestOnes(nums,k)
    print(ans)