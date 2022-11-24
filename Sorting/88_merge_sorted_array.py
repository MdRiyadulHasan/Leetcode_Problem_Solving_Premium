class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = (m+n)-1
        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[last] = nums2[n-1]
                n-=1
            else:
                nums1[last] = nums1[m-1]
                m-=1
                
            last-=1
        while n>0:
            nums1[last] = nums2[n-1]
            n-=1
            last -=1
        return nums1
if __name__ == '__main__':
    nums1 = [1,2,5,0,0,0]
    nums2 = [3,4,7]
    m= 3
    n = 3
    ob = Solution()
    ans = ob.merge(nums1,m,nums2,n)
    print(ans)