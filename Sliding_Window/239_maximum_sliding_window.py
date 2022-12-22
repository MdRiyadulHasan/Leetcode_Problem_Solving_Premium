from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        l=r=0
        q=deque()
        res=[]
        while r<len(nums):
            while q and q[-1]<nums[r]:
                q.pop()
            q.append(nums[r])
            if r-l+1<k:
                r+=1
            elif r-l+1==k:
                res.append(q[0])
                if q[0]==nums[l]:
                    q.popleft()
                l+=1
                r+=1
        return res
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k=3
    ob = Solution()
    ans = ob.maxSlidingWindow(nums,k)
    print(ans)