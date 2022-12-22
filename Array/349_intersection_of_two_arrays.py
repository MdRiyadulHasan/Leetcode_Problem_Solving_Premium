class Solution:
    def intersection(self, nums1, nums2):
        res = []
        # for n in nums1:
        #     if n not in res and n in nums2:
        #         res.append(n)
        # return res
        nums_map = {}
        for n in nums1:
            if n in nums_map:
                nums_map[n]+=1
            else:
                nums_map[n]=1
        for n in nums2:
            if n in nums_map and nums_map[n]>0:
                res.append(n)
                nums_map[n]=0
        return res