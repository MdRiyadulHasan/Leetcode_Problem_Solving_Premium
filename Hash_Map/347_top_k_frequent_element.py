class Solution:
    def topKFrequent(self, nums, k: int):
        dict = {}
        for n in nums:
            if n in dict:
                dict[n]+=1
            else:
                dict[n]=1
        res = sorted(dict, key = lambda x: (-dict[x],x))
        return res[:k]
if __name__=='__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    ob = Solution()
    ans =ob.topKFrequent(nums,k)
    print(ans)