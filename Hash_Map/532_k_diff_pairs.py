from collections import Counter
class Solution:
    def findPairs(self, nums, k: int) -> int:
        c = Counter(nums)
        cnt = 0
        if k==0:
            for key, val in c.items():
                if val>1:
                    cnt+=1
        else:
            for key,val in c.items():
                if key+k in c:
                    cnt+=1
        return cnt
if __name__ == '__main__':
    nums = [3,1,4,1,5]
    k = 2
    ob = Solution()
    ans = ob.findPairs(nums,k)
    print(ans)
