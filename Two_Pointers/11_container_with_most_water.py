class Solution:
    def maxArea(self, height) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l<r:
            area = (r-l)* min(height[l],height[r])
            res = max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    ob = Solution()
    ans = ob.maxArea(height)
    print(ans)