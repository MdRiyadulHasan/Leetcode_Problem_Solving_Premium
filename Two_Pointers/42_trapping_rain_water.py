class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n<=2:
            return 0
        leftmax = height[0]
        rightmax = height[n-1]
        l = 1
        r = n-2
        trapped_water = 0
        while l<=r:
            if leftmax<rightmax:
                if leftmax<=height[l]:
                    leftmax = height[l]
                else:
                    trapped_water+=leftmax-height[l]
                l+=1
            else:
                if rightmax<=height[r]:
                    rightmax = height[r]
                else:
                    trapped_water+=rightmax-height[r]
                r-=1
        return trapped_water
if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ob = Solution()
    ans = ob.trap(height)
    print(ans)