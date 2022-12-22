import collections
class Solution:
    def intersect(self, nums1, nums2):
        res = []
        nums_map = collections.Counter(nums1)
        for n in nums2:
            if n in nums_map and nums_map[n]>0:
                res.append(n)
                nums_map[n]-=1
        return res