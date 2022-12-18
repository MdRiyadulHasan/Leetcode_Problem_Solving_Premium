class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r = n
        res = 0
        while l<=r:
            mid = (l+r)//2
            coins = (mid/2)*(mid+1)
            if coins>n:
                r = mid-1
            else:
                l=mid+1
                res = max(res,mid)
        return res